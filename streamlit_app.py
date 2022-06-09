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

#create to repeatable code block (called a function)
def get_fruitvice_data(this_fruit_choice):
	fruitvice_response = requests.get ("https://fruityvice.com/api/fruit/" + fruit_choice)	
	fruitvice_normalized = pandas.json_normalize(fruitvice_response.jason()) 	
	return fruitvice_normalized

#new section to display fruitvice api response 
streamlit.header('Fruitvice Fruit Advice!')
try:
	fruit_choice = streamlit.text_input ('What fruit would you like information about?')
	if not fruit_choice:
		streamlit.error("Please select a fruit toi get inforamtion.")
	else:
		back_from_function = get_fruitvice_data (fruit_choice)
		streamlit.dataframe(back_from_function)
except URLerror as e:
	streamlit.error()

#dont run anything past here where we troubleshoot

#import snowflake.connector
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
streamlit.header("THE FRUIT LOAD LIST CONTAINS:")
#snowflake-related functions
def get_fruit_load_list():
	with my_cnx.cursor() as my_cur:
		my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")	
		return my_cur.fetchall()

#add a button to load the fruit
if streamlit.button('Get fruit load list'):
#	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])	
	my_data_rows = get_fruit_load_list()
	streamlit.dataframe(my_data_rows)

streamlit.stop()

#allow the end user to add a fruit to the list
def insert_row_snowflake (new_fruit):
	with my_cnx.cursor() as my_cur:
		my_cur.execute ("insert into fruit_load_list values ('from streamlit')")	
		return ("thanks for adding " + new_fruit)

my_fruit = streamlit.text_input ('what fruit would you like to add?', 'jackfruit')
if streamlit.button('Get fruit load list'):
	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])	
	back_from_function = insert_row_snowflake (my_fruit)
	steamlit.text(back_from_function)
		

