from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import IncluirLocal
import time
import unittest




class OuvidTeste(unittest.TestCase):
    
    def test_incluirLocal(self):
        result = IncluirLocal.incluirLocal('600028', '123', 2, 'Local CT1' )
        self.assertTrue
        
    def test_incluirLocalTypo(self):
        result = IncluirLocal.incluirLocal('600028', '123', 2, ' ' )
        self.assertFalse
        
    def test_incluirLocalSemNome(self):
        result = result = IncluirLocal.incluirLocal('600028', '123', 2, '' )
        self.assertFalse
        
    def test_incluirLocalSemUndTec(self):
        result = result = IncluirLocal.incluirLocal('600028', '123', 1, 'Local CT4' )
        self.asserTrue
        
    def test_incluirLocalInfinito(self):
        result = result = IncluirLocal.incluirLocal('600028', '123', 3, 'Local CT5 Local CT5 Local CT5 Local CT5 Local CT5 Local CT5 Local CT5 Local CT5 Local CT5' )
        self.assertFalse    
        
        
if __name__ == '__main__':
    unittest.main()