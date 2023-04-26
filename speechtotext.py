# this program create a function that knows how to convert speech to text
import importlib
from pickle import TRUE
#insatlling pyaudio
try:
    importlib.util.find_spec('pyaudio')
    print("PyAudio is installed")
except ImportError:
    print("PyAudio is not installed")
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyaudio'])
#insatlling speechrecognition
try:
    importlib.util.find_spec('speech_recognition')
    print("SpeechRecognition is installed")
except ImportError:
    print("SpeechRecognition is not installed")
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'speech_recognition'])
#insatlling keyboard
try:
    importlib.util.find_spec('keyboard')
    print("keyboard is installed")
except ImportError:
    print("keyboard is not installed")
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'keyboard'])

#import speech to text module
import speech_recognition as sr

#initialize recognizer
r = sr.Recognizer()
#function that converts speech to text
def speechtotext():
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            return text
        except:
            print("Sorry could not recognize what you said")
            return "Sorry could not recognize what you said"
        
#main function for debugging
if __name__ == "__main__":
    speechtotext()

