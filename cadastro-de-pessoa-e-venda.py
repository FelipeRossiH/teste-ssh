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


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pessoas/new")
print('### Acessei Tela Pessoa')
print('### Abrindo Gerador de CPF. ')
url = 'https://www.4devs.com.br/gerador_de_cpf'
print('#### Aguardando ...')
browser = Firefox()
browser.get(url)
print('### Novo navegador aberto.\n#### Gerador de CPF\n##### 3 segundos para prosseguir')
sleep(3)
browser.find_element(By.ID,'bt_gerar_cpf').click()
browser.find_element(By.ID,'texto_cpf').click()

browser.find_element(By.CLASS_NAME, "clipboard-copy").click()


print('### CPF copiado.')
CPFcopiado = clipboard.paste()

sleep(2)
browser.close()
print('### Gerador de CPF encerrado.')


nome_element = navegador.find_element(By.NAME, 'pessoa[nome]')
nome_element.send_keys('Nome automatizado')
print('### Passei nome.')

nome_element = navegador.find_element(By.NAME, 'pessoa[apelido]')
nome_element.send_keys('Apelido automatizado')
print('### Passei apelido.')

sleep(2)
navegador.find_element(By.NAME,'pessoa[cpf_cnpj]').click()
pyautogui.hotkey('ctrl','v')
sleep(3)
print('### CPF inserido: ', CPFcopiado)

nome_element = navegador.find_element(By.NAME, 'pessoa[data_nascimento_fundacao]')
nome_element.send_keys('19/02/1990')
print('### Passei data de nascimento.')

navegador.find_element(By.NAME,'pessoa[identidade]')

elemento = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[17]/ul/li[2]/a')
sleep(3)
elemento.click()
sleep(2)


navegador.find_element(By.ID,'tipo_endereco_id_0').click()
nome_element = navegador.find_element(By.ID, 'tipo_endereco_id_0')
nome_element.send_keys('R')
print('### Passei tipo de endereço.')

nome_element = navegador.find_element(By.ID, 'autocompletar_cep_id_0')
nome_element.send_keys('89805-545')
print('### Passei CEP.')
sleep(2)
pyautogui.hotkey('down')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

nome_element = navegador.find_element(By.ID, 'numero_0')
nome_element.send_keys('322')
print('### Passei número de endereço.')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('down')

elemento = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/form/div[19]/div/input[2]')
elemento.click()
hora_fim = datetime.datetime.now()
print('Fim de execução: ', hora_fim)
tempo_total = (hora_fim - hora_inicio)
sleep(2)


print('###### Pessoa física cadastrada com sucesso\n##### CPF cadastrado: ', CPFcopiado, 'Tempo de execução: ', tempo_total)

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
navegador.find_element(By.ID,'forma_pagamento_id_0').click()
nome_element = navegador.find_element(By.ID, 'forma_pagamento_id_0')
nome_element.send_keys('V')
sleep(2)
pyautogui.hotkey('ENTER')
print('### Passei forma de pagamento carnê')

sleep(2)
navegador.find_element(By.XPATH,'//*[@id="forma_pagamento_id_0"]').click()
sleep(2)
nome_element = navegador.find_element(By.XPATH, '//*[@id="parcela_0"]')
sleep(2)
nome_element.send_keys('0')
pyautogui.hotkey('tab')
sleep(3)
print('### Passei forma de pagamento carnê')

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
