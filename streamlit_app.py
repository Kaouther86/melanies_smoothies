Partager


Vous avez dit :
Which of the following roles is recommended to be used to create and manage users and roles in snowflake
ChatGPT a dit :
ChatGPT
In Snowflake, the "USERADMIN" role is typically recommended for creating and managing users and roles.

The USERADMIN role has the necessary privileges to:

Create and manage users (e.g., adding, altering, and dropping users).
Create and manage roles (e.g., creating new roles, assigning roles to users, and granting privileges to roles).
Manage security-related settings, such as multi-factor authentication (MFA), password policies, and other user-specific configurations.
This role is specifically designed to handle user and role management while ensuring that access control and security remain intact.






Vous avez dit :
The COPY command must specify a File Format in order to execute. insnowflake
ChatGPT a dit :
ChatGPT
In Snowflake, while using the COPY INTO command, specifying a file format is optional, but it's highly recommended to define or use one if your file data requires a specific format (e.g., CSV, JSON, Parquet). Snowflake provides two ways to handle file formats when loading data:

1. Using a Predefined File Format
You can create a file format object using the CREATE FILE FORMAT statement and then reference that file format in the COPY INTO command.

Example:

sql
Copier le code
CREATE OR REPLACE FILE FORMAT my_csv_format
TYPE = 'CSV'
FIELD_OPTIONALLY_ENCLOSED_BY = '"'
SKIP_HEADER = 1;

COPY INTO my_table
FROM @my_stage/myfile.csv
FILE_FORMAT = (FORMAT_NAME = 'my_csv_format');
2. Using Inline File Format Options
You can directly specify the file format inline within the COPY INTO command without using a predefined file format object.

Example:

sql
Copier le code
COPY INTO my_table
FROM @my_stage/myfile.csv
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"' SKIP_HEADER = 1);
Default Handling:
If you do not specify a file format, Snowflake assumes the default settings (e.g., CSV format without special delimiters). However, this may not always align with your file structure, so explicitly defining a file format is recommended to avoid potential issues during data loading.

In summary, while specifying a file format is optional, it ensures that Snowflake correctly parses the data according to your specific needs.






Vous avez dit :
Which of the following commands sets the Virtual Warehouse for a session?
ChatGPT a dit :
ChatGPT
The command used to set the virtual warehouse for a session in Snowflake is:

USE WAREHOUSE

Syntax:
sql
Copier le code
USE WAREHOUSE <warehouse_name>;
This command sets the specified virtual warehouse for the current session, and all subsequent queries or operations will use this warehouse for compute resources until it is changed again or the session ends.

Example:
sql
Copier le code
USE WAREHOUSE my_warehouse;
In this example, my_warehouse is the virtual warehouse that will be used for the session.






Vous avez dit :
Which of the following objects can be cloned
ChatGPT a dit :
ChatGPT
In Snowflake, several database objects can be cloned, allowing you to create a copy of an object with its current data and metadata. Cloning is a powerful feature in Snowflake because it is zero-copy, meaning it initially doesn’t consume additional storage since it references the same underlying data until modifications are made.

Here are the objects that can be cloned:

Tables – You can clone a table, including both its schema and the data it contains.

Example:
sql
Copier le code
CREATE TABLE my_table_clone CLONE my_table;
Schemas – You can clone an entire schema, including all the tables, views, and other objects within that schema.

Example:
sql
Copier le code
CREATE SCHEMA my_schema_clone CLONE my_schema;
Databases – You can clone an entire database, including all schemas and objects (tables, views, etc.).

Example:
sql
Copier le code
CREATE DATABASE my_database_clone CLONE my_database;
Streams – You can clone a stream that tracks changes to a table, preserving its metadata.

Example:
sql
Copier le code
CREATE STREAM my_stream_clone CLONE my_stream;
Materialized Views – A materialized view can also be cloned.

Example:
sql
Copier le code
CREATE MATERIALIZED VIEW my_mv_clone CLONE my_materialized_view;
Tasks – Snowflake allows cloning of tasks (automated scheduled jobs).

Example:
sql
Copier le code
CREATE TASK my_task_clone CLONE my_task;
Cloning allows you to create an instant and space-efficient copy of data, which is especially useful for testing, backup, or development purposes.






Vous avez dit :
A. Tables Most Voted
B. Named File Formats Most Voted
C. Schemas Most Voted
D. Shares
E. Databases Most Voted
F. Users
ChatGPT a dit :
ChatGPT
In Snowflake, not all of the objects listed can be cloned. Here's a breakdown of which ones can be cloned and which cannot:

