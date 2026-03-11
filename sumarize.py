from google import genai

# 1. Configurar a chave de API
GEMINI_API_KEY = "AIzaSyCZdiJnmwjEUbxXvENpW4dknNSZnA_qzyE"
client = genai.Client(api_key=GEMINI_API_KEY)

def resumir_texto_gemini(texto, max_palavras=50):
    """
    Função para resumir texto usando o Gemini.
    """
    # 2. Criar o prompt de instrução
    prompt = f"""
    Resuma o texto abaixo em no máximo {max_palavras} palavras.
    Forneça os pontos principais de forma concisa.
    
    Texto:
    \"\"\"{texto}\"\"\"
    
    Resumo:
    """

    # 3. Gerar o conteúdo usando o client
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    
    return response.text

# --- Exemplo de Uso ---
texto_longo = """
COROLLA CROSS GR-SPORT
Design: Teto solar elétrico com função antiesmagamento, rodas de liga leve 18" e saias esportivas laterais TOYOTA GAZOO Racing. Acabamento interno em couro, material sintético e ultrasuede na cor preta com costuras em vermelho.
Performance: Motor de 2.0 L Dual VVT-iE 16 V DOHC Flex com potência de 175 cv (E) e 21,3 Kgf.m de torque. Transmissão automática CVT de 10 velocidades.
Segurança: 7 airbags, sensores de estacionamento dianteiro e traseiro com suporte à frenagem de estacionamento, e TSS⁴ (Toyota Safety Sense) com controle adaptativo de velocidade de cruzeiro para todas as velocidades, assistente de pré-colisão, sistema de alerta de oscilação, farol alto automático e sistema de alerta de mudança de faixa com controle de direção.
"""

resumo = resumir_texto_gemini(texto_longo)
print(resumo)
