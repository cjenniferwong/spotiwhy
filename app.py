import streamlit as st
import numpy as np
import pandas as pd
# import time

options = ['letters', 'numbers']


def welcome_message():
    st.title('Welcome to Spotiwhy')
    st.subheader('looking to understand your musical profile')


@st.cache
def generate_data(n_columns=10, n_rows=10000):
    data = []
    letter_list = ['a', 'b', 'c', 'd', 'e']
    options = ['letters', 'numbers']
    for _ in range(n_columns):
        type = np.random.choice(options)
        if type == 'letters':
            data.append(np.random.randint(0, 100, n_rows))
        else:
            data.append(np.random.choice(letter_list, n_rows))
    df = pd.DataFrame(data).T
    df.columns = [f'column_{num}' for num in range(len(df.columns))]
    print('hello world')
    # time.sleep(10)
    return df


def main():
    welcome_message()
    with st.spinner('testing...'):
        st.markdown('## data generated')
    option = st.sidebar.selectbox('Which number do you like best?',
                                  options)

    st.write(f'You selected: {option}')
    original = generate_data()
    if option == 'letters':
        user_input = st.text_input('please write something')
        st.write(f'user wrote: {user_input}')
        data = original
        data

    if option == 'numbers':
        data = original
        # st.write('hello world')
        x = st.slider('Enter a value')
        sampled = data.sample(x)
        st.write(x)
        sampled


if __name__ == '__main__':
    main()
