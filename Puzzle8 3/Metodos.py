
from queue import Queue, LifoQueue, PriorityQueue  
from Puzzle import Puzzle 

def bfs(estado_inicial, estado_objetivo):
    visitados = set()
    frontera = Queue()
    puzzle_inicial = Puzzle(estado_inicial)
    frontera.put((puzzle_inicial, []))  # Cada elemento es (estado_actual, camino)

    while not frontera.empty():
        puzzle, camino = frontera.get()
        estado_actual = puzzle.estado

        if puzzle.es_igual(estado_objetivo):
            return camino + [estado_actual]

        visitados.add(tuple(map(tuple, estado_actual)))

        for nuevo_estado in puzzle.generar_movimientos():
            if tuple(map(tuple, nuevo_estado)) not in visitados:
                frontera.put((Puzzle(nuevo_estado), camino + [estado_actual]))

    return None

def dfs(estado_inicial, estado_objetivo):
    visitados = set()
    frontera = LifoQueue()
    puzzle_inicial = Puzzle(estado_inicial)
    frontera.put((puzzle_inicial, []))  

    while not frontera.empty():
        puzzle, camino = frontera.get()
        estado_actual = puzzle.estado

        if puzzle.es_igual(estado_objetivo):
            return camino + [estado_actual]

        estado_tuple = tuple(map(tuple, estado_actual))
        if estado_tuple in visitados:
            continue
        visitados.add(estado_tuple)

        for nuevo_estado in puzzle.generar_movimientos():
            nuevo_puzzle = Puzzle(nuevo_estado)
            frontera.put((nuevo_puzzle, camino + [estado_actual]))  # Actualizar el camino correctamente

    return None


def heuristica_manhattan(estado, objetivo):
    distancia = 0
    for i in range(3):
        for j in range(3):
            valor = estado[i][j]
            if valor != 0:
                for x in range(3):    # Encuentra la posición del valor en el estado objetivo
                    for y in range(3):
                        if objetivo[x][y] == valor:
                            distancia += abs(x - i) + abs(y - j)
                            break  
    return distancia

def astar(estado_inicial, estado_objetivo):
    """Implementa el algoritmo A*."""
    visitados = set()
    frontera = PriorityQueue()
    puzzle_inicial = Puzzle(estado_inicial)
    frontera.put((0, puzzle_inicial, []))

    while not frontera.empty():
        _, puzzle, camino = frontera.get()
        estado_actual = puzzle.estado

        if puzzle.es_igual(estado_objetivo):
            return camino + [estado_actual]

        visitados.add(tuple(map(tuple, estado_actual)))

        for nuevo_estado in puzzle.generar_movimientos():
            if tuple(map(tuple, nuevo_estado)) not in visitados:
                costo = len(camino) + 1 + heuristica_manhattan(nuevo_estado, estado_objetivo)
                frontera.put((costo, Puzzle(nuevo_estado), camino + [estado_actual]))

    return None

def greedy(estado_inicial, estado_objetivo):
    visitados = set()
    frontera = PriorityQueue()
    puzzle_inicial = Puzzle(estado_inicial)
    frontera.put((heuristica_manhattan(puzzle_inicial.estado, estado_objetivo), puzzle_inicial, []))

    while not frontera.empty():
        _, puzzle, camino = frontera.get()
        estado_actual = puzzle.estado

        if puzzle.es_igual(estado_objetivo):
            return camino + [estado_actual]

        visitados.add(tuple(map(tuple, estado_actual)))

        for nuevo_estado in puzzle.generar_movimientos():
            if tuple(map(tuple, nuevo_estado)) not in visitados:
                frontera.put((heuristica_manhattan(nuevo_estado, estado_objetivo), Puzzle(nuevo_estado), camino + [estado_actual]))

    return None