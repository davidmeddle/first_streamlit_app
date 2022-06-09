import streamlit
import requests
import pandas
import snowflake.connector
from urllib.error import URLError




streamlit.title ('My parents new healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:",list (my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header('Fruitvice Fruit Advice!')
fruit_choice = streamlit.text_input ('What fruit would you like information about?', 'Kiwi')
streamlit.write ('Thye user entered', fruit_choice)
#import requests
fruitvice_response = requests.get ("https://fruityvice.com/api/fruit/" + fruit_choice)

fruitvice_normalized = pandas.json_normalize(fruitvice_response.json()) 

streamlit.dataframe(fruitvice_normalized)

#dont run anything past here where we troubleshoot
streamlit.stop()




#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("THE FRUIT LOAD LIST CONTAINS:")
streamlit.dataframe(my_data_rows)


my_fruit = streamlit.text_input ('what fruit would you like to add?', 'jackfruit')
streamlit.write ('Thye user entered', my_fruit)


#this will not work corrctly, but go with it for now
my_cur.execute ("insert into fruit_load_list values ('from streamlit')")

