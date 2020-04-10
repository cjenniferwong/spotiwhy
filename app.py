import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


options = ['Home', 'Demo']


def welcome_message():
    st.title('Welcome to Spotiwhy')
    st.subheader('this project looks to understand the components of your musical profile')


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
    df = pd.DataFrame(data).T  # this seems to be faster than vstack
    df.columns = [f'column_{num}' for num in range(len(df.columns))]
    print('generating data again')
    return df


def main():
    welcome_message()
    with st.spinner('L O A D I N G...'):
        st.write('')

    option = st.sidebar.selectbox('Pages', options)
    original = generate_data()

    if option == 'Home':
        user_input = st.text_input('please write something')
        st.write(f'user wrote: {user_input}')

    if option == 'Demo':
        st.write('this is just useless data so i can get aquainted with streamlit')
        x = st.slider('Number of Simulations')
        sampled = original.sample(x)
        # generating charts
        sns.distplot(sampled['column_0'].value_counts(normalize=True))
        st.pyplot()
        if st.checkbox('Show df:'):
            st.dataframe(sampled['column_0'].value_counts(normalize=True))


if __name__ == '__main__':
    main()
