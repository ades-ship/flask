# from flask import Flask
# ### WSGI Application
# app=Flask(__name__)

# # decorator for url
# @app.route('/')  
# def welcome():
#     return "welcome to my youtube channel.please please please subscribe to my channel"


# @app.route('/members')
# def members():
#     return "welcome to my youtube channel guys. please subscribe to my channel"

# # @app.route('/?')
# # def adesh():
# #     return "welcome to my village"

# if __name__=='__main__':
#     app.run(debug=True)   

# building url dynamically
# flask variables rules and url building



# video-4
from flask import Flask,redirect,url_for


app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to my youtube channel"

@app.route('/success/<int:score>')
def success(score):
    return "the person has passed the exam an the mark is " + str(score)
    # return "<html><body><h1>The result is passed</h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "the person is failed and get mark " +  str(score)
    # return '<html><body><h1>The result is failed </h1></body></html>'
 

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks>=50:
        result= "success"
    else:
        result='fail'
    return redirect(url_for(result,score=marks))



if __name__=='__main__':
    app.run(debug=True)



# integrating html with flask framework with http verbs
