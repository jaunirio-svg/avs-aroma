from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, perfume):
        prompts = [
            f"Aja como CEO de uma Grife: Defina o posicionamento de luxo para o perfume {perfume}. Foque na pirâmide olfativa e no desejo.",
            f"Aja como estrategista de TikTok: Crie 3 ganchos virais para o perfume {perfume}. Foque em 'rastro' e 'elogios'.",
            f"Aja como Fotógrafo: Gere 3 prompts de imagem para o perfume {perfume} (Estilo Luxo, Cinematic, 8k).",
            f"Aja como Roteirista: Crie 2 roteiros de 12 segundos para o perfume {perfume} focados em desejo e status.",
            f"Aja como Social Media de Perfumaria: Sugira 10 hashtags e 3 legendas prontas com emojis para o perfume {perfume}."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "Você é um especialista em marketing de perfumaria de luxo. Sua missão é criar estratégias de venda e viralização para perfumes, unindo sofisticação e ganchos de atenção para redes sociais."},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
