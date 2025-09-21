import base64
import os
from openai import AzureOpenAI
from app.prompt_templates import BASE_PROMPT

def generate_stride_analysis(image_bytes: bytes):
    # Codifica a imagem em base64
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

    # Constrói o prompt
    prompt = BASE_PROMPT.format(image_data=image_b64)

    # Configura o cliente da Azure OpenAI
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        api_version="2023-07-01-preview",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )

    # Envia para o modelo GPT
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return {
        "result": response.choices[0].message.content
    }
