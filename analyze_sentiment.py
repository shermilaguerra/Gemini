from google import genai

# Configure sua API Key
GEMINI_API_KEY = "AIzaSyCZdiJnmwjEUbxXvENpW4dknNSZnA_qzyE"
client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_sentiment(texto):
    prompt = f"""Analise o sentimento do texto abaixo.
    Retorne apenas: Positivo, Negativo ou Neutro.
    Texto: {texto}"""
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",  # ou "gemini-2.0-flash-exp" se preferir
        contents=prompt
    )
    return response.text.strip()

# Exemplo de uso
comentario = "O atendimento foi rápido e resolveu meu problema!"
print(analyze_sentiment(comentario))
