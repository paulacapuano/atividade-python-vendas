import pandas as pd

clientes_df = pd.read_csv("clientes.csv")
pedidoss_df = pd.read_csv("pedidos.csv")

merged_df = pd.merge(clientes_df, pedidoss_df, left_on="id", right_on="cliente_id")

grouped_df_count = merged_df.groupby(["nome"]).agg({"valor_total": "count"})
grouped_df_sum = merged_df.groupby(["nome"]).agg({"valor_total": "sum"})
grouped_df_max = merged_df.groupby(["nome"]).agg({"valor_total": "max"})
grouped_df_min = merged_df.groupby(["nome"]).agg({"valor_total": "min"})

print("-" * 100)
print(grouped_df_count)
print("-" * 100)
print(grouped_df_sum)
print("-" * 100)
print(grouped_df_max)
print("-" * 100)
print(grouped_df_min)