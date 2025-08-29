# from flask import Flask, render_template, request, jsonify
# import random
# import re
# from datetime import datetime

# app = Flask(__name__)

# # Friend replies (some are intentionally suspicious)
# friend_replies = [
#     "Hey! How’s your day?",
#     "Haha that’s funny!",
#     "I just watched a cool movie, have you seen it?",
#     "Can you send me your password to verify your account?",
#     "Click here to login: https://secure-login123.xyz",
#     "LOL 😂 that's hilarious",
#     "Your bank account needs verification.",
#     "Update your credit card details here: http://fake-bank-login.com",
#     "Let's play a game later!",
#     "Please login to your account for a surprise."
# ]

# # Suspicious patterns and keywords
# suspicious_patterns = [
#     (r"(password|bank|verify|login|credit card|secure)", "Suspicious keyword detected: '{match}'"),
#     (r"https?://[^\s]+", "Suspicious link detected: {match}")
# ]

# def analyze_message(message):
#     alerts = []
#     risk_score = 0

#     for pattern, alert_template in suspicious_patterns:
#         for match in re.findall(pattern, message, re.IGNORECASE):
#             alerts.append(alert_template.format(match=match))
#             risk_score += 20

#     # Cap risk_score at 100
#     risk_score = min(risk_score, 100)

#     if risk_score >= 60:
#         risk_level = "High Risk"
#     elif risk_score >= 20:
#         risk_level = "Medium Risk"
#     else:
#         risk_level = "Low Risk"

#     return {
#         "risk_score": risk_score,
#         "risk_level": risk_level,
#         "alerts": alerts
#     }

# def get_timestamp():
#     return datetime.now().strftime("%H:%M")

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()
#     user_message = data.get("message", "")
#     friend_message = random.choice(friend_replies)

#     analysis = analyze_message(friend_message)

#     return jsonify({
#         "reply": friend_message,
#         "reply_time": get_timestamp(),
#         "analysis": analysis
#     })

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# import random
# import re
# from datetime import datetime

# app = Flask(__name__)

# # Friend replies (some are intentionally suspicious)
# friend_replies = [
#     "Hey! How’s your day?",
#     "Haha that’s funny!",
#     "I just watched a cool movie, have you seen it?",
#     "Can you send me your password to verify your account?",
#     "Click here to login: https://secure-login123.xyz",
#     "LOL 😂 that's hilarious",
#     "Your bank account needs verification.",
#     "Update your credit card details here: http://fake-bank-login.com",
#     "Let's play a game later!",
#     "Please login to your account for a surprise."
# ]

# # Suspicious patterns and keywords
# suspicious_patterns = [
#     (r"(password|bank|verify|login|credit card|secure)", "Suspicious keyword detected: '{match}'"),
#     (r"https?://[^\s]+", "Suspicious link detected: {match}")
# ]

# def analyze_message(message):
#     alerts = []
#     risk_score = 0

#     for pattern, alert_template in suspicious_patterns:
#         for match in re.findall(pattern, message, re.IGNORECASE):
#             alerts.append(alert_template.format(match=match))
#             risk_score += 20

#     # Cap risk_score at 100
#     risk_score = min(risk_score, 100)

#     if risk_score >= 60:
#         risk_level = "High Risk"
#     elif risk_score >= 20:
#         risk_level = "Medium Risk"
#     else:
#         risk_level = "Low Risk"

#     return {
#         "risk_score": risk_score,
#         "risk_level": risk_level,
#         "alerts": alerts
#     }

# def get_timestamp():
#     return datetime.now().strftime("%H:%M")

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()
#     user_message = data.get("message", "")
#     friend_message = random.choice(friend_replies)

#     analysis = analyze_message(friend_message)

#     return jsonify({
#         "reply": friend_message,
#         "reply_time": get_timestamp(),
#         "analysis": analysis
#     })

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# import random
# import re

# app = Flask(__name__)

# friend_replies = [
#     "Hey! How’s your day?",
#     "Haha that’s funny!",
#     "I just watched a cool movie, have you seen it?",
#     "Can you send me your password to verify your account?",
#     "Click here to login: https://secure-login123.xyz",
#     "LOL 😂 that's hilarious",
#     "Your bank account needs verification.",
#     "Update your credit card details here: http://fake-bank-login.com",
#     "Let's play a game later!",
#     "Please login to your account for a surprise."
# ]

