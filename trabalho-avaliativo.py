import streamlit as st
import requests
import pandas as pd



st.title('Coletando informações')
st.markdown('Digite seus dados conforme indicado abaixo')

def conseguir_nome():
  name = st.text_input(
  label = 'Digite seu nome',
  placeholder = 'digite aqui'
)
  return name

def conseguir_telelfone():
  tell = st.text_input(
   label = 'Digite seu telefone',
   placeholder = 'Somente números'
)
  return tell

def conseguir_mail():
  mail = st.text_input(
   label = 'Digite seu e-mail',
   placeholder = 'digite aqui'
)
  return mail

def conseguir_cpf():
   cpf = st.text_input(
    label = 'Digite seu cpf',
    placeholder = ' somente números'
)
   return cpf

def conseguir_cep():
  cep = st.text_input(
   label = 'Digite seu cep',
   placeholder = 'Somente números'
)
  return cep
