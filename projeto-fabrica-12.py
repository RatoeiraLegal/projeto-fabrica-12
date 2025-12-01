import pandas as pd

pd.set_option('display.max_rows', None)

# Removendo Colunas sem informações.
dados = pd.read_csv("Tabela_Clubes.csv", header=0)
dados = dados.iloc[0:,:13]

# Mostre as primeiras linhas do DataFrame
print(f"{dados.head(10)}\n")

# Quais os times aparecem na tabela e quantas vezes cada um aparece?
print(dados['Clubes'].value_counts())
print()

# Quantos times diferentes temos no DataFrame?
print(f"Temos {(dados['Clubes'].nunique())} times diferentes")
print()

# Quais os anos que aparecem no DataFrame?
a = dados['Ano'].sort_values()
uniq = a.unique()
print(uniq)
print()

# Quais os campeões de cada ano?
print(dados[dados['Pos.'] == 1])
print()

# Qual o time que foi mais vezes campeão?
print(f"O time campeão com mais vitórias é o {dados[dados['Pos.'] == 1]['Clubes'].value_counts().idxmax()} com {dados[dados['Pos.'] == 1]['Vitorias'].sum()} vitórias\n")

# Agora uma piada 😄, quais times paulistas não aparecem nenhuma vez como campeão?
print("EU NÃO SEI QUAIS SÃO PAULISTAS!\n")

# Qual o time com mais derrotas?
# print(f"O time com mais derrotas é o {dados["Clubes"]} com ")
max_derrotas = dados.loc[dados["Derrotas"].idxmax()]

print("Time com mais derrotas:", max_derrotas["Clubes"])
print("Quantidade de derrotas:", max_derrotas["Derrotas"])

min_derrotas = dados.loc[dados["Derrotas"].idxmin()]

print("Time com mais derrotas:", min_derrotas["Clubes"])
print("Quantidade de derrotas:", min_derrotas["Derrotas"])

max_estrangeiros = dados.loc[dados["Estrangeiros"].idxmax()]
print(max_estrangeiros["Clubes"])

min_estrangeiros = dados.loc[dados["Estrangeiros"].idxmin()]
print(min_estrangeiros["Clubes"])
#{dados['Clubes']['Derrotas'].sum()} derrotas\n
# Qual o time com maior número de estrangeiros?
# print(f"O time com maior número de estrangeiros é o {dados[]}")