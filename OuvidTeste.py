from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import ouvidoria_test
import time
import unittest

class OuvidTeste(unittest.TestCase):

    # Happy path
    def CT0(self):
        result = ouvidoria_test.incluirLocal('601160', '601160', 2, 'LocalCT1')
        self.assertTrue(result)

    # Errar senha
    def CT1(self):
        result = ouvidoria_test.incluirLocal('601160', '601160', 2, 'LocalCT1')
        self.assertFalse(result)

    # Errar login
    def CT2(self):
        result = ouvidoria_test.incluirLocal('601160', '601160', 2, 'LocalCT1')
        self.assertFalse(result)

    # Incluir local com nome vazio
    def CT3(self):
        result = ouvidoria_test.incluirLocal('601160', '601160', 2, '')
        self.assertFalse(result)

    # Incluir local sem nome
    def CT4(self):
        result = result = ouvidoria_test.incluirLocal('601160', '601160', 2, '')
        self.assertFalse(result)

    # Incluir local sem unidade técnica
    def CT5(self):
        result = result = ouvidoria_test.incluirLocal('601160', '601160', 1, 'LocalCT4')
        self.assertFalse(result)

    # Incluir local com unidade técnica fora do dropList
    def CT6(self):
        result = result = ouvidoria_test.incluirLocal('601160', '601160', 7, 'LocalCT4')
        self.assertFalse(result)

    # Incluir local com mais de 20 caracteres
    def CT7(self):
        result = result = ouvidoria_test.incluirLocal('601160', '601160', 3, 'LocalCT7LocalCT7LocalCT7LocalCT7LocalCT7LocalCT7LocalCT7LocalCT7')
        self.assertTrue(result)

    # Incluir local com caracteres especiais
    def CT8(self):
        result = result = ouvidoria_test.incluirLocal('601160', '601160', 3, 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ')
        self.assertTrue(result)

    if __name__ == '__main__':
        unittest.main()
