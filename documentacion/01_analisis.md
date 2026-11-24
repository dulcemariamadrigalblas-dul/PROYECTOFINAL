1. Nombre del problema:
Sistema de Análisis de Crecimiento Microbiológico en Cajas de Petri
Asignatura:
Microbiología

2. Descripción, justificación y planteamiento original
Durante las prácticas de microbiología se realizan cultivos de microorganismos en medios de cultivo sólidos contenidos en cajas de Petri.
Después del periodo de incubación es necesario observar las colonias desarrolladas y contabilizarlas para posteriormente analizar el crecimiento microbiano.
El proceso suele realizarse manualmente, lo que puede consumir tiempo y provocar errores de conteo.

El sistema permitirá registrar información de cultivos microbiológicos, calcular concentraciones microbianas expresadas en UFC/mL, clasificar el crecimiento observado y generar estadísticas generales para facilitar el análisis de laboratorio.

El problema fue estudiado previamente durante prácticas de microbiología relacionadas con el crecimiento de microorganismos en medios de cultivo.

3. ENTRADAS
A)nombre: no. caja
  tipo: int
  Restricciones: >0
  Significado:identificador de la caja
B)nombre:no. colonias
  tipo: int
  Restricciones: >=0
  Significado: colonias observadas
C)nombre: Dilución
  tipo: float
  Restricciones: >0
  Significado: dilución que se usó (-2,-3,-4, etc.)
D)nombre:Volumen sembrado
  tipo: float
  Restricciones: >0
  Significado: Volumen sembrado en mL
E)nombre: Tipo de medio (AGAR)
  tipo: str
  Restricciones: No vacío
  Significado: Medio de cultivo utilizado

4. PROCESOS
a) Registro del cultivo
   el sistema almacenará los datos de cada cultivo
b) Cálculo de UFC/mL
   Se utiliza la fórmula:
   UFC/mL = Colonias / (dilución x Vaolumen)
c) ejemplo:
    Colonias = 150
    Dilución = 0.001
    Volumen = 0.1 mL
    UFC/mL = 150 / (0.001 × 0.1)
    UFC/mL = 1,500,000 UFC/mL
d) Clasificación del crecimiento
Rango:  0, sin crecimiento
        1-30 Bajo
        31-300 Aceptable
        +200 Incontable
e) Estadísticas
calcular:
    promedio de colonias
    mayor creciemiento
    menor crecimiento
    total de cultivos registrados

5. SALIDAS ESPERADAS
a) deberá mostrar:
    Numero de caja
    Número de colonias.
    Tipo de medio.
    UFC/mL calculadas.
    Clasificación del crecimiento.
    Promedio general.
    Caja con mayor crecimiento.
    Caja con menor crecimiento.
    Total de cultivos registrados.

6. EJEMPLO ORIGINAL RESUELTO
    a)Datos
        Número de colonias: 150
        Dilución: 0.001
        Volumen sembrado: 0.1 mL
    b) Procedimiento
        UFC/mL = Colonias / (Dilución × Volumen)
        UFC/mL = 150 / (0.001 × 0.1)
        UFC/mL = 1,500,000
    c) Resultado
        UFC/mL = 1,500,000
    d)Clasificación = Aceptable

7. ALCANCE
La aplicación tendrá las siguientes funcionalidades:
    Registrar cultivos microbiológicos.
    Almacenar múltiples cultivos.
    Calcular UFC/mL automáticamente.
    Clasificar crecimiento.
    Buscar cultivos por número de caja.
    Mostrar todos los cultivos registrados.
    Calcular estadísticas generales.
    Validar datos ingresados por el usuario.
    Funcionar mediante un menú interactivo de consola

8. COMPROBACION DE REQUISITOS TÉCNICOS
A) Requisito:                           B) Cumple
    Problema visto en otra asignatura       SI
    Entradas identificables	                Sí
    Procesos identificables	                Sí
    Salidas identificables	                Sí
    Reglas y validaciones	                Sí
    Aplicación en consola	                Sí
    Mínimo dos clases	                    Sí
    Variables y tipos de datos	            Sí
    Condicionales	                        Sí
    Ciclos	                                Sí
    Listas	                                Sí
    Funciones	                            Sí
    Objetos	                                Sí
    Ejemplo resuelto para validar           SI

CONCLUSIÓN
    El problema cumple con todos los requisitos establecidos para el Proyecto Integrador de Programación II debido a que proviene de otra asignatura, contiene entradas, procesos, salidas, reglas de decisión y permite implementar una aplicación orientada a objetos con múltiples clases y funcionalidades.