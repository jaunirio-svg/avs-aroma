from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        item_l = item.lower()
        
        # --- BLOQUEIO DE CONTEXTO ---
        if "asad" in item_l:
            info = "Produto: Perfume Lattafa Asad. Visual: Frasco cilíndrico preto, anéis dourados em relevo, tampa pesada. Notas: Tabaco e Café."
            cat = "Perfumaria Árabe"
            proibido = "Proibido falar de relógios, ponteiros, joias, diamantes ou notebooks."
        elif any(x in item_l for x in ["carro", "porsche", "ferrari"]):
            info = f"Produto: Veículo {item}. Visual: Couro, ronco do motor e chave de presença."
            cat = "Automóveis de Luxo"
            proibido = "Proibido falar de perfumes ou joias."
        else:
            info = f"Produto: {item}. Foco em materiais nobres."
            cat = "Luxo"
            proibido = ""

        prompts = [
            f"Como Consultor de Luxo, faça uma análise técnica da autoridade de '{item}'. (Máximo 10 linhas). Base: {info}",
            f"Como Estrategista, crie 3 ganchos para Stories sobre '{item}'. Foque no status de usar este produto específico. {proibido}",
            f"Como Copywriter, escreva 2 legendas magnéticas para '{item}'. Foque em exclusividade. {proibido}",
            f"Como Diretor de Vídeo, descreva 2 cenas de unboxing de '{item}'. DESCRIÇÃO OBRIGATÓRIA: Se for o perfume Asad, descreva o frasco de vidro preto, os anéis dourados e a caixa luxuosa. Se for carro, descreva o volante. {proibido}",
            f"Como Social Media, dê 10 hashtags de luxo e uma frase de impacto para '{item}'."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Você é um especialista em {cat}. Você NUNCA usa exemplos de outras categorias. Seja fiel às características físicas de {item}. {proibido}"},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
