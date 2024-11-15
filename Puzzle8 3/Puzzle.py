import copy

class Puzzle:
    def __init__(self, estado):
        self.estado = estado

    def encontrar_espacio_vacio(self):
        for i in range(3):
            for j in range(3):
                if self.estado[i][j] == 0:
                    return i, j
        return None
    
    #def siguiente_paso(self):
    #if self.solucion and self.indice_paso < len(self.solucion):
        # Avanza al siguiente paso
     #   self.estado_actual = self.solucion[self.indice_paso]
      #  self.actualizar_tablero()
       # self.indice_paso += 1
        #self.label_pasos.config(text=f"Paso: {self.indice_paso} de {len(self.solucion)}")
    #else:
     #   messagebox.showinfo("Fin de la Solución", "No hay más pasos disponibles.")


    def generar_movimientos(self):
        movimientos = []
        x, y = self.encontrar_espacio_vacio()
        direcciones = [("arriba", -1, 0), ("abajo", 1, 0), ("izquierda", 0, -1), ("derecha", 0, 1)]

        for direccion, dx, dy in direcciones:
            nuevo_x, nuevo_y = x + dx, y + dy
            if 0 <= nuevo_x < 3 and 0 <= nuevo_y < 3:
                nuevo_estado = [fila[:] for fila in self.estado]
                nuevo_estado[x][y], nuevo_estado[nuevo_x][nuevo_y] = nuevo_estado[nuevo_x][nuevo_y], nuevo_estado[x][y]
                movimientos.append(nuevo_estado)
        return movimientos

    def es_igual(self, otro_estado):
        return self.estado == otro_estado
    
    def __hash__(self):
        return hash(tuple(map(tuple, self.estado)))
    
    def __repr__(self):
        return repr(self.estado)

    def calcular_distancia_manhattan(self, objetivo):
        distancia = 0
        for i in range(3):
            for j in range(3):
                valor = self.estado[i][j]
                if valor != 0:
                    objetivo_x, objetivo_y = divmod(valor - 1, 3)
                    distancia += abs(objetivo_x - i) + abs(objetivo_y - j)
        return distancia

    def __lt__(self, otro):
        return self.calcular_distancia_manhattan([[1, 2, 3], [4, 5, 6], [7, 8, 0]]) < otro.calcular_distancia_manhattan([[1, 2, 3], [4, 5, 6], [7, 8, 0]])