# Analizador lexico

def AnalizadorLexico(entrada):
    elementos = []
    estado = None
    indice = 0
    cadena = entrada + '$'
    while (indice <= (len(cadena) - 1) and estado == None):
        lexema = ''
        token = 'error'
        tipo = None
        while (indice <= (len(cadena) - 1) and estado != 20):
            if estado == None:
                if (cadena[indice].isspace()):
                    estado = None
                elif cadena[indice].isalpha() or cadena[indice] == '_':
                    estado = 0
                    lexema += cadena[indice]
                    token = 'id'
                    tipo = 0
                elif cadena[indice].isdigit():
                    estado = 1
                    lexema += cadena[indice]
                    token = 'entero'
                    tipo = 1
                elif cadena[indice] == '$':
                    estado = 20
                    lexema += cadena[indice]
                    token = 'pesos'
                    tipo = 23

                else:
                    estado = 20
                    token = 'error'
                    lexema = cadena[indice]
                indice += 1

            elif estado == 0:
                if cadena[indice].isdigit() or cadena[indice].isalpha() or cadena[indice] == '_':
                    estado = 0
                    lexema += cadena[indice]
                    token = 'id'
                    indice += 1
                else:
                    estado = 20
            elif estado == 1:
                if cadena[indice].isdigit():
                    estado = 1
                    lexema += cadena[indice]
                    token = 'entero'
                    indice += 1
                elif cadena[indice] == '.':
                    estado = 2
                    lexema += cadena[indice]
                    token = 'error'
                    indice += 1
                else:
                    estado = 20
            elif estado == 2:
                if cadena[indice].isdigit():
                    estado = 2
                    lexema += cadena[indice]
                    token = 'real'
                    indice += 1
                else:
                    estado = 20

        estado = None
        elementos.append({'token': token, 'lexema': lexema, 'tipo': tipo})

    return elementos


def main():

    entrada = input("Ingrese una cadena: ")
    estados = AnalizadorLexico(entrada)
    for i in range(len(estados)):
        print(estados[i])


if __name__ == '__main__':
    main()
