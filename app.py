from flask import Flask, render_template
import pysrt


app = Flask(__name__, static_folder="static")
app.config["UPLOAD_FOLDER"] = "static"
app.use_static_route = True

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/uploadsrtfile")
def upload_srt():
    return render_template('uplpoad_srt.html')





if __name__ == "__main__":
    app.run(debug=True)

