Controle de Contas Bancárias com API REST

Este projeto implementa uma API RESTful para gerenciar contas bancárias e realizar operações como depósitos, saques e transferências. Ele é construído usando Python com o framework Flask.

Funcionalidades Implementadas

Endpoints da API:
- POST /reset: Reinicia o sistema, limpando todos os dados das contas.
- GET /balance?account_id=<account_id>: Retorna o saldo da conta especificada.
- POST /event: Permite realizar operações como depósito, saque e transferência entre contas.

Operações Suportadas:
- Depósito: Adiciona um valor a uma conta existente.
- Saque: Remove um valor de uma conta existente.
- Transferência: Move um valor de uma conta para outra conta existente.

Estrutura do Projeto
- app.py: Arquivo principal contendo a aplicação Flask com os endpoints da API.
- services.py: Lógica de negócios para manipulação de contas e transações.
- requirements.txt: Lista de dependências Python necessárias para executar o projeto.

Tecnologias Utilizadas
- Python
- Flask

Como Executar o Projeto
Clone o repositório:
 git clone https://github.com/seu_usuario/nome_do_projeto.git

Navegue até o diretório do projeto:
 cd nome_do_projeto

Crie um ambiente virtual:
 python -m venv venv

Ative o ambiente virtual:
- No Windows:
   venv\Scripts\activate

- No macOS/Linux:
  source venv/bin/activate

Instale as dependências:
 pip install -r requirements.txt

Execute a aplicação:
 flask run
