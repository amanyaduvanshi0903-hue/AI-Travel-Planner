from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "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"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        city = request.form["city"]

        prompt = f"""
        Create a travel plan for {city} for 2-3 days.
        Include:
        - Top places to visit
        - Famous food
        - Best time to visit
        - Suggested itinerary day-wise
        """

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [{"role": "user", "content": prompt}]
            }
        )

        data = response.json()
        result = data["choices"][0]["message"]["content"]

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)