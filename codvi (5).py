import os
class persona ():
		def __init__(self, nacimiento, nombre, apellido, genero, nacionalidad, edad):
			self.nacimiento = nacimiento
			self.nombre = nombre
			self.apellido = apellido
			self.genero = genero
			self.nacionalidad = nacionalidad
			self.edad = edad
			
def write (f,b):
		f=open('lista.txt', 'a')
		f.write (b)
		f.close ()	
		
class paciente (persona):
	def __init__(self, nacimiento, nombre, apellido, genero, nacionalidad, edad,vital, tos, fiebre, dolor, respiracion, garganta):
			persona.__init__(self, nacimiento, nombre, apellido, genero, nacionalidad, edad)
			self.vital = vital
			self.tos = tos
			self.fiebre = fiebre
			self.dolor = dolor
			self.respiracion = respiracion
			self.garganta = garganta
			
	def Condicion(self):
		#if self.fiebre==False and self.tos== False and self.dolor==False and self.respiracion==False and self.garganta==False:
		self.condicion="No posee ninguna enfermedad"
		
		if self.vital==False:
			self.condicion= "La persona ha fallecido, será registrada en la lista de defunciones con sus respectivos datos"
	
		elif self.fiebre==True and self.tos == True and self.dolor==True and self.respiracion== True and self.garganta==True:
			self.condicion = "Coronavirus"
		elif self.fiebre==False and self.tos == False and self.dolor==False and self.respiracion== False and self.garganta==False:
			self.condicion = "Curado"
		elif self.fiebre==True and self.tos== True:
			self.condicion = "Refriado"

		elif self.respiracion==True and self.garganta==True:
			self.condicion = "Alergia"

		else:
			self.condicion = "Sin corfirmar"
	def mostrar(self):
		print ('_________')
		print(self.nombre)
		print ('_________')
		print (self.apellido)
		print ('_________')
		print (self.edad)
		print ('_________')
		print(self.genero)
		print ('_________')
		print(self.nacionalidad)
		print ('_________')
		print(self.edad) 
		print ('_________')
		
def informacion ():
	print ("""El nuevo coronavirus es un virus respiratorio que se propaga principalmente por contacto con una persona infectada 
a través de las gotículas respiratorias que se generan cuando esta persona tose o estornuda.""")
	a = input ()
	os.system ('cls')
	print ("""LAVARSE LAS MANOS CON FRECUENCIA
Lávese las manos con frecuencia con un desinfectante de manos a base de alcohol o con agua y jabón.

MEDIDAS DE HIGIENE RESPIRATORIAS
Al toser o estornudar, cúbrase la boca y la nariz con el codo flexionado o con un pañuelo
DISTANCIAMIENTO SOCIAL
Mantenga distancia entre usted y las demás personas debido al nivel de contagio del virus

EVITAR CONTACTO CON EL ROSTRO
Las manos tocan muchas superficies que pueden estar contaminadas con el virus. """) 
	a = input ()
	os.system ('cls')
	 
opc=0

paises = ["Venezuela", "Colombia", "Brasil", "Chile" ]
tu2 = paciente("24 de enero de 1965","Andres","Grillo","Masculino","Brasil",50,True,True,True,True,True,True)
tu = paciente("24 de enero de 1965","Andreina","Perez","Femenino","Colombia",20,True,False,False,False,False,False)
lista=[]
lista.append(tu)
lista.append(tu2)
for element in lista:
	element.Condicion()
