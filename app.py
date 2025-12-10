from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_lang():
    lang = request.args.get("lang", "en").lower()
    return "zh" if lang in ("zh", "cn", "zh-cn") else "en"


@app.route("/")
def home():
    lang = get_lang()
    return render_template("horizon_index.html", lang=lang)


@app.route("/lang/<code>")
def switch_lang(code):
    # simple helper so you can link to /lang/zh or /lang/en
    lang = "zh" if code.lower() in ("zh", "cn", "zh-cn") else "en"
    return redirect(url_for("home", lang=lang))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