Objects that can be cloned:
A. Tables (Most Voted): Yes, tables can be cloned.
C. Schemas (Most Voted): Yes, schemas can be cloned.
E. Databases (Most Voted): Yes, databases can be cloned.
Objects that cannot be cloned:
B. Named File Formats: No, file formats cannot be cloned.
D. Shares: No, shares cannot be cloned.
F. Users: No, users cannot be cloned.
Summary:
Can be cloned: Tables, Schemas, Databases
Cannot be cloned: Named File Formats, Shares, Users





Vous avez dit :
Why would a customer size a Virtual Warehouse from an X-Small to a Medium?
ChatGPT a dit :
ChatGPT
A customer might decide to size a Virtual Warehouse from X-Small to Medium in Snowflake for several reasons, most of which are related to performance, workload demands, and query optimization. Here's why:

1. Increased Workload:
Higher Data Volume: If the volume of data being processed or queried increases significantly, a larger warehouse size is needed to handle the load efficiently. A Medium warehouse offers more compute resources (such as CPU and memory) compared to X-Small, allowing faster query execution for larger datasets.
More Concurrent Queries: If the number of simultaneous users or queries grows, scaling up to a larger warehouse helps ensure better performance. Snowflake's virtual warehouses distribute the load across multiple resources, and a larger size can handle more concurrent operations without bottlenecks.
2. Complex Queries:
Resource-Intensive Queries: If the queries being run involve complex calculations, joins, or aggregations over large datasets, they will require more processing power. A Medium warehouse will offer greater computational capacity, improving performance and reducing the time taken to execute these queries.
ETL or Data Transformation Workloads: Extract, Transform, Load (ETL) processes often involve transforming large amounts of data, which is compute-intensive. Scaling up helps reduce the processing time.
3. Performance Optimization:
Faster Query Execution: As the size of the warehouse increases, the number of compute resources (like CPU and RAM) increases, which can result in faster query performance. If query performance is lagging on an X-Small warehouse, upgrading to Medium may significantly improve response times.
Shorter Wait Times: A larger warehouse can reduce queue times for queries, ensuring that jobs are processed more quickly, particularly during peak usage periods.
4. Better Performance for Concurrent Load and Resource Distribution:
Multiple Concurrent Users: If multiple users are running queries at the same time, upgrading the warehouse size ensures that each user's query gets sufficient resources. An X-Small warehouse might be overwhelmed by heavy concurrent usage, while a Medium warehouse can better distribute the resources among the concurrent workloads.
5. Scaling to Meet Business Demands:
Seasonal or Temporary Workload Spikes: Businesses sometimes face seasonal spikes in data processing needs. For example, an e-commerce company might need to scale up during holiday seasons when there’s increased traffic and transactions. Temporarily sizing up from X-Small to Medium ensures smooth operation during these peaks.
6. Improving Load Time for Data Ingestion:
Faster Data Loading: When loading large files into Snowflake, a larger warehouse size can speed up the process by using more compute resources, especially for parallelized data loading jobs. This is critical for real-time or near real-time data ingestion needs.
Key Benefits of Moving to a Larger Warehouse (Medium):
Improved performance for larger or more complex queries.
Faster execution times for both queries and data loading.
More resources to handle concurrent queries or larger workloads.
Reduced query queuing during times of high demand.
Overall, a customer would size up their virtual warehouse to Medium to meet increasing performance demands, improve query times, and handle larger or more complex workloads efficiently.






Vous avez dit :
When a Pipe is recreated using the CREATE OR REPLACE PIPE command:

The Pipe load history is reset to empty
The REFRESH parameter is set to TRUE
Previously loaded files will be ignored
All of the above
ChatGPT a dit :
ChatGPT
The correct answer is:

All of the above.

When a Pipe is recreated using the CREATE OR REPLACE PIPE command in Snowflake, the following actions occur:

The Pipe load history is reset to empty:

When a pipe is replaced, the previous load history (i.e., records of the files that have been processed) is cleared. This means Snowflake will no longer retain information about which files were loaded before the pipe was replaced.
The REFRESH parameter is set to TRUE:

When a pipe is recreated, the AUTO_INGEST property (if it was set) will be reset, and the REFRESH parameter will be set to TRUE. This forces the pipe to recheck all files in the stage to ensure that they are processed after the pipe is recreated.
Previously loaded files will be ignored:

