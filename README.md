## Nome do Projeto
AutoDeployMA — Sistema Multiagente para Automação de Testes e Publicação de Aplicativos Flutter

## 👨‍🎓 Integrantes
Vinicius Rodrigues Barros


## 💡 Ideia Principal
O projeto propõe a criação de um sistema automatizado que realiza testes e publicação de aplicativos Flutter na Google Play Store. A ideia é que, sempre que o código do app for atualizado, agentes inteligentes verifiquem se tudo está funcionando corretamente através de testes automatizados e, caso não haja erros, façam o upload do aplicativo diretamente para a loja. Assim, o processo de entrega se torna mais ágil, seguro e eficiente.

## 🎯 Objetivos
Automatizar o processo de testes unitários de projetos Flutter.

Garantir que apenas versões testadas e estáveis sejam publicadas na Play Store.

Reduzir a intervenção manual no processo de deploy.

Diminuir erros humanos e acelerar o ciclo de desenvolvimento e entrega.

Integrar práticas de DevOps e CI/CD com um modelo baseado em sistemas multiagente.

## 👥 Público-Alvo
Desenvolvedores de aplicativos Flutter que desejam automatizar seu processo de entrega contínua.

Equipes de software com foco em qualidade, produtividade e integração contínua.

Startups e empresas que lançam atualizações frequentes de seus apps.

## 🤖 Agentes Envolvidos
Agente de Teste: Executa os testes unitários do projeto Flutter e valida os resultados.

Agente de Decisão: Avalia os resultados dos testes e determina se a build está apta para ser publicada.

Agente de Deploy: Realiza a assinatura e o upload do aplicativo para a Google Play Store automaticamente, caso os testes sejam aprovados.

Agente de Monitoramento (opcional): Acompanha logs, falhas e status da publicação, gerando alertas se necessário.

## 🧱 Tecnologias Pretendidas
Flutter/Dart: Para o desenvolvimento do aplicativo principal. É a tecnologia-alvo do processo de testes e deploy.

Python: Usado para orquestrar os agentes, por sua simplicidade, integração com bibliotecas de automação e suporte a scripts.

unittest / integration_test (Flutter): Para testes unitários e de integração.

GitHub Actions / GitLab CI / Jenkins (opcional): Para integração contínua, caso o projeto evolua para uso com ferramentas CI.

Google Play Developer API: Para automação do envio do bundle .aab à Google Play.

Gradle: Para build e assinatura do app.

Kivy / Tkinter (opcional): Para interface gráfica do script, caso desejem uma UI para o sistema de automação.

A escolha de Python se justifica pela sua alta produtividade, facilidade de leitura e ampla disponibilidade de bibliotecas de automação. O Flutter é o alvo da automação, por isso o uso dessas ferramentas específicas se alinha ao ecossistema do projeto.

## Como Utilizar

Passo a Passo: Autodeploy na Google Play (usando google-play-service.json)
1. Pré-requisitos
Python 3.7+ instalado.
Ferramentas do Flutter instaladas.
Conta no Google Play Console e acesso ao projeto.
2. Obter o arquivo de credenciais (google-play-service.json)
Acesse o Google Cloud Console.
Crie um projeto ou selecione o existente.
Ative a API Google Play Developer.
Crie uma conta de serviço e gere o arquivo de credenciais JSON.
Dê permissão à conta de serviço no Google Play Console (Configurações > Acesso à API).
Baixe o arquivo (ex: google-play-service.json) e coloque no mesmo diretorio em que se encontra deploy_playstore.py
3. Instalação das Dependências
No terminal, execute:
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

4. Executar o Script de Autodeploy
No terminal, execute:  python deploy_playstore.py --flavor <nome do flavor> 

Siga as instruções do script (informe caminhos, track, etc. se solicitado).

5. Verificação
Confira no Google Play Console se o upload foi realizado.
Verifique se o app está na track correta (internal, beta, production).
Checklist Final
 google-play-service.json presente e correto
 APK/AAB gerado
 Credenciais da Google Play API configuradas
 Dependências Python instaladas
 Script executado com sucesso
Posso inserir este passo a passo no seu README.md?
