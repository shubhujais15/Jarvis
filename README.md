# **Jarvis**

Jarvis is a Python-based personal assistant designed to perform various tasks, including playing music, providing weather updates, and more. Inspired by the AI assistant from the Iron Man series, this project aims to enhance user productivity through voice commands.

---

## **Table of Contents**

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Contributors](#contributors)
- [License](#license)

---

## **Features**

- 🎵 **Music Playback**: Plays songs from a predefined music library.
- 🌦️ **Weather Updates**: Provides current weather information for specified locations.
- 🔍 **Web Search**: Performs web searches and retrieves information.
- 📅 **Date and Time**: Announces the current date and time.
- 🗣️ **Voice Interaction**: Responds to voice commands using speech recognition.

---

## **Installation**

To set up the project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shubhujais15/Jarvis.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Jarvis
   ```

3. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

1. **Ensure your microphone is connected and functioning properly.**

2. **Run the main script:**

   ```bash
   python main.py
   ```

3. **Speak your commands clearly when prompted.**

---

## **Dependencies**

The project relies on the following Python packages:

- **SpeechRecognition**: For recognizing speech input.
- **pyttsx3**: For text-to-speech conversion.
- **requests**: For making HTTP requests (e.g., fetching weather data).
- **pyaudio**: For accessing microphone input.

For a complete list, refer to the `requirements.txt` file.

---

## **Configuration**

- **Weather API**: To enable weather updates, obtain an API key from a weather service provider (e.g., OpenWeatherMap) and configure it in the script.
- **Music Library**: Ensure that the `musicLibrary.py` file contains the correct paths to your local music files.

---

## **Contributors**

- **Shubham Jaiswal**  
  [GitHub Profile](https://github.com/shubhujais15)

---

Feel free to explore, contribute, and provide feedback to enhance Jarvis! 
