from reportlab.platypus import SimpleDocTemplate, TableStyle, Table
from reportlab.lib import colors
from gspread_dataframe import get_as_dataframe
from reportlab.lib.units import inch
import gspread

#tamanho da pagina
pagesize = (11 * inch, 11 * inch)
#cria o pdf
pdf = SimpleDocTemplate("dataframe.pdf", pagesize=pagesize)
#autentica no Google Sheets via Service Account usando o arquivo JSON de credenciais 
gc = gspread.service_account("credenciais3.json")
#abre a planilha e seleciona a primeira aba 
worksheet = gc.open("desafio2").sheet1
#converte o coneudo da aba em dataframe 
data=get_as_dataframe(worksheet)
#lista que vai armazenar os dados 
table_data = []
#itera as linhas perguntando ao usuario
for i, row in data.iterrows():
    linha =  int(input("deseja imprimir esta linha? [0=Não, 1-Sim]?"))
    if (linha==1):
        table_data.append(list(row))
#itera as colunas perguntando ao usuario
for index,content in data.items():
    coluna= int(input("deseja incluir a coluna [0=Não, 1-Sim]?"))  
    if (coluna==1):
        table_data.append(list(content))
#cria um flowable table a partir dos dados escolhidos
table = Table(table_data)
#estilizando a table
LIST_STYLE = TableStyle(
    [('LINEABOVE', (0,0), (-1,0), 2, colors.green),
    ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
    ('LINEBELOW', (0,-1), (-1,-1), 2, colors.green),
    ('ALIGN', (1,1), (-1,-1), 'RIGHT'),
    ])
table.setStyle(LIST_STYLE)
#cria lista para adicionar a table com os dados
pdf_table=[]
#adiciona a table 
pdf_table.append(table)
#Gera o arquivo pdf
pdf.build(pdf_table)