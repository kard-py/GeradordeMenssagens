import pandas as pd
import json


def genMSG(aluno):

    msg = f"""Olá Boa Tarde Sou o Secretario da Escola Municipal São Domingos de Sorriso - MT Preciso do Histórico Escolar de Alguns Ex-alunos da sua escola ({aluno['escola_origem']} - {aluno['cidade_origem']}):\nNome dos Alunos - Data de Transferencia:\n{aluno['Nome']} Trasferido em: {aluno['data_transf']}\nAtt."""

    return msg


historicos = pd.read_csv("./HISTORICOS.csv")
historicos = json.loads(historicos.to_json(orient='table'))
db = historicos['data']
file = open("result.txt", "a")
for item in db:
    print(item['Nome'])
    msg = genMSG(item)
    file.write(msg)
    file.write("\n\n")


file.close()
