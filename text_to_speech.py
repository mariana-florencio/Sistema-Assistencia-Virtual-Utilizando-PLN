from gtts import gTTS
from IPython.display import Audio

text_to_say = 'Olá, tudo bem?'
language = 'pt-BR'

gtts_object = gTTS(text = text_to_say, lang = language, slow = False)

gtts_object.save('gtts.wav')
Audio('gtts.wav')