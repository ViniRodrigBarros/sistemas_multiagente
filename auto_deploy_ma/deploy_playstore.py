import os
import argparse
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload 

FLAVOR_PACKAGE_MAP = {
    "rest": "com.application.ifpb",
}

parser = argparse.ArgumentParser()
parser.add_argument("--flavor", required=True, help="Nome do flavor (ex: dev, rest, prod)")
args = parser.parse_args()

FLAVOR = args.flavor

if FLAVOR not in FLAVOR_PACKAGE_MAP:
    print(f"❌ Flavor '{FLAVOR}' não está configurado em FLAVOR_PACKAGE_MAP.")
    exit(1)

PACKAGE_NAME = FLAVOR_PACKAGE_MAP[FLAVOR]
ENTRY_POINT = f"lib/main.dart"
AAB_PATH = f"build/app/outputs/bundle/{FLAVOR}Release/app-{FLAVOR}-release.aab"
CREDENTIALS_PATH = "google_play_service.json"

# === 1. Gerar App Bundle ===
print(f"🔨 Gerando App Bundle para flavor '{FLAVOR}'...")
build_command = f"flutter build appbundle --flavor {FLAVOR} -t {ENTRY_POINT}"
os.system(build_command)

if not os.path.exists(AAB_PATH):
    print(f"❌ Erro: App Bundle não encontrado em {AAB_PATH}!")
    exit(1)

print("✅ App Bundle gerado com sucesso!")

# === 2. Autenticação ===
print("🔑 Autenticando na API do Google Play...")

SCOPES = ["https://www.googleapis.com/auth/androidpublisher"]
credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=SCOPES)
service = build("androidpublisher", "v3", credentials=credentials)

# === 3. Criar edição ===
print("📦 Criando nova edição na Google Play...")
edit_request = service.edits().insert(body={}, packageName=PACKAGE_NAME)
edit = edit_request.execute()
edit_id = edit["id"]

# === 4. Upload do AAB ===
print("⬆️ Fazendo upload do App Bundle...")

media = MediaFileUpload(AAB_PATH, mimetype="application/octet-stream", resumable=True)  # ✅ Correção aqui
aab_upload_request = service.edits().bundles().upload(
    editId=edit_id,
    packageName=PACKAGE_NAME,
    media_body=media
)
aab_upload_response = aab_upload_request.execute()

print(f"✅ Upload concluído! Versão: {aab_upload_response['versionCode']}")

# === 5. Publicar em Teste Interno ===
print("🚀 Publicando no canal de Teste Interno...")
release = {
    "releases": [
        {
            "name": f"Teste Interno ({FLAVOR})",
            "status": "completed",
            "versionCodes": [aab_upload_response["versionCode"]],
        }
    ]
}
track_request = service.edits().tracks().update(
    editId=edit_id,
    packageName=PACKAGE_NAME,
    track="internal",
    body=release
)
track_response = track_request.execute()

# === 6. Confirmar Publicação ===
print("✅ Confirmando publicação...")
commit_request = service.edits().commit(editId=edit_id, packageName=PACKAGE_NAME)
commit_request.execute()

print(f"🎉 App ({FLAVOR}) publicado com sucesso no Google Play Teste Interno!")
