from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        item_l = item.lower()
        
        # --- FILTRO DE CONTEXTO REALISTA ---
        if "asad" in item_l:
            info_visual = "Frasco cilíndrico de vidro preto pesado, com 3 anéis dourados em relevo. Tampa metálica preta e dourada."
            cat = "Perfumaria Árabe de Luxo"
            proibido = "PROIBIDO falar de relógios, notebooks, telas ou joias. Fale apenas do perfume, do frasco e do cheiro."
        elif any(x in item_l for x in ["carro", "porsche", "ferrari"]):
            info_visual = "Interior em couro, volante esportivo e ronco do motor."
            cat = "Automobilismo Premium"
            proibido = "PROIBIDO falar de perfumes ou relógios."
        else:
            info_visual = "Acabamento artesanal e materiais nobres."
            cat = "Artigos de Luxo"
            proibido = ""

        prompts = [
            f"Como Consultor de Luxo, analise a autoridade de '{item}'. Foque na qualidade absoluta e na marca. (Máximo 10 linhas).",
            f"Como Estrategista, crie 3 ganchos de autoridade para Stories sobre '{item}'. {proibido}",
            f"Como Copywriter, escreva 2 legendas magnéticas para '{item}'. Foque no prazer de possuir este item específico. Termine com 'Link na Bio'.",
            f"Como Diretor de Arte, descreva 2 cenas de unboxing REALISTAS para '{item}'. Cena 1: O peso do objeto ao abrir a caixa. Cena 2: O detalhe visual de {info_visual}. É TERMINANTEMENTE PROIBIDO citar relógios ou eletrônicos.",
            f"Como Social Media, dê 10 hashtags de luxo e uma frase de impacto para '{item}'."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Você é um especialista em {cat}. Você cria conteúdo para um AFILIADO DE VENDAS. Seja fiel à realidade física do produto {item}. {proibido}"},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
