class Cultivo:

    def __init__(self, numero_caja,
                 tipo_medio,
                 dilucion,
                 volumen,
                 colonias):

        self.numero_caja = numero_caja
        self.tipo_medio = tipo_medio
        self.dilucion = dilucion
        self.volumen = volumen
        self.colonias = colonias

    def calcular_ufc(self):

        return self.colonias / (
            self.dilucion * self.volumen
        )

    def clasificar_crecimiento(self):

        if self.colonias == 0:
            return "Sin crecimiento"

        elif self.colonias <= 30:
            return "Bajo"

        elif self.colonias <= 300:
            return "Aceptable"

        else:
            return "Incontable"

    def mostrar_datos(self):

        print("\n===== CULTIVO =====")
        print(f"Caja: {self.numero_caja}")
        print(f"Medio: {self.tipo_medio}")
        print(f"Dilucion: {self.dilucion}")
        print(f"Volumen: {self.volumen}")
        print(f"Colonias: {self.colonias}")
        print(f"UFC/mL: {self.calcular_ufc():,.2f}")
        print(
            f"Clasificacion: "
            f"{self.clasificar_crecimiento()}"
        )
        