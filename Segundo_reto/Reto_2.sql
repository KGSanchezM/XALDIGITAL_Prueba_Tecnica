CREATE TABLE Aerolineas (
    ID_AEROLINEA INT PRIMARY KEY,
    NOMBRE_AEROLINEA VARCHAR(100)
);

INSERT INTO Aerolineas (ID_AEROLINEA, NOMBRE_AEROLINEA) VALUES
(1, 'Volaris'),
(2, 'Aeromar'),
(3, 'Interjet'),
(4, 'Aeromexico');

CREATE TABLE Aeropuertos (
    ID_AEROPUERTO INT PRIMARY KEY,
    NOMBRE_AEROPUERTO VARCHAR(100)
);

INSERT INTO Aeropuertos (ID_AEROPUERTO, NOMBRE_AEROPUERTO) VALUES
(1, 'Benito Juarez'),
(2, 'Guanajuato'),
(3, 'La Paz'),
(4, 'Oaxaca');

CREATE TABLE Movimientos (
    ID_MOVIMIENTO INT PRIMARY KEY,
    DESCRIPCION VARCHAR(100)
);

INSERT INTO Movimientos (ID_MOVIMIENTO, DESCRIPCION) VALUES
(1, 'Salida'),
(2, 'Llegada');


CREATE TABLE Vuelos (
    ID_AEROLINEA INT,
    ID_AEROPUERTO INT,
    ID_MOVIMIENTO INT,
    DIA DATE
);

INSERT INTO Vuelos (ID_AEROLINEA, ID_AEROPUERTO, ID_MOVIMIENTO, DIA) VALUES
(1, 1, 1, '2021-05-02'),
(2, 1, 1, '2021-05-02'),
(3, 2, 2, '2021-05-02'),
(4, 3, 2, '2021-05-02'),
(1, 3, 2, '2021-05-02'),
(2, 1, 1, '2021-05-02'),
(2, 3, 1, '2021-05-04'),
(3, 4, 1, '2021-05-04'),
(3, 4, 1, '2021-05-04');

-- 1. ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?

SELECT A.NOMBRE_AEROPUERTO
FROM((
    SELECT ID_AEROPUERTO ,count(*) AS NUMERO_VUELOS FROM Vuelos
    GROUP BY ID_AEROPUERTO
    ORDER BY count(*) DESC
    LIMIT 1)AS V
JOIN Aeropuertos AS A
ON A.ID_AEROPUERTO = V.ID_AEROPUERTO);

-- Los aeropuertos con mayor movimiento son La Paz y Benito Juarez

-- 2. ¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año?

SELECT A.NOMBRE_AEROLINEA
FROM((
    SELECT ID_AEROLINEA , count(*)
    FROM Vuelos
    GROUP BY ID_AEROLINEA
    ORDER BY count(*) DESC
    LIMIT 1) AS V
JOIN Aerolineas AS A
ON V.ID_AEROLINEA = A.ID_AEROLINEA);

-- Las dos aerolineas con mayor número de vuelos son Interjet y Aeromar

-- 3. ¿En qué día se han tenido mayor número de vuelos?

SELECT DIA
FROM vuelos
GROUP BY DIA
ORDER BY count(*) DESC
LIMIT 1;

-- El día con más vuelos fue el 2021-05-02

-- 4. ¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día?


SELECT A.NOMBRE_AEROLINEA
FROM (
    SELECT ID_AEROLINEA, DIA, COUNT(*) AS NUMERO_VUELOS
    FROM Vuelos
    GROUP BY ID_AEROLINEA, DIA
    HAVING COUNT(*) > 2
    ) AS V
JOIN Aerolineas AS A ON A.ID_AEROLINEA = V.ID_AEROLINEA
GROUP BY A.NOMBRE_AEROLINEA
HAVING COUNT(*) = (SELECT COUNT(DISTINCT DIA) FROM Vuelos);


-- No existen aerolineas que tengan mas de dos vuelos por día

















