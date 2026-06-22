from flask import Flask , render_template
##instance of flask , this will be out wsgi

##wsgi app
app=Flask(__name__)

##route is important 

@app.route("/")
def Welcome():
    return "<html><H1> welcome to the business </H1> </html>"



@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template ('about.html')
##this will be the entry point of any python program
if __name__=="__main__":
    app.run(debug=True)