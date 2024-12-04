from flask import Flask, request, jsonify
from AlgoA import a_star

app = Flask(__name__)

# Exemple de graphe (à remplacer par votre propre structure de données)
graph = {
    (34.7406, 10.7603): [((34.75, 10.78), 2), ((34.76, 10.75), 3)],
    (34.75, 10.78): [((34.76, 10.75), 1)],
    (34.76, 10.75): [],
}

@app.route('/calculate-route', methods=['POST'])
def calculate_route():
    data = request.json
    start = tuple(data.get('start'))
    end = tuple(data.get('end'))
    path = a_star(start, end, graph)
    return jsonify({"path": path})

if __name__ == "__main__":
    app.run(debug=True)
