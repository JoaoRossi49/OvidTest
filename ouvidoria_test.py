from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

def incluirLocal(_username, _password, unidadeTecnica, nomeLocal):
    try:
        # Instancia webdriver e chama link de gestor
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://haishc2.famema.br")
        time.sleep(2)

        # Entra passando credenciais
        element = driver.find_element(By.ID, 'username')
        element.send_keys(_username)
        element = driver.find_element(By.ID, 'password')
        element.send_keys(_password)
        time.sleep(2)

        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/button')
        element.send_keys(Keys.ENTER)
        time.sleep(5)

        # Clica no botão incluir novo local
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div[2]/div[1]/button')
        element.click()
        time.sleep(2)

        # Seleciona unidade técnica hci
        element = driver.find_element(By.XPATH, '//*[@id="demo-simple-select"]')
        element.click()
        element = driver.find_element(By.XPATH, f'//*[@id="menu-"]/div[3]/ul/li[{unidadeTecnica}]')
        element.click()

        # Seleciona input text field e envia nome do local
        element = driver.find_element(By.XPATH, '//*[@id="outlined-basic"]')
        element.send_keys(nomeLocal)
        time.sleep(2)

        # Salva novo local
        element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div[2]/button[1]')
        time.sleep(1)
        element.click()
        time.sleep(1)
        return True
    except:
        return False

def Login(_username, _password, unidadeTecnica, nomeLocal):
    
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