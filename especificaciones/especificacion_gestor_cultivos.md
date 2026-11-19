Clase: GestorCultivos


Objetivo: 
Administrar todos los cultivos microbiológicos registrados.

Responsabilidad:
Controlar el almacenamiento, búsqueda y análisis de cultivos

A) Atributos
Nombre: lista_cultivos
Tipo: list


B) Constructor:
1. init()
Función:
Crear una lista vacía para almacenar los objetos Cultivo

C) Métodos
1. agregar_cultivo()
Objetivo: Añade un nuevo cultivo

2. Entradas: Objeto cultivo

4. Algoritmo: 
insertar el objeto en lista_cultivos

5. Resultado: cultivo guardado


D) mostrar_todos()
1. Objetivo: Muestra todos los cultivos registrados

2. Algoritmo: recorre la lista con un ciclo for

3. Resultado: informacion de cada cultivo

E) buscar_caja()
1. Objetivo: encontrar un cultivo por número de caja

2. Entrada: Numero de caja

3. Resultado: Mostrar datos del cultivo

4. Validación: si no existe, mostrar mensaje "error" 


F) estadísticas()
1. objetivo: obtener indicadores

2. cálculos: Colonias, caja con mayor creciemiento, num total de cultivos



F) Reglas
La lista solo debe almacenar objetos Cultivo
No eliminar registros automáticamente
Las estadísticas se calculan únicamente si existen cultivos registrados