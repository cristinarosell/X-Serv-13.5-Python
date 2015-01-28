#!/usr/bin/python
fich=open("/etc/passwd", "r")

usuarios=fich.readlines()
fich.close()

dicc={}

for usuario in usuarios:
	
	lista=usuario.split(':')
	
	name= lista[0]
	shell=lista[-1][:-1]
	dicc[name]=shell

print "Numero de usuarios:", len(dicc)

print "root", dicc["root"]

try: 
	print dicc["imaginario"]
except KeyError:
	print "Usuario imaginario no existe"
	
