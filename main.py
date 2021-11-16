import os
import pyjokes
import pyttsx3
import sys
import time
import speech_recognition as sr
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    engine.setProperty('voice', voice.id)


def alexa_listener():
    try:
        # this will try to get a audio and transform it in to a readable text
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            text = "listening"
            print(text)
            for i in range(2):
                sys.stdout.write(".")
                sys.stdout.flush()

            audio = recognizer.listen(source)
            output = recognizer.recognize_google(audio)
            output1 = output.lower()
            if 'alexa' in output1:
                output1 = output1.replace('alexa', '')
                print(output1)
    except KeyError:
        pass
    except KeyboardInterrupt:
        exit()

# and will return this:
    return output1


def speak(t):
    # here you have the code to speak.
    engine.say(t)
    engine.runAndWait()


# here you have the special functions that require a different handle

def spotify():
    def search_spotify(x):
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="fa1cdae006e7420db745b9af34c62f08",
                                                                   client_secret="aaad931eeae642b49350285b0f0b5029"))
        result_search = sp.search(q=x, limit=3)
        return result_search

    output = alexa_listener()
    search = output
    result = search_spotify(search)
    for idx, item in enumerate(result['tracks']['items']):
        speak(idx, item['name'])

# here is the function that will be running for eternity

# so unless it gives an error than it will stop



def alexa():
    output = alexa_listener()
    # here you can write your commands
    try:
        print(output)
        if "say hello to" in output:
            if "alexa" in output:
                output.replace("alexa", '')
            speak("Hello" + output[12:] + ". I Hope Everything is fine!")


        elif "play some music" in output:
            time.sleep(2)
            speak("Here it goes something smooth")
            os.system("start C:\\Users\\Utilizador\\Desktop\\projects\\python\\music.mp3")

        elif "search on spotify " in output:
            speak("now you just need to say the song that you want to search")
            spotify()

        elif "tell" and "joke" in output:
            speak(pyjokes.get_joke())

        elif "search" and "spotify" or "search" and "on" "spotify" in output:
            speak("feature isn't available yet, sorry!")

        elif "options" or "help" in output:
            speak("Now alexa (me), have small features, so there is some of them: "
                  "Play some music, "
                  "the spotify feature is still being devolved, say hello to somebody, tell jokes, and the rest is "
                  "being devolved")
        else:
            speak("Sorry try again, if you want to now my functions say \"help\" or \"options\"")

    except KeyboardInterrupt:
        exit()
    except speech_recognition.UnknownValueError:
        alexa()
    except RequestError:
        alexa()
    except UnknownValueError:
        alexa()

while True:
    alexa()
