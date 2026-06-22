from flask import Flask , jsonify , request

app= Flask (__name__)


##initialize data

items = [
    {"id": 1, "name": "item 1" , "description":"haha item1"},
    {"id": 2, "name": "item 2" , "description":"haha item2"},

]

@app.route('/')
def home():
    return "welcome to the to do list"

## get: retrive all the items

@app.route('/items',methods=['get'])
def get_items():
    return jsonify(items)


if __name__== '__main__':
    app.run(debug=True)