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

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/especificacoes_produtos")
print('### Abrindo especificação do produto')
print('### Adicionar')
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/a').click()

nome_element = navegador.find_element(By.XPATH, '//*[@id="descricao"]')
nome_element.send_keys('Especificação Automática')
print('### Passei descrição especificação.')
print('Texto Curto (até 255 caracteres)')
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
sleep(2)
navegador.find_element(By.XPATH,'//*[@id="tipo"]').click()
pyautogui.hotkey('down')
pyautogui.hotkey('tab')
print('Texto Longo (sem limite de caracteres)')
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
sleep(2)
navegador.find_element(By.XPATH,'//*[@id="tipo"]').click()
pyautogui.hotkey('down')
pyautogui.hotkey('tab')
print('Número inteiro')
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
sleep(2)
navegador.find_element(By.XPATH,'//*[@id="tipo"]').click()
pyautogui.hotkey('down')
pyautogui.hotkey('tab')
print('Número decimal')
sleep(2)
nome_element = navegador.find_element(By.XPATH, '//*[@id="casas_decimais"]')
nome_element.send_keys('2')
print('### Passei 2 casas decimais')
sleep(3)
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
sleep(2)
navegador.find_element(By.XPATH,'//*[@id="tipo"]').click()
pyautogui.hotkey('down')
pyautogui.hotkey('tab')
print('Lista Pré-definida')
sleep(2)
nome_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_0"]')
nome_element.send_keys('Primeira opção')
print('### Passei primeira opção')
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/table/tfoot/tr/td/button').click()
sleep(2)
nome_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_1"]')
nome_element.send_keys('Segunda opção')
print('### Passei segunda opção')
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
sleep(2)
navegador.find_element(By.XPATH,'//*[@id="tipo"]').click()
pyautogui.hotkey('down')
pyautogui.hotkey('tab')
print('Sim/Não')
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
sleep(2)
navegador.find_element(By.XPATH,'//*[@id="tipo"]').click()
pyautogui.hotkey('down')
pyautogui.hotkey('tab')
print('Lista Pré-definida (Multiselect)')
sleep(2)
nome_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_0"]')
nome_element.send_keys('Primeira opção')
print('### Passei primeira opção')
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/table/tfoot/tr/td/button').click()
sleep(2)
nome_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_1"]')
nome_element.send_keys('Segunda opção')
print('### Passei segunda opção')
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
sleep(2)
navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/a[2]').click()
navegador.find_element(By.XPATH,'/html/body/div[8]/div/div/div[2]/button[2]').click()
print('Realizado exclusão de especificação do produto')































###########################################################################################################
#navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
#sleep(2)
#print('Texto Curto (até 255 caracteres)')
#navegador.find_element(By.XPATH,'//*[@id="tipo"]').click()
#pyautogui.hotkey('down')
#pyautogui.hotkey('tab')
#sleep(3)
###########################################################################################################
#navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
#sleep(1)
#navegador.find_element(By.XPATH,'//*[@id="tipo"]').click()
#pyautogui.hotkey('down')
#print('Texto Longo (sem limite de caracteres)')
#pyautogui.hotkey('tab')
#sleep(3)
###########################################################################################################
#navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
#sleep(2)
#navegador.find_element(By.XPATH,'//*[@id="tipo"]').click()
#pyautogui.hotkey('down')
#pyautogui.hotkey('tab')
#print('Número inteiro')
#navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
#sleep(3)
###########################################################################################################
#navegador.find_element(By.XPATH,'//*[@id="tipo"]').click()
#pyautogui.hotkey('down')
#pyautogui.hotkey('tab')
#print('Número decimal')
#print('cliquei')
#nome_element.send_keys('2')
#sleep(3)
#print('### Passei 2 casas decimais')
#navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
###########################################################################################################
#navegador.find_element(By.XPATH,'//*[@id="tipo"]').click()
#sleep(3)
#pyautogui.hotkey('down')
#pyautogui.hotkey('tab')
#print('Lista Pré-definida')
#nome_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_0"]')
#sleep(3)
#nome_element.send_keys('3')
#print('### Passei opção')
#navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[2]/div/div/table/tfoot/tr/td/button').click()
##navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
#sleep(3)
#nome_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_1"]')
#nome_element.send_keys('4')
#print('### Passei segunda opção')
#navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
#sleep(2)
#navegador.find_element(By.XPATH,'//*[@id="tipo"]').click()
#pyautogui.hotkey('down')
#pyautogui.hotkey('tab')
#print('Sim/Não')
#navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
#sleep(2)
#navegador.find_element(By.XPATH,'//*[@id="tipo"]').click()
#pyautogui.hotkey('down')
#pyautogui.hotkey('tab')
#print('Lista Pré-definida (Multiselect)')
#nome_element = navegador.find_element(By.XPATH, '//*[@id="item_especificacao_produto_descricao_0"]')
#sleep(2)
#nome_element.send_keys('3')
#print('### Passei opção')
#navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/input[2]').click()
#navegador.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/form/div[3]/div/a[2]').click()
