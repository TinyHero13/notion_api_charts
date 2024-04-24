import streamlit as st
import plotly.express as px
from notion_data import dataframe_notion

df_notion = dataframe_notion()

st.text('Notion bookmark overview')

category_counts = df_notion['category'].value_counts().reset_index()
category_counts.columns = ['category', 'count']

fig = px.bar(category_counts, x='category', y='count', title='Categorias')
st.plotly_chart(fig)

st.dataframe(df_notion)
