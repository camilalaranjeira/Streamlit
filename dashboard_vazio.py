import streamlit as st
import pandas as pd
import plotly.express as px

#######################
# Configurações gerais da página
st.set_page_config(
    page_title="Meu dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

#######################
# Estilização CSS 
# Crie o seu arquivo .css
with open('style.css', 'r') as fp:
    st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)

#######################
# Carregamento de dados com Pandas
df = pd.read_csv('caminho/para/dados.csv')


#######################
# Sidebar (barra lateral)
# inclua elementos de interatividade
# fornecidos pelo Streamlit e/ou
# informações sobre os dados
with st.sidebar:
    st.title('📊 Meu dashboard')


#######################
# Criando Plots
# crie uma função para cada gráfico
# a função deve retornar o objeto do gráfico.
# Use e abuse do Plotly!

def plot1(input1, input2, input3):
    return 

def plot2(input1, input2, input3):
    return 

def plot3(input1, input2, input3):
    return


#######################
# Apresentando plots no painel 
# principal do dashboard 

# criando colunas e suas larguras
col = st.columns((3, 4.5), gap='medium')

# preencha as colunas incorporando seus
# dados e plots como elementos Streamlit
with col[0]:
    
    # plot 1
    st.markdown('#### Título 1 da coluna 1')
    p1 = plot1(0,0,0)
    st.plotly_chart(p1, use_container_width=True)

    # display dados
    st.markdown('#### Título 2 da coluna 1')
    st.dataframe(df, width=None) 


with col[1]:

    # plot 2
    st.markdown('#### Título 1 da coluna 2')
    p2 = plot2(0,0,0)
    st.plotly_chart(p2, use_container_width=True)


    # plot 3
    st.markdown('#### Título 2 da coluna 2')
    p3 = plot3(0,0,0)
    st.plotly_chart(p3, use_container_width=True)