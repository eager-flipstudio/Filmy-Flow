from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template(
        'index.html',
        app_name=app.config['APP_NAME'],
        app_version=app.config['APP_VERSION'],
        apk_url=app.config['APK_DOWNLOAD_URL'],
        telegram_url=app.config['TELEGRAM_URL'],
        screenshots=app.config['SCREENSHOTS'],
        firebase_db_url=app.config['FIREBASE_DB_URL']
    )

if __name__ == '__main__':
    app.run(debug=True)