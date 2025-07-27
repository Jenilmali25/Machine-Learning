#Put and Delete ----HTTP Verbs
#Working with API's ---Json

from flask import Flask, jsonify, request

app=Flask(__name__)
data = {
            "Jenil" : {
                "age": 20,
                "language": "Python"
            },
            "Mansi" : {
                "age":21,
                "language":"c++"
            }
        }

@app.route('/')
def home():
    return "Welcome to sample TODO List App"

#retrieve all the apps
@app.route('/items')
def get_items():
    return jsonify(data)

#get a specific item by id 
@app.route('/items/<string:name>', methods=['GET'])
def get_item(name):
    item = data.get(name)
    if data:
        return jsonify(item)
    return jsonify({"Error":"Item not Found"})


if __name__ == "__main__":
    app.run(debug=True)