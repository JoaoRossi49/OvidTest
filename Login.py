from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest



def incluirLocal(_username, _password, unidadeTecnica, nomeLocal):
    
    try: 
        #Instancia webdriver e chama link de gestor
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://haishc2.famema.br")
        time.sleep(2)
        #Entra passando credenciais
        element = driver.find_element(By.ID, 'username')
        element.send_keys(_username)
        element = driver.find_element(By.ID, 'password')
        element.send_keys(_password)
        time.sleep(2)
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/button')
        if (len(element)> 0):
            return True
        else:
            return False
    except Exception as e: 
        return False