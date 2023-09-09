from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Makati, Philippines',
        'salary': '₱ 330,000',
    },
    {
        'id': 2,
        'title': 'Frontend Engineer',
        'location': 'Manila, Philippines',
        'salary': '$ 43,500',
    },
    {
        'id': 3,
        'title': 'Backend Engineer',
        'location': 'Ontario, Canada',
        'salary': '$ 149,000',
    },
    {
        'id': 4,
        'title': 'Web Developer',
        'location': 'Sydney, Australia',
        'salary': '$ 95,000',
    }
]

@app.route("/")
def index():
    return render_template("index.html", 
                           jobs=JOBS)
    
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)