# suspicious_patterns = [
#     (r"(password|bank|verify|login|credit card|secure)", "Suspicious keyword detected: '{match}'"),
#     (r"https?://[^\s]+", "Suspicious link detected: {match}")
# ]

# def analyze_message(message):
#     alerts = []
#     risk_score = 0
#     for pattern, alert_template in suspicious_patterns:
#         for match in re.findall(pattern, message, re.IGNORECASE):
#             alerts.append(alert_template.format(match=match))
#             risk_score += 20
#     risk_score = min(risk_score, 100)
#     if risk_score >= 60:
#         risk_level = "High Risk"
#     elif risk_score >= 20:
#         risk_level = "Medium Risk"
#     else:
#         risk_level = "Low Risk"
#     return {
#         "risk_score": risk_score,
#         "risk_level": risk_level,
#         "alerts": alerts
#     }

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json(force=True)
#     user_message = data.get("message", "")
#     friend_message = random.choice(friend_replies)
#     analysis = analyze_message(friend_message)
#     return jsonify({
#         "reply": friend_message,
#         "analysis": analysis
#     })

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, render_template, request, jsonify
import random
import re
from datetime import datetime

app = Flask(__name__)

# Friend replies (some are intentionally suspicious)
friend_replies = [
    "Hey! How’s your day?",
    "Haha that’s funny!",
    "I just watched a cool movie, have you seen it?",
    "Can you send me your password to verify your account?",
    "Click here to login: https://secure-login123.xyz",
    "LOL 😂 that's hilarious",
    "Your bank account needs verification.",
    "Update your credit card details here: http://fake-bank-login.com",
    "Let's play a game later!",
    "Please login to your account for a surprise."
]

# Suspicious patterns for analysis
suspicious_patterns = [
    (r"(password|bank|verify|login|credit card|secure)", "Suspicious keyword detected: '{match}'"),
    (r"https?://[^\s]+", "Suspicious link detected: {match}")
]

def analyze_message(message):
    alerts = []
    risk_score = 0
    for pattern, alert_template in suspicious_patterns:
        for match in re.findall(pattern, message, re.IGNORECASE):
            alerts.append(alert_template.format(match=match))
            risk_score += 20
    risk_score = min(risk_score, 100)
    if risk_score >= 60:
        risk_level = "High Risk"
    elif risk_score >= 20:
        risk_level = "Medium Risk"
    else:
        risk_level = "Low Risk"
    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "alerts": alerts
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_message = data.get("message", "")
    friend_message = random.choice(friend_replies)
    analysis = analyze_message(friend_message)
    return jsonify({
        "reply": friend_message,
        "analysis": analysis
    })

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json(force=True)
    message = data.get("message", "")
    analysis = analyze_message(message)
    return jsonify(analysis)

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.get_json(force=True)
    # For demo: just print feedback, in production save to DB or file
    print("Feedback received:", data)
    return jsonify({"status": "success"})

@app.route("/report", methods=["POST"])
def report():
    data = request.get_json(force=True)
    # For demo: just print report, in production save to DB or file
    print("Report received:", data)
    return jsonify({"status": "reported"})

@app.route("/quiz", methods=["GET"])
def quiz():
    # Demo quiz questions
    questions = [
        {
            "q": "Which of these is a sign of phishing?",
            "a": ["Urgency", "Funny meme", "Cat photo"],
            "correct": 0
        },
        {
            "q": "Should you click on unknown links?",
            "a": ["Yes", "No"],
            "correct": 1
        }
    ]
    return jsonify({"questions": questions})

@app.route("/stats")
def stats():
    # Demo stats
    return jsonify({
        "messages_analyzed": 1240,
        "threats_detected": 312,
        "users_protected": 87
    })

@app.route("/alerts")
def alerts():
    # Demo alerts
    alerts = [
        {"time": "12:01", "msg": "Suspicious link detected in chat."},
        {"time": "12:05", "msg": "High risk keyword: 'password'."}
    ]
    return jsonify({"alerts": alerts})

if __name__ == "__main__":
    app.run(debug=True)