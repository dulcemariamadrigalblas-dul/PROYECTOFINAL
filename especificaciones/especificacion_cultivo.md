Clase: Cultivo


Objetivo: 
Representar una caja de Petri de un análisis microbiológico.

Responsabilidad:
Almacenar los datos de un cultivo y realizar los cálculos para determinar las UFC/mL y la clasificación del crecimiento.

A) Atributos
Nombre: numero_caja
Tipo: int 
Significado: Identificador de la caja
Valor inicial: Recibido por parámetro

Nombre: Colonias
Tipo: int 
Significado: Número de colonias observadas	
Valor inicial: Recibido por parámetro

Nombre: dilución
Tipo: float
Significado: Dilución que se utilizó
Valor inicial: Recibido por parámetro

Nombre: Volumen
Tipo: float
Significado: Volumen sembrado en mL
Valor inicial: Recibido por parámetro

Nombre: tipo_cultivo
Tipo: str
Significado: tipo de microorganismo
Valor inicial: Recibido por parámetro




B) Constructor:
1. init()
Datos que recibe:
numero_caja
colonias
dilucion
volumen
tipo_cultivo
2. Función
Inicializar todos los atributos de la clase.

C) Métodos
1. calcular_ufc()
Objetivo: Calcular las UFC/mL.

2. Entradas: No recibe parámetros adicionales.

3. Atributos utilizados:
colonias
dilucion
volumen

4. Algoritmo: 
UFC/mL = Colonias / (Dilución × Volumen)

5. Resultado: retorna el valor calculado

6. Validaciones
La dilución debe ser mayor a 0
El volumen debe ser mayor a 0


D) clasificar_crecimiento()
1. Objetivo: determinar el nivel de crecimiento

2. Clasificación
Colonias	Clasificación
   0	   Sin crecimiento
  1-30	       Bajo
 31-300	     Aceptable
 + 300	    Incontable

3. Resultado: texto

E) mostrar_datos()
1. Objetivo: mostrar la información del cultivo

2. Resultado
Imprime:
Número de caja
Colonias
Tipo de cultivo
UFC/mL
Clasificaión


F) Reglas
No permitir diluciones menores o iguales a cero
No permitir volumen menor o igual a cero
No permitir cantidades negativas de colonias
El cálculo de UFC debe seguir exactamente la fórmula