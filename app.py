import streamlit as st
import random


def koloneuro():
    kolon = set()
    while len(kolon) < 5:
        kolon.add(random.randint(1, 50))
    return tuple(sorted(list(kolon)))


def supereuro():
    kolon = set()
    while len(kolon) < 2:
        kolon.add(random.randint(1, 10))
    return tuple(sorted(list(kolon)))


def kolonlotto():
    kolon = set()
    while len(kolon) < 6:
        kolon.add(random.randint(1, 49))
    return tuple(sorted(list(kolon)))


def lotto():
    kolon = st.text_input("Kac tane kolon oynamak istersiniz? (1 - 12)")
    super_sayi = random.randint(1, 9)
    
    try:
        kolon = int(kolon)
        if 0 < int(kolon) < 5:
            sol, sag = st.beta_columns(2)
            with sol:
                st.write("Super Sayi :", super_sayi)
                for i in range(kolon):
                    st.write(f'{i + 1}. Kolon:')
                    st.write(' ', kolonlotto())
                

        elif 4 < kolon < 9:
            sol, sag = st.beta_columns(2)
            with sol:
                st.write("Super Sayi :", super_sayi)
                for i in range(4):
                    st.write(f'{i + 1}. Kolon:')
                    st.write(' ', kolonlotto())
            with sag:
                for i in range(4, kolon):
                    st.write(f'{i + 1}. Kolon:')
                    st.write(' ', kolonlotto())

        elif 8 < kolon < 13:
            sol, orta, sag = st.beta_columns(3)
            with sol:
                st.write("Super Sayi :", super_sayi)
                for i in range(4):
                    st.write(f'{i + 1}. Kolon:')
                    st.write(' ', kolonlotto())
                
            with orta:
                for i in range(4, 8):
                    st.write(f'{i + 1}. Kolon:')
                    st.write(' ', kolonlotto())
            with sag:
                for i in range(8, kolon):
                    st.write(f'{i + 1}. Kolon:')
                    st.write(' ', kolonlotto())
        
        else:
            st.write('Lütfen 1 ile 12 arasi bir sayi giriniz!')
                    
    except:
        st.write("Lütfen 1 ile 12 arasi bir sayi giriniz!")


def euro():
    kolon = st.text_input("Kac tane kolon oynamak istersiniz? (1 - 12)")

    try:
        kolon = int(kolon)
        if 0 < int(kolon) < 5:
            sol, sag = st.beta_columns(2)
            with sol:
                for i in range(kolon):
                    st.write(f'{i + 1}. Kolon:')
                    st.write(' ', koloneuro())
                    st.write(' ', supereuro())

        elif 4 < kolon < 9:
            sol, sag = st.beta_columns(2)
            with sol:
                for i in range(4):
                    st.write(f'{i + 1}. Kolon:')
                    st.write(' ', koloneuro())
                    st.write(' ', supereuro())
            with sag:
                for i in range(4, kolon):
                    st.write(f'{i + 1}. Kolon:')
                    st.write(' ', koloneuro())
                    st.write(' ', supereuro())

        elif 8 < kolon < 13:
            sol, orta, sag = st.beta_columns(3)
            with sol:
                for i in range(4):
                    st.write(f'{i + 1}. Kolon:')
                    st.write(' ', koloneuro())
                    st.write(' ', supereuro())
            with orta:
                for i in range(4, 8):
                    st.write(f'{i + 1}. Kolon:')
                    st.write(' ', koloneuro())
                    st.write(' ', supereuro())
            with sag:
                for i in range(8, kolon):
                    st.write(f'{i + 1}. Kolon:')
                    st.write(' ', koloneuro())
                    st.write(' ', supereuro())
        
        else:
            st.write('Lütfen 1 ile 12 arasi bir sayi giriniz!')
                    
    except:
        st.write("Lütfen 1 ile 12 arasi bir sayi giriniz!")


st.title("Rasgele Secilmis Loto Sayilari")

istek = st.selectbox('Hangi oyunu oynamak istersiniz?',
                    ('--', 'EuroJackPot', 'Lotto'))

if istek == 'EuroJackPot':
    random.seed(10)
    euro()
elif istek == 'Lotto':
    lotto()
else:
    pass

