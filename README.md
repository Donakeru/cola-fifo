# Simulación de una Cola FIFO para Gestión de Procesos

**Daniel Alejandro Chavez Bustos**
*20212020109*

Este proyecto implementa una **cola FIFO** (First-In, First-Out) para gestionar procesos. Cada proceso tiene un **nombre** y una **prioridad**, y la cola gestiona los procesos en el orden en que fueron agregados.

## Descripción

La implementación de la cola FIFO sigue el principio de "Primero en entrar, primero en salir", lo que significa que el primer proceso que se agrega a la cola es el primero en ser procesado.

El programa permite realizar las siguientes operaciones básicas:

- **Agregar procesos a la cola**
- **Mostrar el proceso actual** (el que está al frente de la cola)
- **Eliminar el proceso completado** (el que se encuentra al frente de la cola)
- **Mostrar el estado completo de la cola**, es decir, todos los procesos en la cola ordenados por su orden de llegada.

## Estructura del Código

El código está compuesto por dos clases principales:

### 1. **Clase `Proceso`**
Representa un proceso que contiene:
- **nombre** (str): Nombre identificador del proceso.
- **prioridad** (int): Nivel de prioridad del proceso. Cuanto mayor es el número, mayor es la prioridad.

#### Métodos:
- **`__init__(self, nombre, prioridad)`**: Constructor para inicializar un proceso con un nombre y una prioridad.
- **`__str__(self)`**: Método para representar el proceso como una cadena de texto con su nombre y prioridad.

### 2. **Clase `ColaFIFO`**
Implementa la cola FIFO para gestionar los procesos.

#### Atributos:
- **`cola`** (list): Lista interna que actúa como la cola de procesos.

#### Métodos:
- **`agregar_proceso(self, proceso)`**: Agrega un proceso al final de la cola.
- **`mostrar_proceso_actual(self)`**: Muestra el proceso que está al frente de la cola.
- **`eliminar_proceso_terminado(self)`**: Elimina el proceso al frente de la cola.
- **`mostrar_estado_cola(self)`**: Muestra todos los procesos en la cola en el orden de llegada.
