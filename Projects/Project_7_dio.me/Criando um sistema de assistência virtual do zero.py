import pyttsx3
import speech_recognition as sr
import webbrowser
import requests

# Inicializar o módulo de Text-to-Speech
def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# Inicializar o módulo de Speech-to-Text
def ouvir():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        try:
            audio = recognizer.listen(source)
            comando = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            print("Desculpe, não entendi o que você disse.")
            return ""
        except sr.RequestError as e:
            print(f"Erro no serviço de reconhecimento de fala: {e}")
            return ""

# Automatizar ações
def executar_comando(comando):
    if "wikipedia" in comando:
        falar("Qual assunto você quer pesquisar no Wikipedia?")
        assunto = ouvir()
        if assunto:
            url = f"https://pt.wikipedia.org/wiki/{assunto.replace(' ', '_')}"
            falar(f"Abrindo Wikipedia para {assunto}")
            webbrowser.open(url)

    elif "youtube" in comando:
        falar("Abrindo YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "farmácia" in comando:
        falar("Procurando a farmácia mais próxima.")
        # Substitua 'sua_api_key' pela sua chave de API do Google Maps
        url = "https://www.google.com/maps/search/farmácia+mais+próxima/"
        webbrowser.open(url)

    else:
        falar("Comando não reconhecido. Por favor, tente novamente.")

# Loop principal do assistente
def assistente_virtual():
    falar("Olá, sou sua assistente virtual. Em que posso ajudar?")
    while True:
        comando = ouvir()
        if "sair" in comando or "encerrar" in comando:
            falar("Encerrando o sistema. Até logo!")
            break
        elif comando:
            executar_comando(comando)

# Executar o assistente
if __name__ == "__main__":
    assistente_virtual()
