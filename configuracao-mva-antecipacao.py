import pyautogui, sys
import pyperclip
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep
from datetime import datetime
import clipboard
import datetime
import os



smart = 'https://felipe.testes.smart.sgisistemas.com.br/'
#smart_home = 'https://felipe.testes.smart.sgisistemas.com.br/'
cont = 0
erro = 0
hora_inicio = datetime.datetime.now()


navegador = Firefox()
navegador.get(smart)
sleep(2)
print('### Navegador aberto.')
print('Início de execução: ', hora_inicio)

usuario_element = navegador.find_element(By.NAME, 'usuario')
usuario_element.send_keys('robo.casa')
print('### Passei usuário.')

senha_element = navegador.find_element(By.NAME, 'senha').send_keys("Robo123" + Keys.ENTER)
print('### Passei senha.')

sleep(2)

pyautogui.hotkey('ENTER')
print('### Botão prosseguir Ok.')
sleep(2)

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_mva_antecipacoes")
print('### Configuração MVA Antecipação (%)')

navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()

navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div/button').click()
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div/ul/li[3]/a/label/input').click()
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div/ul/li[4]/a/label/input').click()
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[1]/div/div/ul/li[5]/a/label/input').click()

nome_element = navegador.find_element(By.XPATH, '//*[@id="autocompletar_produtos"]')
nome_element.send_keys('7410')
print('### Passei produto.')
sleep(2)
pyautogui.hotkey('down')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

nome_element = navegador.find_element(By.XPATH, '//*[@id="percentual_mva_antecipacao"]')
nome_element.send_keys('100')
print('### Passei % de MVA Antecipação.')
sleep(1)
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[5]/div/input[2]').click()
sleep(2)
nome_element = navegador.find_element(By.XPATH, '//*[@id="percentual_mva_antecipacao"]')
nome_element.send_keys('0')
print('### Passei % de MVA Antecipação alterado.')
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[5]/div/input[1]').click()
sleep(2)
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[1]/a').click()
sleep(2)
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[5]/div/a[2]').click()
navegador.find_element(By.XPATH,'/html/body/div[8]/div/div/div[2]/button[2]').click()
print('### Excluído cadastro')
sleep(2)
