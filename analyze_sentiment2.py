from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class SentimentAnalysis(BaseModel):
    sentimento_geral: str = Field(description="Sentimento geral expresso no texto (ex: positivo, negativo, neutro, muito negativo)")
    emocao_principal: str = Field(description="Emoção predominante no texto (ex: raiva, frustração, decepção, ansiedade)")
    intensidade_emocional: str = Field(description="Intensidade da emoção (baixa, média, alta)")
    
class TopicAnalysis(BaseModel):
    topicos_principais: List[str] = Field(description="Lista dos principais tópicos mencionados no texto")
    topicos_secundarios: List[str] = Field(description="Lista de tópicos secundários mencionados")

class CustomerBehavior(BaseModel):
    urgencia: str = Field(description="Nível de urgência expresso pelo cliente (ex: baixa, média, alta)")
    comportamento_cliente: List[str] = Field(description="Comportamentos do cliente identificados (ex: persistente, indignado, paciente)")
    acoes_esperadas: List[str] = Field(description="Ações que o cliente espera que sejam tomadas")

class Metadata(BaseModel):
    metadados_uteis: dict = Field(description="Metadados úteis extraídos do texto como entidades, números, prazos, etc.")
    
class CustomerFeedbackAnalysis(BaseModel):
    sentimento_geral: str
    emocao_principal: str
    topicos_mencionados: List[str]
    urgencia: str
    comportamento_do_cliente: List[str]
    acoes_esperadas_pelo_cliente: List[str]
    metadados_uteis: dict

client = genai.Client()

texto_cliente = """
Assunto: Demora no atendimento e falta de retorno

Estou extremamente insatisfeito com o atendimento que venho recebendo de uma concessionária Toyota da minha cidade. Levei meu veículo para revisão há mais de 10 dias e até agora não tive nenhum retorno concreto sobre o diagnóstico. Ligo todos os dias e a resposta é sempre a mesma: "vamos verificar e te retornamos". O retorno nunca acontece. Fui informado de que o problema seria simples e que ficaria pronto em até 3 dias, mas até agora nada. Além disso, quando pergunto se há previsão, os atendentes parecem despreparados, sem paciência e transfiram minha ligação várias vezes sem solução. Estou sem meu carro, precisando me deslocar para o trabalho e dependendo de transporte por aplicativo, o que está gerando um custo extra que não estava nos meus planos. Pior de tudo é ver que outras pessoas que chegaram depois de mim já tiveram seus carros prontos. Sinto que não estou sendo tratado com a prioridade que um cliente fiel da marca merece. Espero que a Toyota tome providências quanto a essa situação, porque do jeito que está, está manchando a imagem de uma marca que sempre admirei.
"""

prompt = f"""
Por favor, analise o seguinte texto de reclamação de um cliente e extraia as informações solicitadas.

Texto do cliente:
{texto_cliente}

Extraia do texto:
- Sentimento geral expresso pelo cliente
- Emoção principal identificada
- Tópicos principais mencionados na reclamação
- Nível de urgência da situação
- Comportamentos do cliente demonstrados no texto
- Ações que o cliente espera que sejam tomadas
- Metadados úteis como: números mencionados (prazos, quantidade de dias), entidades (marca, departamentos), custos extras, comparações com outros clientes

Responda em formato JSON seguindo o schema especificado.
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": CustomerFeedbackAnalysis.model_json_schema(),
    },
)

analise = CustomerFeedbackAnalysis.model_validate_json(response.text)
print(analise.model_dump_json(indent=2))
