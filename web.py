from flask  import Flask , render_template,request,redirect
import  utils.json_utils as json_utils

app=Flask(__name__)
@app.route("/")
def index ():
    return render_template("web.html")


if __name__ =="__main__":
    app.run(debug=True)

