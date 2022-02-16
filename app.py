#import flask dependency
from flask import Flask

#create new flask instance named "app"
app= Flask(__name__)

#establish root
@app.route('/')
def hello_world():
    return 'Hello World'






# if __name__ == "__main__":
#    app.run()




    

