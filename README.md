Controle de Contas Bancárias com API REST
Este projeto implementa uma API RESTful para gerenciar contas bancárias e realizar operações como depósitos, saques e transferências. Ele é construído usando Python com o framework Flask.

Funcionalidades Implementadas
Endpoints da API:

POST /reset: Reinicia o sistema, limpando todos os dados das contas.
GET /balance?account_id=<account_id>: Retorna o saldo da conta especificada.
POST /event: Permite realizar operações como depósito, saque e transferência entre contas.
Operações Suportadas:

Depósito em uma conta existente.
Saque de uma conta existente.
Transferência entre contas.
Estrutura do Projeto
app.py: Arquivo principal contendo a aplicação Flask com os endpoints da API.
services.py: Lógica de negócios para manipulação de contas e transações.
tests/: Diretório contendo testes automatizados para verificar o funcionamento correto da API.
requirements.txt: Lista de dependências Python necessárias para executar o projeto.
Tecnologias Utilizadas
Python
Flask# ebanx_test