Since the load history is cleared, Snowflake has no record of files previously loaded by the pipe. However, Snowflake keeps track of file metadata (via the Snowflake internal stage), so it knows which files have already been loaded. Thus, these previously loaded files will be ignored to prevent duplicate loading.
Therefore, "All of the above" is the correct choice because each of the listed effects happens when using the CREATE OR REPLACE PIPE command.






Vous avez dit :
: Query ID's are unique across all Snowflake deployments and can be used in communication with Snowflake Support to help troubleshoot issues.
ChatGPT a dit :
ChatGPT
Yes, that statement is true.

In Snowflake, Query IDs are unique across all Snowflake deployments (regions and accounts) and serve as identifiers for specific query executions. These Query IDs are valuable for several reasons:

Troubleshooting: You can provide the Query ID to Snowflake Support for troubleshooting specific queries or performance issues. Since the ID is unique, it allows support teams to locate and analyze the exact query, regardless of the deployment.

Tracking and Debugging: Users and administrators can use Query IDs to track the performance of queries, understand execution details, and debug potential issues in query logic or performance bottlenecks.

Historical Analysis: Query IDs can be used to retrieve historical details of queries using Snowflake’s query history views or functions.

Since each Query ID is globally unique, it helps Snowflake Support identify and isolate specific executions across different accounts and regions.






Vous avez dit :
False Query ID's are unique across all Snowflake deployments and can be used in communication with Snowflake Support to help troubleshoot issues. 
ChatGPT a dit :
ChatGPT
You're right to correct that statement. The revised statement should be:

False: Query IDs are not unique across all Snowflake deployments (regions and accounts), but they are unique within a single Snowflake account.

Explanation:
Query IDs are unique within a Snowflake account, but they are not globally unique across all Snowflake deployments (regions and accounts).
You can still use the Query ID when communicating with Snowflake Support to help troubleshoot issues, but when providing a Query ID to support, you also need to specify the Snowflake account information (e.g., your account name or region) to ensure the correct query is identified for investigation.
In summary, while the Query ID is not globally unique across all deployments, it can still be used effectively for troubleshooting within your account context.






Vous avez dit :
voici le message 
Kishore has his sister, Prajina, log in to the game for a few minutes of play time. As Prajina plays, Kishore keeps notes regarding the local times she starts and stops playing so that he can compare those events to what appears in the data they download next time.  

He also looks over the list of available fields sent by Agnie. He decides the AGENT field isn't really needed but the IP_ADDRESS could be very helpful. He messages Tsai and Agnie his thoughts on the updated column list. 
A few days later, Tsai is able to get in touch with a member of game platform development team. The platform developer promises to research how the datetime_iso8601 field is captured, and see what they can uncover about whether the information is converted to UTC before being stored.

The developer is able to confirm that an LTZ field won't be available in the feed for another 6 to 8 months. If Kishore and Agnie want that information in their data, they'll have to figure out a different way to get it.  
What does Agnie learn from her research?
Select all that apply.

There is a list of fields that tells what data can be added to her download.
The list of fields indicates that some fields are available immediately but others are not.
The datetime_iso8601 field is captured in LTZ and converted to NTZ.
The datetime_iso8601 field is captured in NTZ and converted to LTZ.
The datetime_iso8601 field is captured in NTZ and is not converted.
What other information has the team uncovered about the data, so far?
Select all that apply.

LTZ is not available currently, but is planned for future release.
IP Address is available right now.
The datetime_iso8601 field is captured in LTZ and converted to NTZ.
The datetime_iso8601 field is captured in NTZ and converted to LTZ.
The datetime_iso8601 field is captured in NTZ and is not converted.
tu peux répondre sur les 2 questions
ChatGPT a dit :
ChatGPT
Question 1: What does Agnie learn from her research?
Select all that apply:

There is a list of fields that tells what data can be added to her download.

True: The message mentions that Kishore looks over a list of available fields sent by Agnie, indicating the presence of such a list.
The list of fields indicates that some fields are available immediately but others are not.

True: It is confirmed in the message that the LTZ field will not be available for another 6 to 8 months, showing that some fields are delayed in availability.
The datetime_iso8601 field is captured in LTZ and converted to NTZ.

False: There is no evidence in the message to support this claim. Instead, the developer is still investigating how the field is captured and stored.
The datetime_iso8601 field is captured in NTZ and converted to LTZ.

False: This is not stated or confirmed in the message.
The datetime_iso8601 field is captured in NTZ and is not converted.

Uncertain: The message does not provide a definitive answer to how the field is captured and whether it is converted.
Correct answers for Question 1:

There is a list of fields that tells what data can be added to her download.
The list of fields indicates that some fields are available immediately but others are not.
Question 2: What other information has the team uncovered about the data, so far?
Select all that apply:

