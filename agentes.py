from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        item_l = item.lower()
        
        # --- FILTRO RÍGIDO DE PRODUTO ---
        if "asad" in item_l:
            contexto_visual = "Frasco de vidro preto maciço, anéis dourados em relevo no corpo do frasco, tampa pesada com encaixe firme."
            cat = "Perfumaria Árabe de Luxo"
            regras = "PROIBIDO falar de relógios, notebooks, telas ou joias. Foque apenas no perfume, no frasco e no cheiro de tabaco/café."
        elif any(x in item_l for x in ["carro", "porsche", "ferrari"]):
            contexto_visual = "Interior em couro, volante esportivo, chave de presença e ronco do motor."
            cat = "Automobilismo Premium"
            regras = "PROIBIDO falar de perfumes ou relógios. Foque no carro e na performance."
        else:
            contexto_visual = "Acabamento artesanal e materiais nobres."
            cat = "Luxo Geral"
            regras = ""

        prompts = [
            f"Como Consultor, analise a autoridade de '{item}'. Foque na qualidade absoluta. (Max 10 linhas).",
            f"Como Estrategista, crie 3 ganchos para Stories sobre '{item}'. {regras}",
            f"Como Copywriter, escreva 2 legendas magnéticas para '{item}'. Foque no prazer de possuir este item específico.",
            f"Como Diretor, descreva 2 cenas de unboxing de '{item}'. DESCRIÇÃO OBRIGATÓRIA: Descreva o {contexto_visual}. É TERMINANTEMENTE PROIBIDO citar relógios, ponteiros ou eletrônicos. Se falar algo fora de {cat}, o texto será descartado.",
            f"Como Social Media, dê 10 hashtags e uma frase de impacto para '{item}'."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Você é um especialista em {cat}. Sua linguagem é técnica e imponente. {regras}"},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
