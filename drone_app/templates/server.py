from flask import Flask, request, jsonify
from AlgoAStar import astar_search

app = Flask(__name__)

@app.route("/calculate-route", methods=["POST"])
def calculate_route():
    data = request.json
    start = tuple(data["start"])
    end = tuple(data["end"])

    # Exemple de graphe statique
    graph = {
        (34.7416, 10.7552): [((34.7420, 10.7580), 1.5)],
        (34.7420, 10.7580): [((34.7416, 10.7552), 1.5), ((34.7450, 10.7600), 2)],
        (34.7450, 10.7600): [((34.7420, 10.7580), 2)],
    }

    path = astar_search(graph, start, end)
    if path:
        return jsonify({"path": path})
    else:
        return jsonify({"error": "Aucun chemin trouvé"}), 404

if __name__ == "__main__":
    app.run(debug=True)