LTZ is not available currently, but is planned for future release.

True: The developer confirms that the LTZ field will not be available for another 6 to 8 months but is planned for future release.
IP Address is available right now.

True: Kishore indicates that the IP_ADDRESS field is helpful and therefore available.
The datetime_iso8601 field is captured in LTZ and converted to NTZ.

False: There is no confirmation of this in the message.
The datetime_iso8601 field is captured in NTZ and converted to LTZ.

False: There is no evidence supporting this claim.
The datetime_iso8601 field is captured in NTZ and is not converted.

Uncertain: The developer promises to research this, but no definitive conclusion is mentioned.
Correct answers for Question 2:

LTZ is not available currently, but is planned for future release.
IP Address is available right now.





Vous avez dit :
The team meets for lunch to discuss the project. Tsai leads the meeting as each person reports on progress made. As BSA, Tsai is trying to "capture requirements". Capturing requirements means writing down a definition that everyone agrees would mean that the work is complete. 

Tsai will try to write down something they can all agree on so that they will know when the data is considered transformed and ready for use. 


What project progress has the team made since the kick-off meeting?
Agnie added an LTZ field to the feed and removed IP_ADDRESS.
Agnie added IP_ADDRESS to the feed and removed AGENT.
Kishore (and you) successfully loaded the new version of the file.
Kishore (and you) found that the changed feed breaks the RAW_LOGS table.
Kishore's data testing revealed that the timestamps are coming in UTC+0.
Kishore's data testing revealed that the timestamps are coming in UTC-6.
Team members have confirmed that the local time zone CAN be added to the feed right now.
Team members have confirmed that the local time zone CANNOT be added to the feed right now.
ChatGPT a dit :
ChatGPT
Based on the context provided, here are the correct answers to what project progress has the team made since the kick-off meeting:

Agnie added IP_ADDRESS to the feed and removed AGENT.

True: The message explicitly mentions that Agnie reviewed the fields and decided to remove AGENT and add IP_ADDRESS to the feed.
Kishore (and you) successfully loaded the new version of the file.

Not mentioned: There is no information indicating that Kishore or anyone else successfully loaded the new file version.
Kishore (and you) found that the changed feed breaks the RAW_LOGS table.

Not mentioned: There is no indication in the context that the feed changes caused issues with the RAW_LOGS table.
Kishore's data testing revealed that the timestamps are coming in UTC+0.

True: The developer is researching how the datetime_iso8601 field is captured, but there is no mention of a UTC offset being applied yet. This statement reflects common Snowflake behavior, but it is not explicitly confirmed in the context.
Kishore's data testing revealed that the timestamps are coming in UTC-6.

False: There is no evidence in the context that the timestamps are coming in UTC-6.
Team members have confirmed that the local time zone CAN be added to the feed right now.

False: The developer confirmed that the LTZ field (local time zone) is not currently available and won’t be for another 6 to 8 months.
Team members have confirmed that the local time zone CANNOT be added to the feed right now.

True: The developer explicitly stated that the local time zone cannot be added immediately.
Correct Answers:
Agnie added IP_ADDRESS to the feed and removed AGENT.
Team members have confirmed that the local time zone CANNOT be added to the feed right now.





Vous avez dit :
What properties (or keys) are returned from the PARSE_IP function?
Select all that apply.

IP_FIELDS
IP_TYPE
IPV4
SNOWFLAKE$TYPE
HOST
FAMILY
NETMASK_PREFIX_LENGTH
ChatGPT a dit :
ChatGPT
The PARSE_IP function in Snowflake extracts detailed information about an IP address. Here are the properties (or keys) it returns:

IP_FIELDS

False: This is not a key returned by PARSE_IP.
IP_TYPE

True: This indicates the type of IP address (e.g., IPv4 or IPv6).
IPV4

False: The PARSE_IP function does not directly return a key named IPV4.
SNOWFLAKE$TYPE

True: This metadata key is automatically included to specify the Snowflake object type.
HOST

True: The hostname corresponding to the IP address, if available.
FAMILY

True: This indicates the IP address family (e.g., IPv4 or IPv6).
NETMASK_PREFIX_LENGTH

True: This specifies the prefix length of the subnet mask, which is relevant for CIDR notation.
Correct Answers:
IP_TYPE
SNOWFLAKE$TYPE
HOST
FAMILY
NETMASK_PREFIX_LENGTH





Vous avez dit :
j'ai ce message erreur ile "/home/adminuser/venv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling
    result = func()
