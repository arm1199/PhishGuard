from flask import Flask, render_template, request, jsonify, session
import re

app = Flask(__name__)
app.secret_key = "phishguard_secret" 


# Scripted dialogue between Stranger and Victim
dialogue_script = [
    {"msg": "Hey! How are you doing today?", "suspicious": False},
    {"msg": "That's great! I just got a new phone, it's awesome.", "suspicious": False},
    {"msg": "By the way, do you use online banking?", "suspicious": True},
    {"msg": "I had some trouble logging in. Can you help me check if this link works for you? https://secure-login123.xyz", "suspicious": True},
    {"msg": "Also, what's your email address? I want to send you something.", "suspicious": True},
    {"msg": "Can you send me a photo of your credit card? I need to verify something.", "suspicious": True},
    {"msg": "My account is locked, can you send me the code you just got by SMS?", "suspicious": True},
    {"msg": "Don't tell anyone about our chat, okay?", "suspicious": True},
    {"msg": "Can you send me a nude photo?", "suspicious": True},
    {"msg": "Please, just one, I love sexy girls.", "suspicious": True},
    {"msg": "Okay you won, I'm giving up.", "suspicious": False}
]

# Suggestions for each dialogue step
suggestions = [
    "You can reply politely and keep the conversation general.",
    "Acknowledge, but avoid sharing personal info.",
    "Be cautious! Don't reveal your banking habits to strangers.",
    "Never click on suspicious links. Tell them you can't check links.",
    "Do not share your email address with strangers.",
    "Never share photos of your credit card or any sensitive documents.",
    "Never share verification codes with anyone. They can be used to steal your accounts.",
    "If someone asks you to keep secrets, it could be a red flag. Stay alert.",
    "🚫 Never share intimate photos. If someone asks, block and report them immediately.",
    "Block and report anyone who pressures you for intimate content.",
    "Thank them, but stay alert for further suspicious requests."
]
# Suspicious patterns for analysis
suspicious_patterns = [
    (r"(password|bank|verify|login|credit card|secure)", "Suspicious keyword detected: '{match}'"),
    (r"https?://.*(login|verify|secure|update|reset|bank|paypal|user|account)[^ ]*", "Suspicious link detected: {match}")
]

def analyze_message(message):
    alerts = []
    risk_score = 0
    highlights = []  # List of (start, end) for risky matches
    for pattern, alert_template in suspicious_patterns:
        for match in re.finditer(pattern, message, re.IGNORECASE):
            alerts.append(alert_template.format(match=match.group()))
            risk_score += 20
            highlights.append({"start": match.start(), "end": match.end()})

    # Detect requests for intimate photos
    intimate_keywords = [
        "intimate photo", "nude", "send nudes", "naked photo", "lewd photo",
        "nudes", "naked pic", "nude pic", "sexy photo", "sexy pic"
    ]
    lower_msg = message.lower()
    if any(word in lower_msg for word in intimate_keywords):
        alerts.append("Request for intimate photos")
        risk_score = max(risk_score, 80)  # Make sure it's high risk

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
        "alerts": alerts,
        "highlights": highlights
    }

def get_next_dialogue():
    idx = session.get("dialogue_idx", 0)
    if idx < len(dialogue_script):
        reply = dialogue_script[idx]
        session["dialogue_idx"] = idx + 1
        suggestion = suggestions[idx]
        ended = False
        return reply, suggestion, ended
    else:
        return {"msg": "End of conversation.", "suspicious": False}, "Click 'Restart' to try again.", True

@app.route("/")
def index():
    session["dialogue_idx"] = 0  # Reset dialogue on page load
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_message = data.get("message", "")
    reply_data, suggestion, ended = get_next_dialogue()
    analysis = analyze_message(reply_data["msg"]) if reply_data["suspicious"] else {"risk_score": 0, "risk_level": "Low Risk", "alerts": [], "highlights": []}
    return jsonify({
        "reply": reply_data["msg"],
        "analysis": analysis,
        "suggestion": suggestion,
        "ended": ended
    })

@app.route("/reset", methods=["POST"])
def reset():
    session["dialogue_idx"] = 0
    return jsonify({"status": "reset"})

@app.route("/analyze_link", methods=["POST"])
def analyze_link():
    data = request.get_json(force=True)
    link = data.get("link", "")
    analysis = analyze_message(link)
    return jsonify(analysis)


if __name__ == "__main__":
    app.run(debug=False)