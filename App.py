import os 
os.system("cls")

import streamlit as st
from datetime import datetime

st.sidebar.image("LOGO.png")
st.sidebar.title("Locadora de Importados 🚙") 

carro = st.sidebar.selectbox("Selecione o carro que deseja alugar:",
                             ["BMW-X6","McLAREN 765 SVJ","MERCEDES-G63","PUROSANGUE","ROLLS-ROYCE"]) 

valores_diarias = {"BMW-X6":1300, "McLAREN 765 SVJ":17000, "MERCEDES-G63":3000, "PUROSANGUE":12500, "ROLLS-ROYCE":15000} 
valor_diaria = valores_diarias[carro]

st.image(f"{carro}.png")
st.subheader(f"{carro} - Diária: R$ {valores_diarias [carro]}")

data_retirada = st.date_input("Selecione o dia da retirada: ", datetime.now(), datetime.now())
data_devolução = st.date_input("Selecione a data da devolução", data_retirada, data_retirada)
if st.button("Alugar"):
    dias = (data_devolução - data_retirada).days
    valor_total = valor_diaria * dias
    st.write(f"Carro escolhido **{carro}**")
    st.metric("Total do aluguel", f"R$ {valor_total:.2f}")
  
st.markdown("<br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)


st.feedback("stars")
st.text_area("Deixe um comentário: ")
if st.button("Comentar"):
    st.balloons()
    