from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        # Base de Conhecimento Blindada
        if "asad" in item.lower():
            info_tecnica = """
            PRODUTO: Lattafa Asad (Perfume Árabe).
            NOTAS REAIS: Pimenta Preta, Abacaxi, Tabaco, Café, Patchouli, Sândalo, Baunilha, Âmbar e Benjoim.
            DESIGN: Frasco preto cilíndrico com anéis dourados em relevo e tampa preta com detalhes em ouro.
            PERFIL: Inspirado no Sauvage Elixir, mas com toque árabe de tabaco e baunilha.
            """
        elif "club de nuit" in item.lower():
            info_tecnica = """
            PRODUTO: Armaf Club de Nuit Intense Man.
            NOTAS REAIS: Limão, Groselha Preta, Maçã, Bergamota, Abacaxi, Rosa, Jasmim, Bétula, Almíscar, Âmbar Cinzento.
            DESIGN: Frasco preto fosco, corrente com medalhão e cristais.
            PERFIL: Famoso pelo rastro quilométrico e fixação extrema.
            """
        else:
            info_tecnica = f"Produto genérico: {item}. Foque em luxo e sofisticação."

        prompts = [
            f"Aja como CEO: Com base em: {info_tecnica}, descreva o posicionamento de luxo de {item}. Use as notas REAIS de Tabaco e Café se for o Asad. Descreva o frasco preto com anéis dourados.",
            f"Aja como Estrategista: 3 ganchos TikTok para {item}. Use termos como 'Rastro de Milionário', 'Cheiro de Poder' e 'Elogios garantidos'.",
            f"Aja como Fotógrafo: 3 prompts 8k para o frasco real de {item}. Detalhe os anéis dourados (se for Asad) ou a corrente (se for Club de Nuit).",
            f"Aja como Roteirista: 2 roteiros de 12s. Foque no close-up do borrifador e na reação de 'pescoço virando' quando o rastro passa.",
            f"Aja como Social Media: 10 hashtags (Ex: #PerfumesArabes #LattafaAsad #ModaMasculina) e 3 legendas magnéticas. PROIBIDO culinária."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Você é a Inteligência Autônoma do Almir. Você tem acesso à ficha técnica: {info_tecnica}. Você NUNCA inventa notas cítricas para perfumes que são de tabaco. Você é direto, luxuoso e técnico."},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
