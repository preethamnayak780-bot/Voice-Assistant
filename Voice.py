import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize voice engine
engine = pyttsx3.init()

# Set voice speed
engine.setProperty("rate", 170)


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

            print("Recognizing...")
            command = recognizer.recognize_google(audio)

            print("You:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
            return ""

        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return ""


def assistant():
    speak("Hello! I am your voice assistant. How can I help you?")

    while True:

        command = listen()

        if command == "":
            continue

        # Time
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The time is " + current_time)

        # Date
        elif "date" in command:
            today = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + today)

        # Open Google
        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        # Open YouTube
        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        # Search Google
        elif command.startswith("search"):
            search_query = command.replace("search", "", 1).strip()

            if search_query:
                speak("Searching for " + search_query)
                url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
                webbrowser.open(url)
            else:
                speak("What should I search for?")

        # Open calculator
        elif "calculator" in command:
            speak("Opening calculator")
            os.system("start calc")

        # Open Notepad
        elif "notepad" in command:
            speak("Opening Notepad")
            os.system("start notepad")

        # Greeting
        elif "hello" in command or "hi" in command:
            speak("Hello! Nice to talk with you.")

        # Exit
        elif "exit" in command or "stop" in command or "goodbye" in command:
            speak("Goodbye!")
            break

        else:
            speak("I don't know that command yet.")


# Start assistant
assistant()
