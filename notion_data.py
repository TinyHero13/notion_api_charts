import requests
import pandas as pd

def notion_d():
    token = 'secret_u1XebWgmw630Pu9Ckv3x7D3L9tIjZfaYNd11SdsyEDT'
    databaseID ="398823e7b3a940d19497248d5d23d592"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2022-02-22"
    }

    readUrl = f"https://api.notion.com/v1/databases/{databaseID}/query"
    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    return data

def dataframe_notion():
    data = notion_d()
    df_notion = pd.DataFrame(data['results'])
    df_notion['tools'] = df_notion['properties'].apply(lambda x: x['Ferramenta']['select']['name'] if x['Ferramenta']['select'] is not None else None)
    df_notion['category'] = df_notion['properties'].apply(lambda x: x['Categoria']['select']['name'] if x['Categoria']['select'] is not None else None)
    df_notion['Type'] = df_notion['properties'].apply(lambda x: x['Tipo']['select']['name'] if x['Tipo']['select'] is not None else None)
    df_notion.drop(columns=['properties', 'public_url', 'icon', 'url', 'created_by', 'last_edited_by', 'cover', 'parent', 'archived', 'in_trash', 'object'], inplace=True)
    return df_notion

