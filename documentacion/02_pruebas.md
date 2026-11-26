# ---------------Pruebas y validación--------------------------

## Caso 1 - Ejemplo original
 Identificador
    CP-01

### Objetivo

    Validar el ejemplo utilizado durante el análisis del problema.

### Entradas

    Numero de caja: 1

    Colonias: 150

    Dilución: 0.001

    Volumen: 0.1

    Medio: MRS

### Resultado esperado

UFC/mL = 1,500,000

Clasificación = Aceptable

### Resultado obtenido

UFC/mL = 1,500,000

Clasificación = Aceptable

### Estado

Correcto

### Observaciones

Coincide con el ejemplo original.

---

## Caso 2 - Caso normal

    ### Identificador

    CP-02

### Objetivo

    Validar captura normal de datos.

### Entradas

    Numero de caja: 2

    Colonias: 75

    Dilución: 0.01

    Volumen: 1

    Medio: PDA

### Resultado esperado

UFC/mL = 7500

Clasificación = Aceptable

### Resultado obtenido

UFC/mL = 7500

Clasificación = Aceptable

### Estado

Correcto

---

## Caso 3 - Caso límite

    ### Identificador

        CP-03

### Objetivo

    Evaluar el límite inferior permitido.

### Entradas

    Numero de caja: 3

    Colonias: 0

    Dilución: 0.001

    Volumen: 0.1

    Medio: MRS

### Resultado esperado

Clasificación = Sin crecimiento

### Resultado obtenido

Clasificación = Sin crecimiento

### Estado

Correcto

---

## Caso 4 - Entrada inválida

### Identificador

CP-04

### Objetivo

Validar protección de entradas.

### Entradas

Colonias = texto

### Resultado esperado

Mostrar mensaje de error.

### Resultado obtenido

Mostrar mensaje de error.

### Estado

Correcto

---

## Caso 5 - Crecimiento incontable

### Identificador

CP-05

### Objetivo

Comprobar clasificación superior.

### Entradas

Numero de caja: 5

Colonias: 450

Dilución: 0.001

Volumen: 0.1

Medio: PDA

### Resultado esperado

Clasificación = Incontable

### Resultado obtenido

Clasificación = Incontable

### Estado

Correcto

### Observaciones

Clasificación correcta para más de 300 colonias.