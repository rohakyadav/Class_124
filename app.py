from flask import Flask
# creating flask object
app = Flask(__name__)
#defining route
@app.route("/") 
def hello_world(): 
    return "Hello World!"
if __name__ =='__main__':
    app.run()


