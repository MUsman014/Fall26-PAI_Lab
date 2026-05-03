from flask import Flask, render_template, request
import random

app = Flask(__name__)


# =========================
# 🧠 Court AI Engine
# =========================
class CourtAI:
    def __init__(self):
        self.prosecution_points = [
            "Evidence strongly suggests involvement of the accused in the case.",
            "Witness statements and factual records support prosecution claims.",
            "The accused actions appear to violate established legal principles."
        ]

        self.defense_points = [
            "There is reasonable doubt regarding the accused's involvement.",
            "The evidence is insufficient to establish guilt beyond doubt.",
            "Intent of the accused cannot be clearly proven from available facts."
        ]

        self.verdicts = [
            "GUILTY — Evidence supports conviction.",
            "NOT GUILTY — Reasonable doubt exists.",
            "CASE DISMISSED — Insufficient evidence."
        ]

    def analyze_case(self):
        prosecution = random.choice(self.prosecution_points)
        defense = random.choice(self.defense_points)
        return prosecution, defense

    def decide_verdict(self):
        return random.choice(self.verdicts)


# Create AI instance
court_ai = CourtAI()


# =========================
# 🌐 ROUTES
# =========================
@app.route('/')
def home():
    """Render homepage"""
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_case():
    """Process case and generate AI analysis"""

    case_text = request.form.get('case', '').strip()

    # Input validation
    if not case_text:
        return render_template(
            'result.html',
            case="No case provided",
            prosecution="Invalid input received.",
            defense="No analysis available.",
            verdict="CASE REJECTED"
        )

    # AI processing
    prosecution, defense = court_ai.analyze_case()
    verdict = court_ai.decide_verdict()

    return render_template(
        'result.html',
        case=case_text,
        prosecution=prosecution,
        defense=defense,
        verdict=verdict
    )


# =========================
# 🚀 RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)