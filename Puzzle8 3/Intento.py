import tkinter as tk
from tkinter import messagebox
from Puzzle import Puzzle
from Metodos import bfs, dfs, astar, greedy

class Aplicacion:
    def __init__(self, maestro):
        self.maestro = maestro
        maestro.title("Resolver 8-Puzzle")
        
        self.estado_inicial = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]  # Estado inicial
        self.estado_objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Estado final
        self.estado_actual = [fila[:] for fila in self.estado_inicial]  # Copia profunda del estado inicial
        #self.solucion = []  # Lista para almacenar la solución completa
        #self.indice_paso = 0  # Índice del paso actual en la solución

        self.crear_widgets()


    def crear_widgets(self):
        self.marco_tablero = tk.Frame(self.maestro)
        self.marco_tablero.grid(row=0, column=0, padx=10, pady=10)
        #self.boton_siguiente_paso = tk.Button(self.marco_botones, text="Siguiente Paso", command=self.siguiente_paso, width=12, font=("Arial", 12))
        #self.boton_siguiente_paso.pack(pady=5)


        self.botones = []
        for i in range(3):
            fila = []
            for j in range(3):
                boton = tk.Button(self.marco_tablero, text=str(self.estado_actual[i][j]), font=("Arial", 32),
                                width=6, height=3)
                boton.grid(row=i, column=j, padx=5, pady=5)
                fila.append(boton)
            self.botones.append(fila)

        # Crear un marco para los botones de control
        self.marco_botones = tk.Frame(self.maestro)
        self.marco_botones.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        self.label_metodo = tk.Label(self.marco_botones, text="Método: Ninguno", font=("Arial", 12))
        self.label_metodo.pack(pady=10)

        self.label_pasos = tk.Label(self.marco_botones, text="Pasos: 0", font=("Arial", 12))
        self.label_pasos.pack(pady=10)

        # Botones para cada algoritmo de búsqueda
        self.boton_bfs = tk.Button(self.marco_botones, text="BFS", command=self.resolver_bfs, width=10, font=("Arial", 12))
        self.boton_bfs.pack(pady=5)

        self.boton_dfs = tk.Button(self.marco_botones, text="DFS", command=self.resolver_dfs, width=10, font=("Arial", 12))
        self.boton_dfs.pack(pady=5)

        self.boton_astar = tk.Button(self.marco_botones, text="A*", command=self.resolver_astar, width=10, font=("Arial", 12))
        self.boton_astar.pack(pady=5)

        self.boton_greedy = tk.Button(self.marco_botones, text="Greedy", command=self.resolver_greedy, width=10, font=("Arial", 12))
        self.boton_greedy.pack(pady=5)

        self.boton_reset = tk.Button(self.marco_botones, text="Reiniciar", command=self.reiniciar_tablero, width=10, font=("Arial", 12))
        self.boton_reset.pack(pady=20)

    def actualizar_tablero(self):
        for i in range(3):
            for j in range(3):
                self.botones[i][j].config(text=str(self.estado_actual[i][j]) if self.estado_actual[i][j] != 0 else "")

    def animar_solucion(self, pasos):
        for i, paso in enumerate(pasos):
            self.estado_actual = paso
            self.actualizar_tablero()
            self.maestro.update()
            self.maestro.after(1000)  # Espera 1 segundo entre pasos
            self.label_pasos.config(text=f"Pasos: {len(pasos)}")
        messagebox.showinfo("Solución Completa", "El puzzle ha sido resuelto.")

    def resolver_bfs(self):
        self.label_metodo.config(text="Método: BFS")  # Actualiza el label
        solucion = bfs(self.estado_inicial, self.estado_objetivo)
        if solucion:
            self.animar_solucion(solucion)
        else:
            messagebox.showerror("Error", "No se encontró solución.")

    def resolver_dfs(self):
        self.label_metodo.config(text="Método: DFS")  # Actualiza el label
        solucion = dfs(self.estado_inicial, self.estado_objetivo)
        if solucion:
            self.animar_solucion(solucion)
        else:
            messagebox.showerror("Error", "No se encontró solución.")

    def resolver_astar(self):
        self.label_metodo.config(text="Método: A*")  # Actualiza el label
        solucion = astar(self.estado_inicial, self.estado_objetivo)
        if solucion:
            self.animar_solucion(solucion)
        else:
            messagebox.showerror("Error", "No se encontró solución.")

    def resolver_greedy(self):
        self.label_metodo.config(text="Método: Greedy")  # Actualiza el label
        solucion = greedy(self.estado_inicial, self.estado_objetivo)
        if solucion:
            self.animar_solucion(solucion)
        else:
            messagebox.showerror("Error", "No se encontró solución.")

    def reiniciar_tablero(self):
        self.estado_actual = [fila[:] for fila in self.estado_inicial]  # Copia profunda del estado inicial
        self.actualizar_tablero()
        self.label_metodo.config(text="Método: Ninguno")  # Restablece el label al estado inicial
        self.label_pasos.config(text="Pasos: 0")
  
# Código para ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
