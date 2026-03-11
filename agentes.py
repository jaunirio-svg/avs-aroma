from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, perfume):
        prompts = [
            f"Aja como CEO de uma Grife: Defina o posicionamento de altíssimo luxo para o perfume {perfume}. Descreva a pirâmide olfativa (notas de saída, coração e base) e o status que ele entrega. Use português impecável e sofisticado.",
            f"Aja como Influenciador de Elite: Crie 3 ganchos para o TikTok sobre o perfume {perfume}. Foque no 'Rastro irresistível' e no 'Poder de atração'.",
            f"Aja como Fotógrafo de Luxo: Gere 3 prompts técnicos de imagem para o perfume {perfume}. Estilo 'Cinematic lighting, 8k, Luxury perfume bottle, studio background, elegant shadows'.",
            f"Aja como Copywriter Viral: Crie 2 roteiros de 12 segundos para o perfume {perfume}. Foque em mistério e desejo.",
            f"Aja como Especialista em TikTok Shop: Sugira 10 hashtags de perfumaria e 3 opções de legendas prontas com emojis."
        ]
        
        respostas = []
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "Você é um especialista em perfumaria de luxo francesa e árabe. Seu tom é elegante, persuasivo e focado exclusivamente em fragrâncias."},
                          {"role": "user", "content": p}]
            )
            respostas.append(completion.choices[0].message.content)
        return respuestas
