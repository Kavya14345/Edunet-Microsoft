
# 🔊 AI Voice Assistant – Kavya Sampathirao

This project is a voice-controlled virtual assistant built using Python that helps users perform system-level tasks, access online platforms, read files, and interact with services like ChatGPT, YouTube, and more—all via natural spoken language.

> 🎓 **Developed as part of AI Azure Internship by Edunet Foundation in collaboration with Microsoft**

---

## 📽️ Demo
[Watch the demo here](https://github.com/Kavya14345/Edunet-Microsoft/blob/main/demo.mp4) 

---
## Project Code:
[Watch the code here](https://github.com/Kavya14345/Edunet-Microsoft/blob/main/voice_assistant.py) 

---

## 🚀 Features

- 🎙️ Voice recognition and speech feedback  
- 📁 Open/delete local files/folders using voice  
- 🌐 Search Google & YouTube  
- 📜 Read PDF aloud  
- 🖼️ Take and save screenshots  
- ⌨️ Type text into applications  
- 💬 Voice input sent to ChatGPT and response automation  
- 🧠 Converts number words like "two" to 2 for commands  
- 📄 Opens applications: Notepad, Word, Excel, PowerPoint, GitHub, LinkedIn  
- 🔇 Toggle voice feedback (mute/unmute)

---

## ⚙️ Tech Stack

- Python 3.11+  
- `speech_recognition` for voice input  
- `pyttsx3` for speech output  
- `pyautogui` for automation  
- `tkinter` for GUI  
- `pywhatkit` for YouTube  
- `fitz` (PyMuPDF) for PDF reading  
- Logging and multithreading support

---

## 🔧 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/voice-assistant.git
   cd voice-assistant
````

2. Install the required packages:

   ```bash
   pip install pyttsx3 SpeechRecognition pyautogui pywhatkit word2number fitz PyMuPDF
   ```

3. Run the application:

   ```bash
   python voice_assistant.py
   ```

---

## 🗣️ Example Voice Commands

| Task                       | Command Example                                |
| -------------------------- | ---------------------------------------------- |
| Open folder or file        | "Open folder projects"                         |
| Delete folder or file      | "Delete file test.pdf"                         |
| Google search              | "Search Google for Python tutorials"           |
| YouTube search             | "Search in YouTube for funny cats"             |
| Play song on YouTube       | "Play song Shape of You"                       |
| ChatGPT query              | "Chat GPT" (then speak your query)             |
| Type text                  | "Type text" → say "Hello world"                |
| Screenshot                 | "Take screenshot"                              |
| Read a PDF                 | "Read PDF" (GUI dialog will open)              |
| Open Notepad               | "Open Notepad"                                 |
| Open Word/Excel/PowerPoint | "Open Word" / "Open Excel" / "Open PowerPoint" |
| Open websites              | "Open GitHub" / "Open LinkedIn"                |

---

## 🧠 Code Structure Summary

| Section                         | Description                                         |
| ------------------------------- | --------------------------------------------------- |
| `speak(text)`                   | Converts text to speech                             |
| `listen_command()`              | Captures user's voice and converts to text          |
| `search_folders_files()`        | Searches for files/folders in specified directories |
| `extract_number()`              | Converts spoken numbers to integers                 |
| `open_item()` / `delete_item()` | Opens or deletes selected file/folder               |
| `open_chatgpt()`                | Opens ChatGPT, listens to user query, auto-types it |
| `type_text_into_app()`          | Types spoken text into the current application      |
| `take_screenshot()`             | Captures and saves a screenshot                     |
| `read_pdf()`                    | Reads and speaks contents of selected PDF           |
| `assistant_loop()`              | Main command loop handling user input               |
| GUI (Tkinter)                   | Provides buttons to start, stop, and exit assistant |

---

## 🙋‍♀️ About Me

👩‍💻 **Sampathirao Kavya**
B.Tech CSE, 3rd Year
JNTU-GV Vizianagaram
🔗 LinkedIn: [linkedin.com/in/kavya](https://www.linkedin.com/in/kavya-sampathirao-9b142b256/)
🌱 Passionate about AI, ML, and automation

---

## 📚 Internship Info

This project was built as a capstone project submission for:

**AI-Azure Virtual Internship Program**
Organized by: **Edunet Foundation**
Supported by: **Microsoft Azure AI**

---

## 📌 Note

Make sure your microphone is enabled and permissions are granted for speech recognition to work properly. GUI responsiveness may be affected if long tasks run without threading.

---
