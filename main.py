import streamlit as st

Page_cliente = st.sidebar.selectbox(
    'Cliente', ['Incluir', 'Consultar'], 0)

if Page_cliente == 'Incluir':
    st.experimental_set_query_params()
    If Page_cliente == 'Incluir':
        st.write("""OK""")


    
