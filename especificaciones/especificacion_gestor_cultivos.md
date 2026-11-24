Clase: GestorCultivos


Objetivo: 
Administrar todos los cultivos registrados por el usuario

Responsabilidad:
Almacenar, buscar, mostrar y generar estadísticas de los cultivos.

A) Atributos
Nombre: lista_cultivos
Tipo: list


B) Constructor:
1. init()
Función:
Crear una lista llamada lista_cultivos

C) Métodos
1. agregar_cultivo()
Objetivo: Añade un nuevo cultivo

2. Entradas: Objeto cultivo

3. Atributos:
lista_cultivos

4. Algoritmo: 
insertar el cultivo usando append()

5. Resultado: cultivo guardado


D) mostrar_todos()
1. Objetivo: Muestra todos los cultivos registrados

2. Algoritmo: recorre la lista_cultivos con un ciclo for

3. Resultado: informacion de cada cultivo

E) buscar_cultivo()
1. Objetivo: encontrar un cultivo por número de caja

2. Entrada: Numero de caja

3. Algoritmo: recorrer la lista hasta encontrar coincidencia

4. Resultado: Mostrar datos del cultivo

5. Validación: si no existe, mostrar mensaje "error" 


F) estadísticas()
1. objetivo: Generar estadísticas generales

2. cálculos: total de cultivos, promedio de colonias, mayor y menor crecimiento

3. resultados:
mostrar estadísticas



F) Reglas
Solo se almacenarán objetos Cultivo.
No eliminar registros automáticamente.
Las estadísticas se calcularán únicamente si existen registros.
La lista debe permanecer disponible durante toda la ejecución.