import pandas as pd
 
df_infinitive = pd.read_csv("verbs.csv", delimiter=",", index_col=None)
df_forms = pd.read_csv("forms.csv", delimiter=",", index_col=None)

df_final = pd.merge(df_infinitive, df_forms, on="infinitive")
column_names = ["translation", "infinitive", "sg_Ip_form", "sg_IIp_form", "sg_IIIp_form", "pl_Ip_form", "pl_IIp_form", "pl_IIIp_form"]

df_final.columns = column_names

print(df_final.head())
'''
col_list = list(df.columns)
x, y = col_list.index(0), col_list.index(1)
col_list[y], col_list[x] = col_list[x], col_list[y]
df = df[col_list]
'''

df_final.to_csv("verbs_final.csv", index=False, header=True)