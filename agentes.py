from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        # Instrução reforçada para identificar o produto sem "alucinar" categorias erradas
        diretriz = f"Analise o produto '{item}'. Se for um perfume árabe (como Lattafa, Maison Alhambra), identifique as notas reais. Se for outro item de luxo, mantenha o foco técnico. Proibido confundir marcas de luxo com culinária ou itens genéricos."
        
        prompts = [
            f"Aja como CEO: Forneça detalhes técnicos REAIS de {item}. Se for perfume, use a pirâmide olfativa correta (Ex: Asad da Lattafa tem notas de pimenta preta, tabaco e baunilha).",
            f"Aja como Estrategista: 3 ganchos TikTok para {item}. Foque no rastro e exclusividade.",
            f"Aja como Diretor de Arte: 3 prompts 8k focados no frasco/design real de {item}. Descreva o acabamento físico (ouro, preto, relevos).",
            f"Aja como Roteirista: 2 roteiros de 12s focados no uso de {item} em ambientes de alto padrão.",
            f"Aja como Social Media: 10 hashtags e 3 legendas magnéticas para {item}. (Mantenha o foco em perfumaria e lifestyle de luxo)."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "Você é um expert em Branding de Luxo. Você conhece profundamente perfumes árabes e marcas premium. Se o usuário digitar apenas o nome de um perfume famoso, você DEVE recuperar os dados reais dele no seu banco de dados."},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
