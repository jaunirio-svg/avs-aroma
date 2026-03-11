from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, perfume):
        prompts = [
            f"Aja como CEO de uma Grife: Defina o posicionamento de altíssimo luxo para o perfume {perfume}. Fale sobre a pirâmide olfativa (notas de saída, corpo e fundo) e o desejo que ele desperta. Use linguagem elegante.",
            f"Aja como Influenciador de Elite: Crie 3 ganchos para o TikTok sobre o perfume {perfume}. Foque no 'Efeito que ele causa ao passar' e no 'Rastro irresistível'.",
            f"Aja como Fotógrafo de Luxo: Gere 3 prompts técnicos de imagem para o perfume {perfume}. Estilo 'Cinematic, 8k, High-end luxury, Soft lighting, Glass reflections'.",
            f"Aja como Copywriter Viral: Crie 2 roteiros de 12 segundos para o perfume {perfume}. Use ganchos de curiosidade e luxo extremo.",
            f"Aja como Especialista em TikTok Shop: Sugira 10 hashtags de perfumaria fina e 3 opções de legendas prontas (Uma Curta, Uma Misteriosa e Uma de Venda) com emojis."
        ]
        
        respostas = []
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "Você é um especialista em perfumaria de luxo e marketing viral. Nunca fale sobre software ou TI."},
                          {"role": "user", "content": p}]
            )
            respostas.append(completion.choices[0].message.content)
        return respostas
