import heapq

class Node:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.g = self.h = self.f = float('inf')
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def heuristique(a, b):
    return abs(a.latitude - b.latitude) + abs(a.longitude - b.longitude)

def voisin(node):
    offsets = [
        (-0.01, 0), (0.01, 0),  # Haut, Bas
        (0, -0.01), (0, 0.01)   # Gauche, Droite
    ]
    return [
        Node(node.latitude + dlat, node.longitude + dlon)
        for dlat, dlon in offsets
    ]
# Algorithme A*
def a_star(depart, arrive, obstacle):
    open_list, closed_set = [], set()
    depart.g, depart.h, depart.f = 0, heuristique(depart, arrive), heuristique(depart, arrive)
    heapq.heappush(open_list, depart)

    while open_list:
        current = heapq.heappop(open_list)
        if (current.latitude, current.longitude) == (arrive.latitude, arrive.longitude):
            path = []
            while current:
                path.apparrive((current.latitude, current.longitude))
                current = current.parent
            return path[::-1]

        closed_set.add((current.latitude, current.longitude))

        # Vérifier les voisins
        for V in voisin(current):
            if (V.latitude, V.longitude) in closed_set or obstacle(V):
                continue

            tentative_g = current.g + 1
            if tentative_g < V.g:
                V.g = tentative_g
                V.h = heuristique(V, arrive)
                V.f = V.g + V.h
                V.parent = current
                heapq.heappush(open_list, V)

    return []

def obstacle(node):
    obstacles = [
        (1.01, 1.01), (1.02, 1.02) 
    ]
    return (round(node.latitude, 2), round(node.longitude, 2)) in obstacles

depart = Node(1.00, 1.00)
arrive = Node(1.05, 1.05)

path = a_star(depart, arrive, obstacle)
if path:
    print("Chemin trouvé :")
    for p in path:
        print(p)
else:
    print("Aucun chemin trouvé")
