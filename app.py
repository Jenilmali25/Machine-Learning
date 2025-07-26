from flask import Flask, render_template

#wsgi appln
app=Flask(__name__)

@app.route('/')
def neww():
    return "<html><h1>This is head</h1></html>"

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/aboutus')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)