from unittest import TestCase

from dominio import Usuario, Leilao, Avaliador, Lance


class TestAvaliador(TestCase):

    def test_avalia(self):
        carolina = Usuario('carolina')
        catarina = Usuario('catarina')

        leilao = Leilao("Fogão Brastemp 6 bocas")

        carolina_lance = Lance(carolina, 150.0)
        catarina_lance = Lance(catarina, 100.0)

        leilao.lances.append(catarina_lance)
        leilao.lances.append(carolina_lance)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEquals(menor_valor_esperado, avaliador.menor_lance)
        self.assertEquals(maior_valor_esperado, avaliador.maior_lance)
