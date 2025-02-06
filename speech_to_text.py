import speech_recognition as sr
import webbrowser

recognizer = sr.Recognizer()

def search_google(command):
    search = '+'.join(command.split())
    url = f'https://www.google.com/search?q={search}'
    webbrowser.open(url)

with sr.Microphone() as source:
    print('Diga algo para pesquisar no Google...')
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)  # captura o áudio

try:
    text = recognizer.recognize_google(audio, language='pt-BR')  # transcreve o áudio
    print('Você disse:', text)
    search_google(text)

except sr.UnknownValueError:
    print('Não foi possível entender o áudio.')
except sr.RequestError:
    print('Erro ao conectar ao serviço de reconhecimento de voz.')


