#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

html= """<style>
body {
  background-color: black;
  text-align: center;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
}
</style>
</head>
<body>

<h1>TRIVIA TIME</h1>
<p>What is the best programming langauage to learning?</p>
<img src="https://images.unsplash.com/photo-1526379095098-d400fd0bf935?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fHB5dGhvbiUyMGNvZGV8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60" alt="Avatar" style="width:200px">

    <form action = "/login" method = "POST">
        <p><input type = "text" name = "nm"></p>
        <p><input type = "submit" value = "submit"></p>
    </form>

</body>
</html>"""

@app.route("/correct")
def success():
    return f"That is correct!"

@app.route("/")
def start():
    return html

@app.route("/login", methods = ["POST"])
def login():
    if request.method == "POST":
        if request.form.get("nm") == "Python":
                return redirect("/correct")
        else:
            return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

