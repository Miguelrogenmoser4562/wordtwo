"""
COMMENTS:

The code is completly different when compared to the original one, but here is what it does.
It takes the user to the website "home.html" and waits to get a response from them. Then it gets
that input and get a word from Bard( get_word function). After that, it recieves and sends information to the client until 
the "used" list contains all of the words found in the word, or the website simply stops sending sending information due to 
the lives becoming 0.

"""
from flask import render_template, request, Blueprint, redirect
from bardapi import Bard
from dotenv import load_dotenv
load_dotenv()

app = Blueprint('app', __name__)

correct_word = "" 
used = []
_BARD_API_KEY="eAhplk9Fj5buEU5g79eMPXX7K9ZPlm3ZuJ72CqNa92nqk9ke2x-FBfh9QjhMP_pm9ox0sg."

@app.route("/", methods=["POST", "GET"])
def home():
    global correct_word
    if request.method == "GET":
        used.clear()
        return render_template("/templates/home.html", lenght=len(correct_word), word=correct_word, lives=3)


@app.route("/game_input", methods=["POST", "GET"])
def game_input():
    topic = request.form.get("topic")
    global correct_word
    correct_word = get_word(topic)
    return render_template("/templates/home_reset.html", lenght=len(correct_word), word=correct_word)


@app.route("/check_key", methods=["POST"])
def checking():
    key = request.form['value']
    if key not in correct_word:
        return "bad"

    elif key in used:
        return "meh"

    elif key in correct_word:
        locations = []
        for x in range(len(correct_word)):
            if correct_word[x] == key:
                locations.append(x)
        used.append(key)
        for x in correct_word:
            if x != " ":
                if x not in used:
                    return locations
        return "good"
    
def get_word(input):
   bard = Bard(token=_BARD_API_KEY)
   answer = bard.get_answer(f"Tell me the name of a real thing that falls under this category, but just the name and nothing else: {input}. For example, if I were to say 'us states', I would like you to give me the name of a state. Do not include any characters that are not spaces or letters.")
   return answer['content'].lower().strip()
