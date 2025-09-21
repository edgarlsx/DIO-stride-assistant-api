BASE_PROMPT = """
Você é um especialista em segurança da informação.
Abaixo está a imagem (em base64) de um diagrama de arquitetura de sistemas.

Sua tarefa é realizar uma análise de ameaças baseada na metodologia STRIDE:
- Spoofing
- Tampering
- Repudiation
- Information Disclosure
- Denial of Service
- Elevation of Privilege

Baseado na estrutura da arquitetura apresentada, identifique riscos associados a cada uma das seis categorias e retorne em **formato JSON**, como no exemplo abaixo:

{
  "Spoofing": "...",
  "Tampering": "...",
  "Repudiation": "...",
  "Information Disclosure": "...",
  "Denial of Service": "...",
  "Elevation of Privilege": "..."
}

Imagem codificada:
{image_data}
"""
