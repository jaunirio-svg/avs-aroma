from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        item_l = item.lower()
        
        # --- BASE DE CONHECIMENTO TÉCNICO ---
        if "asad" in item_l:
            detalhes = "Lattafa Asad: Notas densas de Tabaco, Café e Pimenta. Frasco cilíndrico preto com anéis dourados em relevo."
            cat = "Perfume"
        elif any(x in item_l for x in ["carro", "porsche", "ferrari", "bmw", "mercedes"]):
            detalhes = f"Veículo {item}. Engenharia de performance, acabamento em couro e fibra de carbono."
            cat = "Automóvel"
        else:
            detalhes = f"Produto {item}. Foco em materiais nobres e construção premium."
            cat = "Geral"

        prompts = [
            f"Aja como Consultor de Luxo: Análise técnica sobre '{item}'. Foque na qualidade e autoridade. Base: {detalhes}.",
            f"Aja como Estrategista: 3 ganchos de autoridade para Stories sobre '{item}'.",
            f"Aja como Copywriter de Elite: 2 legendas magnéticas para '{item}'. Fale de status e exclusividade.",
            f"Aja como Diretor de Arte: Descreva 2 cenas de unboxing EXCLUSIVAS de '{item}'. Foque no peso real, na textura do material de '{item}' e no som da abertura. PROIBIDO citar relógios ou celulares se o produto não for esse.",
            f"Aja como Social Media: 10 hashtags de luxo e uma frase de impacto para '{item}'."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Você é um Consultor de Luxo. Categoria: {cat}. Você é estritamente fiel ao produto '{item}'. Não use exemplos de outras categorias. Se for perfume, fale do frasco e líquido. Se for carro, fale da chave e motor."},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
