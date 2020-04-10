import streamlit as st


def welcome_message():
    st.title('Welcome to Spotiwhy')
    st.subheader('looking to understand your musical profile')


def print_me():
    return('please help')


def main():
    welcome_message()
    st.write('hello world')

    # st.write(print_me())
    # the below just prints things into the terminal
    # print(print_me())
    # the below just prints it in the terminal LOL
    # print('i have entered the main fcn')


if __name__ == '__main__':
    main()
