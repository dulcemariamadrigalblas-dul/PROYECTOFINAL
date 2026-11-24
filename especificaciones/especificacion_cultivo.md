Clase: Cultivo


Objetivo: 
Representar un cultivo microbiológico registrado en una caja de Petri.

Responsabilidad:
Almacenar los datos de un cultivo y realizar los cálculos relacionados con las UFC/mL y la clasificación del crecimiento microbiológico.

A) Atributos
Nombre: numero_caja
Tipo: int 
Significado: Identificador de la caja
Valor inicial: Recibido en constructor

Nombre: Colonias
Tipo: int 
Significado: Número de colonias observadas	
Valor inicial: Recibido en constructor

Nombre: dilución
Tipo: float
Significado: Dilución que se utilizó
Valor inicial: Recibido en constructor

Nombre: Volumen
Tipo: float
Significado: Volumen sembrado en mL
Valor inicial: Recibido en constructor

Nombre: tipo_medio
Tipo: str
Significado: Medio de cultivo utilizado
Valor inicial: Recibido en constructor




B) Constructor:
1. init()
Datos que recibe:
numero_caja
colonias
dilucion
volumen
tipo_medio
2. Inicializacion
Cada parámetro recibido se almacena en su atributo correspondiente usando self.
3. Ejemplo
cultivo = Cultivo(
    1,
    150,
    0.001,
    0.1,
    "MRS"
)

C) Métodos
1. calcular_ufc()
Objetivo: Calcular las UFC/mL.

2. Entradas: No recibe parámetros

3. Atributos utilizados:
self.colonias
self.dilucion
self.volumen

4. Algoritmo: 
UFC/mL = Colonias / (Dilución × Volumen)

5. Resultado: retorna un valor float

6. Validaciones
Dilución >0
volumen >0


D) clasificar_crecimiento()
1. Objetivo: determinar el nivel de crecimiento

2. Clasificación
   Colonias	           Clasificación
   0	                  Sin crecimiento
   1-30	               Bajo
   31-300	            Aceptable
   + 300	               Incontable

3. Resultado: texto

E) mostrar_datos()
1. Objetivo: mostrar la información del cultivo
2. Entradas: ninguna
3. Algoritmo: Mostrar cada atributo junto con las UFC calculadas y la clasificación.
2. Resultado: información desplegada.



F) Reglas
No permitir colonias negativas
No permitir diluciones menores o iguales a cero
No permitir volumen menor o igual a cero
La fórmula de UFC/mL no debe modificarse.
La clasificación debe respetar los rangos establecidos.