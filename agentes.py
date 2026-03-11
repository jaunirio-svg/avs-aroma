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
            f"Aja como Diretor de Arte: Descreva 2 cenas de unboxing/detalhe FOCO TOTAL EM '{item}'. Se for carro, foque na chave, no volante e no painel. Se for perfume, no peso do vidro e na tampa. Proibido citar outros objetos.",
munidade: Sugira 10 hashtags de nicho de luxo e uma frase de impacto para fixar sua autoridade como consultor."
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
