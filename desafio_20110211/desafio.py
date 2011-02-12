"""
Desafio PUG-PE  
ID: 1
Semana: 11/02/2011

Problema:

    Dado uma lista de elementos, o objetivo eh converter esta lista em uma lista de sub-listas de elementos consecutivos duplicados.
    Assim que um elemento subsequente for diferente do anterior, a sublista eh gerada e passa para o proximo elemento. Entao 
    no exemplo abaixo dado 5 a's quando encontrar um b ele gera a sublista de 5 a's e comeca a gerar a sublista de b's ate encontrar um
    elemento que nao seja b, e assim sucessivamente. 
    >>> x = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
    >>> ret = pack(x)
    >>> ret
    >>> [['a','a','a','a','a','a'],['b'],['c','c'],['d'],['e','e','e','e']]
    >>> x = ['a', 'b', 'c']
    >>> ret = pack(x)
    >>> ret 
    >>>[['a'], ['b'], ['c']]
    >>> x = []
    >>> ret = pack(x)
    >>> ret
    >>> []
     
  Seu trabalho eh construir essa lista de elementos.  Favor utilizar Testes usando doctest ou UnitTest para validar sua solucao.

"""

import unittest

def pack(l):
    nl = {}
    for elem in l:
        if elem in nl:
            nl[elem] += [elem]
        else:
            nl[elem] = [elem]
    return [v for v in sorted(nl.values())]


class Desafio1(unittest.TestCase):

    def test_lista_simples(self):
        self.assertEquals([], pack([]))

    def test_lista_um_elemento(self):
        self.assertEquals([[1]], pack([1]))

    def test_lista_dois_elementos_diferentes(self):
        self.assertEquals([[1], [2]], pack([1, 2]))

    def test_lista_dois_elementos_iguais(self):
        self.assertEquals([[1, 1]], pack([1, 1]))

    def test_lista_dois_tipos_distintos(self):
        self.assertEquals([[1, 1], [2, 2]], pack([1, 2, 1, 2]))

    def test_lista_tres_tipos_distintos(self):
        self.assertEquals([['a'], ['b'], ['c']], pack(['a', 'b', 'c']))

    def test_lista_desordenada(self):
        self.assertEquals([['a', 'a'], ['b', 'b'], ['c', 'c']], pack(['b','c', 'a', 'b', 'a', 'c']))

    def test_pack_duplicates(self):
        sampleList = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
        self.assertEqual([['a','a','a','a','a','a'],['b'],['c','c'],['d'],['e','e','e','e']],
                    pack(sampleList))


if __name__ == '__main__':
    unittest.main()    
