import speech_recognition as sr
import pyttsx3 
import pywhatkit 
import datetime 
import wikipedia
import pyjokes 
import sys
import webbrowser 
from datetime import date

engine=pyttsx3.init()
engine.setProperty("rate", 150) 
voices = engine.getProperty("voices")
engine.setProperty('voice', voices [1].id) 
recognizer=sr.Recognizer()

def engine_talk(text):
     engine.say(text) 
     engine.runAndWait()

def run_alexa():

    with sr.Microphone() as source: 
        recognizer.adjust_for_ambient_noise(source,duration=1) 
        print('\n')
        print("Start Speaking!!") 
        engine_talk('listening..🧏‍♂️ ') 
        recordedaudio=recognizer.listen(source)
    
    try:
        command=recognizer.recognize_google(recordedaudio,language='en-in') 
        command = command.lower()
        if 'alexa' in command :
            command = command.replace('alexa', '') 
            print('you said'+command)
        
        else :
            print('you said : '+command)

        if 'hello' in command :
            print('hello What should i Do For  you 🙆‍♀️!!') 
            engine_talk('hello,What should i Do For  you  🙋‍♀️!!!')

        elif 'who are you' in command :
                print('I am mini version of alexa 🙋‍♀️')
                engine_talk('I am mini version of alexa, What should i Do For  you 🙋‍♀️')

        elif 'can you do' in command :
            print(''' Tell me a joke,Make A Call, What's on my shopping list, Search on wikipedia,Play Music,What's Weather, tell date and time,Show  my Reminder ,Set A Reminder,Play Slepping song ,Read my message,Set Alarm ,find location, locate area on map,Open youtube,gmail, git hub, *** What should i Do For  you !!!??''')
            engine_talk('''Tell me a joke,Make A Call, What's on my shopping list, Search on wikipedia,Play Music,What's Weather, tell date and time,Show  my Reminder ,Set A Reminder,Play Slepping song ,Read my message,Set Alarm ,find location, locate area on map,Open youtube,gmail, git hub, *** What should i Do For  you !!!??''')

               
        elif 'play' in command:
            song = command.replace('play', '')
            print('Playing' +song) 
            engine_talk('Playing' +song) 
            pywhatkit.playonyt(song)

        elif 'date and time' in command :
            today = date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')
    # Textual month, day and year
            d2 = today.strftime("%B %d, %Y")
            print("Today's Date is ", d2, 'Current time is', time) 
            engine_talk('Today is : '+ d2)
            engine_talk('and current time is '+ time)

        elif 'time and date' in command :
            today = date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')
    # Textual month, day and year
            d2 = today.strftime("%B %d, %Y")
            print("Today's Date is ", d2, 'Current time is', time) 
            engine_talk( 'Current time is '+ time) 
            engine_talk('and Today is : '+ d2)


        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('The current time is' +time) 
            engine_talk('The current time is') 
            engine_talk(time)

        elif 'date' in command: 
            today = date.today()
            print("Today's date:", today)
    # Textual month, day and year d2 = today.strftime("%B %d, %Y") print("Today's Date is ", d2)
            engine_talk('The todays date is') 
            engine_talk(d2)

        elif 'tell me about' in command:
            name = command.replace('tell me about' , '') 
            info = wikipedia.summary(name, 1) 
            print(info)
            engine_talk(info)

        elif 'wikipedia' in command:
            name = command.replace('wikipedia' , '') 
            info = wikipedia.summary(name, 1) 
            print(info)
            engine_talk(info)
        elif 'what is' in command:
            name = command.replace('what is ' , '') 
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)

        elif 'who is ' in command:
            name = command.replace('who is' , '') 
            info = wikipedia.summary(name, 1) 
            print(info)
            engine_talk(info)

        elif 'what is ' in command :
            search = 'https://www.google.com/search?q='+command 
            print(' Here is what i found on the internet..')
            engine_talk('searching... Here is what i found on the internet..')
            webbrowser.open(search)

        elif 'joke' in command:
            _joke = pyjokes.get_joke() 
            print(_joke) 
            engine_talk(_joke)

        elif 'search' in command :
            search = 'https://www.google.com/search?q='+command 
            engine_talk('searching... ')
            webbrowser.open(search)

        elif "my location" in command:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            engine_talk("You must be somewhere near here, as per Google maps")

        elif 'locate ' in command :
            engine_talk('locating ...')
            loc = command.replace('locate', '')
        if 'on map' in loc :
            loc= loc.replace('on map',' ')
            url = 'https://google.nl/maps/place/'+loc+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc) 
            engine_talk('Here is the location of '+loc)

        elif 'on map' in command : 
            engine_talk('locating ...') 
            loc = command.split(" ")
            print(loc[1])
            url = 'https://google.nl/maps/place/'+loc[1] +'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc[1])
            engine_talk('Here is the location of '+loc[1])


        elif 'location of' in command : 
            engine_talk('locating ...')
            loc = command.replace('find location of', '')
            url = 'https://google.nl/maps/place/'+loc+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc)
            engine_talk('Here is the location of '+loc)


        elif 'where is ' in command :
            engine_talk('locating ...')
            loc = command.replace('where is', '')
            url = 'https://google.nl/maps/place/'+loc+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc) 
            engine_talk('Here is the location of '+loc)

        elif 'bootcamps' in command :
            search = 'https://www.geeksforgeeks.org/' 
            engine_talk('opening boot camps')
            webbrowser.open(search)

        elif 'boot camps' in command :
            search ='https://www.geeksforgeeks.org/'
            engine_talk('opening boot camps')
            webbrowser.open(search)
        
        elif 'python bootcamp' in command :
            search = 'https://www.geeksforgeeks.org/python-programming-language/?ref=shm' 
            engine_talk('showing python Material') 
            webbrowser.open(search)

        elif 'data struture bootcamp' in command :
            search ='https://www.geeksforgeeks.org/data-structures/?ref=shm'
            engine_talk('showing data struture Material') 
            webbrowser.open(search)


        elif 'open google' in command : 
            print('opening google ...')
            engine_talk('opening google..')
            webbrowser.open_new('https://www.google.co.in/')

        elif 'gmail' in command : 
            print('opening gmail ...') 
            engine_talk('opening gmail..')
            webbrowser.open_new('http://mail.google.com/mail/')

        elif 'open youtube' in command : 
            print('opening you tube ...') 
            engine_talk('opening you tube..')
            webbrowser.open_new('http://in.youtube.com/')

        elif 'open instagram' in command : 
            print('opening instagram ...') 
            engine_talk('opening insta gram...')
            webbrowser.open_new('https://www.instagram.com')

        elif 'open geeksforgeeks' in command : 
            print('opening geeksforgeeks ...') 
            engine_talk('opening geeksforgeeks...')
            webbrowser.open_new('https://www.geeksforgeeks.org/')

        elif 'open github' in command :
            print('opening git hub ...') 
            engine_talk('opening git hub...')
            webbrowser.open_new('https://github.com/')

        elif 'bye' in command:
            print('OK No Problem, Take Care 😊***!!') 
            engine_talk('OK No Problem, Take Care 😊!') 
            sys.exit()

        elif 'thank you' in command : 
                print('Im Honoured To Serve ☺ ') 
                engine_talk('Im Honoured To Serve ☺ ')

        elif 'stop' in command:
            print('Got It👍') 
            engine_talk('Got It👍') 
            sys.exit()

        elif 'tata' in command:
            print('See you Later😊') 
            engine_talk('See you Later😊') 
            sys.exit()

        else:
            print(' Here is what i found on the internet..') 
            engine_talk('Here is what i found on the internet..') 
            search = 'https://www.google.com/search?q='+command 
            webbrowser.open(search)

    except Exception as ex: print(ex)

print('Clearing background noise...Please wait')
engine_talk('Clearing background noise...Please wait') 
print('\n')
print('I am mini version of alexa, What should i Do For  you  🙋‍♀️!!') 
engine_talk ("I am mini version of alexa, What should i Do For  you 🙋‍♀️!!")


while True:
    run_alexa()

