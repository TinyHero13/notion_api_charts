import requests
import pandas as pd
import streamlit as st

class Notion():
    def __init__(self):
        self.token = st.secrets["TOKEN"]
        self.databaseID = st.secrets["DATABASEID"]
        self.headers = {
                "Authorization": "Bearer " + self.token,
                "Content-Type": "application/json",
                "Notion-Version": "2022-02-22"
            }
    
    def get_data(self):
        readUrl = f"https://api.notion.com/v1/databases/{self.databaseID}/query"
        res = requests.request("POST", readUrl, headers=self.headers)
        data = res.json()
        return data

    def dataframe_notion(self):
        data = self.get_data()
        df_notion = pd.DataFrame(data['results'])
        df_notion['tools'] = df_notion['properties'].apply(lambda x: x['Ferramenta']['select']['name'] if x['Ferramenta']['select'] is not None else None)
        df_notion['category'] = df_notion['properties'].apply(lambda x: x['Categoria']['select']['name'] if x['Categoria']['select'] is not None else None)
        df_notion['Type'] = df_notion['properties'].apply(lambda x: x['Tipo']['select']['name'] if x['Tipo']['select'] is not None else None)
        df_notion.drop(columns=['properties', 'public_url', 'icon', 'url', 'created_by', 'last_edited_by', 'cover', 'parent', 'archived', 'in_trash', 'object'], inplace=True)
        return df_notion

