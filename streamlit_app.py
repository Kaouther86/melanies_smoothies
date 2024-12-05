# Import Python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests

# App title
st.title(":cup_with_straw: Customize Your Smoothie :cup_with_straw:")

# App description
st.write("Choose the fruits you want in your custom Smoothie")

# Input field for name on smoothie
name_on_order = st.text_input('Name on Smoothie:', key='name_input')
st.write('The name on your smoothie will be:', name_on_order)

# Connect to Snowflake
cnx = st.connection("snowflake")
session = cnx.session()

# Fetch fruit options from Snowflake
my_dataframe = session.table("smoothies.public.fruit_options").select(
    col('Fruit_name'), col('Search_on')
)

# Convert Snowflake DataFrame to Pandas DataFrame
pd_df = my_dataframe.to_pandas()

# Multiselect for ingredients
ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:',
    pd_df['FRUIT_NAME'],
    max_selections=5,
    key='ingredients_multiselect'
)

# Check if user has selected ingredients
if ingredients_list:
    ingredients_string = ' '.join(ingredients_list)

    # Display nutrition information for each selected fruit
    for fruit_chosen in ingredients_list:
        search_on = pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
        st.subheader(f"{fruit_chosen} Nutrition Information")

        # Fetch nutrition data from API
        try:
            fruityvice_response = requests.get(f"https://my.smoothiefroot.com/api/fruit/{search_on}")
            if fruityvice_response.status_code == 200:
                fv_data = fruityvice_response.json()
                st.dataframe(data=fv_data, use_container_width=True)
            else:
                st.error(f"Could not fetch data for {fruit_chosen}. Please try again.")
        except Exception as e:
            st.error(f"Error fetching data: {str(e)}")

    # Prepare the SQL insert statement
    my_insert_stmt = f"""
                INSERT INTO smoothies.public.orders (ingredients, name_on_order)
                VALUES ('{ingredients_string}', '{name_on_order}')
            """

    # Display the button to submit the order
    if st.button('Submit Order', key='submit_button'):
        try:
            session.sql(my_insert_stmt).collect()
            st.success(f"Your Smoothie is ordered, {name_on_order}!", icon="✅")
        except Exception as e:
            st.error(f"Error submitting order: {str(e)}")
