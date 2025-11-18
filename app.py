from flask import Flask, render_template

app = Flask(__name__)


# דף הבית
@app.route("/")
def home():
    return render_template("HomePage.html", page_head_title="Homepage")


# תפריט ללא גלוטן
@app.route("/search")
def search():
    return "<h1>תפריט ללא גלוטן (עמוד יגיע בהמשך)</h1>"


# תפריט ראשי
@app.route("/upload")
def upload():
    return "<h1>תפריט ראשי (עמוד יגיע בהמשך)</h1>"


# קצת עלינו
@app.route("/about")
def about():
    return "<h1>קצת עלינו (עמוד יגיע בהמשך)</h1>"

# קצת עלינו
@app.route("/contact")
def contact():
    return "<h1>צור קשר (עמוד יגיע בהמשך)</h1>"


if __name__ == "__main__":
    app.run(debug=True)
