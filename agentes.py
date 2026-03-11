from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        # Identificação de Categoria para evitar misturar perfume com outros itens
        item_lower = item.lower()
        perfumes_conhecidos = {
            "asad": "Perfume Árabe Lattafa Asad. Notas: Pimenta Preta, Tabaco, Café, Baunilha. Frasco preto com anéis dourados.",
            "club de nuit": "Perfume Árabe Armaf Club de Nuit Intense. Notas: Limão, Abacaxi, Bétula, Almíscar. Frasco preto com corrente."
        }

        # Define o contexto baseado no que o usuário digitou
        contexto = "Produto de Luxo Geral"
        eh_perfume = False

        for nome, info in perfumes_conhecidos.items():
            if nome in item_lower:
                contexto = info
                eh_perfume = True
                break
        
        # Ajuste dinâmico de tom de voz
        if eh_perfume:
            instrucao_nicho = "Foque em Pirâmide Olfativa, rastro, fixação e design do frasco."
        else:
            instrucao_nicho = "Foque em engenharia, materiais nobres, durabilidade, legado e status técnico do objeto."

        prompts = [
            f"Aja como CEO: Defina o posicionamento de luxo de '{item}' baseado em: {contexto}. {instrucao_nicho}",
            f"Aja como Estrategista Viral: 3 ganchos TikTok para '{item}'. Use 'Status', 'Exclusividade' e 'Desejo'.",
            f"Aja como Diretor de Arte: 3 prompts 8k para '{item}'. Foque nas texturas reais (metal, couro, vidro ou fibra de carbono).",
            f"Aja como Roteirista: 2 roteiros de 12s para '{item}'. Mostre o produto em um ambiente que exale sucesso.",
            f"Aja como Social Media: 10 hashtags específicas para a categoria de '{item}' e 3 legendas magnéticas."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Você é um consultor de branding de luxo. Identifique o produto e use APENAS termos da categoria dele. Se não for perfume, não fale de cheiro. Se for objeto, fale de design e utilidade."},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
