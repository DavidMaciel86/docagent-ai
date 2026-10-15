# 🤖 DocAgent AI

Agente de Inteligência Artificial desenvolvido em Python para análise
e interação com documentos PDF.

O projeto utiliza Agno para construção e orquestração do agente e
Groq para acesso ao modelo de linguagem.

## 🎯 Objetivo

Demonstrar de forma prática conceitos de:

- Agentes de IA
- Integração com LLMs via API
- Engenharia de prompts
- Processamento de documentos PDF
- Separação de responsabilidades
- Gerenciamento de dependências com UV
- Boas práticas com variáveis de ambiente

## 🧠 Como funciona

O DocAgent AI extrai o conteúdo textual de um documento PDF e permite
que o usuário converse com um agente de IA sobre as informações
presentes no documento.

Fluxo simplificado:

```text
PDF
 ↓
Extração de texto
 ↓
Contexto do documento
 ↓
Agente Agno
 ↓
LLM via Groq
 ↓
Resposta baseada no documento
```

## 🛠️ Tecnologias

- Python 3.12
- Agno
- Groq API
- PyPDF
- python-dotenv
- UV
- Git / GitHub

## 📂 Estrutura

```text
docagent-ai/
├── data/
│   └── exemplo.pdf
├── prompts/
│   ├── __init__.py
│   └── document_prompts.py
├── services/
│   ├── __init__.py
│   └── pdf_service.py
├── main.py
├── pyproject.toml
├── uv.lock
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Executando o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/DavidMaciel86/docagent-ai.git
```

### 2. Entre no diretório

```bash
cd docagent-ai
```

### 3. Instale as dependências

O projeto utiliza o UV para gerenciamento de dependências:

```bash
uv sync
```

### 4. Configure a variável de ambiente

Crie um arquivo `.env` na raiz do projeto com base em `.env.example`:

```env
GROQ_API_KEY=sua_chave_aqui
```

> O arquivo `.env` contém informações sensíveis e não deve ser versionado.

### 5. Execute o agente

```bash
uv run main.py
```

Após a inicialização, faça perguntas sobre o documento carregado. Para encerrar, digite `sair`.

## 💬 Exemplos de perguntas

O repositório inclui o arquivo `data/exemplo.pdf` para demonstração.

Após carregar o documento, experimente:

- Faça um resumo do documento.
- Quais itens são necessários para realizar uma pesquisa no Google?
- Qual é o passo a passo apresentado no documento?
- Quais navegadores são mencionados?
- Como posso refinar uma pesquisa?
- Para que servem as aspas em uma pesquisa no Google?
- Qual exemplo de pesquisa é apresentado?

### Teste de resposta fora do contexto

Experimente também:

- Como criar uma conta no Gmail?

Essa informação não está presente no PDF. O comportamento esperado é que
o Agente informe que não encontrou a resposta no documento, em vez de
inventar uma informação.

## 🏗️ Arquitetura

O projeto separa diferentes responsabilidades:

- `services/` — processamento e extração de conteúdo dos documentos.
- `prompts/` — comportamento e instruções do agente.
- `main.py` — criação do agente e fluxo principal da aplicação.

Essa separação permite evoluir o projeto futuramente sem concentrar
todas as responsabilidades em um único arquivo.

## 🔮 Possíveis evoluções

- Upload dinâmico de PDFs
- Interface web
- Suporte a múltiplos documentos
- Memória de conversação
- RAG
- API com FastAPI
- Deploy em ambiente cloud

## 📚 Contexto

Projeto desenvolvido como aplicação prática de estudos em Engenharia
de Agentes de IA, explorando Agno, APIs de modelos de linguagem e
desenvolvimento de aplicações de IA com Python.
