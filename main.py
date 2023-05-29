import pandas as pd
import json



def genMSG(aluno):

    msg = f"""Email:{aluno["email"]}\nAssunto: Requerimento de Historico Escolar E.M. São Domingos de Sorriso - MT\n\nOlá Boa Tarde Sou o Secretario da Escola Municipal São Domingos de Sorriso - MT Preciso do Histórico Escolar de Alguns Ex-alunos da sua escola ({aluno['escola_origem']} do municipio de {aluno['cidade_origem']}):\nNome dos Alunos - Data de Transferencia:\n{aluno['alunos']}\nAtt."""

    return msg


historicos = pd.read_csv("./HISTORICOS.csv")
historicos = json.loads(historicos.to_json(orient='table'))
db = historicos['data']

escolas_com_email = [
"U.E. COMUNITARIA CODÓ NOVO",
"E.M. BOAS NOVAS",
"E.M. PEDRO ABREU",
"U.I. JOSE ARAUJO BEZERRA",
"U.E.B. JOSEFINA SERRÃO",
"C.A. NIZETH OLIVEIRA RIBEIRO",
"E.M.E.F. TEREZINHA DE JESUS",
"E.M. PRINCESA ISABEL",
"U.E.M. RIO PRETO",
"U.E.M. MARCELO THADEU",
"E.M.E.F. ERICO VERISSIMO",
"E.M.E.F. VINICIUS DE MORAES",
"E.M. TANCREDO NEVES",
"UNIDADE ESCOLAR SANTA LUIZA",
"E.M. 13 DE MAIO",
"U.I. ALZIRA CESAR MENESES",
"E.M. GUSTAVO ADOLFO WILKE",
"E.M.E.B. RODRIGO DAMASCENO",
"E.M.E.F. JOAO PRUDENCIO DE BRITO",
"E.M. PEDRO LIMA",
"E.R.M. VITOR VALENDOLR",
"E.M.E.F. EJA ANGELO DEBIASE",
"E.M. SANTOS DUMONT",
"E.M. MANOEL JOSE DA SILVA"

]

"""
{
    'index': 287,
    'Nº Ch.': 30,
    'Nome': 'ISAAC MATIAS RIBEIRO',
    'Situação': None, 
    'Fone 1': 66999241185.0,
    'Fone 2': None,
    'Turma': '7º ANO H',
    'deve_documento': 'HISTORICO',
    'escola_origem': 'E.M. VALTER LEITE PEREIRA',
    'cidade_origem': None,
    'email': None,
    'telefone': None,
    'data_transf': '30/11/2020',
    'solicitado': None,
    'observação': None
}
"""
dados = []
for e in escolas_com_email:
    alunos = []
    cidade_origem = ""
    email = ""
    for i in db:
        if i['escola_origem'] == e:
            alunos.append("{} Trasferido em: {}".format(i['Nome'],i['data_transf']))
            cidade_origem = i['cidade_origem']
            email = i['email']
    
    
    alunos = tuple(alunos)
    alunoMSG = "\n".join(alunos)



    dados.append({
        'escola_origem':e,
        'cidade_origem':cidade_origem,
        'alunos':alunoMSG,
        'email':email
    })





doc = open('results.txt', 'a')

for e in dados:
    msg = genMSG(e)
    doc.write(msg)
    doc.write("\n--------------------------------------------\n")

doc.close()