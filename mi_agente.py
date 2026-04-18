"""
mi_agente.py — Aquí defines tu agente.
╔══════════════════════════════════════════════╗
║  ✏️  EDITA ESTE ARCHIVO                      ║
╚══════════════════════════════════════════════╝

Tu agente debe:
    1. Heredar de la clase Agente
    2. Implementar el método decidir(percepcion)
    3. Retornar: 'arriba', 'abajo', 'izquierda' o 'derecha'

Lo que recibes en 'percepcion':
───────────────────────────────
percepcion = {
    'posicion':       (3, 5),          # Tu fila y columna actual
    'arriba':         'libre',         # Qué hay arriba
    'abajo':          'pared',         # Qué hay abajo
    'izquierda':      'libre',         # Qué hay a la izquierda
    'derecha':        None,            # None = fuera del mapa

    # OPCIONAL — brújula hacia la meta.
    # No es percepción real del entorno, es información global.
    # Usarla hace el ejercicio más fácil. No usarla es más realista.
    'direccion_meta': ('abajo', 'derecha'),
}

Valores posibles de cada dirección:
    'libre'  → puedes moverte ahí
    'pared'  → bloqueado
    'meta'   → ¡la meta! ve hacia allá
    None     → borde del mapa, no puedes ir

Si tu agente retorna un movimiento inválido (hacia pared o
fuera del mapa), simplemente se queda en su lugar.
"""

from entorno import Agente


class MiAgente(Agente):
    """
    Tu agente de navegación.

    Implementa el método decidir() para que el agente
    llegue del punto A al punto B en el grid.
    """

    def __init__(self):
        super().__init__(nombre="Mi Agente")
        
        
        self.anterior = None  # ← clave
        
        # Puedes agregar atributos aquí si los necesitas.
        # Ejemplo:
        #   self.pasos = 0
        #   self.memoria = {}

    def al_iniciar(self):
        
        self.anterior = None   # Aqui se guarda la posicion anterior

    def decidir(self, percepcion):
        
        """
        Decide la siguiente acción del agente.
        
        Parámetros:
            percepcion – diccionario con lo que el agente puede ver

        Retorna:
            'arriba', 'abajo', 'izquierda' o 'derecha'
        """
        # ╔══════════════════════════════════════╗
        # ║   ESCRIBE TU LÓGICA AQUÍ             ║
        # ╚══════════════════════════════════════╝

        # Ejemplo básico (bórralo y escribe tu propia lógica):
        #
        # vert, horiz = percepcion['direccion_meta']
        #
        # if percepcion[vert] == 'libre' or percepcion[vert] == 'meta':
        #     return vert
        # if percepcion[horiz] == 'libre' or percepcion[horiz] == 'meta':
        #     return horiz
        #
        # return 'abajo'
        

        pos = percepcion['posicion']  # esta es la posicion en la que se encuentra actualmente
        
        vert, horiz = percepcion['direccion_meta'] # estas son las direcciones hacia la meta vetical y horizontal


        # Esta funcion es para poder validar el movimiento para moverse a esa direccion
        def es_valido(d):
            return d in percepcion and (percepcion[d] == 'libre' or percepcion[d] == 'meta') # solo permite movimientos libres y la meta

        # Esta funcion es para poder calcular la nueva posición que se podria llegar
        def mover(d):
            f, c = pos
            if d == 'arriba':
                return (f - 1, c)
            
            if d == 'abajo':
                return (f + 1, c)
            
            if d == 'izquierda':
                return (f, c - 1)
            
            return (f, c + 1)


        # Es para ver si la meta está al lado para ir
        for d in [vert, horiz]:
            
            if d in percepcion and percepcion[d] == 'meta':
                self.anterior = pos
                return d


        # Esto es para intentar ir hacia la meta pero sin retroceder
        for d in [vert, horiz]:
            
            if es_valido(d) and mover(d) != self.anterior:   # intenta avanzar a donde esta la meta pero no regresa a una posicion anterior
                self.anterior = pos
                return d


        # Esto es para buscar cualquier movimiento válido sin retroceder
        for d in self.ACCIONES:    # recorre el bucle para buscar un camino libre sino es que no puede ir directo a la meta pero no retrocede
            
            if es_valido(d) and mover(d) != self.anterior: # se mueve si es un camino valido pero que no sea repetido
                self.anterior = pos
                return d

        # Esto es para que si no hay otra opción, moverse igual 
        for d in self.ACCIONES:
            
            if es_valido(d):  # hace que si hay un camino valido, se mueva ahi aunque sea un lugar repetido para que continue su camino hacia la meta
                self.anterior = pos
                return d


        return 'arriba'  # esto es por seguridad 