# 🔐 STRIDE Threat Analysis API

Este projeto implementa uma **API REST** desenvolvida com **FastAPI**, **Python** e **Azure OpenAI**, capaz de realizar **análise de ameaças STRIDE** a partir de imagens com diagramas de arquitetura de sistemas.

---

## 🎯 Objetivo

- Receber uma imagem de arquitetura (ex: desenho de sistemas)
- Utilizar **engenharia de prompt** com Azure OpenAI para:
  - Realizar uma **análise automática de ameaças** segundo a metodologia **STRIDE**:
    - Spoofing
    - Tampering
    - Repudiation
    - Information Disclosure
    - Denial of Service
    - Elevation of Privilege
- Retornar os riscos detectados em formato JSON

---

## 🧱 Tecnologias

- [Python 3.11+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Azure OpenAI (GPT-4)](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Uvicorn](https://www.uvicorn.org/)
- [Base64 (imagem como texto)]

---

## 🚀 Como executar localmente

### 1. Clone o repositório

---

git clone https://github.com/seu-usuario/stride-analysis-api.git

cd stride-analysis-api

---

## 2. Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

---

## 3. Instale as dependências
pip install -r requirements.txt

---

4. Configure as variáveis de ambiente

Crie um arquivo .env com suas credenciais do Azure OpenAI:

AZURE_OPENAI_KEY=your-azure-api-key

AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/

---

5. Execute a API
uvicorn app.main:app --reload

Acesse a documentação interativa em:

📍 http://localhost:8000/docs

---

📦 Estrutura de diretórios
stride-analysis-api/
├── app/

│   ├── main.py

│   ├── utils.py

│   └── prompt_templates.py

├── requirements.txt

├── .env

└── README.md

🔍 Exemplo de uso

✅ Requisição:

POST /analyze

Parâmetro: upload de imagem .jpg ou .png

✅ Resposta esperada:
{
  "result": {
    "Spoofing": "Usuários podem se passar por outros sem autenticação entre serviços.",
    "Tampering": "Não há verificação de integridade entre APIs.",
    "Repudiation": "Falta de registros confiáveis de ações do usuário.",
    "Information Disclosure": "Informações sensíveis expostas sem criptografia.",
    "Denial of Service": "Não há limitação de requisições no gateway.",
    "Elevation of Privilege": "Permissões amplas atribuídas a todos os usuários."
  }
}

📚 Referências

STRIDE Threat Modeling

Azure OpenAI Docs

FastAPI
