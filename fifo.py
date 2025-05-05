"""
DANIEL ALEJANDRO CHAVEZ BUSTOS
20212020109

Implementación de una cola FIFO (First-In, First-Out) para gestión de procesos
Cada proceso tiene un nombre y una prioridad, y se manejan con operaciones básicas:
- Agregar procesos
- Mostrar proceso actual
- Eliminar proceso completado
- Mostrar estado completo de la cola
"""

class Proceso:
    """
    Clase que representa un proceso con nombre y prioridad
    """
    
    def __init__(self, nombre, prioridad):
        """
        Constructor de la clase Proceso
        
        Args:
            nombre (str): Nombre identificador del proceso
            prioridad (int): Nivel de prioridad (mayor número = mayor prioridad)
        """
        self.nombre = nombre    # Atributo para almacenar el nombre del proceso
        self.prioridad = prioridad  # Atributo para almacenar la prioridad
    
    def __str__(self):
        """
        Método especial para representación en string del objeto
        
        Returns:
            str: Descripción formateada del proceso
        """
        return f"Proceso: {self.nombre}, Prioridad: {self.prioridad}"


class ColaFIFO:
    """
    Clase que implementa una cola FIFO para manejar procesos
    Utiliza una lista interna para almacenar los procesos en orden de llegada
    """
    def __init__(self):
        """
        Constructor de la clase ColaFIFO
        Inicializa una lista vacía para almacenar los procesos
        """
        self.cola = []  # Lista que funcionará como cola FIFO
    
    def agregar_proceso(self, proceso):
        """
        Agrega un nuevo proceso al final de la cola
        
        Args:
            proceso (Proceso): Objeto Proceso a agregar a la cola
        """
        self.cola.append(proceso)  # Añade el proceso al final de la lista
        print(f"Proceso {proceso.nombre} agregado a la cola.")
    
    def mostrar_proceso_actual(self):
        """
        Muestra el proceso que está al frente de la cola (próximo a ejecutarse)
        Si la cola está vacía, muestra un mensaje indicándolo
        """
        if not self.cola:
            print("La cola está vacía.")
        else:
            # Muestra el primer elemento de la lista (índice 0)
            print("Proceso actual:", self.cola[0])
    
    def eliminar_proceso_terminado(self):
        """
        Elimina el proceso al frente de la cola (que ya terminó su ejecución)
        Sigue el principio FIFO: First-In, First-Out
        Si la cola está vacía, muestra un mensaje de error
        """

        if not self.cola:
            print("La cola está vacía, no hay procesos para eliminar.")
        else:
            # Remueve y retorna el primer elemento de la lista (operación FIFO)
            proceso_eliminado = self.cola.pop(0)
            print(f"Proceso {proceso_eliminado.nombre} eliminado de la cola.")
    
    def mostrar_estado_cola(self):
        """
        Muestra el estado completo de la cola, listando todos los procesos
        en orden de ejecución (primero el más antiguo, luego los más recientes)
        Si la cola está vacía, muestra un mensaje indicándolo
        """
        if not self.cola:
            print("La cola está vacía.")
        else:
            print("Estado actual de la cola:")
            # Enumera cada proceso con su posición en la cola
            for i, proceso in enumerate(self.cola, 1):  # Comienza la enumeración en 1
                print(f"{i}. {proceso}")

    def procesar_toda_la_cola(self):
        """
        Método nuevo que procesa toda la cola hasta vaciarla
        mostrando el estado en cada paso
        """
        print("\nIniciando procesamiento de toda la cola...")
        while self.cola:
            self.mostrar_proceso_actual()
            self.mostrar_estado_cola()
            print("Procesando...")
            self.eliminar_proceso_terminado()
        
        print("\nProcesamiento completado!")
        self.mostrar_estado_cola()

if __name__ == "__main__":
    # Crear la cola
    cola = ColaFIFO()
    
    print("=== Agregando procesos a la cola ===")
    cola.agregar_proceso(Proceso("P1", 3))
    cola.agregar_proceso(Proceso("P2", 1))
    cola.agregar_proceso(Proceso("P3", 4))
    cola.agregar_proceso(Proceso("P4", 2))
    cola.agregar_proceso(Proceso("P5", 5))
    
    # Mostrar estado inicial
    print("\n=== Estado Inicial de la Cola ===")
    cola.mostrar_estado_cola()
    
    # Procesar toda la cola automáticamente
    cola.procesar_toda_la_cola()
    
    # Verificar que la cola quedó vacía
    print("\n=== Verificación Final ===")
    cola.mostrar_proceso_actual()