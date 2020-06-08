from builtins import print

try:
    import Queue as queue
except ImportError:
    import queue


""" Defino el grafo  """
grafo = {
    '1': {'2': 2,'3': 1},
    '2': {'4': 1},
    '3': {'4': 3,'5':4},
    '4': {'6': 2},
    '5': {'6': 2},
    '6': { }
}

rumania = {
    'Oradea': {'Sibiu': 151,'Zerind': 71},
    'Zerind': {'Oradea': 71,'Arad': 75},
    'Arad': {'Zerind': 75,'Sibiu': 140,'Timisoara': 118},
    'Timisoara': {'Arad': 118,'Lugoj': 111},
    'Lugoj': {'Timisoara': 111,'Mehadia': 70},
    'Mehadia': {'Lugoj': 70,'Dobreta': 75},
    'Dobreta': {'Mehadia': 75,'Caiova': 120},
    'Caiova': {'Dobreta': 120,'Rimnicu': 146,'Pitesti': 138},
    'Rimnicu': {'Sibiu': 80,'Pitesti': 97,'Caiova': 146},
    'Sibiu': {'Arad': 140,'Oradea': 151,'Fagaras': 99,'Rimnicu': 80},
    'Fagaras': {'Sibiu': 99,'Bucarest': 211},
    'Pitesti': {'Rimnicu': 97,'Caiova': 138,'Bucarest': 101},
    'Bucarest': {'Pitesti': 101,'Giurgiu': 90,'Fagaras': 211,'Urziceni': 85},
    'Giurgiu': {'Bucarest': 90},
    'Urziceni': {'Bucarest': 85,'Hirsova': 98,'Vaslui': 142},
    'Hirsova': {'Urziceni': 98,'Efoire': 86},
    'Efoire': {'Hirsova': 86},
    'Vaslui': {'Iasi': 92,'Urziceni': 142},
    'Iasi': {'Neamt': 87,'Vaslui': 92},
    'Neamt': {'Iasi': 87}
}


