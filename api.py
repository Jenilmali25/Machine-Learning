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
    return "Welcome to Detials of Students Retrival API"

#retrieve all the apps
@app.route('/items')
def get_items():
    return jsonify(data)

#get a specific item by id 
@app.route('/items/<string:name>', methods=['GET'])
def get_item(name):
    item=""
    for key, value in data.items():
        if key==name:
            item = value
            break
    if item:
        return jsonify(item)
    return jsonify({"Error":"Item not Found"})


# Post : create a new Student details 
@app.route('/items', methods=['POST'])
def create():
        if not request.json or not "name" in request.json:
             return jsonify({"error":"item not found"})
        new_item={
             
        }

if __name__ == "__main__":
    app.run(debug=True)