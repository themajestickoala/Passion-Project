from flask import Flask, render_template             
app = Flask(__name__)
@app.route('/home', methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.route('/upload.php', methods=['GET','POST'])
def upload():
    return render_template("imgReceived.html")
    if __name__ == "__main":
        app.run(debug=True)
