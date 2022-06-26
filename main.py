## integrate html with flask 
## http verb GET And POST

from flask import Flask,redirect,url_for,render_template,request


app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    # return "the person has passed the exam an the mark is " + str(score)
    # return "<html><body><h1>The result is passed</h1></body></html>"
    res=""
    if score>=50:
        res="pass"
    else:
        res="fail"

    return render_template('result.html',result=res)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person is failed and get mark " +  str(score)
    # return '<html><body><h1>The result is failed </h1></body></html>'
 
#  result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks>=50:
        result= "success"
    else:
        result='fail'
    return redirect(url_for(result,score=marks))

# result checker with html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        total_score=(science+maths+c+datascience)/4
    res=""
    
    return redirect(url_for('success',score=total_score))




if __name__=='__main__':
    app.run(debug=True)