while opc !=7:
	print ('_________________________________________________________')
	print ("""Sistema de control con respecto al nuevo virus CODVI-19
1) Revisión de sintomas
2) Modificar status de un paciente
3) Pacientes registrados
4) Informacion sobre el virus
5) Persona de mayor edad registrada
6) Persona de menor edad registrada
7) Salir
_________________________________________________________""")
	opc= int(input ('Ingrese la opcion deseada: '))
	os.system ('cls')
	
	if opc==1:
		fl = open(archivo,"a") 
		nom= input ('NOMBRE: ')
		apel= input ('APELLIDO: ')
		nacim= input ('FECHA DE NACIMIENTO: ')
		ed=int(input ('EDAD: '))
		gene= input ('GENERO: ')
		i = 0
		for nacion in paises:
			print(i , nacion)
			i = i + 1
		opc= int(input ('NACIONALIDAD: '))
		nacio = paises[opc]
		os.system ('cls')
		
		print ("¿La persona se encuentra en estado vital?")
		vital=input ()
		if vital=="si":
			vi =True
		else:
			vi=False
			print ('')
		print("¿Presenta tos seca ?")
		tos = input()
		if tos=="si":
			to = True
		else:
			to = False
		print ("¿Presenta fiebre mayor a los 39°?")
		fiebre= input()
		if fiebre=="si":
			fi = True
		else:
			fi = False
		print ("""¿Presenta dolor agudo en las extremidades o inmovilización 
en alguna zona del cuerpo debido al dolor?""")
		dolor= input() 
		if dolor=="si":
			do = True
		else:
			do = False
		print ("¿Presenta problemas agudos para respirar (sin procedencia de asma ya diagnosticada)?")
		respiracion= input()
		if respiracion=="si":
			re = True
		else:
			re = False
		print ("¿Presenta dolor agudo en la garganta o incapacidad para hablar debido a la molestia?")
		garganta = input()
		
		if garganta=="si":
			ga = True
		else:
			ga = False
		a= input 
		os.system ('cls')
		paci = paciente(nacim, nom, apel, gene, nacio,ed, vi, to, fi, do, re, ga)
		paci.Condicion()
		a = input("Presione ENTER para analizar cuestionario")
		os.system ('cls')
		print ("La condición del paciente es: ")
		print ('')
		print (paci.condicion)
		print ('')
		a= input('Presione ENTER para continuar')
		os.system ('cls')
		lista.append (paci)
			
	elif opc==2:
		for element in lista:
			element.mostrar()
			opc= int(input(""""Modificar este usuario: 
1) Si
2) No
Opcion: """))
		
			if opc==1:
				while True:
					print('______________________________')
					print ('0: Estado vital del paciente')

					if element.tos==True:
						b = "Si"
					else : 
						b= "No"
					print('______________________________')
					print("1: ¿Presenta tos seca ?", b )
					
					if element.fiebre==True:
						b = "Si"
					else : 
						b= "No"
					print('______________________________')
					print("2: ¿Presenta fiebre mayor a 39° ?", b )
					
					if element.dolor==True:
						b = "Si"
					else : 
						b= "No"
					print('______________________________')
					print("3: ¿Presenta dolencia muscular severa?", b )
					
					if element.respiracion==True:
						b = "Si"
					else : 
						b= "No"
					print('______________________________')
					print("4: ¿Presenta dificultad aguda para respirar ?", b )
					
					if element.garganta==True:
						b= "Si"
					else:
						b= "No"
					print('______________________________')
					print ("5:¿Presenta dolor severo en la garganta o incapacidad de hablar", b)
					print('______________________________')
					print("6: Salir")
					opc = int(input('Que dato desea modificar (Al confirmar el dato que cambie, el sistema lo registrara): '))
					if opc ==0:
						
						element.vital=False 
					elif opc==1:
						if element.tos==True:
							element.tos=False
						else:
							element.tos=True
					elif opc==2:
						if element.fiebre==True:
							element.fiebre=False
						else:
							element.fiebre=True
					elif opc==3:
						if element.dolor==True:
							element.dolor=False
						else:
							element.dolor=True
					elif opc==4:
						if element.respiracion==True:
							element.respiracion=False
						else:
							element.respiracion=True
					elif opc==5:
						if element.garganta==True:
							element.garganta=False
						else:
							element.garganta=True
					elif opc==6:
						break
				element.Condicion()
			if opc==2:
				print()

	elif opc==3:
		coro = 0
		sos = 0
		vita =0
		gen = 0
		cura = 0
		F=0
		lista2 = []
		print("1: Menores de edad")
		print("2: Adultos ")
		print("3: Ancianos")
		print("4. Pacientes femeninos")
		print("5. Pacientes masculinos")
		print ("6.Respecto a su nacionalidad")
		opc = int(input())
		os.system ('cls')
		if opc ==1:
			for element in lista:
				os.system ('cls')
				if element.edad<18:	
					lista2.append(element)
		elif opc ==2:
			for element in lista:
				if element.edad>=18 and element.edad<64:
					lista2.append(element)
		elif opc ==3:
			for element in lista:
				if element.edad>65:
					lista2.append(element)	
		elif opc ==4:
			for element in lista:
				if element.genero=="Femenino":
					lista2.append(element)
		elif opc ==5:
			
			for element in lista:
				
				if element.genero== "Masculino":
					lista2.append(element) 
		elif opc == 6:
			i = 0
			for nacio in paises:
				print(i,":", nacio)
				i = i + 1
			opc = int(input("Elija su opcion: "))
			pais = paises[opc]
			for element in lista:
				if element.nacionalidad==pais:
					lista2.append(element)
		total = 0
		for element in lista2:
			total = total +1 		
		for element in lista2:
			if element.condicion=="Coronavirus":
				coro = coro +1
		
		for element in lista2:
			
			if element.vital==False:
				vita=vita+1
		for element in lista2:
			if element.condicion=="Curado":
				cura = cura + 1
				
		print("Numero de casos totales en esta categoria:", total)
		print("Numero de casos en esta categoria con coronavirus:",coro)
		print("Numero de casos sin confirmar en esta categoria:",sos)
		print("Numero de casos curados: ", cura )
		print("Numero de fallecidos: ",vita)
		
		
	elif opc==4:
		informacion ()
		print ()
		print ('Presione ENTER para salir')
		a=input ()
		os.system ('cls')
	
	elif opc==5:
		
		print("""1. En escala a Coronavirus
2. En escala de alergia
3. En escala de resfriado
""")
		opc = int(input("Ingrese la opcion: "))
		if opc==1:
			condi = "Coronavirus"
		elif opc==2:
			condi = "Alergia"
		elif opc==3: 
			condi = "Resfriado"
		mayor=0
		
		for element in lista:
			if element.edad>mayor and element.condicion==condi:
				mayor = element.edad
				pacientoso = element
		if  mayor!=0:
			pacientoso.mostrar()
		else: 
			print("No existe persona con esta condicion")
	
	elif opc==6:
		
		print("""1. En escala a Coronavirus
2. En escala de alergia
3. En escala de resfriado
""")
		opc = int(input("Ingrese la opcion: "))
		if opc==1:
			condi = "Coronavirus"
		elif opc==2:
			condi = "Alergia"
		elif opc==3: 
			condi = "Resfriado"
		menor=1000
		
		for element in lista:
			if element.edad<menor and element.condicion==condi:
				mayor = element.edad
				pacientoso = element
		if  mayor!=0:
			pacientoso.mostrar()
		else: 
			print("No existe persona con esta condicion")
			
#profe estoy triste porque no vimos clases más con usted :c
#espero se esté cuidando <3
