import speech_recognition as sr
import webbrowser
import time
import playsound
import cmd
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()
def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            guru_speak(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            guru_speak("Sorry, My speech service is down")
        return voice_data
def guru_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 10000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if "what is your name" in voice_data:
        guru_speak("My name is Guru")
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        guru_speak(time)
    if "search" in voice_data:
        search = record_audio("What do you want to search for?")
        if search == "go back":
            guru_speak("how can I help you")
        else:
            url = "https://google.com/search?q=" + search
            webbrowser.get().open(url)
            guru_speak("Here is what I found for " + search)
    if "find location" in voice_data:
        location = record_audio("What is the location you are looking for?")
        if location == "go back":
            guru_speak("how can I help you")
        else:
            url = "https://google.nl/maps/place/" + location + "/&amp;"
            webbrowser.get().open(url)
            guru_speak("Here is the location of " + location)

    if "stop the system" in voice_data:
        guru_speak("Stopping the system")
        exit()
    if there_exists(["open browser"]):
        url = "https://google.com"
        webbrowser.get().open(url)
    if there_exists(["open video"]):
        url = "https://youtube.com"
        webbrowser.get().open(url)
    if there_exists(["say hi", "say hello"]):
        guru_speak("Hello, I am Guru, I would like to help you in you're daily life")





time.sleep(1)
guru_speak("How can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)
