from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_reply(msg):
    msg = msg.lower()

    if "emergency" in msg:
        return "Call 1122 immediately or visit emergency ward."

    if "doctor" in msg:
        return "We have specialists in Cardiology, Neurology, and Surgery."

    if "appointment" in msg:
        return "You can book appointment at reception or online desk."

    if "visiting" in msg:
        return "Visiting hours are 4 PM to 8 PM daily."

    if "department" in msg:
        return "Departments: Emergency, Pediatrics, Orthopedics, Cardiology."

    if "pharmacy" in msg:
        return "Pharmacy is open 24/7 inside hospital."

    if "hello" in msg or "hi" in msg:
        return "Hello! I am Hospital Assistant Bot."

    return "Sorry, I didn't understand. Ask about hospital services."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.form["message"]
    reply = get_reply(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)