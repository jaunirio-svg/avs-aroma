from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        item_l = item.lower()
        
        # --- BANCO DE DADOS DE CONTEXTO RÍGIDO ---
        if "asad" in item_l:
            info = "Lattafa Asad: Perfume Árabe. Visual: Frasco cilíndrico de vidro preto pesado, com 3 anéis dourados em relevo no corpo. Tampa metálica preta e dourada. Caixa luxuosa."
            cat = "Perfumaria de Elite"
            regras = "PROIBIDO falar de relógios, joias, telas, engrenagens ou notebooks. Fale apenas do frasco, do líquido e do ritual de borrifar."
        elif any(x in item_l for x in ["carro", "porsche", "ferrari"]):
            info = f"Veículo {item}. Visual: Interior em couro, volante com logo em destaque, ronco do motor e chave de presença."
            cat = "Automobilismo Premium"
            regras = "PROIBIDO falar de perfumes ou joias."
        else:
            info = f"Produto {item}. Foco em materiais nobres."
            cat = "Artigos de Luxo"
            regras = ""

        prompts = [
            f"Como Consultor de Luxo, analise a autoridade de '{item}'. Foque no peso da marca e qualidade dos materiais. (Max 10 linhas).",
            f"Como Estrategista, crie 3 ganchos para Stories sobre '{item}'. {regras}",
            f"Como Copywriter, escreva 2 legendas magnéticas para '{item}'. Inclua 'Link na Bio'. {regras}",
            f"Como Diretor de Arte, descreva 2 cenas de unboxing REALISTAS para '{item}'. CENA 1: O peso do objeto e a abertura da caixa. CENA 2: O detalhe visual específico ({info}). É TERMINANTEMENTE PROIBIDO falar de relógios ou joias se o produto for perfume.",
            f"Como Social Media, dê 10 hashtags de luxo e uma frase de impacto para '{item}'."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Você é um especialista em {cat}. Você escreve roteiros para um AFILIADO DE VENDAS. Seja 100% fiel ao produto {item}. {regras}"},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