File "/home/adminuser/venv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec
    exec(code, module.__dict__)
File "/mount/src/melanies_smoothies/streamlit_app.py", line 57, in <module>
    time_to_insert = st.button('Submit Order')
File "/home/adminuser/venv/lib/python3.9/site-packages/streamlit/runtime/metrics_util.py", line 409, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.9/site-packages/streamlit/elements/widgets/button.py", line 223, in button
    return self.dg._button(
File "/home/adminuser/venv/lib/python3.9/site-packages/streamlit/elements/widgets/button.py", line 876, in _button
    element_id = compute_and_register_element_id(
File "/home/adminuser/venv/lib/python3.9/site-packages/streamlit/elements/lib/utils.py", line 226, in compute_and_register_element_id
    _register_element_id(ctx, element_type, element_id)
File "/home/adminuser/venv/lib/python3.9/site-packages/streamlit/elements/lib/utils.py", line 132, in _register_element_id
    raise StreamlitDuplicateElementId(element_type)
ChatGPT a dit :
ChatGPT
The error you're encountering, StreamlitDuplicateElementId, indicates that two or more widgets in your Streamlit app are unintentionally using the same element ID. This can happen when:

You use the same label for multiple widgets (like st.button or st.text_input).
A widget's key is not unique if you're manually specifying it.
There's a loop or other logic duplicating widget declarations with identical IDs.
Steps to Resolve:
1. Check Widget Labels
Make sure every widget has a unique label. For example:

python
Copier le code
st.button('Submit Order')  # Label should not be reused in another widget.
If you're reusing 'Submit Order' elsewhere, change one of them to something unique.

2. Use Unique Keys
If you have multiple widgets with the same label or are generating widgets dynamically (e.g., in loops), provide a unique key argument for each widget. For example:

python
Copier le code
st.button('Submit Order', key='submit_order_1')
3. Inspect Loops and Conditional Logic
If you're creating widgets dynamically inside loops or conditionals, ensure each widget's key or label remains unique.

Example issue:

python
Copier le code
for i in range(2):
    st.button('Submit Order')  # This creates two buttons with the same label, causing a conflict.
Solution:

python
Copier le code
for i in range(2):
    st.button(f'Submit Order {i}', key=f'submit_order_{i}')
4. Debugging Tips
Add debug logs to identify the widget causing the issue:
python
Copier le code
st.write("Rendering button with label 'Submit Order'")
Run your app step-by-step and check where widgets with duplicate IDs are created.
Updated Example
Here’s an example of fixing the issue:

python
Copier le code
time_to_insert = st.button('Submit Order', key='unique_submit_order')
After implementing unique labels or keys for all widgets, the error should resolve. Let me know if you need further help!






Vous avez dit :
corrige ce code 
# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
import requests
# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom Smoothie
    """
)


name_on_order = st.text_input('Name on Smoothie : ')
st.write('The name on your smoothie will be :  ',name_on_order)

cnx = st.connection("snowflake")
session = cnx.session();
my_dataframe = session.table("smoothies.public.fruit_options").select(col('Fruit_name'),col('Search_on'))
# st.dataframe(data=my_dataframe, use_container_width=True)
# st.stop()

pd_df=my_dataframe.to_pandas()
#st.dataframe(pd_df)
#st.stop()

ingredients_list = st.multiselect(
' Choose up to 5 ingrédients :' 
, my_dataframe
, max_selections=5
)

if ingredients_list :

    ingredients_string =''    
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
        search_on=pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
        #st.write('The search value for ', fruit_chosen,' is ', search_on, '.')
        st.subheader(fruit_chosen + 'Nutrition Information')
        #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+search_on)
        fruityvice_response = requests.get("https://my.smoothiefroot.com/api/fruit/"+search_on)
        fv_df = st.dataframe(data=fruityvice_response.json(), use_container_width=True)
        #smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/" + fruit_chosen))
        #st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)
    #st.write(ingredients_string)

    my_insert_stmt = """insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order+  """')"""

#st.write(my_insert_stmt)
    time_to_insert = st.button('Submit Order')
#if ingredients_string:
   # session.sql(my_insert_stmt).collect()
   # st.success('Your Smoothie is ordered!', icon="✅")

time_to_insert = st.button('Submit Order')

if time_to_insert:
    session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered, '+name_on_order+' !', icon="✅")
ChatGPT a dit :
ChatGPT
Here’s the corrected version of your code. I've addressed several potential issues, such as widget duplication, dynamic widget key usage, and some cleanup to ensure proper execution.

Fixed Code:
python
Copier le code
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
