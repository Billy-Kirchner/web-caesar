from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height 120px;
            }}
        </style>
    </head>
    <body>
        <form action="encrypt" method="post">
            <label>
                Rotate by:
                <input type="text" id="rotate-input"name="rotate-input" value="0">
            </label>
            <textarea rows="4" cols="50" id="text-input" name="text-input">{0}</textarea>
            <input type="submit">

    </body>
</html>
"""

@app.route("/encrypt", methods=["POST"])
def encrypt():
    text = request.form['text-input']
    rot = int(request.form['rotate-input'])
    new_text = rotate_string(text, rot)
    new_text_html = "<h1>" + new_text + "</h1>"
    return form.format(new_text)


@app.route("/")
def index():
    return form.format("")

app.run()


