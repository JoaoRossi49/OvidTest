import ouvidoria_test
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

class OuvidTest(unittest.TestCase):
    
    # Happy path
    def test_happyPath(self):
        result = ouvidoria_test.incluirLocal('paulo.otero', '123', 2, 'LocalCT1')
        self.assertTrue(result)
        
    # Errar senha
    def test_errarSenha(self):
        result = ouvidoria_test.Login('paulo.otero', '12')
        self.assertFalse(result)
        
    # Errar login
    def test_errarLogin(self):
        result = ouvidoria_test.Login('paulo.otero', '123')
        self.assertFalse(result)
        
    # Incluir local com nome vazio
    def test_nomeEspaco(self):
        result = ouvidoria_test.incluirLocal('paulo.otero', '123', 2, ' ')
        self.assertFalse(result)
        
    # Incluir local sem nome
    def test_nomeVazio(self):
        result =  ouvidoria_test.incluirLocal('paulo.otero', '123', 2, '')
        self.assertFalse(result)
        
    # Incluir local sem unidade técnica
    def test_semUnidadetécnica(self):
        result =  ouvidoria_test.incluirLocal('paulo.otero', '123', 1, 'LocalCT4')
        self.assertFalse(result)
        
    # Incluir local com unidade técnica fora do dropList
    def test_foraDroplist(self):
        result =  ouvidoria_test.incluirLocal('paulo.otero', '123', 7, 'LocalCT4')
        self.assertFalse(result)
        
    # Incluir local com caracteres especiais e acima de 20 caracteres
    def test_estouroCaracteres(self):
        result = ouvidoria_test.incluirLocal('paulo.otero', '123', 3, 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåçèéêëìíîïðñòóôõö÷øùúûüýþÿ')
        self.assertTrue(result)
        
        
if __name__ == '__main__':
    unittest.main()
