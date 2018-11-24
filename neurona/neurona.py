from numpy import exp, array, random, dot

def main():
	class neurona:
		def __init__(self):
			random.seed(1)
			self.weights = 2 * random.random((2, 1)) - 1
		
		def entrena(self, entradas, salidas, num):
			for iteration in range(num):
				output = self.piensa(entradas)
				error = salidas - output
				adjustment = 0.01 * dot(entradas.T, error)
				self.weights += adjustment
			
		def piensa(self, entradas):
			return (dot(entradas, self.weights))
		
	
	neurona = neurona()
	entradas = array([   [2,3], [1,3], [5,2], [12,3], ])
	salidas = array([[    10,     8,    14,     30],  ]).T
	
	
	veces = int(input("¿Cuantas veces quieres que entrene? 1-10000: "))
	
	neurona.entrena(entradas, salidas, veces)
	
	
	n1 = input("Dime un número: ")
	n2 = input("Dime otro número: ")
	
	resultado = neurona.piensa(array([int(n1), int(n2)]))
	print("Creo que el resultado es: {}".format(resultado))
			
if __name__ == "__main__":
	main()
