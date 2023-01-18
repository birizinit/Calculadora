# -*- coding: utf-8 -*-
import streamlit as st

st.title("Calculadora de Peso")

n1=st.text_input("Peso: ")
n2=st.text_input("Qtd Solicitada: ")

if n1 and n2:
    n1=float(n1)
    n2=int(n2)
    n3=(n1*0.10+n1)*n2
    st.write(f'O peso total é de {n3} ')