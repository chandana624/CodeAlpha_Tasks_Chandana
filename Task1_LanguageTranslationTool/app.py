from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""
    error_message = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        source = request.form.get("source", "en")
        target = request.form.get("target", "hi")

        if text:
            try:
                url = "https://api.mymemory.translated.net/get"

                params = {
                    "q": text,
                    "langpair": f"{source}|{target}"
                }

                response = requests.get(url, params=params, timeout=10)
                response.raise_for_status()

                data = response.json()

                if data.get("responseStatus") == 200:
                    translated_text = data["responseData"]["translatedText"]
                else:
                    error_message = "Translation could not be completed."

            except Exception:
                error_message = (
                    "Unable to connect to the translation service. "
                    "Please try again later."
                )

    return render_template(
        "index.html",
        translated_text=translated_text,
        error_message=error_message
    )


if __name__ == "__main__":
    app.run(debug=True)
