from flask import Flask,render_template,request
from random import choice,shuffle
from string import ascii_lowercase

app = Flask(__name__)

@app.route("/",methods=["POST", "GET"])
def generator_psswrd():

    if request.method == "POST":
        digit = int(request.form['digit'])
        letter = int(request.form['letter'])

        digit_lst = [choice([str(x) for x in range(9)]) for x in range(digit)]

        letter_lst = [choice(ascii_lowercase) for i in range(letter)]

        digit_and_letter = digit_lst + letter_lst

        shuffle(digit_and_letter)

        digit_and_letter = f"<h2>Сгенерированный пароль - {''.join(digit_and_letter)}</h2>"

        return render_template("generator_password.html", digit_and_letter=digit_and_letter)

    return render_template("generator_password.html")

if __name__ == "__main__":
    app.run(debug=True)