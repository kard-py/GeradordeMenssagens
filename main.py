from playwright.sync_api import sync_playwright
import pandas as pd
import json
import time


def genMSG(aluno):

    msg = f"""Olá Boa Tarde Sou o Secretario da Escola Municipal São Domingos de Sorriso - MT Preciso do Histórico Escolar de Alguns Ex-alunos da sua escola ({aluno['escola_origem']} - {aluno['cidade_origem']}):\nNome dos Alunos - Data de Transferencia:\n{aluno['Nome']} Trasferido em: {aluno['data_transf']}\nAtt."""

    return msg


historicos = pd.read_csv("./HISTORICOS.csv")
historicos = json.loads(historicos.to_json(orient='table'))
db = historicos['data']


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://webmail.sorriso.mt.gov.br/")
    page.locator(
        '//*[@id="rcmloginuser"]').fill("emsaodomingos@sorriso.mt.gov.br")
    page.locator('//*[@id="rcmloginpwd"]').fill('')
    page.locator('//*[@id="submitloginform"]').click()
    time.sleep(5)
    print(page.title())
    page.goto('https://webmail.sorriso.mt.gov.br/?_task=mail&_action=compose')
    time.sleep(5)
    print(page.title())
    page.locator('//*[@id="_to"]').fill('caiodetz654@gmail.com')
    time.sleep(1)
    page.locator('#compose-subject').fill(
        "Solicitação de Envio de Historico Escolar Escola Municipal São Domingos - Sorriso- MT")
    time.sleep(1)
    page.frame_locator('#composebody_ifr').locator(
        '//*[@id="tinymce"]/p[1]').click()
    page.keyboard.type("TESTE\nTESTE")
    time.sleep(1)
    page.locator('#rcmbtn108').click()
    time.sleep(10)
    print(page.title())
    browser.close()
