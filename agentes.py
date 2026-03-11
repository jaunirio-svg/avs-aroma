from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, perfume):
        prompts = [
            f"Aja como CEO de uma Grife: Defina o posicionamento de altíssimo luxo para o perfume {perfume}. Fale sobre a pirâmide olfativa e o desejo que ele desperta.",
            f"Aja como Influenciador de Elite: Crie 3 ganchos para o TikTok sobre o perfume {perfume}. Foque no rastro e na atração.",
            f"Aja como Fotógrafo de Luxo: Gere 3 prompts técnicos de imagem para o perfume {perfume} (Estilo Cinematic, 8k, Luxury).",
            f"Aja como Copywriter Viral: Crie 2 roteiros de 12 segundos para o perfume {perfume}.",
            f"Aja como Especialista em TikTok Shop: Sugira 10 hashtags e 3 legendas prontas com emojis."
        ]
        
        # AQUI ESTAVA O ERRO: Nome da lista deve ser igual ao do return
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "Você é um especialista em perfumaria de luxo. Nunca fale de TI ou software."},
                          {"role": "user", "content": p}]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas # Corrigido para português
