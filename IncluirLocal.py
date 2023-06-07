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
        element.send_keys(Keys.ENTER)
        time.sleep(5)
        #Clica no botão incluir novo local
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div[2]/div[1]/button')
        element.click()
        time.sleep(2)
        #Seleciona unidade técnica hci
        element = driver.find_element(By.XPATH, '//*[@id="demo-simple-select"]')
        element.click()
        element = driver.find_element(By.XPATH, f'//*[@id="menu-"]/div[3]/ul/li[{unidadeTecnica}]') 
        element.click()
        #Seleciona inputtextfield e envia nome de local
        element = driver.find_element(By.XPATH, '//*[@id="outlined-basic"]')
        element.send_keys(nomeLocal)
        time.sleep(2)
        #Salva novo local
        element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div[2]/button[1]') 
        time.sleep(2)
        element.click()
        time.sleep(2)
        element.find_element(By.CLASS_NAME, 'MuiTypography-root MuiTypography-h2 css-qu1qus')
        print(f'Tag name: {element.tag_name}') 
        print(f'Text name: {element.text}')
        print(f'Role: {element.aria_role}') 
        if (element.text == 'Selecione uma Unidade e informe um nome para o Local!'):
            return False
        else:
            return True
    except Exception as e: 
        return False
    
incluirLocal('600028', '123', '2', ' ')