Especificación del Programa Principal


1. Objetivo: Permitir al usuario interactuar con menú de opciones.

2. Objeto: GestorCultivos

3. Menú
Registrar cultivo
Mostrar cultivos
Buscar cultivo por número de caja
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
Salir

5. Métodos que se llamarán
-Opción 1
agregar_cultivo()

-Opción 2
mostrar_todos()

-Opción 3
buscar_caja()

-Opción 4
Finalizar


6. Validaciones
El usuario debe ingresar una opción válida
Los valores numéricos deben ser mayores que cero cuando corresponda
No se permite el ingreso de texto en campos numéricos

7. Condición de salida
El programa termina cuando el usuario selecciona la opción 4.