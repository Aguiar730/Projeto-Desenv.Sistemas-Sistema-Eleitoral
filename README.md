# Sistema Eleitoral 2026

## 📋 Sobre o Projeto

O Sistema Eleitoral 2026 é um projeto desenvolvido em Python com o objetivo de simular uma eleição presidencial entre candidatos fictícios. O sistema permite o cadastro de eleitores, validação da idade mínima para votação, registro de votos, apuração automática dos resultados e armazenamento dos dados em um arquivo CSV.

O projeto foi desenvolvido como atividade acadêmica do curso Técnico em Desenvolvimento de Sistemas, buscando aplicar conceitos fundamentais da linguagem Python de forma prática e interativa.

## 🎯 Objetivos

* Simular um processo eleitoral.
* Aplicar conceitos de programação em Python.
* Utilizar funções para organizar o código.
* Trabalhar com estruturas condicionais e de repetição.
* Realizar tratamento de erros.
* Manipular arquivos CSV para armazenamento de dados.
* Desenvolver habilidades de trabalho em equipe.

## ⚙️ Funcionalidades

* Cadastro de eleitores.
* Validação da idade mínima para votação.
* Escolha e confirmação do voto.
* Contabilização automática dos votos.
* Cálculo de porcentagem dos candidatos.
* Identificação do vencedor da eleição.
* Desempate automático por sorteio.
* Armazenamento dos dados dos eleitores em arquivo CSV.
* Consulta dos dados registrados.
* Interface interativa utilizando mensagens e efeitos de digitação.

## 📚 Bibliotecas Utilizadas

### time

Utilizada para criar pausas durante a execução do programa através da função `sleep()`.

### os

Utilizada para limpar a tela do terminal, proporcionando uma interface mais organizada.

### random

Responsável por realizar o sorteio de um vencedor em caso de empate.

### csv

Utilizada para armazenar e consultar os dados dos eleitores em arquivos CSV.

## 🛠️ Funções Desenvolvidas

### limpar_tela()

Limpa a tela do terminal durante a execução do programa.

### digitar(texto)

Exibe os textos gradualmente, simulando uma digitação.

### linha(), linha_2() e linha_3()

Criam divisões visuais para melhorar a organização da interface.

### confirmar_voto(nome)

Solicita a confirmação do voto antes de registrá-lo.

### decidir_empate(empate)

Realiza o sorteio de um vencedor quando ocorre empate entre candidatos.

## 🚀 Como Executar

1. Certifique-se de possuir o Python instalado.
2. Faça o download do arquivo `Sistema Eleitoral.py`.
3. Execute o programa através do terminal:

```bash
python "Sistema Eleitoral.py"
```

4. Siga as instruções exibidas na tela.

## 📂 Estrutura dos Dados

Os dados dos eleitores são armazenados automaticamente no arquivo:

```text
Dados dos Eleitores.csv
```

Cada registro contém:

* Nome do eleitor
* Idade
* Candidato escolhido

## 👥 Integrantes do Grupo

* Kauã
* Victor
* Gabriel
* Ruan
* Daniel

## 📝 Considerações Finais

Durante o desenvolvimento do projeto, foram enfrentados desafios relacionados à integração do código e correção de erros. Com pesquisas, testes e orientação do professor, a equipe conseguiu concluir o sistema de forma funcional, aplicando diversos conceitos estudados ao longo do curso.

Este projeto contribuiu para o aprimoramento dos conhecimentos em programação, lógica computacional, organização de código e trabalho em equipe.

