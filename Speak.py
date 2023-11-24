import pyttsx3 #pip install pyttsx3



def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[len(voices) -1].id)
    engine.setProperty('rate',180)
    print("  ")
    print(f"A.I : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("  ")
    
Say("Hello sir!")