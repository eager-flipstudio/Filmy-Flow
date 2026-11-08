import os

class Config:
    APP_NAME = "Filmy Flow"
    APP_VERSION = "Inception"

    APK_DOWNLOAD_URL = "https://dl.4d2.sh/HYi7MWuxhf6u.apk"
    TELEGRAM_URL = "https://t.me/FilmyFlowOfficial"

    SCREENSHOTS = [
        "https://dl.4d2.sh/mQH9BLZ6JMUW.jpg",
        "https://dl.4d2.sh/3VBSQOZTU30X.jpg",
        "https://dl.4d2.sh/BS6y1ssrxjTY.jpg",
        "https://dl.4d2.sh/Y5rF1oDisNBV.jpg",
        "https://dl.4d2.sh/ti1IOvKiTS7A.jpg",
    ]

    FIREBASE_DB_URL = os.environ.get(
        'FIREBASE_DB_URL',
        'https://filmyflowfusion-default-rtdb.firebaseio.com'
    )