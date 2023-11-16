#Implemente el ejercicio del control de bitácoras de ambiente. Usando una clase que permita almacenar la información del computador y las novedades asociadas a él.
#Se debe definir las mismas operaciones o métodos definidos en el ejercicio anterior:
#Agregar información del pc
#Editar información del pc
#Eliminar información del pc
#Agregar novedad
#Mostrar equipos con las novedades registradas
#Buscar un equipo 

# Definición de la clase Computador para almacenar información del PC y novedades
class Computador:
    def _init_(self, id, marca, modelo):
        # Inicialización de atributos de la instancia
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.novedades = []

    # Método para agregar novedades al computador
    def agregarNovedad(self, novedad):
        self.novedades.append(novedad)

    # Método para mostrar las novedades asociadas al computador
    def mostrarNovedades(self):
        return self.novedades

    # Método para representar el objeto como una cadena
    def _str_(self):
        return f"ID: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}"

# Definición de la clase AmbienteComputacional para gestionar los computadores
class AmbienteComputacional:
    def _init_(self):
        # Inicialización de la lista de equipos en el ambiente
        self.equipos = []

    # Método para agregar un equipo al ambiente
    def agregarEquipo(self, equipo):
        self.equipos.append(equipo)

    # Método para editar la información de un equipo en el ambiente
    def editarEquipo(self, id, nuevaMarca, nuevoModelo):
        # Busca el equipo por su ID
        equipo = next((eq for eq in self.equipos if eq.id == id), None)
        if equipo:
            # Actualiza la marca y el modelo del equipo encontrado
            equipo.marca = nuevaMarca
            equipo.modelo = nuevoModelo

    # Método para eliminar un equipo del ambiente
    def eliminarEquipo(self, id):
        # Filtra la lista de equipos, excluyendo el equipo con el ID dado
        self.equipos = [eq for eq in self.equipos if eq.id != id]

    # Método para buscar un equipo por su ID
    def buscarEquipo(self, id):
        # Busca y devuelve el equipo con el ID dado
        return next((eq for eq in self.equipos if eq.id == id), None)