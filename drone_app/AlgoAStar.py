import heapq

def heuristic(a, b):
    """
    Heuristique utilisée dans l'A* : distance de Manhattan ou Euclidienne.
    """
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def astar_search(graph, start, end):
    """
    Algorithme A* pour trouver le chemin le plus court dans un graphe.
    :param graph: Graphe sous forme de dictionnaire avec coordonnées comme clés
                  et liste de voisins [(voisin, coût)] comme valeurs.
    :param start: Point de départ (lat, lng).
    :param end: Point d'arrivée (lat, lng).
    :return: Chemin le plus court sous forme de liste de points [(lat, lng)].
    """
    # File de priorité pour explorer les chemins
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # Garde une trace des nœuds explorés et de leurs parents
    came_from = {}
    cost_so_far = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            # Reconstruire le chemin une fois la destination atteinte
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1]  # Retourner le chemin dans l'ordre inverse

        for neighbor, cost in graph.get(current, []):
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, end)
                heapq.heappush(open_set, (priority, neighbor))
                came_from[neighbor] = current

    return None  # Aucun chemin trouvé

# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple de graphe
    graph = {
        (0, 0): [((0, 1), 1), ((1, 0), 1)],
        (0, 1): [((0, 0), 1), ((1, 1), 1)],
        (1, 0): [((0, 0), 1), ((1, 1), 1)],
        (1, 1): [((0, 1), 1), ((1, 0), 1)],
    }
    start = (0, 0)
    end = (1, 1)
    path = astar_search(graph, start, end)
    print("Chemin trouvé :", path)
