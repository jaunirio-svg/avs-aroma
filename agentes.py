from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        item_l = item.lower()
        
        # --- BANCO DE DADOS RESTRITIVO ---
        if "asad" in item_l:
            detalhes = "Lattafa Asad: Perfume Árabe. Frasco cilíndrico preto, anéis dourados em relevo, tampa pesada. Líquido denso."
            cat = "Perfume"
        elif any(x in item_l for x in ["porsche", "carro", "ferrari"]):
            detalhes = f"Veículo {item}. Couro, fibra de carbono, ronco do motor, chave de presença."
            cat = "Automóvel"
        else:
            detalhes = f"Produto {item}. Materiais premium e acabamento de alta gama."
            cat = "Geral"

        prompts = [
            f"Aja como Consultor de Luxo: Análise técnica de '{item}'. Foque na autoridade e qualidade absoluta. Base: {detalhes}.",
            f"Aja como Especialista: 3 ganchos de autoridade para Stories focados EXCLUSIVAMENTE em '{item}'.",
            f"Aja como Copywriter de Elite: 2 legendas magnéticas para '{item}'. Fale de status e do prazer de possuir este item específico.",
            f"Aja como Diretor de Arte: Descreva 2 cenas de unboxing de '{item}'. É PROIBIDO falar de relógios ou tecnologia. Foque no material real de '{item}': se for perfume, fale do vidro e da tampa; se for carro, fale do volante e couro. Descreva o som real desse produto.",
            f"Aja como Social Media: 10 hashtags de nicho e uma frase de impacto que firme sua autoridade sobre '{item}'."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Você é um Consultor de Luxo focado em converter vendas por autoridade. Você NUNCA mistura categorias. Se o usuário pediu {cat}, você fala APENAS de {cat}. Seja técnico, imponente e detalhista."},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
