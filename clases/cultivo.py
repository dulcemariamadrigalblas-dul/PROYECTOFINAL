class Cultivo:
    '''
    Representa un cultivo microbiológico
    '''

    def __init__(self, tipo_medio, tipo, dilucion, volumen, colonias):
        self.tipo_medio = tipo_medio
        self.tipo = tipo
        self.dilucion = dilucion
        self.volumen = volumen
        self.colonias = colonias

    def calcular_ufc(self):
        '''
        Calcula las Unidades Formadoras de Colonias (UFC) del cultivo.
        '''
        if self.colonias == 0:
            return "Sin crecimiento"
        
        elif self.colonias <= 30:
            return "Crecimiento bajo"
        
        elif self.colonias <= 300:
            return "Crecimiento aceptable"
        
        elif self.colonias > 300:
            return "Incontable"
    
    def mostrar_ datos(self):
        '''
        Muestra toda la información
        '''
        print(f"Medio: {self.tipo_medio}")
        print(f"Numero de caja: {self.numero_caja}")
        print(f"Dilución: {self.dilucion}")
        print(f"Volumen: {self.volumen} mL")
        print(f"Colonias: {self.colonias}")
        print(f"UFC/mL: {self.calcular_ufc():,.2f}")
