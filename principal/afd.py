

from ast import Break, Try
from cgi import print_directory
from cgitb import text
from email import message
from gc import callbacks
from lib2to3.pgen2.tokenize import tokenize
from logging import exception
from secrets import token_bytes
from tokenize import Token
from turtle import width
from xml.etree import ElementInclude


class AutomataPila:
    def __init__(self,textoPlano):
        self.textoPlano=textoPlano
        self.diccionario=[]
        self.Tokens=[]
        
        
    def reciboDatos(textoPlano):
        
        TokenControles=[]
        TokenPropiedades=[]
        TokenColocacion=[]
        listaPropiedades=[]
        contador=0
        errores=[]
        identificador=""
        palabraClave=""
        
        listaFilas=textoPlano.split("\n")
        for e in listaFilas:
            listaFilas[contador]=listaFilas[contador].rstrip()
            listaFilas[contador]=listaFilas[contador].lstrip()
            print(listaFilas[contador])
            contador+=1
            
        print("---------------------------")
        if listaFilas[0]=="<!--Controles":
            print("todo bien")
        else:
            errores.append("error de etiqueta")
            print("error")
            
        for element in listaFilas:
            
            palabraClave=""
            for letra in element:
                
                palabraClave+=letra
                
                if palabraClave == "Contenedor" :
                    control=element.split(" ")
                    id=control[1]
                    print(id)
                    TokenControles.append({
                        "Contenedor":id
                    })
                    
                
                if palabraClave=="Boton":
                    control=element.split(" ")
                    id=control[1]
                    print(id)
                    TokenControles.append({
                        "Boton":id
                    })
                    
                    
                if palabraClave=="Etiqueta":
                    control=element.split(" ")
                    id=control[1]
                    print(id)
                    TokenControles.append({
                        "Etiqueta":id
                    })
                    
                if palabraClave=="check":
                    print("si")
                    
                if palabraClave=="RadioBoton":
                    print("si")
                    
                if palabraClave=="Texto":
                    control=element.split(" ")
                    id=control[1]
                    print(id)
                    TokenControles.append({
                        "Texto":id
                    })
                    
                if palabraClave=="AreaTexto":
                    print("si")
                    
                if palabraClave=="Clave":
                    control=element.split(" ")
                    id=control[1]
                    print(id)
                    TokenControles.append({
                        "Clave":id
                    })
                if palabraClave=="Controles -->":
                    print("Termino los controles")
                    break
                
            
        print(TokenControles)        
        exception=False
        for element in listaFilas:
            palabraClave=""
            for letra in element:
                palabraClave+=letra
                
                if palabraClave=="<!--propiedades":
                    exception=True
                    
                
                if palabraClave=="//#$inicio de" and identificador=="" and palabraClave!="//#$inicio de cmd":
                    separacion=element.split(" ")
                    identificador=separacion[2]
                    
                if palabraClave=="//#$inicio de cmd":
                    separacion=element.split(" ")
                    identificador=separacion[2]
                    
                    
                if palabraClave==identificador and identificador!="":
                    separar=element.split(".")
                    listaPropiedades.append(separar[1])
                    
                    
                    
                if palabraClave=="//#$fin de " + identificador:
                    TokenPropiedades.append({identificador:listaPropiedades})
                    identificador=""
                    listaPropiedades=[]
                    
        
        condicion=False
        for element in listaFilas:
            palabraClave=""
            for letra in element:
                palabraClave+=letra
                if palabraClave=="<!--Colocacion":
                    condicion=True
                if palabraClave=="Colocacion -->":
                    condicion =False
                    break
            if condicion==True and palabraClave!="<!--Colocacion":
                TokenColocacion.append(element)
        
        
        
        
    def Afd(textoPlano):
        condicionPropiedades=False
        condicionColocacion=False
        contador=0
        identificadores=[]
        estilos=[]
        controles=[]
        propiedades=[]
        posiciones=[]
        listaFilas=textoPlano.split("\n")
        for e in listaFilas:
            listaFilas[contador]=listaFilas[contador].rstrip()
            listaFilas[contador]=listaFilas[contador].lstrip()
            
            contador+=1
        for element in listaFilas:
            if element=="<!--Controles":
                for elem in listaFilas:
                    controles.append(elem)
                    if elem=="Controles -->":
                        break
            
            if condicionPropiedades==True:
                propiedades.append(element)
            
            if element=="<!--propiedades":
                condicionPropiedades=True
                propiedades.append(element)

            if element=="propiedades -->":
                condicionPropiedades=False
            
            
            if condicionColocacion==True:
                posiciones.append(element)
            if element=="<!--Colocacion":
                condicionColocacion=True
                posiciones.append(element)
            if element=="Colocacion -->":
                condicionColocacion=False
        
        
        
        
        for element in controles:
            if element=="<!--Controles":
                continue
            if element=="Controles -->":
                continue
            else:
                element=element.strip(";")
                print(element)
                separacion=element.split(" ")
                identificadores.append(separacion[1])

    
        for element in identificadores:
            
            for propiedad in propiedades:
                
                
                if element in propiedad:
                    estilos.append({
                        element:propiedad
                    })
        
        fondo=""
        colorLetra=""
        traduccionEstilos=[{
            "setAncho":"width:",
            "setAlto":"height:",
            "setColorFondo":"background-color:rgb"+"("+fondo+")",
            "setColorLetra":"color:rgb"+"("+colorLetra+")",
            "setTexto":"texto",
            "add":"<"
        }]
        
        
        
        textosDiccionario=[]
        print("SEPARACION.----------------------")
        
        ArchivoCss=open("Styles.css","w")
        
        for ide in identificadores:
            fondo=""
            colorLetra=""
            left=""
            top=""
            mensaje="#"+ide+"{"
            print(ide)
            for estilo in estilos:
                if ide in estilo:
                    
                    elemento=estilo[ide]
                    
                    try:
                        separacion=elemento.split(".")
                        style=separacion[1]
                        
                    except :
                        continue
                    #print(style)
                    palabraClave=""
                    posicion=0
                    
                    for letra in style:
                        
                        palabraClave+=letra
                        
                        if style[posicion+1]=="(":
                            
                            token=palabraClave
                            
                            for element in traduccionEstilos:
                                if token in element:
                                        
                                    
                                    texto=element[token]
                        
                                    
                                    
                            
                        elif style[posicion+1]!="(":
                            posicion+=1
                    
                    separacion2=style.split("(")
                    numeros=separacion2[1]
                    numeros=numeros.lstrip()
                    numeros=numeros.strip(");")
                    if numeros[0]=='"':
                        numeros=numeros.strip('"')
                        textosDiccionario.append({
                            ide:numeros
                        })
                        
                    
                    
                    
                    
                    if texto=="background-color:rgb"+"("+fondo+")":
                        
                        fondo=numeros
                        mensaje+="background-color:rgb("+ numeros+")"+";"
                    
                    
                    elif texto=="color:rgb"+"("+colorLetra+")":
                        
                        colorLetra=numeros
                        mensaje+="color:rgb("+numeros+")"+";"
                    elif texto=="texto":
                        mensaje=mensaje
                    else :
                        mensaje+=texto+numeros+";"
                        
                    
                    print("----------------------")
            
            for elemento in posiciones:
                
                if ide in elemento:
                    try:
                        separacion=elemento.split(".")
                        position=separacion[1]
                       
                        
                    
                    except:
                        continue
                    palabraClave=""
                    for letter in position:
                        palabraClave+=letter
                        if "setPosicion" in palabraClave:
                            separacion2=position.split("(")
                            Stripeo=separacion2[1]
                            Stripeo=Stripeo.strip(");")
                            Stripeo=Stripeo.split(",")
                            
                            mensaje+="top:"+Stripeo[1] +";"+ "left:" + Stripeo[0]+";"
                            
                            
                            
                            break

            mensaje+="position: absolute;"
            mensaje+="font-size: 12px;"
            mensaje+="}"
            ArchivoCss.write(mensaje)
            
            
        ArchivoCss.close()
        
        

        #SE COMIENZAN CON LAS FUNCIONES PARA GENERAR EL ARCHIVO HTML
        
        print("##########################################")
        mensaje2="<html> <head> <link href=\"/Styles.css\" rel=\"stylesheet\" type=\"text/css\"> </head> <body> "
        
        controlesDiccionario=[]
        for element in controles:
            try:
                separacion=element.split(" ")
                separacion[1]=separacion[1].strip(";")
                controlesDiccionario.append({
                    separacion[1]:separacion[0]
                })
            except:
                continue
            
        controlesDiccionario.pop(-1)
        print(controlesDiccionario)
        for ide in identificadores:
            
            print(ide)
            
            for elemento in posiciones:
                
                palabraClave=""
                for letra in elemento:
                    palabraClave+=letra
                    
                    
                    
                    if "("+ide+")"in palabraClave:
                        separacion=palabraClave.split(".")
                        
                        for cosa in controlesDiccionario:
                            if ide in cosa:
                                 
                                if cosa[ide]=="Contenedor":
                                    print("Esto es un contenedor")
                                    mensaje2+="<div id=\"" + ide +"\"></div>" 
                                
                                elif cosa[ide]=="Boton":
                                    
                                    for text in textosDiccionario:
                                        if ide in text:
                                            setText=text[ide]
                                            print("el texto es: " + setText)
                                            break  
                                        
                                    mensaje2+="<input type=\"submit\" id=\"" + ide+"\" value=\"" + setText + "\" style=\"text-align: center\"/>"
                                   
                                    print("Esto es un Boton")
                                    
                                elif cosa[ide]=="Check":
                                    for text in textosDiccionario:
                                        if ide in text:
                                            setText=text[ide]
                                            break
                                    mensaje2+="<input type=\"checkbox\" id=\""+ide+"\"/>"+ setText
                                    
                                    print("Esto es un Check")
                                    
                                elif cosa[ide]=="RadioBoton":
                                    print("Esto es un RadioBoton")
                                    for text in textosDiccionario:
                                        if ide in text:
                                            setText=text[ide]
                                            break
                                    mensaje2+="<input type \"radio\" name=\"Group\" id=\""+ ide+"\"/>" + setText
                                    
                                    
                                elif cosa[ide]=="Texto":
                                    print("Esto es un Texto")
                                    for text in textosDiccionario:
                                        if ide in text:
                                            setText=text[ide]
                                            break
                                    mensaje2+="<input type=\"text\" id=\""+ ide+"\" value=\""+setText + "\" style=\"text-align: center\"/>"
                                    
                                elif cosa[ide]=="AreaTexto":
                                    for text in textosDiccionario:
                                        if ide in text:
                                            setText=text[ide]
                                            break
                                    mensaje2+="<textarea id=\""+ ide + "\">" + setText + "</textarea>"
                                    print("Esto es un AreaTexto")
                                    
                                elif cosa[ide]=="Clave":
                                    print("Esto es un Clave")
                                    for text in textosDiccionario:
                                        if ide in text:
                                            setText=text[ide]
                                            break
                                    mensaje2+="<input type=\"password \" id=\"" +ide + "\" value=\"" + setText + "\" style=\"text-align:center\"/>"    
                                    
                                elif cosa[ide]=="Etiqueta":
                                    print("Esto es un Etiqueta")
                                    for text in textosDiccionario:
                                        if ide in text:
                                            setText=text[ide]
                                            break
                                    mensaje2+="<label id=\""+ ide + "\">" + setText+ "</label>"
                                     
                            
                        
                        if separacion[0] in identificadores:
                            
                            print("Esta dentro de los identificadores")
                        elif separacion[0]=="this":
                            print("ESTA EN EL THIS")
                            
                        print("ANDAMOS POR ACA "+palabraClave)
                        break
                        
        mensaje2+="</body></html>"
        
        f=open("holamundo.html","w")
       
        
        f.write(mensaje2)
        
        f.close()
        