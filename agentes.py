from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, perfume):
        # Reforçamos que o objeto é sempre um PERFUME DE LUXO
        prompts = [
            f"Aja como CEO Estrategista: Defina o posicionamento de luxo e público-alvo para o PERFUME {perfume}. Foque em fragrância e olfato.",
            f"Aja como Caçador de Tendências: Crie 3 ganchos virais para o PERFUME {perfume} no TikTok. Foque no cheiro e na reação das pessoas.",
            f"Aja como Engenheiro de Prompts: Gere 3 descrições para imagens (Hero, Lifestyle e Luxo) do frasco do PERFUME {perfume}.",
            f"Aja como Analista de Viralização: Crie um roteiro de 12 segundos para o PERFUME {perfume}. O foco é sedução e elegância.",
            f"Aja como Analista de Algoritmo: Sugira 10 hashtags de PERFUMARIA e o melhor CTA para vender o PERFUME {perfume} no link da bio."
        ]
        
        respostas = []
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": p}]
            )
            respostas.append(completion.choices[0].message.content)
        return respostas
