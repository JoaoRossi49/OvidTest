from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from random import randint

def incluirLocal(_username, _password, unidadeTecnica, nomeLocal):
    try:
        # Instancia webdriver e chama link de gestor
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://g1.globo.com")
        time.sleep(2)

        # Entra passando credenciais
        element = driver.find_element(By.ID, 'username')
        element.send_keys(_username)
        element = driver.find_element(By.ID, 'password')
        element.send_keys(_password)
        time.sleep(2)

        element = driver.find_element(By.XPATH, '/html/body/div/div/form/button')
        element.click()
        time.sleep(5)

        # Clica no botão incluir novo local
        element = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div[1]/button')
        element.click()
        time.sleep(2)

        # Seleciona unidade técnica hci
        element = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div[2]/div[1]/div/div')
        element.click()
        element = driver.find_element(By.XPATH, f'//*[@id="menu-"]/div[3]/ul/li[{unidadeTecnica}]')
        element.click()

        # Seleciona input text field e envia nome do local
        element = driver.find_element(By.XPATH, '//*[@id="outlined-basic"]')
        element.send_keys(nomeLocal)
        time.sleep(2)

        # Salva novo local
        element = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div[2]/button[1]')
        time.sleep(1)
        element.click()
        time.sleep(1)
        alert = driver.find_element(By.CLASS_NAME, 'MuiAlert-message css-1xsto0d')
        print(alert.text)
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
    
def inserirRespostas(_local, _nome, _telefone):
     
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(f"https://cmdbackendtestehc.famema.br/{_local}")
        time.sleep(1)
        
        #Se identifica
        driver.find_element(By.XPATH, '/html/body/div/div/div/input[1]').send_keys(_nome)
        driver.find_element(By.XPATH, '/html/body/div/div/div/input[2]').send_keys(_telefone)
        driver.find_element(By.XPATH, '/html/body/div/div/div/img[2]').click()
        time.sleep(1)
        
        #Clica nas respostas
        for i in range (10):
            try:
                _avaliacao = randint(1,5)
                element = driver.find_element(By.XPATH, f'/html/body/div/div/div/div[{i+1}]/div/img[{_avaliacao}]')
                element.click()
            except:
                pass    
        driver.find_element(By.XPATH, '/html/body/div/div/div/button').click()
        time.sleep(3)
        return True
    except:
        return False
    
    
for i in range (250):
    inserirRespostas(161, '', '')
    print(f'Inclui a resposta nº{i} no local 161')
    inserirRespostas(162, '', '')
    print(f'Inclui a resposta nº{i} no local 162')
    inserirRespostas(163, '', '')
    print(f'Inclui a resposta nº{i} no local 163')