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

            if cultivo.numero_caja == numero_caja:
                cultivo.mostrar_datos()
                return

        print("\nCultivo no encontrado.")

    def estadisticas(self):

        if len(self.lista_cultivos) == 0:
            print("\nSin registros.")
            return

        total = len(self.lista_cultivos)

        promedio = (
            sum(
                cultivo.colonias
                for cultivo in self.lista_cultivos
            )
            / total
        )

        print("\n===== ESTADISTICAS =====")
        print(f"Total de cultivos: {total}")
        print(
            f"Promedio de colonias: "
            f"{promedio:.2f}"
        )
        