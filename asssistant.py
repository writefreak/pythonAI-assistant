import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Initialize the speech engine
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You said:", command)
            return command
    except:
        print("Sorry, I couldn't hear you.")
        return ""

def run_assistant():
    talk("Hello. What can I do for you?")
    while True:
        command = listen()

        if 'hello' in command:
            talk("Hi there! How are you?")
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The time is {time}")
        elif 'play' in command:
            song = command.replace('play', '')
            talk(f"Playing {song}")
            pywhatkit.playonyt(song)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            talk(info)
        elif 'stop' in command or 'quit' in command or 'exit' in command:
            talk("Goodbye.")
            break
        else:
            talk("Sorry, I didn’t get that. Please try again.")
if __name__ == "__main__":
    run_assistant()
