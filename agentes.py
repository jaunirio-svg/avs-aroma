from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, perfume):
        prompts = [
            f"Aja como CEO Estrategista: Defina o posicionamento de luxo e público-alvo para o perfume {perfume}.",
            f"Aja como Caçador de Tendências: Crie 3 ganchos virais para o perfume {perfume} no TikTok.",
            f"Aja como Engenheiro de Prompts: Gere 3 descrições para imagens (Hero, Lifestyle e Luxo) do perfume {perfume}.",
            f"Aja como Analista de Viralização: Crie um roteiro de 12 segundos para {perfume}.",
            f"Aja como Analista de Algoritmo: Sugira 10 hashtags e o melhor CTA."
        ]
        
        respostas = []
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": p}]
            )
            respostas.append(completion.choices[0].message.content)
        return respostas
