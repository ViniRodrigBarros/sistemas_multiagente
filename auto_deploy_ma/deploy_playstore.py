import os
import argparse
import subprocess
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload 

# Passo 1: Rode - pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
# Passo 2: Rode - python deploy_playstore.py --flavor <nome do flavor> 

def run_tests():
    """Executa os testes do projeto"""
    print("🧪 Executando testes...")
    try:
        result = subprocess.run(
            ["flutter", "test"],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        
        if result.returncode == 0:
            print("✅ Todos os testes passaram!")
            print("\n📊 Resumo dos testes:")
            print(result.stdout)
            return True
        else:
            print("❌ Alguns testes falharam!")
            print("\n📊 Resumo dos testes:")
            print(result.stdout)
            print("\n❌ Erros:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Erro ao executar testes: {e}")
        return False

def ask_user(prompt):
    """Pergunta ao usuário e retorna True para 'sim' ou 's', False para 'não' ou 'n'"""
    while True:
        response = input(f"{prompt} (s/n): ").lower().strip()
        if response in ['s', 'sim', 'y', 'yes']:
            return True
        elif response in ['n', 'não', 'nao', 'no']:
            return False
        else:
            print("Por favor, responda com 's' para sim ou 'n' para não.")

FLAVOR_PACKAGE_MAP = {
    "rest": "com.sttp.neat_3",
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

print(f"🚀 Script de deploy para flavor: {FLAVOR}")
print("=" * 50)

# === 0. Perguntar se quer rodar os testes ===
if ask_user("Deseja executar os testes antes de publicar?"):
    tests_passed = run_tests()
    if not tests_passed:
        print("\n❌ Testes falharam! Deseja continuar mesmo assim?")
        if not ask_user("Continuar com o deploy?"):
            print("🚫 Deploy cancelado pelo usuário.")
            sys.exit(0)
    print("\n" + "=" * 50)

# === 1. Perguntar se quer publicar ===
if not ask_user("Deseja prosseguir com a publicação na Play Store?"):
    print("🚫 Deploy cancelado pelo usuário.")
    sys.exit(0)

print("\n" + "=" * 50)
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
