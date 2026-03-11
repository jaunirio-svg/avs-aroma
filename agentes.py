from groq import Groq

class AgenteAVS:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def executar_fluxo(self, item):
        # BANCO DE DADOS INTERNO PARA NÃO DAR ERRO DE CONTEXTO
        contexto_especifico = ""
        
        if "asad" in item.lower():
            contexto_especifico = "O Asad da Lattafa é um perfume árabe masculino, famoso por ser inspirado no Sauvage Elixir. Notas Reais: Pimenta Preta, Abacaxi, Tabaco, Café, Patchouli, Sândalo e Baunilha. O frasco é preto com detalhes dourados em relevo."
        elif "club de nuit" in item.lower():
            contexto_especifico = "O Club de Nuit Intense Man da Armaf é um perfume árabe focado em rastro e projeção, inspirado no Creed Aventus. Notas: Limão, Groselha, Maçã, Rosa, Jasmim, Bétula, Almíscar e Âmbar Cinzento. O frasco é preto fosco com uma corrente e medalhão pendurado."
        
        diretriz = f"Considere este contexto técnico: {contexto_especifico}. Identifique o produto '{item}' e gere conteúdo de luxo. Proibido falar de comida ou acessórios externos como relógios. Foco no frasco e no rastro."
        
        prompts = [
            f"Aja como CEO: Defina o posicionamento premium de {item}. Use a pirâmide olfativa correta mencionada no contexto. Fale do design do frasco.",
            f"Aja como Estrategista Viral: Crie 3 ganchos magnéticos para TikTok sobre {item}. Foque no 'Rastro de Milionário' e nos elogios.",
            f"Aja como Fotógrafo: Gere 3 prompts de imagem 8k focados no frasco de {item}. Descreva o brilho do vidro e os detalhes metálicos.",
            f"Aja como Roteirista: Crie 2 roteiros de 12s. Close no borrifador e na reação das pessoas ao sentirem o rastro.",
            f"Aja como Social Media: Sugira 10 hashtags de PERFUMARIA e 3 legendas magnéticas. Proibido hashtags de comida."
        ]
        
        respostas = [] 
        for p in prompts:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "Você é um especialista em Perfumaria Árabe e Branding de Luxo. Você nunca alucina. Você entrega dados técnicos precisos e roteiros prontos para postar."},
                    {"role": "user", "content": p}
                ]
            )
            respostas.append(completion.choices[0].message.content)
        
        return respostas
