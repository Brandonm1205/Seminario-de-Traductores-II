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
                elif cadena[indice] == ';':
                    estado = 20
                    lexema += cadena[indice]
                    token = 'punto_y_coma'
                    tipo = 12
                elif cadena[indice] == ',':
                    estado = 20
                    lexema += cadena[indice]
                    token = 'coma'
                    tipo = 13
                elif cadena[indice] == '(':
                    estado = 20
                    lexema += cadena[indice]
                    token = 'parentesis apertura'
                    tipo = 14
                elif cadena[indice] == ')':
                    estado = 20
                    lexema += cadena[indice]
                    token = 'parentesis cerradura'
                    tipo = 15
                elif cadena[indice] == '{':
                    estado = 20
                    lexema += cadena[indice]
                    token = 'llave apertura'
                    tipo = 16
                elif cadena[indice] == '}':
                    estado = 20
                    lexema += cadena[indice]
                    token = 'llave cerradura'
                    tipo = 17
                elif cadena[indice] == '+' or cadena[indice] == '-':
                    estado = 20
                    lexema += cadena[indice]
                    token = 'opSuma'
                    tipo = 5
                elif cadena[indice] == '*' or cadena[indice] == '/':
                    estado = 20
                    lexema += cadena[indice]
                    token = 'opMultiplicacion'
                    tipo = 6

                elif cadena[indice] == '=':
                    lexema += cadena[indice]
                    token = 'asignación'
                    estado = 8
                    tipo = 18
                elif cadena[indice] == '<' or cadena[indice] == '>':
                    lexema += cadena[indice]
                    token = 'opRelacional'
                    estado = 8
                    tipo = 7
                elif cadena[indice] == '!':
                    estado = 8
                    lexema += cadena[indice]
                elif cadena[indice] == '|':
                    estado = 9
                    lexema += cadena[indice]
                elif cadena[indice] == '&':
                    estado = 10
                    lexema += cadena[indice]

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

            elif estado == 8:
                if cadena[indice] != '=':
                    estado = 20
                else:
                    estado = 20
                    tipo = 7
                    lexema += cadena[indice]
                    token = 'opRelacional'
                    indice += 1

            elif estado == 9:
                if cadena[indice] != '|':
                    estado = 20
                else:
                    estado = 20
                    tipo = 8
                    lexema += cadena[indice]
                    token = 'opOr'
                    indice += 1
            elif estado == 10:
                if cadena[indice] != '&':
                    estado = 20
                else:
                    estado = 20
                    tipo = 9
                    lexema += cadena[indice]
                    token = 'opAnd'
                    indice += 1

        estado = None
        elementos.append({'token': token, 'lexema': lexema, 'tipo': tipo})

    for elemento in elementos:
        if elemento['lexema'] == "if":
            elemento['token'] = "condicional SI"
            elemento['tipo'] = 19
        if elemento['lexema'] == "else":
            elemento['token'] = "else"
            elemento['tipo'] = 22
        if elemento['lexema'] == "int" or elemento['lexema'] == "float" \
                or elemento['lexema'] == "char" or elemento['lexema'] == "void":
            elemento['token'] = "tipo de dato"
            elemento['tipo'] = 4
        if elemento['lexema'] == "while":
            elemento['token'] = "While"
            elemento['tipo'] = 20
        if elemento['lexema'] == "return":
            elemento['token'] = "Return"
            elemento['tipo'] = 21

    return elementos


def main():

    entrada = input("Ingrese una cadena: ")
    estados = AnalizadorLexico(entrada)
    for i in range(len(estados)):
        print(estados[i])


if __name__ == '__main__':
    main()
