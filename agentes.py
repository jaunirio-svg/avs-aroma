from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        item_l = item.lower()
        
        # Manter a precisão técnica para evitar relógios, mas restaurar o tom de luxo
        if "asad" in item_l:
            desc_tecnica = "Lattafa Asad. Notas: Tabaco, Café e Pimenta. Frasco: Vidro preto maciço, anéis dourados em relevo, tampa metálica pesada."
            cat = "Perfumaria Árabe de Luxo"
        else:
            desc_tecnica = f"Produto {item} de alta gama."
            cat = "Artigos de Luxo"

        prompts = [
            # 1. ANÁLISE TÉCNICA (O CORAÇÃO DO PROJETO)
            f"Aja como Consultor de Luxo. Escreva uma 'Análise Técnica: A Supremacia de {item}'. Use a estrutura: Materiais de Alta Qualidade, Autoridade da Marca, Performance de Elite e Conclusão. Use um tom erudito e imponente. Base: {desc_tecnica}.",
            
            # 2. GANCHOS DE AUTORIDADE
            f"Aja como Especialista em Luxo. Crie 3 Ganchos de Autoridade para Stories. Use títulos fortes como 'O Padrão de Excelência' ou 'A Escolha dos Connoisseurs'. Explique por que quem entende escolhe o {item}.",
            
            # 3. LEGENDAS DE ALTO PADRÃO
            f"Aja como Copywriter de Elite. Escreva 2 legendas que foquem no 'Prazer da Exclusividade' e no 'Reconhecimento Social'. Use linguagem magnética e termine com Link na Bio.",
            
            # 4. ROTEIRO DE UNBOXING (RESTAURANDO A EXPERIÊNCIA SENSORIAL)
            f"Aja como Diretor de Arte. Descreva 2 Cenas de Unboxing cinematográficas para {item}. Foque na iluminação, na textura da caixa, no peso do {item} e no som (clique, spray ou manuseio). PROIBIDO CITAR RELÓGIOS OU TECNOLOGIA. Foque apenas no {cat}.",
            
            # 5. HASHTAGS E FRASE DE IMPACTO
            f"Aja como Gestor de Comunidade de Luxo. Forneça 10 hashtags de nicho e uma frase de impacto que fixe sua autoridade como guardião da exclusividade."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Você é o Especialista Supremo em {cat}. Sua linguagem é formal, sofisticada e autoritária. Siga rigorosamente a estrutura de tópicos solicitada, usando Markdown para destacar cabeçalhos e negritos."},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
