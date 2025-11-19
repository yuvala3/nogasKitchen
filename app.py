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
        "description": "פלפל ממולא באורז ובשר, ברוטב אדום. יש אפשרות טבעונית/צמחונית/לל״ג.",
        "price": 15,
        "image": "img/pilpel.jpg"
    },
    {
        "name": "עוף בקינמון",
        "description": "עוף ברוטב קינמון בתוספת תפוחי אדמה ובצלים",
        "price": 40,
        "image": "img/ofbekinamon.jpg"
    },
    {
        "name": "עוף ספריטו",
        "description": "תבשיל עוף עם תפוחי אדמה ובטטה ברוטב מתוק",
        "price": 45,
        "image": "img/of.jpg"
    },
    {
        "name": "קישוא ממולא",
        "description": "קישוא ממולא באורז ובשר, ברוטב אדום. יש אפשרות טבעונית/צמחונית/לל״ג",
        "price": 22,
        "image": "img/kishu.jpg"
    },
    {
        "name": "גולאש הונגרי",
        "description": "תבשיל גולאש - בשר בקר, בתוספת תפוחי אדמה ובטטה",
        "price": 65,
        "image": "img/gulash.jpg"
    },
    {
        "name": "קציצות בשר ברוטב",
        "description": "קציצות בשר ברוטב אדום בתוספת אפונה, תפוחי אדמה ובצל",
        "price": 65,
        "image": "img/basar.jpg"
    },
    {
        "name": "שניצלים",
        "description": "שניצלים מטוגנים- ניתן להזמין אפויים",
        "price": 65,
        "image": "img/shnizel.jpg"
    },
    {
        "name": "נודלס מוקפץ עוף",
        "description": "אטריות נודלס מוקפצות עם ירקות ועוף, ניתן להזמין צמחוני",
        "price": 65,
        "image": "img/mukpaz.jpg"
    },
    {
        "name": "תבשיל בקר ברוטב הונגרי",
        "description": "בשר מסוג שריר 8 בתבשיל הונגרי",
        "price": 65,
        "image": "img/shrir8.jpg"
    }
]

sides_data = [
    { "name": "אורז לבן", "description": "אורז לבן, יש אפשרות לאורז צהוב", "price": 25, "image": "img/rice.jpg" },
    { "name": "אורז עם ירקות", "description": "אורז עם ירקות", "price": 25, "image": "img/orezyerakot.jpg" },
    { "name": "מג׳דרה", "description": "מג׳דרה - אורז עם עדשים ובצל", "price": 25, "image": "img/mejadara.jpg" },
    { "name": "בורגול", "description": "בורגול עם ירקות", "price": 25, "image": "img/burgul.jpg"},
    { "name": "זיתים מבושלים", "description": "תבשיל זיתים ברוטב אדום", "price": 25, "image": "img/zeitim.jpg"},
    {"name": "תחתיות ארטישוק", "description": "תחתיות ארטישוק ברוטב", "price": 25, "image": "img/artishok.jpg"},
    {"name": "נודלס עם ירקות", "description": "נודלס מוקפץ עם ירקות- יש אפשרות ללא ירקות/תוספת חלבון", "price": 25, "image": "img/nudels.jpg"},
    {"name": "שעועית ירוקה", "description": "שעועית ירוקה מבושלת ברוטב", "price": 25, "image": "img/shueet.jpg"},
    {"name": "בורקס בשר", "description": "בורקס בשר טחון בתערובת בצלים", "price": 10, "image": "img/burekasbasar.jpg"},
    {"name": "לביבות ירק", "description": "לביבות ירק עשירות בויטמינים וירקות, ניתן להזמין אפויות/מטוגנות", "price": 10, "image": "img/yerek.jpg"},
    {"name": "לביבות תרד", "description": "לביבות תרד, ניתן להזמין אפויות/מטוגנות", "price": 10,"image": "img/teredlevivot.jpg"},
    {"name": "סלט חצילים", "description": "סלט חצילים", "price": 10,"image": "img/salathazilim.jpg"},
    {"name": "סלט תפוחי אדמה במיונז", "description": "סלט תפוחי אדמה רכים במיונז עם מלפפונים חמוצים וביצה קשה", "price": 10,"image": "img/tapuh.jpg"},
    {"name": "כרובית ברוטב אדום", "description": "כרובית מבושלת ברוטב אדום, רכה וטעימה :)", "price": 10, "image": "img/kruvit.jpg"},
    {"name": "תפוחי אדמה ספריטו", "description": "תפוחי אדמה מבושלים ברוטב מתוק", "price": 10, "image": "img/sifrito.jpg"},
    {"name": "אגרול", "description": "אגרול עם ירקות/בשר/עוף/טופו, מטוגן או אפוי", "price": 10, "image": "img/egrol.jpg"},
    {"name": "פטריות ממולאות", "description": "תבשיל פטריות ממולאות בשר, ניתן להחליף למנה צמחונית", "price": 10,
     "image": "img/mashrooms.jpg"}
]