"""
 -------->   Busqueda Dijkstra
"""
def busquedaDijkstra(grafo,origen,buscado):
    print("")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("-_-_-                            _-_-_")
    print("-_-_-    D I J K S T R A         _-_-_")
    print("-_-_-                            _-_-_")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("")
    print("<---------------< Grafo >--------------------->")
    for key in grafo.items():
        print("*    ------->  Nodo: ",key[0],"---> Hijos: ",key[1])
    print("")
    print("< Valor origen: ",origen,", Valor buscado: ",buscado,">")
    print("")

    """---------------- Estructuras que utilizo en la busqueda ---------------------"""
    pendientes = queue.PriorityQueue()  # La cola tiene como parametros el valor acumulado y el nombre del nodo, se insertan de forma ordenada por peso
    etiquetas = [(0, origen, origen)]  # lista de etiquetas para poder hacer vuelta atras del recorrido avanzado
    visitados = []  # lista para ver cuales fueron los nodos visitados
    pendientes.put((0, origen))  # Pongo el valor acumulado del primer nodo=0 y el nombre del nodo
    encontrado = False  # marca para que salga del bucle cuando lo encuentre


    """ -------------- Comienzo el bucle principal de la busqueda ---------------------------------------- """
    while pendientes and not encontrado:

        # ----> actualizo mi nodo actual, saco el elemento con valor acumulado mas bajo de la cola de prioridad
        # ---> (0,'nombreNodo') este seria un ejemplo del contenido de un nodo: su costo y su nombre
        nodo_actual = pendientes.get()

        # ---> pregunto si el nodo actual es el buscado
        if nodo_actual[1] == buscado:
            print()
            encontrado = True
        else:
            # ----> Pongo a el nodo actual como visitado
            if nodo_actual[1] not in visitados:
                visitados.append(nodo_actual[1])

            ############################################################
            #
            # --->      EXPANDO EL NODO ACTUAL PARA VER SI TIENE HIJOS
            #
            #############################################################

            for hijo_nodo_actual in grafo[
                nodo_actual[1]].items():  # ('Sibiu', 151) ---> ese seria un ejemplo del contenido del hijo_nodo_actual
                marca = False
                if hijo_nodo_actual[0] not in visitados:
                    for elemento in etiquetas:
                        if elemento[2] == hijo_nodo_actual[0]:
                            if hijo_nodo_actual[1] + nodo_actual[0] <= elemento[0]:
                                etiquetas.remove(elemento)  # Borro el elemento porque su valor no es el mas optimo
                                marca = True
                    if marca:
                        # ----> como marca= True quiere decir que el nodo ya estaba etiquetado y que hubo que cambiar el valor que tenia la etiqueta
                        # ----> añado el valor del nodo hijo porque era mas optimo que el que tenia
                        etiquetas.append((hijo_nodo_actual[1] + nodo_actual[0], nodo_actual[1], hijo_nodo_actual[0]))
                    else:
                        # ----> Agrego el nodo a etiquetas[] porque si marca=False entonces  ese nodo no estaba etiquetado
                        etiquetas.append((hijo_nodo_actual[1] + nodo_actual[0], nodo_actual[1], hijo_nodo_actual[0]))

                    """"
                     ------ > Actualizo el valor de la cola pendientes
                    """
                    if pendientes.qsize() == 0:  # -----> si el tamaño de la cola es 0 entonces solo añado el nodo hijo
                        # ---> Añado a la cola pendientes a el hijo del nodo actual
                        pendientes.put((hijo_nodo_actual[1] + nodo_actual[0], hijo_nodo_actual[0]))
                    else:
                        # ---> el tamaño de la cola es != 0 entonces tengo que verificar que dentro de la cola no exista un nodo
                        # ---> que tenga el mismo nombre que el nodo hijo y que su peso sea menor mayor que el del nodo hijo
                        pendientes.put((hijo_nodo_actual[1] + nodo_actual[0], hijo_nodo_actual[0]))
                        lista = []
                        for j in range(pendientes.qsize()):
                            nodo = pendientes.get()
                            if nodo[1] == hijo_nodo_actual[0]:
                                if hijo_nodo_actual[1] + nodo_actual[0] <= nodo[0]:
                                    # ---> Busca si la lista no contiene el nodo, entonces lo agreaga. Sino no.
                                    if not lista.__contains__(
                                            (hijo_nodo_actual[1] + nodo_actual[0], hijo_nodo_actual[0])):
                                        lista.append((hijo_nodo_actual[1] + nodo_actual[0], hijo_nodo_actual[0]))
                            else:
                                lista.append(nodo)
                        # ----> vuelvo a llenar la cola pendientes con los elementos de la lista !
                        for k in lista:
                            pendientes.put(k)

            #######################################
            #
            #       TERMINA EL EXPANDIR DEL NODO
            #
            #######################################
    """ ---------- termina el bulce while aca ----------------------"""
    """ ------------- Busco la etiqueta del nodo destino que tiene el menor peso acumulado ------------------------- """
    ultimas_etiquetas = []   # lista auxiliar en donde pongo todas las etiquetas que pertenecen al nodo final
    for elemento in etiquetas:
        if elemento[2] == buscado:
            ultimas_etiquetas.append(elemento)
    vuelta_atras = []   # ---> esta lista tendra todos los valores del camino de vuelta atras, va a tener los nombres de los nodos recorridos en el camino critico
    etiqueta_atras = min(ultimas_etiquetas)  # ---- >  busco la mas chica de las etiquetas que tenga el nodo final
    vuelta_atras.append(etiqueta_atras[2])   # ---> añado el nombre del nodo final a la lista
    etiqueta_actual = etiqueta_atras[1]      # ---> la etiqueta actual es el nombre del nodo padre del nodo final
    vuelta_atras.append(etiqueta_actual)     # ----> añado el nombre del nodo padre del nodo final

    # ------>  Mientras la etiqueta actual sea distinta a la etiqueta origen (sea distinta del nombre del nodo inicial) entonces busco los nodos padres de la etiqueta actual
    # ------> variable etiquetas es una lista con contenido ---> (pesoAcumulado <Integer>,nodoPadre <String>,nombreNodoEtiquetado <String>)
    while etiqueta_actual != origen:
        l = 0
        encontrado = False
        while l <= len(etiquetas) and not encontrado:
            actual = etiquetas[l]
            if actual[2] == etiqueta_actual:
                # ----> una vez que encontro el elemento con el mismo nombre que etiqueta_actual, añade a actual[1] a la lista
                encontrado = True
                etiqueta_actual = actual[1]   # ---> actual[1] es el nodo padre al que tengo que ir, por eso ahora debo buscar ese nodo para continuar la vuelta atras
                vuelta_atras.append(actual[1])
            l = l + 1  #---> incremento variable de control
    """----------- termina bucle while ------------------------"""

    # ----------------- termina el while --------------------------------------------------
    # ----> Muestro los resultados de la busqueda
    # ----> vuelta_atras = tiene los nombres de todos los nodos que recorri para el camino con menos costo
    # ----> etiqueta_atras[0] = tiene el valor acumulado del recorrido que tiene menor costo
    print("-----------------------------------------------")
    print("----------- RESULTADOS DE LA  BUSQUEDA --------")
    print("----->    Camino: ", vuelta_atras)
    print("----->    Costo: ", etiqueta_atras[0])
    print("-----------------------------------------------")
    print("-----------------------------------------------")
"""
--------> TERMINA LA FUNCION DE BUSQUEDA DIJKSTRA  -------------------------------------------------------------------------
"""


# ----> llamo a la busqueda dijkstra
busquedaDijkstra(grafo,'3','6')
busquedaDijkstra(rumania,'Arad','Bucarest')