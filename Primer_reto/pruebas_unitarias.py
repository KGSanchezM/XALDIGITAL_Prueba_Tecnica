import unittest
import pandas as pd
import XALDIGITAL_Reto_tecnico as RT

class Pruebas(unittest.TestCase):
    def test_obtener_respuestas(self):
        respuestas = RT.obtener_respuestas()
        self.assertIsInstance(respuestas, pd.DataFrame)
        self.assertGreater(len(respuestas), 0)

    def test_cantidad_respuestas_contestadas(self):
        respuestas = RT.obtener_respuestas()
        respuestas_contestadas, respuestas_no_contestadas = RT.cantidad_respuestas_constestadas(respuestas)
        self.assertIsInstance(respuestas_contestadas, int)
        self.assertIsInstance(respuestas_no_contestadas, int)
        self.assertGreaterEqual(respuestas_contestadas, 0)
        self.assertGreaterEqual(respuestas_no_contestadas, 0)

    def test_respuesta_menor_cantidad_vista(self):
        respuestas = RT.obtener_respuestas()
        respuesta_menor_vistas = RT.respuesta_menor_cantidad_vista(respuestas)
        self.assertIsInstance(respuesta_menor_vistas, pd.DataFrame)
        self.assertGreaterEqual(len(respuesta_menor_vistas), 0)

    def test_respuesta_mas_vieja_actual(self):
        respuestas = RT.obtener_respuestas()
        fecha_mas_vieja_legible, respuesta_mas_vieja, fecha_mas_actual_legible, respuesta_mas_actual = RT.respuesta_mas_vieja_actual(respuestas)
        self.assertIsInstance(fecha_mas_vieja_legible, str)
        self.assertIsInstance(fecha_mas_actual_legible, str)
        self.assertIsInstance(respuesta_mas_vieja, pd.DataFrame)
        self.assertIsInstance(respuesta_mas_actual, pd.DataFrame)
        self.assertGreaterEqual(len(respuesta_mas_vieja), 0)
        self.assertGreaterEqual(len(respuesta_mas_actual), 0)

    def test_respuesta_owner_mejor_reputacion(self):
        respuestas = RT.obtener_respuestas()
        respuesta_owner_mayor_reputacion = RT.respuesta_owner_mejor_reputacion(respuestas)
        self.assertIsInstance(respuesta_owner_mayor_reputacion, pd.DataFrame)
        self.assertGreaterEqual(len(respuesta_owner_mayor_reputacion), 0)

if __name__ == '__main__':
    unittest.main()
