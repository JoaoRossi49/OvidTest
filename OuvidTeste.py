import ouvidoria_test
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

class OuvidTest(unittest.TestCase):
    # Happy path
    def test_CT0(self):
        result = ouvidoria_test.incluirLocal('600028', '123', 2, 'LocalCT1')
        self.assertTrue(result)
    # Errar senha
    def test_CT1(self):
        result = ouvidoria_test.incluirLocal('600028', '12', 2, 'LocalCT1')
        self.assertFalse(result)
    # Errar login
    def test_CT2(self):
        result = ouvidoria_test.incluirLocal('6000228', '123', 2, 'LocalCT1')
        self.assertFalse(result)
    # Incluir local com nome vazio
    def test_CT3(self):
        result = ouvidoria_test.incluirLocal('600028', '123', 2, ' ')
        self.assertFalse(result)
    # Incluir local sem nome
    def test_CT4(self):
        result =  ouvidoria_test.incluirLocal('600028', '123', 2, '')
        self.assertFalse(result)
    # Incluir local sem unidade técnica
    def test_CT5(self):
        result =  ouvidoria_test.incluirLocal('600028', '123', 1, 'LocalCT4')
        self.assertFalse(result)
    # Incluir local com unidade técnica fora do dropList
    def test_CT6(self):
        result =  ouvidoria_test.incluirLocal('600028', '123', 7, 'LocalCT4')
        self.assertFalse(result)
    # Incluir local com caracteres especiais e acima de 20 caracteres
    def test_CT8(self):
        result = ouvidoria_test.incluirLocal('600028', '123', 3, 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåçèéêëìíîïðñòóôõö÷øùúûüýþÿ')
        self.assertTrue(result)
        
        
if __name__ == '__main__':
    unittest.main()
