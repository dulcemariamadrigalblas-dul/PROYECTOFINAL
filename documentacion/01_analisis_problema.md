Nombre del problema: Sistema de Conteo y Análisis de Colonias Microbiológicas en Cajas de Petri

asignatura: Microbiología


Descripción:
Durante los análisis microbiológicos es necesario contar las colonias bacterianas que crecen en cajas de Petri para estimar la concentración de microorganismos en una muestra. 


justificación 
Cuando existen muchas cajas y varias diluciones, el conteo manual y los cálculos son lentos y propensos a errores.

planteamiento original:
El sistema permitirá registrar los datos de las cajas de Petri, calcular las UFC/mL (Unidades Formadoras de Colonias por mililitro), clasificar el crecimiento microbiano y guardar los resultados.


Entradas: 
1. nombre: Número de caja
tipo de dato: INT
restriccion: Mayor que 0
2. nombre: Número de colonias
tipo de dato: INT
restriccion: Mayor o igual a 0
3. nombre: Dilución
tipo de dato: float
restriccion: >0
4. nombre: Volumen sembrado
tipo de dato: float
restriccion: >0 
5. nombre: Tipo de cultivo
tipo de dato: STR
restriccion: Bacterias, hongos, levaduras



4.  Procesos: 
operaciones UFC/mL
fórmulas: UFC/mL= Colonias / (Dilución × Volumen)
reglas y decisiones: 
A) CLASIFICACIÓN Y COLONIAS: 
 0 sin crecimiento , 1-30 bajo, 31-300 aceptable, >300 incontable. 



5.  Salidas esperadas. 
Colonias registradas.
Dilución utilizada.
UFC/mL calculadas.
Clasificación del crecimiento.
Historial.



6.  Ejemplo original resuelto: 
datos: Imgagen, Dilución, volumen
procedimiento: relizar el conteo con las fórmulas correpondientes y arrojar el resultado
resultado: Colonias 150, Dilución 10-3, volumen 0.1, UFC/mL 1,500,000




7.  Alcance: 
funcionalidades que tendrá la aplicación
Registrar cajas.
Calcular UFC.
Clasificar crecimiento.
Mostrar historial.
 




8.  Comprobación de que el problema cumple todos los requisitos técnicos. 