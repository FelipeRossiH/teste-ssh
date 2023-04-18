from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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

navegador = Firefox()
navegador.get(smart)
sleep(2)
hora_inicio = datetime.datetime.now()
print('### Navegador aberto em: ', hora_inicio)

usuario_element = navegador.find_element(By.NAME, 'usuario')
usuario_element.send_keys('robo.casa')
print('### Passei usuário.')

senha_element = navegador.find_element(By.NAME, 'senha').send_keys("Robo123" + Keys.ENTER)
print('### Passei senha.')

sleep(2)

pyautogui.hotkey('ENTER')
print('### Botão prosseguir Ok.')
sleep(2)

navegador.get(smart)

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendas")
print('### Acessei Tela de Vendas')

nome_element = navegador.find_element(By.ID, 'autocompletar_pessoa_cliente_fornecedor_id')
nome_element.send_keys('12546')
print('### Passei Cliente 12546.')
sleep(2)
pyautogui.hotkey('down')
pyautogui.hotkey('tab')
#pyautogui.hotkey('tab')

nome_element = navegador.find_element(By.ID, 'coluna_descricao_produto')
sleep(2)
nome_element.send_keys('7410')
print('### Passei produto.')
sleep(2)
pyautogui.hotkey('down')
pyautogui.hotkey('tab')
pyautogui.hotkey('ENTER')

sleep(3)
nome_element = navegador.find_element(By.ID, 'quantidade_local_estocagem_por_filial')
sleep(2)
nome_element.send_keys('1')
print('### Passei quantidade.')
pyautogui.hotkey('ENTER')

sleep(3)
#navegador.find_element(By.ID,'forma_pagamento_id_0').click()
nome_element = navegador.find_element(By.ID, 'forma_pagamento_id_0')
nome_element.send_keys('V')
sleep(2)
#pyautogui.hotkey('ENTER')
print('### Passei forma de pagamento carnê')

#sleep(2)
#navegador.find_element(By.XPATH,'//*[@id="parcela_0"]"]').click()
sleep(2)
nome_element = navegador.find_element(By.XPATH, '//*[@id="parcela_0"]')
sleep(2)
nome_element.send_keys('1')
pyautogui.hotkey('tab')
sleep(3)
print('### Passei quantidade de parcelas')

navegador.find_element(By.ID,'botao_salvar').click()
sleep(3)

navegador.find_element(By.ID,'login_liberacao_venda').click()
nome_element = navegador.find_element(By.ID, 'login_liberacao_venda')
nome_element.send_keys('robo.casa')
pyautogui.hotkey('tab')
print('### Passei usuário de liberação')

navegador.find_element(By.ID,'senha_liberacao_venda').click()
nome_element = navegador.find_element(By.ID, 'senha_liberacao_venda')
nome_element.send_keys('Robo123')
pyautogui.hotkey('tab')
print('### Passei senha de liberação')
pyautogui.hotkey('ENTER')

hora_fim = datetime.datetime.now()
print('Fim de execução: ', hora_fim)
tempo_total = (hora_fim - hora_inicio)
