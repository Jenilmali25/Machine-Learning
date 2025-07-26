#building url dynamically

#jinja 2 template engine

#variable rule
from flask import Flask
app=Flask(__name__)

@app.route('/<int:value>')
def a(value):
    return f"the value is {value}"

if __name__ == "__main__":
    app.run(debug="True")