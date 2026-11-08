from flask import Flask, render_template, Response, stream_with_context, redirect
import requests
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

@app.route('/download')
def download():
    url = app.config['APK_DOWNLOAD_URL']
    filename = app.config['APP_NAME'].replace(' ', '') + '.apk'

    try:
        upstream = requests.get(
            url,
            stream=True,
            headers={'User-Agent': 'Mozilla/5.0'},
            allow_redirects=True,
            timeout=60
        )

        if upstream.status_code != 200:
            return redirect(url)

        def generate():
            for chunk in upstream.iter_content(chunk_size=8192):
                if chunk:
                    yield chunk

        headers = {
            'Content-Disposition': f'attachment; filename="{filename}"',
            'Content-Type': 'application/vnd.android.package-archive',
        }

        if 'Content-Length' in upstream.headers:
            headers['Content-Length'] = upstream.headers['Content-Length']

        return Response(
            stream_with_context(generate()),
            headers=headers,
            status=upstream.status_code
        )
    except Exception as e:
        print(f"Download error: {e}")
        return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)