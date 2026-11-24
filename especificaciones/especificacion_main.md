Especificación del Programa Principal


1. Objetivo: Permitir al usuario interactuar con menú de opciones.

2. Objeto: GestorCultivos
gestor = GestorCultivos()

3. Menú
Registrar cultivo
Mostrar cultivos
Buscar cultivo 
ver estadísticas
Salir


4. Secuencia de Operaciones
Inicio
↓
objeto GestorCultivos
↓
Mostrar menú
↓
Leer opción
↓
Ejecutar método 
↓
Regresar al menú
↓
Salir con opción 5

5. Métodos que se llamarán
-Opción 1
agregar_cultivo()

-Opción 2
mostrar_todos()

-Opción 3
buscar_cultivo()

-Opción 4
estadísticas()

-Opción 4
salir()




6. Validaciones
No aceptar valores negativos para colonias.
No aceptar texto en campos numéricos.
No aceptar diluciones iguales a cero.
No aceptar volúmenes iguales a cero.
Validar que la opción del menú exista.

7. Condición de salida
La aplicación terminará únicamente cuando el usuario seleccione la opción 5.