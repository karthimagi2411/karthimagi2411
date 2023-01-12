from flask  import Flask , render_template,request,redirect
import  utils.json_utils as json_utils
file="web.json"

app=Flask(__name__)
@app.route("/")
def index ():
    data=json_utils.read_json(file)
    return render_template("login.html")

@app.route("/register")
def first ():
    data=json_utils.read_json(file)
    
    return render_template("registration.html")
@app.route ("/go to login", methods=["GET","POST"])
def go_to_login():
    data=json_utils.read_json(file)
    if request.method == "POST":
        firstname=request.form["firstname"]
        lastname=request.form["lastname"]
        email=request.form["email"]
        username=request.form["username"]
        password=request.form["password"]
        conform_pass=request.form["confirmpassword"]
        dob=request.form["dob"]
        information={
            "1":firstname,
            "2":lastname,
            "3":email,
            "4":username,
            "5":password,
            "6":conform_pass,
            "7":dob
        }
        data["karma"].append(information)
        json_utils.write_json(file,data)
        return  render_template("login.html" , data = data["karma"])
    






    



if __name__ =="__main__":
    app.run(debug=True)

