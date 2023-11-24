# Function added

import datetime
from Speak import Say
import wikipedia
import pywhatkit



# two types function
#1.-----------------------------------------------ALL NON INPUT FUNCTION ARE ADDED--------------------------------------


def Time():
    time = datetime.datetime.now().strftime("%h:%M:%S")
    Say(Time)
    
def Date():
    date = datetime.date.today()
    Say(Date)
    
def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(Day)
    
    
    
    
def NonInputExecution(query):
    query = str(query)
    
    if "time" in query:
        Time()
        
    elif "date" in query:
        Date()
        
    elif "day" in query:
        Day()


#2.-------------------------------------------- ALL INPUT FUNCTION ARE ADDED---------------------------------------------

# def Wikipedia(tag,query):
#     name = str(query).replace("","")
#     #import Wikipedia
#     result = wikipedia.summary(name)
#     Say(result)
    
    
def InputExecution(tag,query):
    
    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("tell me about","").replace("what is","").replace("wikipedia","").replace("according to wikipedia","")
        #import Wikipedia
        result = wikipedia.summary(name)
        Say(result)
        
    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        #import pywhatkit
        pywhatkit.search(query)