"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
import random
import requests


@route('/', method='GET')
def index():
    return template("chatbot.html")


emotion = ["afraid", "bored", "confused", "crying", "dancing", "dog", "excited", "giggling", "heartbroke", "inlove",
           "laughing", "money", "no", "ok", "takeoff", "waiting"]

feelings_quest = ["what's up", "whats up", "how are you", "what's new", "what's up?", "whats up?", "how are you?",
                  "what's new?", "whats new?", "what is new?", "what's up ?", "whats up ?", "how are you ?",
                  "what's new ?", "whats new ?", "what is new ?"]

feelings = ["I feel great and you?", "I'm a bit sad today and you?", "I'm so happy today and you?"]

greetings = ["hello", "hi", "hey", 'heyy', "bonjour", "shalom", "salamalikum", 'nice to meet you']

goodbye = ["bye", "goodbye", "see you", "goodnight", "see ya"]

joke = ["A snail walks into a bar and the barman tells him there's a strict policy about having snails in the bar and "
        "so kicks him out. A year later the same snail re-enters the bar and asks the barman "
        "'What did you do that for?'", 'Teacher: Do you have trouble making decisions? Student: Well...yes and no.',
        "it's someone going to a coffee and plouf"]

swearwords = ['fuck', 'shit', 'asshole', 'piss off', 'dick head', 'son of a bitch', 'bastard', 'bitch', 'damn']

bouffon = ['buffon', 'bouffon', 'bufon', 'boufon']

good_or_bad = ['good', 'great', 'super', 'bad']


def principal(input):
    print(input)
    if any(x in input.lower() for x in greetings):
        return greet()
    elif any(x in input.lower() for x in goodbye):
        return bye()
    elif 'Yoav'.lower() in input:
        return hello_yoav()
    elif 'my name is' in input:
        return 'nice to meet you'
    elif any(x in input.lower() for x in feelings_quest):
        return feeling_ans()
    elif any(x in input.lower() for x in good_or_bad):
        return new_quest()
    elif any(x in input for x in emotion):
        return emotions(input)
    elif 'comedy'.lower() in input:
        return comedy()
    elif 'adventure'.lower() in input:
        return adventure()
    elif 'action'.lower() in input:
        return action()
    elif 'documentary'.lower() in input:
        return documentary()
    elif 'history'.lower() in input:
        return history()
    elif 'horror' in input:
        return horror()
    elif 'musical' in input:
        return musical()
    elif any(x in input.lower() for x in swearwords):
        return swear()
    elif any(x in input.lower() for x in bouffon):
        return hello_yoav()
    elif 'joke' in input:
        return make_a_joke()
    elif 'weather' and 'Tel Aviv'.lower() in input:
        return weather()
    elif 'weather' in input:
        return weather()
    elif input.endswith('?'):
        return question()
    else:
        return hello(input)


def emotions(input):
    input = input.split(' ')
    if "money" in input:
        return 'Money, money, money, must be funny'
    elif "dancing" in input:
        return 'wup wup!'
    elif "afraid" in input:
        return "brrr I'm so scared!!!!"
    elif "bored" in input:
        return "Sometimes, when I'm bored I just eat"
    elif "confused" in input:
        return 'I am so confused when someone ask me to make a choice'
    elif "crying" in input:
        return "Sometimes, when I'm happy I cry"
    elif "dog" in input:
        return 'wuf wuf!'
    elif "excited" in input:
        return "I am so excited and I just can't hide it"
    elif "giggling" in input:
        return 'Ha Ha Ha'
    elif "heartbroke" in input:
        return 'If you break my heart, my mother will kill you'
    elif "inlove" in input:
        return "I don't have feelings.."
    elif "laughing" in input:
        return 'can you make me a joke please??'
    elif "no" in input:
        return 'Noooooooooooooooooooo !!!!!!'
    elif "takeoff" in input:
        return 'I need to leave yallah bye'
    elif "waiting" in input:
        return 'When I have to wait, sometimes I just fall asleep'
    return False


def new_quest():
    return 'which kind of movies do you like?'


def greet():
    return random.choice(greetings)


def bye():
    return random.choice(goodbye)


def feeling_ans():
    return random.choice(feelings)


def swear():
    return "why are you so rude?"


def hello_yoav():
    return 'hello Yoav le bouffon'


def make_a_joke():
    return random.choice(joke)


def comedy():
   list = ['The grinch', 'Love actually', 'Green Book']
   return random.choice(list)

def adventure():
    list = ['Captain Marvel', 'Aquaman', 'Avengers']
    return random.choice(list)

def action():
    list = ['Vikings', 'Jack Ryan', 'BayWatch']
    return random.choice(list)

def documentary():
    list = ['McQueen', 'The Gymkhana Files', 'Forensic Files']
    return random.choice(list)

def history():
    list = ['The Last Kingdom', 'The Crown ', 'Poldark']
    return random.choice(list)

def horror():
    list = ['The Walking Dead', 'The Circle ', 'Nightflyers']
    return random.choice(list)

def musical():
    list = ['The Greatest Showman' , 'Dumplin', 'High School Musical']
    return random.choice(list)

def weather():
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/forecast?q=London&APPID=e1185ea30127a965cc653a5a4aa33689')
    weather_obj = json.loads(r.text)
    weather_list = weather_obj['list']
    first_list = weather_list[0]
    main_weather = first_list['main']
    temp = main_weather['temp']
    humidity = main_weather['humidity']

    return "The weather in Tel Aviv is now {0} Kelvin and {1}% humid".format(temp, humidity)


def question():
    return "I don't understand your question"


def hello(name):
    return "{0} {1}".format(random.choice(greetings), name)



@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": principal(user_message)})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()
