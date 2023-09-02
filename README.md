# Sistema Bancário com Python

Repositório do Desafio de Projeto referente ao módulo _Dominando Python Para Ciência de Dados_, parte do bootcamp **Potência Tech powered by iFood | Ciência de Dados com Python**.

> 📌 O projeto está dividido em duas partes: _Criando o Sitema Bancário com Python_ e _Aprimorando o Sistema Bancário com Funções no Python_.

<br>

---

## 🧮 Criando o Sistema Bancário com Python

Aqui temos a primeira parte do projeto, ou primeira versão do programa "sistema bancário". Nesta versão, não era necessário o trabalho com mais de um cliente e o sistema requeria apenas 3 (três) operações básicas: depósito, saque e visualização do extrato.

- Depósito: possível depositar valores positivos. Ser armazenado em uma variável e exibido no extrato.
- Saque: permitir máximo de 3 (três) saques diários com limite de R$500 reais cada. Caso não tenha saldo, exibir mensagem de erro. Ser armazenado em uma variável e exibido no extrato.
- Extrato: listar todos saques e depósitos. No final, exibir o saldo da conta no formato R$XXX.XX

---

## 💳 Aprimorando o Sistema Bancário com Python

Nesta segunda versão do programa "sistema bancário", iremos deixar o código modularizado criando funções para as operações já existentes - depósito, saque e extrato. Porém, estas devem seguir algumas restrições:

- Saque: receber os argumentos apenas por nome (keyword only).
- Depósito: receber os argumentos apenas por posição (positional only).
- Extrato: receber os argumentos por nome e posição (positional only and keyword only). Argumento posicional: saldo; argumento nomeado: extrato.

Ainda, devemos criar duas novas funções:

- Criar cliente: armanezar os clientes em uma lista, sendo cada cliente composto por nome, data de nascimento, cpf e endereço. O endereço deve ser uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. O CPF deve ser armazenado apenas os números, e não pode haver dois cadastros na mesma conta.

- Criar conta bancária: armazenar as contas em uma lista, sendo cada conta composta por agência, número da conta e cliente. O número da conta é sequencial, iniciando em 1 e agência fixa: "0001".


