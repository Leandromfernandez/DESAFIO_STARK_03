""" 1.1. Crear la función ”obtener_dato()” la cual recibirá por parámetro un
diccionario el cual representara a un héroe y también recibirá un string que
hace referencia a una “clave” del mismo
Validar siempre que el diccionario no esté vacío y que el mismo tenga una key
llamada “nombre”. Caso contrario la función retornara un False
 """
 
from data_stark import lista_personajes

def obtener_dato(lista_personajes:list, clave:str):
    if len(lista_personajes)>=1:
        for personaje in lista_personajes:
            if clave in personaje:
                dato = personaje[clave]
                return dato
            
        if clave not in personaje:
            print("La clave no existe. ")
    else:
        print('La lista se encuentra vacia!. ')
        return False
    
    


dato = obtener_dato(lista_personajes, 'altura')

def stark_normalizar_datos(lista_personajes:list, key:str):

    dato_modificado = False
    if len(lista_personajes) >= 1:
        for personaje in lista_personajes:
            for key in personaje:
                valor = personaje[key]
                if valor.isdigit() and valor.count(".") >= 1:
                    personaje[key] = float(valor)
                    dato_modificado = True
                elif valor.isdigit():
                    personaje[key] = int(valor)
                    dato_modificado = True                                      
    else:
        print("La lista se encuentra vacia! ")       

    if dato_modificado == True:
        print("Datos normalizados.")
    else:
        print("Hubo un error al normalizar los datos.\nVerifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")

    
    return personaje[key]




