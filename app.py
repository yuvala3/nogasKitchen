from flask import Flask, render_template

app = Flask(__name__)

# דף הבית
@app.route("/")
def home():
    return render_template("HomePage.html")


# ====== מנות עיקריות - הדאטה ======
mains_data = [
    {
        "name": "פלפל ממולא",
        "description": "פלפל ממולא באורז ובשר, ברוטב אדום וטעים :) יש אפשרות טבעונית/צמחונית/לל״ג.",
        "price": 15,
        "image": "img/pilpel.jpg"
    },
    {
        "name": "עוף בקינמון",
        "description": "עוף ברוטב קינמון בתוספת תפוחי אדמה ובצלים. (כמות- ליטר)",
        "price": 40,
        "image": "img/ofbekinamon.jpg"
    },
    {
        "name": "עוף ספריטו",
        "description": "תבשיל עוף עם תפוחי אדמה ובטטה ברוטב מתוק. (כמות- ליטר)",
        "price": 45,
        "image": "img/of.jpg"
    },
    {
        "name": "קישוא ממולא",
        "description": "קישוא ממולא באורז ובשר, ברוטב אדום וטעים :) יש אפשרות טבעונית/צמחונית/לל״ג.",
        "price": 22,
        "image": "img/kishu.jpg"
    },
    {
        "name": "גולאש הונגרי",
        "description": "תבשיל גולאש - בשר בקר, בתוספת תפוחי אדמה ובטטה. (כמות- ליטר)",
        "price": 65,
        "image": "img/gulash.jpg"
    }
]

# ====== ראוט לעמוד המנות העיקריות ======
@app.route("/mains")
def mains():
    # רק כדי לוודא שמגיע דאטה
    print("DEBUG mains_data length:", len(mains_data))
    return render_template("mains.html", mains=mains_data)


# שאר העמודים (אפשר להשאיר כמו שהם אחר כך)
@app.route("/sides")
def sides():
    return render_template("sides.html")


@app.route("/dairy")
def dairy():
    return render_template("dairy.html")


@app.route("/vegan")
def vegan():
    return render_template("vegan.html")


@app.route("/vegetarian")
def vegetarian():
    return render_template("vegetarian.html")


@app.route("/gluten-free")
def glutenfree():
    return render_template("glutenfree.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/favorites")
def favorite():
    return render_template("favorites.html")


if __name__ == "__main__":
    app.run(debug=True)
