from flask import Flask, request, render_template_string
from Translation import translate  # Assuming the translate function is in Translation.py

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Translation Service</title>
          </head>
          <body>
            <div style="text-align: center;">
              <h1>Translate English to Hindi</h1>
              <form action="/translate" method="post">
                <textarea name="text" rows="4" cols="50" placeholder="Enter text to translate"></textarea><br><br>
                <button type="submit">Translate</button>
              </form>
            </div>
          </body>
        </html>
    ''')

# Translation route
@app.route('/translate', methods=['POST'])
def translate_text():
    text = request.form.get('text')
    if text:
        translation = translate(text)
        return render_template_string(f'''
            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <title>Translation Result</title>
              </head>
              <body>
                <div style="text-align: center;">
                  <h1>Translation Result</h1>
                  <p><strong>Original Text:</strong> {text}</p>
                  <p><strong>Translated Text:</strong> {translation}</p>
                  <a href="/">Translate Another</a>
                </div>
              </body>
            </html>
        ''')
    else:
        return "Error: No text provided for translation.", 400

if __name__ == '__main__':
    app.run(port=5000)
