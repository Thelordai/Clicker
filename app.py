from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Game state
score = 0

@app.route('/')
def index():
    return render_template('index.html', score=score)

@app.route('/click', methods=['POST'])
def click():
    global score
    score += 1
    return jsonify({'score': score})

@app.route('/get_score')
def get_score():
    return jsonify({'score': score})

if __name__ == '__main__':
    app.run(debug=True)
