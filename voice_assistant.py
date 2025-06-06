import os
import shutil
import pyttsx3
import speech_recognition as sr
import time
import subprocess
import webbrowser
import pyautogui
import tkinter as tk
from threading import Thread,Event
from word2number import w2n
import pywhatkit
from tkinter import messagebox,filedialog
import fitz
import logging
import re
logging.basicConfig(filename='assistant.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
engine=pyttsx3.init()
speak_enabled=True
def speak(text):
    print("Assistant:",text)
    if speak_enabled:
        try:
            engine.say(text)
            engine.runAndWait()
        except RuntimeError as e:
            logging.error(f"Speech error:{e}")
def listen_command(timeout=5,phrase_limit=8):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening.....")
        root.update()
        r.adjust_for_ambient_noise(source,duration=1)
        try:
            audio=r.listen(source,timeout=timeout,phrase_time_limit=phrase_limit)
            status_label.config(text="waiting...")
            command=r.recognize_google(audio).lower()
            command_text.set(f"You said:{command}")
            return command
        except sr.WaitTimeoutError:
            status_label.config(text="Listening timeout")
            return ""
        except Exception as e:
            status_label.config(text="Error")
            logging.error(f"Recognition error:{e}")
            speak("Sorry,I didn't catch that.")
            return ""
def search_folders_files(base_path,keyword):
    matches=[]
    for root_dir,dirs,files in os.walk(base_path):
        for d in dirs:
            if keyword.lower() in d.lower():
                matches.append(os.path.join(root_dir,d))
        for f in files:
            if keyword.lower() in f.lower():
                matches.append(os.path.join(root_dir,f))
    return matches
def extract_number(text):
    text=text.lower().strip()
    match=re.search(r'\d+',text)
    if match:
        return int(match.group())
    try:
        return w2n.word_to_num(text)
    except:
        return None
def list_and_choose(matches,action):
    if not matches:
        speak(f"No results found for {action}.")
        return None
    speak(f"I found {len(matches)} results.")
    for i,item in enumerate(matches,1):
        speak(str(i))
        print(f"{i}:{item}")
        time.sleep(0.3)
    speak(f"Please say the number of the item to {action}.")
    choice=listen_command().lower().strip()
    num=extract_number(choice)
    if num is not None and 1<=num<=len(matches):
        return matches[num-1]
    else:
        speak("Invalid number")
        return None
def open_item(path):
    if stop_task_flag.is_set():return
    try:
        subprocess.Popen(f'explorer"{path}"')
        speak(f"Opening {path}")
    except Exception as e:
        speak(f"Failed to Open:{e}")
def delete_item(path):
    if stop_task_flag.is_set():return
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        speak(f"Deleted {path}")
    except PermissionError:
        speak("Cannot delete,as it is currently open.Please close it first")
    except Exception as e:
        speak(f"Failed to delete:{e}")
def play_youtube_song(song_name):
    if stop_task_flag.is_set():return
    speak(f"Playing {song_name} on YouTube.")
    pywhatkit.playonyt(song_name)
def open_chatgpt():
    if stop_task_flag.is_set():return
    webbrowser.open("https://chat.openai.com")
    speak("Opening ChatGPT, please wait...")
    time.sleep(7)
    if stop_task_flag.is_set():return
    speak("You can now speak your query for ChatGPT")
    time.sleep(1)
    query=listen_command(timeout=6,phrase_limit=10)
    if not query.strip():
        speak("I didn't catch your question. Please try again.")
        return
    speak("Typing your query into ChatGPT.")
    pyautogui.hotkey('ctrl','l')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.write(query)
    pyautogui.press("enter")
    speak("Your question has been typed and sent.")
def type_text_into_app():
    if stop_task_flag.is_set():return
    speak("What should I type?")
    text=listen_command()
    if stop_task_flag.is_set():return
    if not text:
        speak("I didn't catch that.Please try again.")
        return
    speak(f"Typing:{text}")
    pyautogui.write(text)
    pyautogui.press("enter")
    speak("Text has been typed and submitted.")
def take_screenshot():
    if stop_task_flag.is_set():
        return
    try:
        screenshot=pyautogui.screenshot()
        save_folder=r"C:/Users/KAVYA/Saved Games/Pictures/Screenshots"
        os.makedirs(save_folder,exist_ok=True)
        filename=os.path.join(save_folder,f"screenshot_{int(time.time())}.png")
        screenshot.save(filename)
        speak(f"Screenshot saved to {filename}")
    except Exception as e:
        speak(f"Failed to save screenshot:{e}")
def read_pdf():
    if stop_task_flag.is_set():return
    file_path=filedialog.askopenfilename(filetypes=[("PDF files","*.pdf")])
    if not file_path:
        speak("No file selected.")
        return
    try:
        with fitz.open(file_path) as pdf:
            speak("Reading first few pages of the PDF.")
            for page in pdf[:5]:
                speak(page.get_text())
    except Exception as e:
        speak(f"Error reading PDF:{e}")
def toggle_speak():
    global speak_enabled
    speak_enabled=not speak_enabled
    state="enabled" if speak_enabled else "disabled"
    speak(f"Voice feedback {state}.")
def run_task(target,*args):
    global current_task_thread
    stop_current_task()
    stop_task_flag.clear()
    current_task_thread=Thread(target=target,args=args,daemon=True)
    current_task_thread.start()
def stop_current_task():
    if current_task_thread and current_task_thread.is_alive():
        stop_task_flag.set()
        speak("Stopping current task.")
        current_task_thread.join(timeout=5)
    stop_task_flag.clear()
def assistant_loop():
    base_paths=["C:\\Users\\KAVYA\\Documents","C:Users\\KAVYA\\Downloads"]
    speak("Voice assistant is now active.Say 'exit' or 'quit' to stop.")
    while assistant_running.get():
        command=listen_command()
        if not assistant_running.get():break
        if not command:continue
        if command in ["stop","cancel"]:
            stop_current_task()
            continue
        if command.startswith("open folder") or command.startswith("open file"):
            keyword=command.replace("open folder","").replace("open file","").strip()
            results=[]
            for base_path in base_paths:
                results.extend(search_folders_files(base_path,keyword))
            chosen=list_and_choose(results,"open")
            if chosen:
                run_task(open_item,chosen)
        elif command.startswith("delete folder") or command.startswith("delete file"):
            keyword=command.replace("delete folder","").replace("delete file","").strip()
            results=[]
            for base_path in base_paths:
                results.extend(search_folders_files(base_path,keyword))
            chosen=list_and_choose(results,"delete")
            if chosen:
                speak(f"Deleting {chosen}")
                run_task(delete_item,chosen)
        elif "play" in command and "song" in command:
            song_name=command.replace("play","").replace("song","").strip()
            run_task(play_youtube_song,song_name)
        elif "chat gpt" in command:
            run_task(open_chatgpt)
        elif "type text" in command:
            run_task(type_text_into_app)
        elif "take screenshot" in command:
            run_task(take_screenshot)
        elif "read pdf" in command:
            run_task(read_pdf)
        elif command in ["mute assistant"]:
            run_task(toggle_speak)
        elif command in ["unmute assistant"]:
            run_task(toggle_speak)
        elif command in ["exit","quit"]:
            stop_current_task()
            speak("Goodbye!")
            assistant_running.set(False)
            break
        elif "search google for" in command or "google" in command:
            query=command.replace("search google for","").replace("google","").strip()
            speak(f"Searching Google for {query}")
            url=f"https://www.google.com/search?q={query.replace(' ','+')}"
            webbrowser.open(url)
            pyautogui.press('enter')
        elif "open linkedin" in command:
            speak("Opening LinkedIn")
            webbrowser.open("https://www.linkedin.com")
            pyautogui.press('enter')
        elif "open github" in command:
            speak("Opening Github")
            webbrowser.open("https://www.github.com")
            pyautogui.press('enter')
        elif "open notepad" in command:
            speak("Opening Notepad")
            subprocess.Popen(["notepad.exe"])
        elif "open word" in command:
            speak("Opening Microsoft Word")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk")
        elif "open excel" in command:
            speak("Opening Microsoft Excel")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk")
        elif "open powerpoint" in command:
            speak("Opening Microsoft PowerPoint")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk")
        elif "open command prompt" in command or "open cmd" in command:
            speak("Opening Command Prompt")
            os.startfile("C:\\Users\\KAVYA\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk")
        elif "open control panel" in command:
            speak("Opening Control Panel")
            os.startfile("C:\\Users\\KAVYA\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk")
        elif "search in youtube for" in command:
            query=command.replace("search in youtube for","").strip()
            speak(f"Searching YouTube for {query}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query.replace(' ','+')}")
            pyautogui.press('enter')
        else:
            speak("Sorry,I didn't understand that command.")
root=tk.Tk()
root.title("Voice Assistant GUI")
root.geometry("450x300")
root.resizable(False,False)
assistant_running=tk.BooleanVar(value=False)
command_text=tk.StringVar()
status_label=tk.Label(root,text="Status: Idle",fg="green")
status_label.pack(pady=10)
command_display=tk.Label(root,textvariable=command_text,wraplength=400,fg="blue")
command_display.pack(pady=10)
tk.Button(root,text="Start Assistant",command=lambda:[assistant_running.set(True),Thread(target=assistant_loop,daemon=True).start()],bg="green",fg="white").pack(pady=5)
tk.Button(root,text="Stop Assistant",command=lambda:[stop_current_task(),assistant_running.set(False)],bg="red",fg="white").pack(pady=5)
tk.Button(root,text="Exit",command=root.quit).pack(pady=5)
current_task_thread=None
stop_task_flag=Event()
root.mainloop()