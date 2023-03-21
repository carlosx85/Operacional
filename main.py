import streamlit as st

Page_cliente = st.sidebar.selectbox(
    'Cliente', ['Incluir', 'Consultar'], 0)

If Page_cliente == 'Incluir' :
    st.write("ok")


    
