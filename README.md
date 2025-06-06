# 🔊 AI Voice Assistant – Kavya Sampathirao

This project is a **voice-controlled desktop assistant** built using Python. It empowers users to perform various system-level and web-based tasks using natural language commands. It integrates with services like **ChatGPT**, **YouTube**, and **Google**, and also manages local files, reads PDFs, types dictated text, and opens popular software and websites.

> 🎓 **Capstone project for the AI Azure Internship by Edunet Foundation in collaboration with Microsoft**

---

## 📽️ Demo

🎥 [Click to watch the project demo](https://github.com/Kavya14345/Edunet-Microsoft/blob/main/demo.mp4)

---

## 🧾 Project Code

📂 [View the Python source code](https://github.com/Kavya14345/Edunet-Microsoft/blob/main/voice_assistant.py)

---

## 🚀 Features

* 🎤 Voice recognition and text-to-speech feedback
* 📂 Open or delete files/folders by name
* 🔎 Search on **Google** or **YouTube** by voice
* 📄 Read content aloud from PDF files
* 🖼️ Take and store screenshots
* ⌨️ Type text in any app by dictating
* 🤖 Interact with **ChatGPT** via voice (auto types the query)
* 🧠 Converts spoken number words like "two" → 2
* 💻 Launches applications: Notepad, Word, Excel, PowerPoint
* 🌐 Opens LinkedIn and GitHub
* 🔇 Supports voice feedback toggle (mute/unmute)

---

## ⚙️ Tech Stack

* **Python 3.11**
* `speech_recognition` – for capturing and recognizing voice
* `pyttsx3` – text-to-speech engine
* `pyautogui` – to automate typing, screenshots, etc.
* `tkinter` – for graphical user interface
* `pywhatkit` – for playing YouTube videos
* `fitz` (PyMuPDF) – to read PDF content
* `word2number` – converts spoken numbers to integers
* `threading` & `logging` – for smooth and tracked multitasking

---

## 🔧 Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Kavya14345/Edunet-Microsoft.git
   cd Edunet-Microsoft
   ```

2. **Install the required packages**

   ```bash
   pip install pyttsx3 SpeechRecognition pyautogui pywhatkit word2number fitz PyMuPDF
   ```

3. **Run the assistant**

   ```bash
   python voice_assistant.py
   ```

---

## 🗣️ Example Voice Commands

| **Task**              | **Command Example**                            |
| --------------------- | ---------------------------------------------- |
| Open folder or file   | `Open folder Projects`                         |
| Delete folder or file | `Delete file notes.pdf`                        |
| Google search         | `Search Google for Python tutorials`           |
| YouTube search        | `Search in YouTube for relaxing music`         |
| Play song on YouTube  | `Play song Shape of You`                       |
| Ask ChatGPT           | `Chat GPT` → (say your query aloud)            |
| Type text             | `Type text` → (e.g., say "Hello world")        |
| Screenshot            | `Take screenshot`                              |
| Read PDF              | `Read PDF` → (select file from dialog)         |
| Open Notepad          | `Open Notepad`                                 |
| Launch Word/Excel/PPT | `Open Word` / `Open Excel` / `Open PowerPoint` |
| Open websites         | `Open GitHub` / `Open LinkedIn`                |

---

## 🧠 Code Structure Overview

| **Function / Section**          | **Description**                                                              |
| ------------------------------- | ---------------------------------------------------------------------------- |
| `speak(text)`                   | Converts text to speech (output)                                             |
| `listen_command()`              | Captures and returns recognized spoken command                               |
| `search_folders_files()`        | Finds matching files/folders based on voice input                            |
| `extract_number()`              | Parses spoken numbers like "two" into `2`                                    |
| `open_item()` / `delete_item()` | Opens or deletes selected files/folders                                      |
| `open_chatgpt()`                | Launches ChatGPT, listens to user’s query, and types it automatically        |
| `type_text_into_app()`          | Types spoken sentence into the active window                                 |
| `take_screenshot()`             | Captures and stores a screenshot in the chosen folder                        |
| `read_pdf()`                    | Reads aloud contents from a selected PDF file                                |
| `assistant_loop()`              | The main loop that listens and dispatches commands                           |
| GUI (Tkinter)                   | Provides interface with start/stop/exit buttons and real-time status updates |

---

## 🙋‍♀️ About Me

👩‍💻 **Sampathirao Kavya**
B.Tech CSE, 3rd Year
📍 JNTU-GV Vizianagaram
🔗 [LinkedIn Profile](https://linkedin.com/in/kavya)
🌟 Passionate about AI, machine learning, automation, and Python development

---

## 📚 Internship Info

This project was submitted as part of:

**AI-Azure Virtual Internship Program**
Organized by: *Edunet Foundation*
Supported by: *Microsoft Azure AI*

---

## 📌 Note

* Ensure your microphone permissions are enabled
* GUI responsiveness may vary with system performance
* Long tasks (e.g., reading PDFs) are threaded to avoid freezing
