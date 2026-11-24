class GestorCultivos:
    def __init__(self):
        self.lista_cultivos = []

    def agregar_cultivo(self, cultivo):
        self.lista_cultivos.append(cultivo)

    def mostrar_todos(self):
        if len(self.lista_cultivos) == 0: 
            print("\nNo hay cultivos registrados.")
            return
        for cultivo in self.lista_cultivos:
            cultivo.mostrar_datos()
    def buscar_cultivo(self, numero_caja):
        for cultivo in self.lista_cultivos:
            if (cultivo.numero_caja == numero_caja):
                cultivo.mostrar_datos()
                return cultivo

    def estadisticas(self):
        if len(self.lista_cultivos) == 0:
            print("\nSin registros.")
            return

        total = len(self.lista_cultivos)
        promedio_colonias = (sum(cultivo.colonias for cultivo in self.lista_cultivos) /  total)

       mayor = max(self.lista_cultivos, key=lambda cultivo: cultivo.colonias)

       menor = min(self.lista_cultivos, key=lambda cultivo: cultivo.colonias)

        print(f"\nTotal de cultivos registrados: {total}")
        print(f"Promedio de colonias: {promedio_colonias:.2f}")
        print(f"Cultivo con mayor número de colonias: {mayor.numero_caja} ({mayor.colonias} colonias)")
        print(f"Cultivo con menor número de colonias: {menor.numero_caja} ({menor.colonias} colonias)")