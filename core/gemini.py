from google import genai
import os
from dotenv import load_dotenv
load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

def product_information(product_list):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"""
Você irá receber um dicionário de produtos.
Gere um texto chamativo e formatado para ser compartilhado em um grupo de Telegram de promoções.

Regras:
- Foque em custo-benefício e praticidade
- Inclua uma piada leve
- Não inclua explicações
- Apenas retorne a mensagem final
- Se houver múltiplos dicionários, separe por '---'

Dados:
{product_list}
    """
    )
    return response.text
