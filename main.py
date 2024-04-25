import streamlit as st
import plotly.express as px
from notion_data import Notion

st.set_page_config(layout="wide")

notion = Notion()
df_notion = notion.dataframe_notion()

st.header('Visão geral bookmark')

col1, col2 = st.columns((2, 2))

category_df = df_notion['category'].value_counts(ascending=True).reset_index()
category_df.columns = ['category', 'count']

fig_category = px.bar(category_df,  x='count', y='category', title='Categorias', orientation='h', text_auto=True)


tools_df = df_notion['tools'].value_counts(ascending=True).reset_index()
tools_df.columns = ['tools', 'count']

fig_tools = px.bar(tools_df, x='count', y='tools', title='Ferramentas', orientation='h', 
                   text_auto=True)

with col1:
    st.plotly_chart(fig_category)

with col2:
    st.plotly_chart(fig_tools)
