from flask import Flask, render_template, request
import openai
import googletrans

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    gpt3_translations = None
    google_translation = None

    if request.method == 'POST':
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']
        text_to_translate = request.form['text_to_translate']

        # Call GPT-3 API
        openai.api_key = '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'
        gpt3_translations = []
        for _ in range(3):
            response = openai.Completion.create(
              engine="text-davinci-003",
              prompt=f"{source_lang}:{target_lang}:{text_to_translate}",
              max_tokens=60
            )
            gpt3_translations.append(response.choices[0].text.strip())

        # Call Google Translate API
        translator = googletrans.Translator()
        google_translation = translator.translate(text_to_translate, src=source_lang, dest=target_lang).text

        return render_template('index.html', gpt3_translations=gpt3_translations, google_translation=google_translation, source_lang=source_lang, target_lang=target_lang, text_to_translate=text_to_translate)
    else:
        return render_template('index.html')        

if __name__ == "__main__":
    app.run(debug=True)
