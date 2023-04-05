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

usuario_element = navegador.find_element(By.NAME, 'usuario')
usuario_element.send_keys('robo.casa')
print('### Passei usuário.')

senha_element = navegador.find_element(By.NAME, 'senha').send_keys("Robo123" + Keys.ENTER)
print('### Passei senha.')

sleep(2)

pyautogui.hotkey('ENTER')
print('### Botão prosseguir Ok.')
sleep(2)

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pessoas")
print('### Abrindo cadastro de pessoas')
error_message = navegador.find_elements(By.NAME,"filtros[nome]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

#sleep(2)
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/produtos")
print('### Abrindo cadastro de produtos')
error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

sleep(2)
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/empresas/1/edit")
print('### Acessei configurações da empresa')

error_message = navegador.find_elements(By.NAME,"pessoa[nome]")
if error_message:
    print("A página foi aberta")
    navegador.find_element(By.NAME,"commit").click()
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
sleep(3)
cont = cont +1

sleep(2)
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_inventarios")
print('### Acessei Relatório de Inventário')

error_message = navegador.find_elements(By.NAME,"filtros[numero_ncm]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_precos_produtos")
print('### Acessei Relatório de Preços de Produto')

error_message = navegador.find_elements(By.NAME,"filtros[status_produto]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/exportacoes_sef")
print('### Acessei SEF II')

error_message = navegador.find_elements(By.NAME,"exportacao_sef[data_base]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/demonstracoes")
print('### Acessei Demonstração de Produto')

error_message = navegador.find_elements(By.NAME,"filtros[pessoas.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/entradas_manuais")
print('### Acessei Entrada Manual')

error_message = navegador.find_elements(By.ID,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tabelas_fretes")
print('### Acessei Tabela de Frete')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_orcamentos")
print('### Acessei Relatório de Orçamentos')

error_message = navegador.find_elements(By.NAME,"filtros[detalhamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_integracoes_servicos")
print('### Acessei Log de Integração Serviços')

error_message = navegador.find_elements(By.NAME,"filtros[lancamento_documento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/escolaridades")
print('### Acessei Escolaridade')

error_message = navegador.find_elements(By.NAME,"filtros[escolaridades.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_dependentes")
print('### Acessei Tipo de Dependente')

error_message = navegador.find_elements(By.NAME,"filtros[tipos_dependentes.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_mva_antecipacoes")
print('### Acessei Configuração MVA Antecipação (%)')

error_message = navegador.find_elements(By.NAME,"filtros[escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_tipos_servicos")
print('### Acessei Configuração por Tipo de Serviço')

error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/especificacoes_produtos")
print('### Acessei Especificação do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_tipos_montagens_produtos")
print('### Acessei Configuração de Tipo de Montagem por Produto')

error_message = navegador.find_elements(By.NAME,"filtros[escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/atualizacoes_codigos_pessoas")
print('### Acessei Atualização de Código de Pessoas')

error_message = navegador.find_elements(By.ID,"gerar_codigo_automaticamente")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_servicos")
print('### Acessei Definição de Serviço')

error_message = navegador.find_elements(By.ID,"servicos.descricao_ilike")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/atualizacoes_automaticas_precos")
print('### Acessei Atualizações Automáticas de Tabela de Preço')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_variacoes_grades")
print('### Acessei Grupo Variações de Grade')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/variacoes_grades")
print('### Acessei Variações de Grade')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/designers_produtos")
print('### Acessei Designer do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_encomendas_produtos")
print('### Acessei Configuração de Encomenda de Produtos')

error_message = navegador.find_elements(By.NAME,"commit")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/mva")
print('### Acessei MVA')

error_message = navegador.find_elements(By.NAME,"filtros[produtos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cores_produtos")
print('### Acessei Cor')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/unidades_medidas")
print('### Acessei Unidade de Medida')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/origens_produtos")
print('### Acessei Origem do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[numero]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/marcas_produtos")
print('### Acessei Marca do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/subgrupos_produtos")
print('### Acessei Subgrupo do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/grupos_produtos")
print('### Acessei Grupo do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/departamentos_produtos")
print('### Acessei Departamento do Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/profissoes")
print('### Acessei Profissão')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/meios_contatos")
print('### Acessei Meio de Contato')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_referencias")
print('### Acessei Tipo de Referência')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/servicos")
print('### Acessei Serviço')

error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/kits_produtos")
print('### Acessei Kit de Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/kits_produtos")
print('### Acessei Kit de Produto')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_analises_compras")
print('### Acessei Relatório de Análise de Compras')

error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/baixar_xmls_mdfe")
print('### Acessei Baixar XML de MDF-e')

error_message = navegador.find_elements(By.NAME,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_detalhamentos_custos")
print('### Acessei Relatório de Detalhamento de Custo')

error_message = navegador.find_elements(By.NAME,"filtros[filial_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/definicoes_liberacoes_pedidos_compras")
print('### Acessei Configuração de Liberação do Pedido de Compra')

error_message = navegador.find_elements(By.ID,"titulo_campo_tipos_pedidos_compras_ids")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_pedidos_compras")
print('### Acessei Relatório de Pedido de Compra')

error_message = navegador.find_elements(By.NAME,"filtros[data_inclusao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_cooperados")
print('### Acessei Relatório de Cooperado')

error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_entradas")
print('### Acessei Relatório de Documentos de Entrada')

error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/encomendas_produtos")
print('### Acessei Encomenda de Produtos')

error_message = navegador.find_elements(By.NAME,"filtros[encomendas_produtos.created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/controles_impressoes_etiquetas")
print('### Acessei Controle de Impressão de Etiquetas')

error_message = navegador.find_elements(By.NAME,"configuracao_impressao_etiqueta_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/impressoes_etiquetas")
print('### Acessei Impressão de Etiquetas')

error_message = navegador.find_elements(By.NAME,"impressao_etiqueta[configuracao_impressao_etiqueta_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/importacoes_xml_nfe")
print('### Acessei Importação do XML da NF-e')

error_message = navegador.find_elements(By.NAME,"filtros[filtro_nome_fornecedor]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/xml_sefaz")
print('### Acessei Baixar XML de Documentos')

error_message = navegador.find_elements(By.NAME,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cancelamento_documentos")
print('### Acessei Cancelamento de Documentos')

error_message = navegador.find_elements(By.NAME,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/devolucoes_documentos")
print('### Acessei Devolução')

error_message = navegador.find_elements(By.ID,"autocompletar_numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/documentos")
print('### Acessei Documentos')

error_message = navegador.find_elements(By.NAME,"filtros[cliente_fornecedor.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/estoques_minimos_ecommerces")
print('### Acessei Estoque Mínimo do E-commerce')

error_message = navegador.find_elements(By.NAME,"filtros[escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_ecommerces")
print('### Acessei Log do E-commerce')

error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/gestoes_ecommerces")
print('### Acessei Gestão E-commerce')

error_message = navegador.find_elements(By.NAME,"filtros[pedidos_ecommerces.id_pedido_ecommerce]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/produtos_ecommerces")
print('### Acessei Produto E-commerce')

error_message = navegador.find_elements(By.NAME,"filtros[produtos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/distribuicoes_mercadorias")
print('### Acessei Distribuição de Mercadoria')

error_message = navegador.find_elements(By.ID,"autocompletar_filial_entrega_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_enderecamentos_estoques")
print('### Acessei Relatório de Endereçamento de Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[detalhamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/movimentacoes_niveis_enderecamentos")
print('### Acessei Produto por Endereçamento')

error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/enderecamentos")
print('### Acessei Níveis de Endereçamento')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1




navegador.get("https://felipe.testes.smart.sgisistemas.com.br/auditorias_estoques")
print('### Acessei Auditoria de Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_encomendas_produtos")
print('### Acessei Relatório de Encomendas')

error_message = navegador.find_elements(By.NAME,"filtros[data_encomenda_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/gestoes_montagens")
print('### Acessei Gestão de Montagem')

error_message = navegador.find_elements(By.NAME,"filtros[previsao_montagem_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/romaneios_montagens")
print('### Acessei Romaneio de Montagem')

error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_razoes_locais_estocagens")
print('### Acessei Relatório Razão de Produto por Local de Estocagem')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_razoes_locais_estocagens")
print('### Acessei Relatório Razão de Produto por Local de Estocagem')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/distribuicoes_estoques")
print('### Acessei Relatório de Distribuição de Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[exibir_estoque_detalhado]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_entregas_transportador")
print('### Acessei Relatório de Entregas por Transportador')

error_message = navegador.find_elements(By.NAME,"filtros[data_venda_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/tipos_ordens_servicos")
print('### Acessei Tipo de Assistência Técnica')

error_message = navegador.find_elements(By.ID,"descricao_ilike")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/escopos_configuracoes_custos")
print('### Acessei Configurações de Custo')

error_message = navegador.find_elements(By.NAME,"filtros[escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_movimentacoes_codigos_unicos")
print('### Acessei Relatório de Movimentações dos Códigos Únicos')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/codigos_unicos")
print('### Acessei Código Único')

error_message = navegador.find_elements(By.NAME,"filtros[produtos.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_codigos_unicos")
print('### Acessei Configuração de Código Único')

error_message = navegador.find_elements(By.NAME,"filtros[definicao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ordens_servicos_documentos")
print('### Acessei Assistência Técnica a partir do Documento')

error_message = navegador.find_elements(By.ID,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ordens_servicos")
print('### Acessei Assistência Técnica')

error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/entregas_montagens")
print('### Acessei Controle de Agendamento de Serviços')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_estoque_minimo_maximo")
print('### Acessei Relatório De Estoque Mínimo/Máximo')

error_message = navegador.find_elements(By.NAME,"filtros[agrupamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1



navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_razoes_produtos")
print('### Acessei Relatório Razão de Produtos')

error_message = navegador.find_elements(By.NAME,"filtros[ativo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_giros_estoques")
print('### Acessei Relatório de Giro Médio do Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[opcoes]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_posicao_estoque")
print('### Acessei Relatório de Posição do Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[tipo_valor]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_auditorias_estoques_produtos")
print('### Acessei Relatório de Auditoria do Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[filial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_transferencias_mercadorias")
print('### Acessei Relatório de Transferência de Mercadoria')

error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/reservas_produtos")
print('### Acessei Gestão de Entrega')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_produto]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/romaneios_separacoes")
print('### Acessei Romaneio de Separação')

error_message = navegador.find_elements(By.NAME,"filtros[id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/auditorias_estoques_configuracoes")
print('### Acessei Configuração Auditoria de Estoque')

error_message = navegador.find_elements(By.ID,"autocompletar_operacao_documento_entrada_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/conferencias_entradas_transferencias")
print('### Acessei Conferência de Entrada por Transferência')

error_message = navegador.find_elements(By.NAME,"filial_destino")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/transferencias_mercadorias")
print('### Acessei Transferência de Mercadoria')

error_message = navegador.find_elements(By.NAME,"filtros[documentos_saidas.numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/parametros_transferencias_mercadorias")
print('### Acessei Parâmetro para Transferência de Mercadoria')

error_message = navegador.find_elements(By.NAME,"filtros[filial_origem.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/requisicoes_mercadorias")
print('### Acessei Requisição de Mercadorias')

error_message = navegador.find_elements(By.ID,"autocompletar_filial_origem_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/movimentacoes_locais_estocagens")
print('### Acessei Movimentação Local de Estocagem')

error_message = navegador.find_elements(By.NAME,"filtros[locais_estocagens.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/locais_estocagens")
print('### Acessei Local de Estocagem')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/fechamentos_estoques")
print('### Acessei Fechamento de Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[filiais.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/estoques_minimo_maximo")
print('### Acessei Estoque Mínimo/Máximo')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/consulta_estoques")
print('### Acessei Consulta de Estoque')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/simulacoes_guias_icms")
print('### Acessei Simulação de Guias de ICMS e ICMS ST')

error_message = navegador.find_elements(By.NAME,"nao_considerar")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_nfe_inutilizadas")
print('### Acessei Relatório de Notas Inutilizadas')

error_message = navegador.find_elements(By.NAME,"filtros[data_inutilizacao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_contabilizacao")
print('### Acessei Relatório de Contabilização')

error_message = navegador.find_elements(By.NAME,"filtros[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/guias_icms_st")
print('### Acessei Guia de Imposto')

error_message = navegador.find_elements(By.NAME,"filtros[tipo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/nf_complementar")
print('### Acessei NF-e Complementar')

error_message = navegador.find_elements(By.NAME,"nf_complementar[tipo_nfe]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/exportacoes_xml_nfe")
print('### Acessei Exporta XML NF-e e NFC-e')

error_message = navegador.find_elements(By.NAME,"exporta_xml_nfe[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sintegra")
print('### Acessei SINTEGRA')

error_message = navegador.find_elements(By.NAME,"sintegra[finalidade_arquivo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sped")
print('### Acessei SPED Fiscal')

error_message = navegador.find_elements(By.NAME,"sped[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/inutilizacao_nfe")
print('### Acessei Inutilização NF-e')

error_message = navegador.find_elements(By.NAME,"filtros[numero_nfe_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/simples_remessa")
print('### Acessei Simples Remessa')

error_message = navegador.find_elements(By.ID,"autocompletar_numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sped_contribuicoes")
print('### Acessei SPED Contribuições')

error_message = navegador.find_elements(By.NAME,"sped[data_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_ecommerces")
print('### Acessei Configuração E-commerce')

error_message = navegador.find_elements(By.NAME,"configuracao_ecommerce[tipo_integracao]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_integracoes_ecommerces")
print('### Acessei Log de Integração do E-commerce')

error_message = navegador.find_elements(By.NAME,"filtros[id_pedido_ecommerce]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/entrada")
print('### Acessei Entrada')

error_message = navegador.find_elements(By.ID,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/sugestoes_compras")
print('### Acessei  Sugestão de Compra')

error_message = navegador.find_elements(By.NAME,"filtros[tipo_custo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pedidos_compras")
print('### Acessei Pedido de Compra')

error_message = navegador.find_elements(By.NAME,"filtros[fornecedores.nome_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cartas_correcoes_documentos")
print('### Acessei Carta de Correção NF')

error_message = navegador.find_elements(By.NAME,"filtros[documentos.numero_lancamento]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

navegador.get("https://felipe.testes.smart.sgisistemas.com.br/juros")
print('### Acessei Juros')

error_message = navegador.find_elements(By.NAME,"filtros[quantidade_dias_atraso_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/pedidos_ecommerces")
print('### Acessei Pedidos E-commerce')

error_message = navegador.find_elements(By.NAME,"filtros[id_pedido_ecommerce]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/csosn_icms")
print('### Acessei CSOSN ICMS')

error_message = navegador.find_elements(By.NAME,"filtros[numero_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/importacoes")
print('### Acessei Importações')

error_message = navegador.find_elements(By.ID,"email_envio_log")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/situacoes")
print('### Acessei Situações')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/situacoes")
print('### Acessei Situações')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/cobrancas_clientes")
print('### Acessei Controle de Cobrança por Cliente')

error_message = navegador.find_elements(By.NAME,"filtros[cobranca_id]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/contas_correntes_colaboradores")
print('### Acessei Conta Corrente do Colaborador')

error_message = navegador.find_elements(By.NAME,"filtros[colaboradores.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_vtex_tracking")
print('### Acessei Configuração VTEX Tracking')

error_message = navegador.find_elements(By.NAME,"configuracao_vtex_tracking[usuario]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/importacoes_integracoes_financeiras")
print('### Acessei Importação Integração Financeira')

error_message = navegador.find_elements(By.NAME,"filtros[nome_arquivo_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_impressoes_etiquetas")
print('### Acessei Configuração de Impressão de Etiquetas')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vinculos_contas_ordens")
print('### Acessei Vínculo de Conta e Ordem')

#error_message = navegador.find_elements(By.CLASS,"btn btn-success")
#if error_message:
#    print("A página foi aberta")
#else:
erro = erro+1
print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/xml_cte")
print('### Acessei Importação de XML CT-e')

error_message = navegador.find_elements(By.NAME,"filtros[data_lancamento_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/integracoes_losango_r0011_produtos")
print('### Acessei Tabela de Integração Losango R0011')

error_message = navegador.find_elements(By.NAME,"Tabela de Integração Losango R0011")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/odts")
print('### Acessei ODT')

error_message = navegador.find_elements(By.NAME,"filtros[_exibicao_ordenacao_consulta]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/vendas")
print('### Acessei Pedido de Venda')

error_message = navegador.find_elements(By.ID,"numero_lancamento")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/exposicoes")
print('### Acessei Exposição')

error_message = navegador.find_elements(By.NAME,"filtros[filial_exposicao.descricao_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/orcamento/orcamentos")
print('### Acessei Exposição')

error_message = navegador.find_elements(By.NAME,"filtros[descricao_contato]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/recuperacoes_servicos")
print('### Acessei Exposição')

error_message = navegador.find_elements(By.ID,"autocompletar_filtro_documento_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/ordens_entregas")
print('### Acessei Controle de Ordem de Entrega')

error_message = navegador.find_elements(By.NAME,"filtros[clientes.codigo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_locais_estocagens_entregas")
print('### Acessei Configuração de Local de Estocagem para Entrega')

error_message = navegador.find_elements(By.ID,"filial_id")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas")
print('### Acessei Relatório de Documentos de Saída')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas_por_itens")
print('### Acessei Relatório de Documentos de Saída por Item')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas_vendedores")
print('### Acessei Relatório de Documentos de Saída - Vendedor')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas_fornecedores")
print('### Acessei Relatório Documentos de Saída - Fornecedor')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_documentos_saidas_fornecedores")
print('### Acessei Relatório Documentos de Saída - Fornecedor')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/logs_importacoes_bancarias_automaticas")
print('### Acessei Log de importação bancária automática')

error_message = navegador.find_elements(By.NAME,"filtros[created_at_maior_igual]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/conferencias_movimentacoes_diversas")
print('### Acessei Conferência de Movimentações Diversas')

error_message = navegador.find_elements(By.NAME,"filtros[movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_recebimentos")
print('### Acessei Relatório de Recebimentos')

error_message = navegador.find_elements(By.NAME,"filtros[data_movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/importacoes_conciliacoes_bancarias")
print('### Acessei Importação Conciliação Bancária')

error_message = navegador.find_elements(By.NAME,"filtros[nome_arquivo_ilike]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/categorias_lancamentos_bancarios")
print('### Acessei Categoria de Lançamento Bancário')

error_message = navegador.find_elements(By.NAME,"filtros[codigo]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_conciliacoes_bancarias")
print('### Acessei Configuração da Conciliação Bancária')

error_message = navegador.find_elements(By.ID,"endereco_webservice")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/configuracoes_contas_correntes_colaboradores")
print('### Acessei Configuração da Conta Corrente do Colaborador')

error_message = navegador.find_elements(By.NAME,"filtros[escopo_type]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_contas_correntes_colaboradores")
print('### Acessei Relatório de Conta Corrente do Colaborador')

error_message = navegador.find_elements(By.NAME,"filtros[valor_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/controle_pdds")
print('### Acessei Controle de PDD')

error_message = navegador.find_elements(By.NAME,"filtros[data_emissao_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1


navegador.get("https://felipe.testes.smart.sgisistemas.com.br/relatorio_historicos_por_centro_custo")
print('### Acessei Relatório de Históricos por Centro de Custo')

error_message = navegador.find_elements(By.NAME,"filtros[data_movimento_inicial]")
if error_message:
    print("A página foi aberta")
else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1





################################################################################
navegador.get("https://felipe.testes.smart.sgisistemas.com.br/home")
print('### Acessei Tela Inicial')

error_message = navegador.find_elements(By.ID,"botao_perfil_barra_menu")
if error_message:
    print("O menu foi aberto")
    navegador.find_element(By.ID,"botao_perfil_barra_menu").click()
    navegador.find_element(By.ID,"botao_sair_perfil_menu").click()
    print("Encerrado")

else:
    erro = erro+1
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>  A PÁGINA CONTÉM ERRO")
cont = cont +1

hora_fim = datetime.datetime.now()
tempo_total = (hora_fim - hora_inicio)
print("-------------------------------------")
print("Robô iniciado em ", hora_inicio)
print("Robô finalizado em ", hora_fim)
print("Tempo de execução", tempo_total)
print("Quantidade de telas verificadas", cont)
print("Telas com erro", erro)
navegador.close()
