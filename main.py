import json #for dict
from difflib import get_close_matches #to find close match
import pyttsx3 #text to speech

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)        #for female voice

def talk(text):
    engine.say(text)
    engine.runAndWait()

data = json.load(open("Dictionary.json"))

def retrive_definition(word):
    word = word.lower()

    #Check for non existing words
    #1st elif: To make sure the program return the definition of words that start with a capital letter (e.g. Delhi, Texas)
    #2nd elif: To make sure the program return the definition of acronyms (e.g. USA, NATO)
    #3rd elif: To find a similar word
    #-- len > 0 because we can print only when the word has 1 or more close matches
    #-- In the return statement, the last [0] represents the first element from the list of close matches
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        #-- If the answers is yes, retrive definition of suggested word
        if (action.lower() == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action.lower() == "n"):
            return ("The word doesn't exist yet.")
        else:
            return ("We don't understand your entry. Try again.")

def show(output):
    if type(output) == list:     # if output DataType is list (multi value)
        for item in output:      # multiple Output/def/meaning
            print("-", item)
            talk(item)
    else:                        # single Output/def/meaning
        print("-", output)
        talk(output)

if __name__ == '__main__':
    word_user = input("Enter a word: ")
    output = retrive_definition(word_user)
    show(output)
