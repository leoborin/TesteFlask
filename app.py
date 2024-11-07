
"""
from flask import Flask

# Inicializar a aplicação Flask
app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return "Eldin Gosta de Bacon."

# Rota adicional
@app.route('/sobre')
def sobre():
    return "Esta é uma aplicação simples feita com Flask."

# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True)
"""

    
from flask import Flask
import warnings
import pandas as pd
import pyodbc

# Suprimir todos os avisos
warnings.filterwarnings("ignore")

# Configurar pandas para exibir todas as colunas
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Configuração da conexão com o banco de dados
driver = '{SQL Server}'
server = '10.200.92.45'
database = 'ALL_STAGE'

# Inicializar a aplicação Flask
app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return "Eldin Gosta de Bacon. 2"

# Rota adicional
@app.route('/sobre')
def sobre():
    return "Esta é uma aplicação simples feita com Flask."

# Rota para exibir o número de registros da consulta SQL
@app.route('/consulta')
def consulta():
    try:
        # Conectar ao banco de dados
        con = pyodbc.connect(driver=driver, server=server, database=database, Trusted_Connection='yes')
        
        # Definir a consulta SQL
        QUERY_z369 = '''
        SELECT VAGAO, ID_VAGAO, SERIE, TREM, SEQUENCIA, [LOCAL], ORIGEM, DESTINO, NR_OS, DT_CARGA, COD_LINHA
        FROM ALL_STAGE.translogic.TELA_164_FOTO
        WHERE 1=1
        -- AND LOCAL IN ('ZAX', 'ZTO', 'ZDZ', 'ZMA', 'ZOI', 'ZRI', 'ZTI', 'ZXH', 'ZDG', 'ZTN', 'ZGT', 'ZSK')
        AND FROTA != 888
        AND NR_OS IS NOT NULL 
        AND NR_OS <> ''
        '''

        # Executar a consulta e carregar o resultado em um DataFrame
        df_QUERY_z369 = pd.read_sql_query(sql=QUERY_z369, con=con)
        
        # Fechar a conexão com o banco de dados
        con.close()
        
        # Retornar o número de registros
        return f"Total de registros na consulta: {len(df_QUERY_z369)}"
    except Exception as e:
        return f"Erro ao executar a consulta: {e}"

# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True)
