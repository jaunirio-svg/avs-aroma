from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        item_l = item.lower()
        
        # --- DEFINIÇÃO RÍGIDA DE CONTEXTO ---
        if "asad" in item_l:
            info = "Produto: Perfume Lattafa Asad. Visual: Frasco cilíndrico preto com anéis dourados em relevo. Notas: Tabaco, Café e Pimenta."
            cat = "Perfumaria Árabe"
        elif any(x in item_l for x in ["porsche", "carro", "bmw"]):
            info = f"Produto: Veículo {item}. Visual: Design aerodinâmico, interior em couro e ronco do motor."
            cat = "Automobilismo de Luxo"
        else:
            info = f"Produto: {item}. Foco em exclusividade e materiais nobres."
            cat = "Luxo Geral"

        # Prompts extremamente restritivos para evitar erros
        prompts = [
            f"Aja como Consultor: Análise técnica de '{item}'. Foque na autoridade da marca e qualidade dos materiais. Baseie-se em: {info}.",
            f"Aja como Estrategista: 3 ganchos para Stories sobre '{item}'. Proibido citar outros produtos.",
            f"Aja como Copywriter: 2 legendas magnéticas para '{item}'. Fale sobre o status de possuir este item específico.",
            f"Aja como Diretor de Vídeo: Descreva 2 cenas de unboxing focadas APENAS em '{item}'. Se for perfume, descreva o vidro e a tampa. Se for carro, a chave e o volante. É PROIBIDO falar de relógios ou celulares.",
            f"Aja como Social Media: 10 hashtags e uma frase de autoridade para '{item}'."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Você é um especialista em {cat}. Você NUNCA usa exemplos de outras categorias. Se o produto é {item}, fale apenas sobre as características físicas e sensoriais de {item}."},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
