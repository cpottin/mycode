#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

questions = {'What year was Disneyland opened?' : ["1925", "1955", "1945","1970"],
        "What is the name of Wendy's dog in Peter Pan?" : ["Nana", "Duke", "Ruby", "Yeller"] , "What does Hakuna Matata mean?" : ["No One Cares", "No Lions Allowed", "No Friends", "No Worries"], "Genie was stuck in the lamp for how many years before Aladdin found him?" : ["200", "5000", "10000","5"]}

correct_answers = ["1955", "Nana", "No Worries", "10000"]

#grab the value 'question'
@app.route("/")
def quiz():
    return render_template("triviatemplate.html", q = questions.keys(), o = questions)

@app.route('/quiz', methods=['POST'])
def answers():
    correct = 0
    for i in questions.keys():
        answered = request.form[i]
       # if answer is in the list of correct answers then increase correct score +1
        if answered in correct_answers:
            correct = correct+1
    return '<h1> Correct Answers: <u> ' +str(correct)+'</u></h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

