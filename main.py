import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

import random
import math

version = 0.2 # Version of Hermes

listener = sr.Recognizer() # Recognizer that listens for speech
engine = pyttsx3.init() # Python text-to-speech used for making Hermes speak
engine.setProperty('rate', 175)
engine.say('Hermes version ' + str(version) + 'online')
engine.runAndWait()


command = '' # The command string gotten from the user's speech

def speak(text):
    '''Uses the TTS engine to make Hermes speak.

    :param text: What hermes is going to say.
    '''

    print('What I am saying: ' + text)
    # Say the text
    engine.say(text)
    # Wait for next command
    engine.runAndWait()

def take_command():
    '''Uses the speech recognizer to convert speech into text: the 'command' string.

    :return: Returns the command string.
    '''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source) # Sets the audio source to be the microphone
            command = listener.recognize_google(voice) # Uses Google's speech recognition to convert what is spoken into a string
            # Fromat command to make processing easier
            command = command.lower() 
            command = command.split()
            if command[0] == 'hermes':
                command.remove('hermes')
            command = " ".join(command)
            # if 'hermes' in command:
            #     command = command.replace('hermes', '')
    except:
        pass
    return command

def run_command():
    '''Runs a command using the speech from take_command().

    "if '[word]' in command:" <- use for searching for keywords
    '''

    # Get command
    command = take_command()

    print('Command: ' + command)
    # Parse command for keywords, and execute proper function and get rid of unecessary words
    # TODO: There has to be a better way to parse commands than a bunch of if satements
    if 'what sandwich should i make' in command:
        sandwich()
    elif 'what kind of sandwich should I make' in command:
        sandwich()
    elif 'play' in command:
        play_song(command)
    elif 'what is the time' in command:
        time()
    elif 'what is the date' in command:
        date()
    elif 'who is' in command:
        command.replace('who is','')
        search(command)
    elif 'what is' in command:
        command.replace('what is','')
        search(command)
    elif 'tell me a joke' in command:
        joke()
    elif 'how are you' in command:
        how_am_i()
    elif 'how many days until' in command:
        command.replace('how many days until','')
        how_many_days_till(command)
    elif 'how many minutes until' in command:
        command.replace('how many minutes until','')
        how_many_days_till(command)
    elif command == 'hello hermes':
        hi()
    elif command == 'hey hermes':
        hi()
    else:
        speak('I did not hear anything')
        print(command)

def sandwich():
    '''A function that pulls from a list of random sandwich ingredients (my preferences) 
    and tells you what to put in your sandwich.
    '''

    main_ingredient = ['peanut butter', 'nutella'] # List of the 'main' ingredients in the sandwich
    second_ingredient = ['jelly', 'marshmallow fluff', 'banana'] # List of ingredients that work well with the main ingredient
    
    # Choose from the main ingredient list
    main = random.choice(main_ingredient)
    
    # Speak the ingredients, Nutella does not get a second ingredient
    if main == 'nutella':
        speak('Just nutella today sir')
    else:
        speak(main + ' and ' + random.choice(second_ingredient) + ' for today sir')

def play_song(play_song):
    '''Plays a requested song on YouTube.

    :param play_song: The song that is requested to be played.
    '''
    song = play_song # The song to be played
    # Get rid of unnecessary words in command
    song = song.replace('play', '')
    # Confirm what song is playing by saying it
    speak('playing' + song)
    # Play song on YouTube
    pywhatkit.playonyt(song)

def time():
    '''Say what time it is.
    '''

    time = datetime.datetime.now().strftime('%I:%M %p') # Current time
    # Say what time it is
    speak('it is currently ' + time)

def date():
    '''Says the date.
    '''
    todaysDate = datetime.datetime.today().strftime('%B %d, %Y') # Current date
    # Says the date
    speak('the current date is ' + todaysDate)

def search(query):
    '''Searches a specific query on Wikipedia.

    :param query: What is to be searched.
    '''

    info = wikipedia.summary(query, 2) # Info on query on Wikipedia
    # Says the info
    speak(info)

def joke():
    '''Tells a joke
    '''
    # TODO: find better joke library (pyjokes can be used if I ask "tell me a computer science joke")
    # Says the joke
    speak(pyjokes.get_joke())


