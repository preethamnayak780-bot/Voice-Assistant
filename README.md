# 🎙️ Python Voice Assistant

A beginner-friendly **Python Voice Assistant** that can listen to voice commands, speak responses, open websites, perform searches, and launch applications.

## 🚀 Features

* 🎤 Voice command recognition
* 🔊 Text-to-speech responses
* 🕐 Tell the current time
* 📅 Tell the current date
* 🌐 Open Google
* ▶️ Open YouTube
* 🔎 Search Google
* 🧮 Open Calculator
* 📝 Open Notepad
* 👋 Respond to greetings
* ❌ Exit the assistant using a voice command

## 🛠️ Technologies Used

* Python 3.13
* SpeechRecognition
* PyAudio
* pyttsx3
* Webbrowser
* Datetime
* OS

## 📦 Installation

### 1. Install Python

This project is designed to run with **Python 3.13**.

Check your Python version:

```bash
py -3.13 --version
```

### 2. Install Required Packages

Open Command Prompt and run:

```bash
py -3.13 -m pip install SpeechRecognition pyttsx3 PyAudio
```

### 3. Check the Installation

```bash
py -3.13 -c "import speech_recognition, pyttsx3, pyaudio; print('All Voice Assistant packages OK')"
```

## ▶️ How to Run

Open Python 3.13 IDLE:

```bash
py -3.13 -m idlelib
```

Then:

1. Open `Voice.py`
2. Press **F5**
3. Allow microphone access if Windows asks
4. Speak your command

## 🎤 Example Commands

You can say:

```text
Hello
What is the time?
What is today's date?
Open Google
Open YouTube
Search Google
Open calculator
Open Notepad
Goodbye
Exit
```

## 📁 Project Structure

```text
Voice-Assistant/
│
├── Voice.py
└── README.md
```

## ⚙️ Python Version Note

This project uses **Python 3.13** because the microphone functionality depends on PyAudio.

If Python 3.14 is installed on your computer, you can keep it installed, but run this project with Python 3.13.

## 🔮 Future Improvements

Planned improvements include:

* Weather information
* Music control
* WhatsApp integration
* Email sending
* System controls
* Voice-based Google search
* ChatGPT integration
* Custom wake word
* Better error handling
* GUI interface

## 👨‍💻 Author

**Preetham Nayak**

This project was created as a Python learning project to practice:

* Python functions
* Modules
* Exception handling
* APIs and libraries
* Voice recognition
* Text-to-speech
* Automation

## 📄 License

This project is for educational and personal use.
