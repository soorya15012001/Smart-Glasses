import subprocess
import json
import vlc
import pafy
import time
import pyttsx3
import speech_recognition as sr
import speech as s




def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 180)
    engine.say(audio)
    engine.runAndWait()


def play():

    speak("Ok, what song do you want to listen ?")

    song = s.takeCommand()
    song = song.lower()
    #song = "zikr by desert rock"
    speak("Ok, playing song "+song)

    param = 'youtube-dl -j --dump-json "ytsearch1:{}"'.format(song)

    status, output = subprocess.getstatusoutput(param)
    output = str(output)
    res = json.loads(output)

    ur = res['webpage_url']
    dur = res['duration']

    url = ur
    video = pafy.new(url)
    best = video.getbestaudio()
    media = vlc.MediaPlayer(best.url)
    media.play()
    time.sleep(dur)