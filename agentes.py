from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        item_l = item.lower()
        
        # --- BANCO DE DADOS DE CONHECIMENTO ---
        contexto = "Produto de Luxo Premium"
        categoria = "Geral"

        # Lógica de Perfumes
        if "asad" in item_l:
            contexto = "Lattafa Asad: Notas de Pimenta Preta, Tabaco, Café e Baunilha. Frasco preto com anéis dourados."
            categoria = "Perfume"
        elif "club de nuit" in item_l:
            contexto = "Armaf Club de Nuit: Notas de Limão, Bétula e Almíscar. Rastro intenso e medalhão no frasco."
            categoria = "Perfume"
        
        # Lógica de Carros
        elif any(x in item_l for x in ["carro", "porsche", "ferrari", "lamborghini", "bmw", "mercedes", "audi", "mclaren"]):
            contexto = f"Veículo de Alta Performance {item}. Foco em aerodinâmica, cavalaria, ronco do motor e fibra de carbono."
            categoria = "Carro"

        # --- DEFINIÇÃO DE INSTRUÇÕES POR CATEGORIA ---
        if categoria == "Perfume":
            instrucao = "Fale de notas olfativas, rastro magnético e elegância do frasco."
        elif categoria == "Carro":
            instrucao = "Fale de torque, potência, velocidade, status nas ruas e o prazer de dirigir uma máquina."
        else:
            instrucao = "Fale de materiais nobres, engenharia de precisão, exclusividade e legado da marca."

        prompts = [
            f"Aja como CEO: Defina o DNA de luxo de '{item}'. Contexto: {contexto}. {instrucao}",
            f"Aja como Estrategista Viral: 3 ganchos TikTok para '{item}'. Foque no desejo e na conquista do topo.",
            f"Aja como Fotógrafo: 3 prompts 8k específicos para '{item}'. Se for carro, detalhe a pintura e as rodas. Se for perfume, o vidro.",
            f"Aja como Roteirista: 2 roteiros de 12s para '{item}'. Foque na experiência sensorial (o som do motor ou o rastro do cheiro).",
            f"Aja como Social Media: 10 hashtags e 3 legendas magnéticas para '{item}'."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Você é um consultor de luxo. Categoria atual: {categoria}. PROIBIDO misturar categorias. Se for carro, não fale de cheiro. Se for perfume, não fale de motor."},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
