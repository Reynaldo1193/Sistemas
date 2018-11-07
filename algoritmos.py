from collections import defaultdict

class Grafo:

	def __init__(self):
		self.grafo = defaultdict(list)

	def adyacencia(self,i,j):
		self.grafo[i].append(j)

	def BFS(self, inicio,final):

        #Marca todos los nodos como no visitados
		visitado = [False] * (len(self.grafo))

		#Lista de nodos BFS
		queue = []

		#Marca el nodo iniical como visitado y lo agrega a la lista
		queue.append(inicio)
		visitado[inicio] = True

		while queue:

			#Elimina de la lista el nodo de inicio
			s = queue.pop(0)
			print (inicio, end = " ")

			#Algoritmo BFS
			for k in self.grafo[inicio]:
				if visitado[k] == False:
                    queue.append(k)
					visited[k] = True

#Llena el grafo con las torres de hanoi
g = Grafo()
g.adyacencia(0, 1)
g.adyacencia(0, 2)
g.adyacencia(1, 0)
g.adyacencia(1, 2)
g.adyacencia(1, 3)
g.adyacencia(2, 0)
g.adyacencia(2, 1)
g.adyacencia(2, 4)
g.adyacencia(3, 1)
g.adyacencia(3, 5)
g.adyacencia(3, 6)
g.adyacencia(4, 2)
g.adyacencia(4, 7)
g.adyacencia(4, 8)
g.adyacencia(5, 3)
g.adyacencia(5, 6)
g.adyacencia(5, 9)
g.adyacencia(6, 3)
g.adyacencia(6, 5)
g.adyacencia(6, 7)
g.adyacencia(7, 4)
g.adyacencia(7, 6)
g.adyacencia(7, 8)
g.adyacencia(8, 4)
g.adyacencia(8, 7)
g.adyacencia(8, 10)
g.adyacencia(9, 5)
g.adyacencia(9, 11)
g.adyacencia(9, 12)
g.adyacencia(10, 8)
g.adyacencia(10, 13)
g.adyacencia(10, 14)
g.adyacencia(11, 9)
g.adyacencia(11, 12)
g.adyacencia(11, 15)
g.adyacencia(12, 9)
g.adyacencia(12, 11)
g.adyacencia(12, 18)
g.adyacencia(13, 10)
g.adyacencia(13, 14)
g.adyacencia(13, 24)
g.adyacencia(14, 10)
g.adyacencia(14, 13)
g.adyacencia(14, 21)
g.adyacencia(15, 11)
g.adyacencia(15, 16)
g.adyacencia(15, 17)
g.adyacencia(16, 15)
g.adyacencia(16, 17)
g.adyacencia(17, 15)
g.adyacencia(17, 16)
g.adyacencia(17, 19)
g.adyacencia(18, 12)
g.adyacencia(18, 19)
g.adyacencia(18, 20)
g.adyacencia(19, 17)
g.adyacencia(19, 18)
g.adyacencia(19, 20)
g.adyacencia(20, 18)
g.adyacencia(20, 19)
g.adyacencia(20, 25)
g.adyacencia(21, 14)
g.adyacencia(21, 22)
g.adyacencia(21, 23)
g.adyacencia(22, 21)
g.adyacencia(22, 23)
g.adyacencia(22, 26)
g.adyacencia(23, 21)
g.adyacencia(23, 22)
g.adyacencia(24, 13)
g.adyacencia(24, 25)
g.adyacencia(24, 26)
g.adyacencia(25, 20)
g.adyacencia(25, 24)
g.adyacencia(25, 26)
g.adyacencia(26, 22)
g.adyacencia(26, 24)
g.adyacencia(26, 25)


print ("Lista Nodo: ")
g.BFS(0,23)
