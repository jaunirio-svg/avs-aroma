from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        item_l = item.lower()
        
        # --- FILTRO RÍGIDO DE CONTEXTO ---
        if "asad" in item_l or "perfume" in item_l or "aroma" in item_l:
            cat = "Perfumaria de Luxo"
            persona = "Especialista em Fragrâncias Árabes"
            detalhes_base = "Frasco de vidro pesado, tampa metálica, spray de alta névoa, notas de tabaco e especiarias. Proibido falar de relógios ou eletrônicos."
        elif any(x in item_l for x in ["carro", "porsche", "ferrari", "bmw"]):
            cat = "Automobilismo Premium"
            persona = "Consultor Automotivo de Luxo"
            detalhes_base = "Chave de presença, couro legítimo, costura à mão, ronco do motor boxer. Proibido falar de perfumes."
        else:
            cat = "Artigos de Luxo"
            persona = "Curador de Estilo"
            detalhes_base = "Acabamento artesanal e materiais nobres."

        # Prompts redesenhados para serem 'impossíveis' de errar
        prompts = [
            f"Como {persona}, faça uma análise técnica da autoridade de '{item}'. Foque na marca e qualidade. (Máximo 15 linhas).",
            f"Como Estrategista, crie 3 ganchos de autoridade para Stories sobre '{item}'. Foque no status de usar este produto específico.",
            f"Como Copywriter, escreva 2 legendas magnéticas para '{item}'. Foque em exclusividade e no prazer da posse.",
            f"Como Diretor, descreva 2 cenas de unboxing de '{item}'. DESCRIÇÃO OBRIGATÓRIA: Se for perfume, descreva o vidro preto e os anéis dourados. Se for carro, descreva o interior e a chave. PROIBIDO CITAR OUTROS PRODUTOS.",
            f"Como Social Media, dê 10 hashtags de luxo e uma frase de impacto para '{item}'."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Você é um especialista em {cat}. Sua missão é criar conteúdo para um AFILIADO DE VENDAS. Seja fiel ao produto '{item}'. {detalhes_base}"},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
