Python 3.7.0b3 (v3.7.0b3:4e7efa9c6f, Mar 29 2018, 18:42:04) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Grafo(object):
	def _init_(self,adyacencia):
		self.ady=adyacencia
		self._init_grafo(-1)
	def _init_grafo(self,inicio):
		self.encontrado=[False for n in self.ady]
		self.procesado=[False for n in self.ady]
		self.padre=[-1 for n in self.ady]
		self.inicio=inicio
	def profundidad (self, inicio):
		self._init_grafo(inicio)
		q=[inicio]
		self.encontrado[inicio]=True
		while q:
			v=q.pop()
			self.procesado[v]=True
			for vecino in self.ady[v]:
				if not self.encontrado[vecino]:
					q.append(vecino)
					self.encontrado[vecino]=True
					self.padre[vecino]=v
	def construir_camino(self, destino):
		if self.padre[destino]== -1 or self.inicio== -1:
			return None
		camino=[destino]
		p=destino
		while p != self.inicio:
			camino.append(self.padre[p])
			p=self.padre[p]
		return camino

	
>>> inicio=3
>>> destino=2
>>> g=Grafo(adyacencia)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    g=Grafo(adyacencia)
NameError: name 'adyacencia' is not defined
>>> inicio=3
>>> destino=2
>>> adyacencia={'3':[1,4],}
>>> adyacencia={'3':[1,4],'1':[2,5],'4':[6]}
>>> g=Grafo(adyacencia)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    g=Grafo(adyacencia)
TypeError: Grafo() takes no arguments
>>> 
