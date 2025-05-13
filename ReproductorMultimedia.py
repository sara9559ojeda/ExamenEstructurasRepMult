class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    def top(self):
        return self.items[-1] if not self.is_empty() else None
    def print_stack(self):
        print("Historial de reproducción:")
        for item in reversed(self.items):
            print(f" - {item}")

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None
    def peek(self):
        return self.items[0] if not self.is_empty() else None
    def is_empty(self):
        return len(self.items) == 0
    def print_queue(self):
        print("Sugerencias de contenido:")
        for item in self.items:
            print(f" - {item}")

class Serie:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def __str__(self):
        return f"{self.nombre} | Género: {self.genero}, Popularidad: {self.popularidad}/5"

class NodoSerie:
    def __init__(self, serie):
        self.serie = serie
        self.prev = None
        self.next = None

class ListaSeries:
    def __init__(self):
        self.head = None

    def insertar_serie(self, nombre, genero, popularidad):
        nueva_serie = Serie(nombre, genero, popularidad)
        nuevo_nodo = NodoSerie(nueva_serie)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = nuevo_nodo
            nuevo_nodo.prev = current

    def listar_series(self):
        current = self.head
        print("Todas las series:")
        while current:
            print(f" - {current.serie}")
            current = current.next

    def filtrar_por_genero(self, genero):
        current = self.head
        print(f"Series de género '{genero}':")
        while current:
            if current.serie.genero.lower() == genero.lower():
                print(f" - {current.serie}")
            current = current.next

    def filtrar_por_popularidad(self, minimo):
        current = self.head
        print(f"Series con popularidad ≥ {minimo}:")
        while current:
            if current.serie.popularidad >= minimo:
                print(f" - {current.serie}")
            current = current.next

class Valoraciones:
    def __init__(self):
        self.valoraciones = []
    def agregar_valoracion(self, usuario, valor):
        self.valoraciones.append((usuario, valor))
    def mostrar_valoraciones(self):
        print("Valoraciones:")
        for usuario, valor in self.valoraciones:
            print(f"{usuario} calificó con {valor}/5")

class NodoEpisodio:
    def __init__(self, titulo):
        self.titulo = titulo
        self.prev = None
        self.next = None

class ListaEpisodios:
    def __init__(self):
        self.head = None
        self.actual = None

    def agregar_episodio(self, titulo):
        nuevo = NodoEpisodio(titulo)
        if self.head is None:
            self.head = nuevo
            nuevo.next = nuevo.prev = nuevo
        else:
            ultimo = self.head.prev
            ultimo.next = nuevo
            nuevo.prev = ultimo
            nuevo.next = self.head
            self.head.prev = nuevo

    def reproducir_actual(self):
        if self.actual:
            print(f"Reproduciendo episodio: {self.actual.titulo}")
        else:
            print("No hay episodios para reproducir.")

    def siguiente(self):
        if self.actual:
            self.actual = self.actual.next
            self.reproducir_actual()

    def anterior(self):
        if self.actual:
            self.actual = self.actual.prev
            self.reproducir_actual()

    def comenzar(self):
        self.actual = self.head
        self.reproducir_actual()

class ReproductorMultimedia:
    def __init__(self):
        self.historial = Stack()
        self.sugerencias = Queue()
        self.series = ListaSeries()
        self.valoraciones = Valoraciones()
        self.capitulos_por_temporada = []
        self.episodios = ListaEpisodios()

    def menu(self):
        while True:
            print("\n REPRODUCTOR MULTIMEDIA")
            print("1. Agregar sugerencia")
            print("2. Reproducir siguiente sugerencia")
            print("3. Agregar serie")
            print("4. Agregar valoración")
            print("5. Agregar capítulo por temporada")
            print("6. Mostrar capítulos")
            print("7. Agregar episodio")
            print("8. Comenzar reproducción de episodios")
            print("9. Episodio siguiente")
            print("10. Episodio anterior")
            print("11. Mostrar historial")
            print("12. Mostrar sugerencias")
            print("13. Mostrar series")
            print("14. Filtrar series por género")
            print("15. Filtrar series por popularidad")
            print("16. Mostrar valoraciones")
            print("0. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                titulo = input("Título de sugerencia: ")
                self.sugerencias.enqueue(titulo)
                print(" Sugerencia agregada.")
            elif opcion == "2":
                video = self.sugerencias.dequeue()
                if video:
                    print(f"Reproduciendo: {video}")
                    self.historial.push(video)
                else:
                    print("No hay sugerencias.")
            elif opcion == "3":
                nombre = input("Nombre de la serie: ")
                genero = input("Género: ")
                popularidad = int(input("Popularidad (1-5): "))
                self.series.insertar_serie(nombre, genero, popularidad)
                print("Serie agregada.")
            elif opcion == "4":
                usuario = input("Nombre del usuario: ")
                valor = input("Valoración (1-5): ")
                self.valoraciones.agregar_valoracion(usuario, valor)
                print("Valoración agregada.")
            elif opcion == "5":
                temp = int(input("Número de temporada (1, 2...): ")) - 1
                cap = input("Título del capítulo: ")
                while len(self.capitulos_por_temporada) <= temp:
                    self.capitulos_por_temporada.append([])
                self.capitulos_por_temporada[temp].append(cap)
                print("Capítulo agregado.")
            elif opcion == "6":
                for i, temporada in enumerate(self.capitulos_por_temporada):
                    print(f"Temporada {i + 1}:")
                    for cap in temporada:
                        print(f" - {cap}")
            elif opcion == "7":
                ep = input("Título del episodio: ")
                self.episodios.agregar_episodio(ep)
                print("Episodio agregado.")
            elif opcion == "8":
                self.episodios.comenzar()
            elif opcion == "9":
                self.episodios.siguiente()
            elif opcion == "10":
                self.episodios.anterior()
            elif opcion == "11":
                self.historial.print_stack()
            elif opcion == "12":
                self.sugerencias.print_queue()
            elif opcion == "13":
                self.series.listar_series()
            elif opcion == "14":
                genero = input("Género a filtrar: ")
                self.series.filtrar_por_genero(genero)
            elif opcion == "15":
                minimo = int(input("Popularidad mínima (1-5): "))
                self.series.filtrar_por_popularidad(minimo)
            elif opcion == "16":
                self.valoraciones.mostrar_valoraciones()
            elif opcion == "0":
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                break
            else:
                print(" Opción inválida")



if __name__ == "__main__":
    reproductor = ReproductorMultimedia()
    reproductor.menu()
