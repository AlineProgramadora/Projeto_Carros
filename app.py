import pandas as pd
import streamlit as st
#python -m streamlit run app.py

#----------------------------------------------- sidebar
st.sidebar.image("logo.png")
st.sidebar.title('aline carros')



carros=['Bmw','corola','porsche','toro','dodge ram','fusca']

opcao=st.sidebar.selectbox('Escolha o carro que foi alugado',carros)

#----------------------------------------------- principal
st.title('aluga-se carros da melhor qualidade para o seu conforto')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo:{opcao}')
st.markdown('---')

dias=st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km=st.text_input(f'Quantos km você rodou com o {opcao}?')

if opcao == 'Bmw':
        diaria = 1012
elif opcao == 'corola':
        diaria = 2397
elif opcao == 'porsche':
        diaria = 20500
elif opcao == 'toro':
        diaria = 30480
elif opcao == 'dodge ram':
        diaria = 20000
elif opcao =='fusca':
        diaria=1000
        
        
if st.button('calcular'):
        dias = int(dias)
        km = float(km)

        total_dias = dias * diaria
        total_km = km * 0.15
        aluguel_total = total_dias+total_km

        st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km . O valor total a pagar é R${aluguel_total:.2f}')

