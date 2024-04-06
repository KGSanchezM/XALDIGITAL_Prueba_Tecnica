![Texto alternativo](\logo.png)


## Prueba Técnica

### Instrucciones

La siguiente prueba técnica consta de una parte dedicada a la programación y otra enfocada hacia SQL.

#### Primer reto

- Usar cualquier lenguaje de programación. Python o Node.js son preferibles.
- Implementar pruebas unitarias (Opcional).

#### Segundo reto

- Realizar queries para responder una serie de preguntas.
  
**Algunas de las cosas que revisaremos del reto:**

- **Software en funcionamiento:** Se revisará si la aplicación funciona tal y como se especifica en el reto.
- **Limpieza del código:** Esperamos que el código sea limpio, comprensible y mantenible.

### Programación

Se deberá desarrollar un proceso de análisis de datos utilizando el siguiente enlace. El proceso debe realizar las siguientes actividades:

1. Conectarse al enlace.
2. Obtener el número de respuestas contestadas y no contestadas.
3. Obtener la respuesta con menor número de vistas.
4. Obtener la respuesta más vieja y más actual.
5. Obtener la respuesta del owner que tenga una mayor reputación.
6. Imprimir en consola del punto 2 al 5.

### SQL

Se tienen las siguientes tablas que contienen información referente hacia los vuelos que se realizan en México.

- Tabla de aerolíneas
- Tabla de aeropuertos
- Tabla de movimientos
- Tabla de vuelos

   | ID_AEROLINEA | NOMBRE_AEROLINEA |
   |--------------|-------------------|
   | 1            | Volaris           |
   | 2            | Aeromar           |
   | 3            | Interjet          |
   | 4            | Aeromexico        |


   | ID_AEROPUERTO | NOMBRE_AEROPUERTO |
   |---------------|-------------------|
   | 1             | Benito Juarez     |
   | 2             | Guanajuato        |
   | 3             | La paz            |
   | 4             | Oaxaca            |


   | ID_MOVIMIENTO | DESCRIPCION |
   |---------------|-------------|
   | 1             | Salida      |
   | 2             | Llegada     |




| ID_AEROLINEA | ID_AEROPUERTO | ID_MOVIMIENTO | DIA       |
|--------------|---------------|---------------|-----------|
| 1            | 1             | 1             | 2021-05-02|
| 2            | 1             | 1             | 2021-05-02|
| 3            | 2             | 2             | 2021-05-02|
| 4            | 3             | 2             | 2021-05-02|
| 1            | 3             | 2             | 2021-05-02|
| 2            | 1             | 1             | 2021-05-02|
| 2            | 3             | 1             | 2021-05-04|
| 3            | 4             | 1             | 2021-05-04|
| 3            | 4             | 1             | 2021-05-04|

Se requiere saber lo siguiente:

1. ¿Cuál es el nombre del aeropuerto que ha tenido mayor movimiento durante el año?
2. ¿Cuál es el nombre de la aerolínea que ha realizado mayor número de vuelos durante el año?
3. ¿En qué día se han tenido mayor número de vuelos?
4. ¿Cuáles son las aerolíneas que tienen más de 2 vuelos por día?