def update_gradual_brightness(given_time):
    '''A function intended to gradually increase brightness of smart lights.
    This is supposed to be healthier to wake up to than a traditional alarm.

    :param given_time: Over how long the lights should brighten (In minutes).
    :return: brightness value.
    '''

    brightness = 0 # Initial brightness level
    time = given_time # Over how long the lights should brighten (In minutes)

    # This equation gradually gets the brightness value to 100 once x == time
    # https://www.geogebra.org/calculator ( input "y = -10( sqrt(100 - x^2) ) + 100" )
    brightness = -10 * math.sqrt(100 - (time ** 2)) + 100
    # Return brightness value
    return brightness

def change_brightness(given_brightness):
    '''Changes the brightness acording to the value gotten from the update_gradual_brightness() function.

    :param given_brightness: The brightness value.
    '''    

    brightness = given_brightness # Get the brightness from the update_gradual_brightness() function
    # TODO: link to smart-home and trigger it automatically every morning
    # TODO: This does not make sense to only calculate this once, it should be in a loop that triggers ever x amount of seconds to get the new brightness

def remind(what, when):
    '''Intended to add to a list of reminders, and then remind the user when those reminder times are met.

    :param what: What the reminder is about.
    :param when: When to remind the user.
    '''

    reminder = what # What to be reminded about
    reminder_time = when # When to remind the user
    # TODO: Link Hermes to a text file and put these into said text file (Or maybe a spreadsheet)

def how_am_i():
    '''Tells the user how Hermes is doing mood-wise (if asked).
    '''

    # TODO: test
    how = ['well', 'good', 'great', 'fine', 'bad'] # List of responses Hermes can use when asked how he is doing

    '''
    TODO: Hermes should give the same response if asked again in a small amount of time. 
    If the mood changes and Hermes is asked again, Hermes should have a different response than the standard
    '''

    ask = [' How are you?', ' How are you doing?'] # Different ways Hermes can ask how the user is doing, to be polite
    # Says both how Hermes is doing and asks how the user is doing
    speak('I am doing ' + random.choice(how) + ' sir.' + random.chooice(ask))

def hi():
    '''Says a greeting to a user.
    '''

    greeting = ['hi', 'hello', 'hey'] # List of greetings
    # Says the greeting
    speak(random.choice(greeting) + ' sir.')
# 
def how_many_days_till(date):
    '''Says how many days until the given date.

    :param date: What date the user wants to query how long it is until.
    '''

    # TODO: actually finish this function
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'] #list of month names
    month_numbers = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',] #list of numbers corresponding to each month
    dates = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth', 'twentieth', 'twenty first', 'twenty second', '', '', '', '', '', '', '', '', '', ''] # List of ways Hermes can say the date
    date_numbers = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''] # Numbers for each day in a month
    
    i = 0 # Iterator 
    
    date1 = datetime.datetime.today() # Today's date

    date2 = date # Given date from User
    
    # Make string into list
    date2 = date2.split()
    # Iterate through list in order to reformat it so it is easier to process
    for word in date2:
        if ',' in word:
            word.replace(',', '')
        while i < months.len():
            if word == months[i]:
                word.replace(word, month_numbers[i])
            i += 1
        i = 0


    # Join list back into string using m/d/y format    
    date2 = "/".join(command)
    # Use datetime to figure out the date from the date2 string
    date2 = datetime.datetime.strptime(date, '%d/%m/%y')
    # Calculate the difference
    difference = date2 - date1

    # TODO: Actually say the difference
    print('there is ' + difference + 'days until ' + date + '.')

def how_long_till(time):
    '''Says how long until given time from the user.

    :param time: The time given by the user in order to find out how far away said time is.
    '''
    
    # TODO: test
    time1 = datetime.datetime.now() # THe current time
    time2 = datetime.datetime.strptime(time, '%I:%M %p') # The requested time in hour:minute (am/pm)
    # Calculate differences between times
    difference = time2 - time1

    # Say the time difference
    speak('there is ' + difference + 'minutes until ' + time + '.')

def log(what):
    print("DELETE ME")

# IF TESTING COMMENT OUT LINE BELOW
#run_command()