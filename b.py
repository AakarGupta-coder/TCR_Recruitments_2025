from c import random_noise

def star(String):
    return "--*--" + String + "--*--"

def wowify(String):
    return "✨" + String.upper() + "✨"

def invert_case(String):
    return ''.join(character.lower() if character.isupper() else character.upper() for character in String)

def add_noise(String):
    return random_noise() + String + random_noise()

def echo(String):
    return (String + " ") * 5 

def wrap_in_brackets(String):
    return "[[" + String + "]]"
 
