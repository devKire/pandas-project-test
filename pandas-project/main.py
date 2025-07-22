import pandas as pd

# Caminho do arquivo
df_gka = pd.read_excel('bases/ATA_GKA_21.07.xlsx')
df_others = pd.read_excel('bases/ATA_OTHERS_21.07.xlsx')


# Lista o nome de todas as abas (sheets)
planilhas_gka = pd.ExcelFile('bases/ATA_GKA_21.07.xlsx')
print('ABAS DA PLANILHA GKA:')
print(planilhas_gka.sheet_names)

planilhas_others = pd.ExcelFile('bases/ATA_OTHERS_21.07.xlsx')
print('ABAS DA PLANILHA OTHERS:')
print(planilhas_others.sheet_names)


# ✅ Carregar diretamente a aba "RISCO"
df_risco_gka = pd.read_excel('bases/ATA_GKA_21.07.xlsx', sheet_name='RISCO')
df_risco_others = pd.read_excel('bases/ATA_OTHERS_21.07.xlsx', sheet_name='RISCO')

# ✅ Visualizar os dados
print("Dados da aba 'RISCO' da planilha GKA:")
print(df_risco_gka.columns)
print("Dados da aba 'RISCO' da planilha OTHERS:")
print(df_risco_others.columns)


# ✅ Consolida os dados (empilha verticalmente)
df_consolidado = pd.concat([df_risco_gka, df_risco_others], ignore_index=True)

# ✅ Visualiza os primeiros registros
print(df_consolidado.head())

# ✅ Quantidade total de linhas
print(f'\nTotal de registros consolidados: {len(df_consolidado)}')