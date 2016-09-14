# coding=utf8

# Esqueleto de código Python para uso no Dojo-SE
# Escrito por Wagner Luís de Araújo Menezes Macêdo <wagnerluis1982@gmail.com>.
# 
# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest

def look_and_say(inicial):
    return 11

def descrever_numero(numero):
    retorno = ''
    contador = 1
    temp_char = ''
    n_str = str(numero)
    for algarismo in n_str:
        if (temp_char == ''):
            temp_char = algarismo
            #continue
        elif (temp_char == algarismo):
            contador += 1
            #continue
        else : 
            temp_char = algarismo
            retorno = retorno + str(contador) + temp_char
            contador = 1
            continue
    retorno = retorno + str(contador) + algarismo
    return int(retorno) 

class ProblemaParaResolverTest(unittest.TestCase):
    def test_simples(self):
        self.assertEqual(11, look_and_say(1))

    def test_descrever_numero_simples(self):
        self.assertEqual(11, descrever_numero(1))
        self.assertEqual(1112, descrever_numero(12))

    def test_descrever_numeros_diferentes(self):
        self.assertEqual(21, descrever_numero(11))

if __name__ == '__main__':
    unittest.main()