from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# =========================
# Flask App
# =========================
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:spatni@localhost:3306/hbnb_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# =========================
# Database Model
# =========================
class AnalysisResult(db.Model):
    __tablename__ = "analysis_results"

    id = db.Column(db.Integer, primary_key=True)
    algo = db.Column(db.String(50), nullable=False)
    items = db.Column(db.Integer, nullable=False)
    steps = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.Float, nullable=False)
    end_time = db.Column(db.Float, nullable=False)
    total_time_ms = db.Column(db.Float, nullable=False)
    time_complexity = db.Column(db.String(20), nullable=False)
    path_to_graph = db.Column(db.Text, nullable=False)

# =========================
# save_analysis ENDPOINT
# =========================
@app.route("/save_analysis", methods=["POST"])
def save_analysis():
    data = request.get_json()

    required_fields = [
        "algo",
        "items",
        "steps",
        "start_time",
        "end_time",
        "total_time_ms",
        "time_complexity",
        "path_to_graph"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    analysis = AnalysisResult(
        algo=data["algo"],
        items=data["items"],
        steps=data["steps"],
        start_time=data["start_time"],
        end_time=data["end_time"],
        total_time_ms=data["total_time_ms"],
        time_complexity=data["time_complexity"],
        path_to_graph=data["path_to_graph"]
    )

    db.session.add(analysis)
    db.session.commit()

    return jsonify({
        "status": "success",
        "id": analysis.id
    }), 201

# =========================
# App Runner
# =========================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8888, debug=True)
