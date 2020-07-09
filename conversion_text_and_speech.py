import pyttsx3
import speech_recognition as sr



def convert_text_to_speech(text):
    engine = pyttsx3.init()
    engine.say('This is PEDI, how can I help you' + text)
    engine.runAndWait()


def convert_speech_to_text():
    r = sr.Recognizer()
### For using already present .wav file
    # with sr.AudioFile('Resources/cutafew.wav') as source:
    #     audio_text = r.listen(source)
    #     try:
    #         text = r.recognize_google(audio_text, language='en')
    #         print('Converting audio transcripts into text ...')
    #         print(text)
    #     except:
    #         print('Sorry.. run again...')

# For using microphone for voice.
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        try:
            final = r.recognize_google(audio_text,language='en-IN')
            print("Text: " + final)
        except:
            print("Sorry, I did not get that")

# CALLING THE FUNCTION
convert_speech_to_text()




