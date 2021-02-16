# Import the required module for text  
# to speech conversion 
from gtts import gTTS
# player.play_song("/path/to/some_mp3.mp3")
# This module is imported so that we can  
# play the converted audio 
import os
import sys

cwd = os.getcwd()
# print("cwd:", cwd)
# print("\n _________", os.path.join(cwd, "horn.mp3"))


# Disable and enable prints:
def blockPrint():    # Disable
    # print('blockPrint activated')
    sys.stdout = open(os.devnull, 'w')
def enablePrint():   # Restore
    sys.stdout = sys.__stdout__
""" usage  -->  blockPrint()  enablePrint() """


def say_smth(str_to_say=False, language='es', horn=False):
    blockPrint()
    if horn:
        os.system("mpg321 --stereo {}".format(os.path.join(cwd, "horn.mp3")))
    # language = 'en'  # english ...  slow=False
    if str_to_say:
#        try:
        myobj = gTTS(text=str_to_say, lang=language, slow=False)
        # Saving the converted audio in a mp3 file named 
        # welcome  
        myobj.save("text_to_say.mp3")
        # Playing the converted file 
        os.system("mpg321 --stereo text_to_say.mp3")
#        except Exception as e:
#            print("______")
#            print("error in text_to_speech.py", e)
    enablePrint()

if __name__ == '__main__':
    texto = ("esto es una prueba ... mmmmmmmmm , sí, funciono!")
    say_smth(horn=True)

