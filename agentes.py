from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        item_l = item.lower()
        
        # --- BASE DE CONHECIMENTO TÉCNICO ---
        if "asad" in item_l:
            detalhes = "Lattafa Asad: Obra-prima árabe. Notas densas de Tabaco, Café e Pimenta. Performance de elite e presença de impacto."
            cat = "Perfume"
        elif any(x in item_l for x in ["carro", "porsche", "ferrari", "bmw"]):
            detalhes = f"Engenharia de ponta {item}. Performance, aerodinâmica e legado de vitórias."
            cat = "Carro"
        else:
            detalhes = f"Produto Premium {item}. Excelência em materiais e acabamento superior."
            cat = "Geral"

        prompts = [
            f"Aja como Consultor de Luxo: Crie uma análise técnica sobre a superioridade de '{item}'. Foque na qualidade dos materiais e na autoridade da marca. {detalhes}. (Proibido falar de preços ou descontos).",
            f"Aja como Especialista: Crie 3 ganchos de autoridade para Stories. Mostre por que quem entende de verdade escolhe o '{item}'.",
            f"Aja como Copywriter de Elite: Escreva 2 legendas de alto padrão. O foco deve ser o 'prazer da exclusividade' e o 'reconhecimento social' que o produto traz.",
            f"Aja como Diretor de Arte: Descreva 2 cenas de unboxing que pareçam um ritual de luxo. Foque no peso do produto e nos detalhes de acabamento.",
            f"Aja como Gestor de Comunidade: Sugira 10 hashtags de nicho de luxo e uma frase de impacto para fixar sua autoridade como consultor."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "Você é um Consultor de Autoridade em Luxo. Sua linguagem é refinada, técnica e imponente. Você não vende preço, você vende excelência, performance e status. O foco é a qualidade absoluta."},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
