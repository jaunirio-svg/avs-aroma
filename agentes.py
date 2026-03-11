from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        item_l = item.lower()
        
        # --- DEFINIÇÃO DE PERSONA E REGRAS RÍGIDAS ---
        if "asad" in item_l:
            p_nome = "Lattafa Asad (Perfume)"
            p_visual = "Frasco de vidro preto maciço, anéis dourados em relevo, tampa pesada metálica."
            p_cat = "Perfumaria de Nicho"
            regras = "PROIBIDO falar de relógios, notebooks, ponteiros, telas, diamantes ou joias. Foque apenas no perfume, no líquido e no frasco."
        elif any(x in item_l for x in ["carro", "porsche", "ferrari"]):
            p_nome = f"Carro {item}"
            p_visual = "Couro legítimo, volante esportivo, ronco do motor e chave de presença."
            p_cat = "Automobilismo Premium"
            regras = "PROIBIDO falar de perfumes ou relógios."
        else:
            p_nome = item
            p_visual = "Materiais nobres e acabamento artesanal."
            p_cat = "Artigos Premium"
            regras = ""

        prompts = [
            f"Como Consultor de {p_cat}, analise a autoridade de '{p_nome}'. Baseie-se no visual: {p_visual}. (Max 10 linhas).",
            f"Como Estrategista, crie 3 ganchos para Stories sobre '{p_nome}'. Mostre por que ele é um símbolo de poder. {regras}",
            f"Como Copywriter, escreva 2 legendas magnéticas para '{p_nome}'. Termine com 'Link na Bio'. {regras}",
            f"Como Diretor, descreva 2 cenas de unboxing EXCLUSIVAS de '{p_nome}'. Cena 1: O peso do frasco/item. Cena 2: O detalhe do material ({p_visual}). É TERMINANTEMENTE PROIBIDO citar outros produtos como relógios ou eletrônicos.",
            f"Como Social Media, dê 10 hashtags e uma frase de impacto para '{p_nome}'."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Você é um especialista focado em {p_cat}. Você é um AFILIADO DE VENDAS. Seja 100% fiel ao produto {p_nome}. {regras}"},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
