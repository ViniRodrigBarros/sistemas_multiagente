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

##👥 Público-Alvo
Desenvolvedores de aplicativos Flutter que desejam automatizar seu processo de entrega contínua.

Equipes de software com foco em qualidade, produtividade e integração contínua.

Startups e empresas que lançam atualizações frequentes de seus apps.

##🤖 Agentes Envolvidos
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

## 📦 Entradas e Saídas Esperadas
**Entradas:**
- Quais dados o sistema recebe?

**Saídas:**
- Quais ações ou informações ele gera?

## 🔁 Interação entre os Agentes
Descreva como os agentes vão se comunicar ou se coordenar.
Pode ser uma descrição textual ou um fluxograma em breve.

## 🗂️ Organização e Planejamento do Projeto
O progresso deste projeto será monitorado através do **GitHub Projects**.

> Acesse a aba "Projects" do repositório para acompanhar:
- Tarefas pendentes
- Tarefas em andamento
- Tarefas concluídas

Cada integrante deve ser responsável por pelo menos uma tarefa no quadro.
Use etiquetas (labels) e comentários para detalhar o andamento e as decisões.

## 📌 Status Inicial do Projeto
- [ ] Ideia discutida e validada com o professor
- [ ] Estrutura básica do repositório criada
- [ ] Quadro no GitHub Projects criado
- [ ] Primeiras tarefas definidas e atribuídas

## 📄 Documentação Futura
Este repositório poderá incluir:
- Diagramas de arquitetura
- Relatórios parciais de progresso
- Scripts de testes ou simulações
- Resultados e conclusões finais

## 👨‍🏫 Acompanhamento pelo Professor
Para que o professor possa acompanhar e orientar o andamento do projeto, **adicione o usuário `igorbarcosta` como colaborador do repositório.**

### Como fazer:
1. Vá até a aba **"Settings"** do seu repositório.
2. Clique em **"Collaborators"** no menu lateral.
3. Digite o nome de usuário: `igorbarcosta`
4. Clique em **"Add collaborator"** e confirme.
