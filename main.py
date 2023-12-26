#note:This was a hobby code,made on a sleepless night,i did not consider the effciency of the code,all i wanted is it to talk back to me with some logic.so feel free to suggest me changes in this code.

from geopy.geocoders import Nominatim﻿
﻿import speech_recognition as sr﻿
﻿from datetime import datetime﻿
﻿import pywhatkit﻿
﻿import wikipedia﻿
﻿import pyttsx3﻿
﻿import pyjokes﻿
﻿﻿
﻿data = ["hi", "hello", "good morning", "good afternoon", "good evening", "good night", "namaste"]﻿
﻿operations = ["add", "subtract", "divide", "multiply", "difference", "sum", "product"]﻿
﻿﻿
﻿listener = sr.Recognizer()﻿
﻿anjali = pyttsx3.init()﻿
﻿voices = anjali.getProperty("voices")﻿
﻿anjali.setProperty('voice', voices[1].id)﻿
﻿﻿
﻿def arithmetic(data):﻿
﻿    a = ""﻿
﻿    b = ""﻿
﻿    operator = 0﻿
﻿    sflag = 0﻿
﻿    eflag = 0﻿
﻿    for i in range(0, len(operations)):﻿
﻿        if operations[i] in data:﻿
﻿            operator = i﻿
﻿    for char in data:﻿
﻿        if char.isnumeric():﻿
﻿            if eflag == 0:﻿
﻿                a += char﻿
﻿                sflag = 1﻿
﻿            elif eflag == 1:﻿
﻿                b += char﻿
﻿        if not char.isnumeric() and sflag == 1:﻿
﻿            eflag = 1﻿
﻿    a = int(a)﻿
﻿    b = int(b)﻿
﻿    try:﻿
﻿        if operator == 0 or operator == 5:﻿
﻿            return str(a + b)﻿
﻿        elif operator == 1:﻿
﻿            return str(a - b)﻿
﻿        elif operator == 2:﻿
﻿            return str(a / b)﻿
﻿        elif operator == 3:﻿
﻿            return str(a * b)﻿
﻿        elif operator == 4:﻿
﻿            return str(abs(a - b))﻿
﻿        else:﻿
﻿            return "is something that I couldn't calculate"﻿
﻿    except:﻿
﻿        return "is something that I couldn't calculate"﻿
﻿﻿
﻿def run_anjali():﻿
﻿    with sr.Microphone(device_index=1) as source:﻿
﻿        print("Speak...")﻿
﻿        voice = listener.listen(source)﻿
﻿        command = listener.recognize_google(voice)﻿
﻿        command = command.lower()﻿
﻿        print(command)﻿
﻿        if command in ["end", "terminate"]:﻿
﻿            return 1﻿
﻿        if "anjali" in command:﻿
﻿            command = command.replace("anjali", "", 1)﻿
﻿            for feed in data:﻿
﻿                if feed in command:﻿
﻿                    anjali.say(feed)﻿
﻿                    anjali.runAndWait()﻿
﻿            if "joke" in command:﻿
﻿                command = command.replace("joke", "")﻿
﻿                joke = pyjokes.get_joke(language="en", category="neutral")﻿
﻿                anjali.say(joke)﻿
﻿                anjali.runAndWait()﻿
﻿                anjali.say("Ha ha ha")﻿
﻿                anjali.runAndWait()﻿
﻿            elif "play" in command:﻿
﻿                anjali.say("Playing")﻿
﻿                anjali.runAndWait()﻿
﻿                pywhatkit.playonyt(command)﻿
﻿            elif "time" in command:﻿
﻿                time = datetime.now().strftime("%H:%M %p")﻿
﻿                anjali.say("It is " + time)﻿
﻿                anjali.runAndWait()﻿
﻿            elif "what is the GPS location of " in command:﻿
﻿                command = command.replace("what is the GPS location of ", "")﻿
﻿                try:﻿
﻿                    loc = Nominatim(user_agent="GetLoc")﻿
﻿                    loc = loc.geocode(command)﻿
﻿                    anjali.say(command + " location is latitude {} and longitude {}".format(loc.latitude, loc.longitude))﻿
﻿                    anjali.runAndWait()﻿
﻿                except:﻿
﻿                    print("Error")﻿
﻿            elif "search for " in command:﻿
﻿                command = command.replace("search for ", "")﻿
﻿                result = wikipedia.summary(command, sentences=3)﻿
﻿                anjali.say(result)﻿
﻿                anjali.runAndWait()﻿
﻿            elif "who created " in command:﻿
﻿                command = command.replace("who created ", "")﻿
﻿                if command == "you":﻿
﻿                    anjali.say("I was created by Bhargav.")﻿
﻿                    anjali.runAndWait()﻿
﻿                else:﻿
﻿                    command = command + " who created"﻿
﻿                    result = wikipedia.summary(command, sentences=3)﻿
﻿                    anjali.say(result)﻿
﻿                    anjali.runAndWait()﻿
﻿            elif "who is " in command:﻿
﻿                command = command.replace("who is ", "")﻿
﻿                command = command[1:]﻿
﻿                result = wikipedia.summary(command, sentences=3)﻿
﻿                anjali.say(result)﻿
﻿                anjali.runAndWait()﻿
﻿            else:﻿
﻿                try:﻿
﻿                    for operator in operations:﻿
﻿                        if operator in command:﻿
﻿                            result = arithmetic(command)﻿
﻿                    anjali.say(result)﻿
﻿                    anjali.runAndWait()﻿
﻿                except:﻿
﻿                    print("Error")﻿
﻿﻿
﻿while True:﻿
﻿    end = run_anjali()﻿
﻿    if end == 1:﻿
﻿        break﻿
﻿
