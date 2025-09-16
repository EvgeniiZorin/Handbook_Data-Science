import streamlit as st
import pandas as pd
import plotly_express as px


st.title('Data Visualisation App')

if "my_input" in st.session_state:
    if st.session_state['my_input'] == "":
        st.write("Welcome, stranger!")
    else:
        st.write("Welcome to my app, ", st.session_state['my_input'])
else:
    st.write('Welcome, stranger!')

# sidebar
# st.sidebar.success('select a page above.')
st.sidebar.subheader('Visualisation Settings')




# setup file upload
uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or Excel file.",
                         type=['csv', 'xlsx'])

global df
if uploaded_file is not None:
    print(uploaded_file)
    print('hello')
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

# global numeric_columns
try:
    st.write(df)
    numeric_columns  = list(df.select_dtypes(['float', 'int']).columns)
except Exception as e:
    print(e)
    st.write('Please upload file to the application!')

# add a select widget to the side bar
chart_select = st.sidebar.selectbox(
    label='select the chart type',
    options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
)


if chart_select == 'Scatterplots':
    st.sidebar.subheader('Scatterplot Settings')
    try:
        x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values)
        # display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

