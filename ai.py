import google.generativeai as genai
from config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_disaster(location, report):
    """
    Analyze the disaster report using Gemini AI.
    """

    prompt = f"""
You are an expert Disaster Management AI.

Analyze the following disaster report.

Location:
{location}

Citizen Report:
{report}

Provide the response in this format:

Risk Level:
Possible Disaster:
Summary:
Immediate Actions:
Safety Tips:
Resources Needed:
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"