from flask import Flask,render_template,request,url_for,jsonify

app=Flask(__name__)


@app.route("/")
def home():
    return "Welcome to my Flask app"

@app.route("/success/<int:score>")
def success(score):
    return "the person has passed with score "+str(score)


@app.route("/fail/<int:score>")
def fail(score):
    return "the person has fail "+str(score)

@app.route("/calculate",methods=["POST","GET"])
def calculate():
    if request.method=="GET":
        return render_template("calculate.html")
    else:
        maths=float(request.form["maths"])
        science=float(request.form["science"])
        history=float(request.form["history"])
        
        average_marks=(maths+science+history)/3
        result=""
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        return render_template("result.html",results=average_marks)


#when ever we create a api we need to create a input jason
@app.route("/api",methods=["POST"])
def calculate_sum():
      #when we post data throuph api it is get_json
      data=request.get_json()
      #refer to the json that u have created
      a_val=float(dict(data)['a'])
      b_val=float(dict(data)['b']) 
      #return json file
      return jsonify(a_val+b_val)



if __name__=="__main__":
    app.run(debug=True)