dairy_data = [
    {"name": "פשטידת פלפלים", "description": "תיאור", "price": 80, "image": "img/pilpelim.jpg"},
    {"name": "פשטידת תירס", "description": "תיאור", "price": 80, "image": "img/tiras.jpg"},
    {"name": "פשטידת בטטה", "description": "תיאור", "price": 80, "image": "img/batata.jpg"},
    {"name": "פשטידת ברוקולי", "description": "תיאור", "price": 80, "image": "img/brokoli.jpg"},
    {"name": "פשטידת פטריות", "description": "תיאור", "price": 80, "image": "img/pitriot.jpg"},
    {"name": "פשטידת תרד", "description": "תיאור", "price": 80, "image": "img/tered.jpg"},
    {"name": "פשטידת תרד ופלפלים", "description": "תיאור", "price": 80, "image": "img/pilpeltered.jpg"},
    {"name": "בורקס גבינות", "description": "בורקס גבינות - בולגרית 5%, עמק 15%", "price": 10, "image": "img/burekasgvina.jpg"},
]

soups_data = [
    {"name": "מרק חרירה", "description": "מרק חרירה מרוקאי עשיר בירקות, עדשים וחומוסים", "price": 40, "image": "img/hrira.jpg"},
    {"name": "מרק כתום", "description": "תיאור", "price": 40, "image": "img/katom.jpg"},
    {"name": "מרק ירקות", "description": "תיאור", "price": 40, "image": "img/yerakot.jpg"},
    {"name": "מרק שעועית", "description": "תיאור", "price": 40, "image": "img/shueetsoup.jpg"},
    {"name": "מרק תירס", "description": "תיאור", "price": 40, "image": "img/tirassoup.jpg"},
    {"name": "מרק עגבניות", "description": "תיאור", "price": 40, "image": "img/tomatosoup.jpg"}
]

fishes_data = [
    {"name": "דג חריימה מרוקאי", "description": "דג אמנון ברוטב אדום מרוקאי פיקנטי", "price": 40, "image": "img/hraime.jpg"},
    {"name": "דג אמנון באגוזים", "description": "דג אמנון ברוטב עשיר עם אגוזי מלך", "price": 40, "image": "img/amnon.jpg"},
    {"name": "פילה סלמון ברוטב אסיאתי", "description": "עם עשבי תיבול, רוטב מתקתק", "price": 40, "image": "img/salmonrotev.jpg"},
    {"name": "פילה סלמון אפוי", "description": "אפוי בתנור עם שמן זית ופלפל גס", "price": 40, "image": "img/salmonafui.jpg"},
    {"name": "פילה סלמון ברוטב אדום", "description": "נתחי סלמון ברוטב אדום עם ירקות", "price": 40,
     "image": "img/salmonadom.jpg"},
    {"name": "דג בורי עם אגוזי מלך", "description": "דג בורי ברוטב עשיר עם אגוזי מלך", "price": 40,
     "image": "img/buri.jpg"}
]

@app.route("/fishes")
def fishes():
    return render_template(
        "menu_page.html",
        page_title="דגים",
        items=fishes_data
    )

@app.route("/mains")
def mains():
    return render_template(
        "menu_page.html",
        page_title="מנות עיקריות",
        page_details="כלל המנות מגיעות בקופסה של ליטר, לאפשרות צמחונית/טבעונית יש לעדכן בעת ההזמנה הטלפונית",
        items=mains_data
    )

@app.route("/sides")
def sides():
    return render_template(
        "menu_page.html",
        page_title="תוספות",
        page_details= "כלל התוספות מגיעות בקופסה של ליטר, לאפשרות צמחונית/טבעונית, יש לעדכן בעת ההזמנה הטלפונית",
        items=sides_data
    )

@app.route("/dairy")
def dairy():
    return render_template(
        "menu_page.html",
        page_title="חלבי",
        items=dairy_data
    )


@app.route("/soups")
def soups():
    return render_template(
        "menu_page.html",
        page_title="מרקים",
        items=soups_data
    )

@app.route("/gluten-free")
def glutenfree():
    return render_template(
        "menu_page.html",
        page_title="ללא גלוטן",
        items=glutenfree_data
    )


if __name__ == "__main__":
    app.run(debug=True,port=8000)
