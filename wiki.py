#for run execute on Termux:
'''
pip install gtts
pip install wikipedia
pkg install mpv
'''

import os
from gtts import gTTS
import wikipedia
wikipedia.set_lang('pt')
p=input('Digite uma palavra para pesquisar: ')
t=(wikipedia.summary(p))
tts=gTTS(t , lang='pt-br')
tts.save('pesquisa.mp3')
os.system('mpv pesquisa.mp3')
