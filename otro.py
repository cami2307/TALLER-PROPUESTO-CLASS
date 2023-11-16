class BitacoraAmbiente:
    def _init_(self):
        self.equipos = []

    def agregar_informacion_pc(self, nombre, informacion):
        equipo = {'nombre': nombre, 'informacion': informacion, 'novedades': []}
        self.equipos.append(equipo)
        return f"Información del equipo {nombre} agregada correctamente."

    def editar_informacion_pc(self, nombre, nueva_informacion):
        for equipo in self.equipos:
            if equipo['nombre'] == nombre:
                equipo['informacion'] = nueva_informacion
                return f"Información del equipo {nombre} editada correctamente."
        return f"Equipo {nombre} no encontrado."

    def eliminar_informacion_pc(self, nombre):
        for equipo in self.equipos:
            if equipo['nombre'] == nombre:
                self.equipos.remove(equipo)
                return f"Información del equipo {nombre} eliminada correctamente."
        return f"Equipo {nombre} no encontrado."

    def agregar_novedad(self, nombre, novedad):
        for equipo in self.equipos:
            if equipo['nombre'] == nombre:
                equipo['novedades'].append(novedad)
                return f"Novedad agregada al equipo {nombre}."
        return f"Equipo {nombre} no encontrado."

    def mostrar_equipos_con_novedades(self):
        equipos_con_novedades = [equipo for equipo in self.equipos if equipo['novedades']]
        if equipos_con_novedades:
            return equipos_con_novedades
        else:
            return "No hay equipos con novedades registradas."

    def buscar_equipo(self, nombre):
        for equipo in self.equipos:
            if equipo['nombre'] == nombre:
                return equipo
        return f"Equipo {nombre} no encontrado."


# Ejemplo de uso:
bitacora = BitacoraAmbiente()

bitacora.agregar_informacion_pc("PC1", "Información de PC1")
bitacora.agregar_informacion_pc("PC2", "Información de PC2")

bitacora.agregar_novedad("PC1", "Novedad 1 en PC1")
bitacora.agregar_novedad("PC2", "Novedad 1 en PC2")

print(bitacora.mostrar_equipos_con_novedades())

print(bitacora.buscar_equipo("PC1"))

bitacora.editar_informacion_pc("PC1", "Nueva información de PC1")

print(bitacora.buscar_equipo("PC1"))

bitacora.eliminar_informacion_pc("PC2")

print(bitacora.mostrar_equipos_con_novedades())