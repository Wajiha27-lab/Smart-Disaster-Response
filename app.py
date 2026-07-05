import os 
import google.generativeai as genai
from dotenv import load_dotenv

import weather
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")
from flask import Flask, render_template, request, send_from_directory  # type: ignore
from weather import get_weather
from database import init_db, save_report, get_reports

app = Flask(__name__)
init_db()

def secure_filename(filename):
    filename = os.path.basename(filename)
    filename = filename.replace(" ", "_")
    valid_chars = "-_.()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(c for c in filename if c in valid_chars).strip(".")

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    location = request.form.get("location")
    report = request.form.get("report", "")

    file = request.files.get("image")
    filename = ""

    if file and file.filename:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    prompt = f"""
you are an emergency disaster response assistant.
Analyze this disaster report.

Location:
{location}

Report:
{report}

Return:
1. Risk Level (Low, Medium, High)
2. Possible Disaster
3. Safety Recommendations
"""
    response = model.generate_content(prompt)

    return render_template(
        "dashboard.html",
        location=location,
        report=report,
        filename=filename,
        ai_response=response.text,
        weather=weather
    )
@app.route("/reports")
def reports():
    data = get_reports()
    return render_template("reports.html", reports=data)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)
