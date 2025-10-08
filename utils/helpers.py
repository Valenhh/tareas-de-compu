# Funciones Auxiliares

"""
Módulo de utilidades para las tareas de Física Computacional.
Contiene funciones comunes que pueden ser utilizadas en múltiples tareas.
"""

import numpy as np
import matplotlib.pyplot as plt

def setup_plot(title="", xlabel="", ylabel=""):
    """
    Configuración básica para gráficos.
    
    Args:
        title (str): Título del gráfico
        xlabel (str): Etiqueta del eje x
        ylabel (str): Etiqueta del eje y
    """
    plt.figure(figsize=(10, 6))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, alpha=0.3)

def save_results(filename, data, header=""):
    """
    Guarda resultados en archivo.
    
    Args:
        filename (str): Nombre del archivo
        data: Datos a guardar
        header (str): Cabecera opcional
    """
    np.savetxt(filename, data, header=header)
    print(f"Resultados guardados en: {filename}")

# Ejemplo de uso
if __name__ == "__main__":
    print("Módulo de utilidades cargado correctamente")