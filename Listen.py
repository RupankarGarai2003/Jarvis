from pyttsx3 import speak
import speech_recognition as sr #pip install speechrecognition

def Listen():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk to zara...")
        r.pause_threshold = 1
       # r.adjust_for_ambient_noise(source)
       # audio = r.listen(source)
        audio = r.listen(source,0,6)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
 
    except Exception as e:
        # print(e)  
        speak("say that again please...")  
        print("Say that again please...")  
        return "None"
    query = query.lower()
    return query

Listen()