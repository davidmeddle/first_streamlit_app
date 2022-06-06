import streamlit

streamlit.title('My partners new the healthy food')
streamlit.header('🥣 Break fastmenu')
streamlit.text ('🐔 Omega 3 and kale')
streamlit.text ('blueberrys and mil')
streamlit.text ('almond latte')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect ("Pick some fruits:", list (my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
