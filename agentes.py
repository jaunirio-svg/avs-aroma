from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        # A IA agora identifica sozinha se é perfume, relógio ou qualquer item de luxo
        diretriz = f"Analise o produto '{item}'. Identifique sua categoria e aplique diretrizes de luxo reais. Se for perfume, fale da pirâmide olfativa. Se for objeto, fale dos materiais e design. Proibido inventar acessórios externos."
        
        prompts = [
            f"Aja como CEO de Luxo: Defina o posicionamento premium para {item}. {diretriz}",
            f"Aja como Estrategista Viral: Crie 3 ganchos de atenção para TikTok sobre {item}. {diretriz}",
            f"Aja como Diretor de Fotografia: Gere 3 prompts de imagem 8k focados nos detalhes físicos de {item}. {diretriz}",
            f"Aja como Roteirista: Crie 2 roteiros de 12s para {item} focados em desejo e status. {diretriz}",
            f"Aja como Social Media: Sugira 10 hashtags da categoria de {item} e 3 legendas magnéticas com emojis."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "Você é um especialista em branding de luxo autônomo. Sua missão é identificar o produto e gerar conteúdo fiel às características reais dele."},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
