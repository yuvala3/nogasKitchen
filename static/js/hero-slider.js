// רשימת תמונות מתחלפות
const heroImages = [
    "/static/img/boxes-noga.jpg",
    "/static/img/mukpaz.jpg",
    "/static/img/ofbekinamon.jpg",
    "/static/img/gulash.jpg",
    "/static/img/burgul.jpg",
    "/static/img/pilpel.jpg",
    "/static/img/hrira.jpg",
    "/static/img/amnon.jpg",
    "/static/img/sifrito.jpg",
    "/static/img/yerakot.jpg",
    "/static/img/basar.jpg",
    "/static/img/shrir8.jpg"
];

let currentIndex = 0;

function changeBackground() {
    const heroSection = document.querySelector('.hero-with-image');
    if (!heroSection) return; // אם הדף לא כולל hero, למנוע שגיאה

    heroSection.style.backgroundImage = `url('${heroImages[currentIndex]}')`;

    // שעון לתמונה הבאה
    currentIndex = (currentIndex + 1) % heroImages.length;
}

// הפעלה אוטומטית כל 4 שניות
setInterval(changeBackground, 3000);

// הפעלה ברגע שהדף נטען
window.onload = changeBackground;
