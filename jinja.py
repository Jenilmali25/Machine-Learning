
#variable rule
from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)

@app.route('/<int:value>')
def a(value):
    res=""
    if(value%2==0):
        res=f"{value} is a Even number"
    else:
        res=f"{value} is a Odd Number"
    return render_template('result.html', results=res)



#jinja 2 template engine
'''
{{   }} expression to print output in html
{%...%} Condiitions and For loops
{#..#} comments
'''
@app.route('/result<int:value>')
def result(value):
    return render_template('result1.html', results=value)


#building url dynamically
@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method=="POST":
        number = float(request.form['m'])
    else:
        return render_template('build_url.html')
    return redirect(url_for('result', value=int(number)))



if __name__ == "__main__":
    app.run(debug=True)