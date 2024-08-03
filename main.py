import streamlit as st
import pyodbc
import pandas as pd


# Configuração da conexão
def get_connection():
    try:
        server = 'localhost'
        database = 'AdventureWorks2017'
        username = 'vitor'
        password = '219288'
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                              'SERVER=' + server + ';'
                              'DATABASE=' + database + ';'
                              'UID=' + username + ';'
                              'PWD=' + password + ';'
                              'Connection Timeout=5;')  # 5 segundos, ajuste conforme necessário
        return conn
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

def fetch_data(query):
    conn = get_connection()
    if conn is not None:
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    else:
        return pd.DataFrame()  # Retorna um DataFrame vazio se a conexão falhar


st.title("Pesquisa De Códigos")

search_query = st.text_input("Digite sua pesquisa:")

if search_query:
    sql_query = f"SELECT FirstName, LastName FROM Person.Person WHERE FirstName LIKE '%{search_query}%'"
    results = fetch_data(sql_query)
    if not results.empty:
        st.write("Resultados da Pesquisa:")
        st.dataframe(results)
    else:
        st.write("Nenhum resultado encontrado.")

st.markdown("***")
st.write("Desenvolvido por *Vitor S.*")
