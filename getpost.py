from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')
def home():
    return "Hello world"


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method=="POST":
        fname = request.form['name']
        return f"Hello {fname}"
    return render_template('form.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method=='POST':
        fname=request.form['name']
        city=request.form['city']
        return f"{fname} from {city}"
    return render_template('form.html')
if __name__=="__main__":
    app.run(debug=True)
    