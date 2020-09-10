class Helpers:

    def __init__(self):
        self.codigo = ['m', 'u', 'r', 'c', 'i', 'e', 'l', 'a', 'g', 'o']
        self.abc = "0123456789"
        self.salida_cadena = ''
        self.salida_numerica = ''

    def encriptar_cadena(self, texto):

        textoMinus = texto.lower()

        for i in range(len(textoMinus)):

            if textoMinus[i] in self.codigo:
                self.salida_cadena += str(self.codigo.index(texto[i]))
            else:
                self.salida_cadena += texto[i]

        return self.salida_cadena

    def desencriptar_cadena(self, texto):

        textoMinus = texto.lower()

        for i in range(len(texto)):

            if texto[i].isdigit():
                self.salida_numerica += self.codigo[int(texto[i])]
            else:
                self.salida_numerica += texto[i]

        return self.salida_numerica

    def encriptar_numero(self, texto):
        n = int(1)

        for l in texto:
            # Si la letra está en el abecedario se reemplaza
            if l in self.abc:
                pos_letra = self.abc.index(l)
                # Sumamos para movernos a la derecha del abc
                nueva_pos = (pos_letra + n) % len(self.abc)
                self.salida_numerica += self.abc[nueva_pos]
            else:
                # Si no está en el abecedario sólo añadelo
                self.salida_numerica += l

        return self.salida_numerica

    def desencriptar_numero(self, texto):
        # Iteramos por posibles valores de desplazamiento
        for i in range(2):
            for l in texto:
                # Si la letra está en el abecedario reemplazamos
                if l in self.abc:
                    pos_letra = self.abc.index(l)
                    # Restamos para movernos a la izquierda
                    nueva_pos = (pos_letra - i) % len(self.abc)
                    self.salida_numerica += self.abc[nueva_pos]
                else:
                    self.salida_numerica += l

