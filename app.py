from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/product-thinking")
def product_thinking():
    return render_template("product_thinking.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/frameworks")
def frameworks():
    return render_template("frameworks.html")


@app.route("/case-study")
def case_study():
    return render_template("case_study.html")


@app.route("/teardowns")
def teardowns():
    return render_template("teardowns.html")


@app.route("/portfolio-summary")
def portfolio_summary():
    return render_template("portfolio-summary.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
