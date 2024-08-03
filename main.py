import streamlit as st
import pyodbc
import pandas as pd


# Configuração da conexão
def get_connection():
    server = 'VICHELE\SQLEXPRESS01'
    database = 'AdventureWorks2017'
    username = 'vitor'
    password = '219288'
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=' + server + ';'
                                               'DATABASE=' + database + ';'
                                                                        'UID=' + username + ';'
                                                                                            'PWD=' + password)
    return conn


def fetch_data(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


def fetch_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df


st.title("Pesquisa De Codigos")

search_query = st.text_input("Digite sua pesquisa:")

if search_query:
    sql_query = f"SELECT FirstName,LastName FROM Person.Person WHERE FirstName LIKE '%{search_query}%'"
    results = fetch_data(sql_query)
    if not results.empty:
        st.write("Resultados da Pesquisa:")
        st.dataframe(results)
    else:
        st.write("Nenhum resultado encontrado.")
        timeout=30

st.markdown("***")
st.write("Desenvolvido por *Vitor s.*")
