import csv

def ler(filename):
    dados = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dados.append(dict(row))
    return dados


def salvar(lista, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=lista[0].keys())
        writer.writeheader()
        for item in lista:
            writer.writerow(item)

def busca_por_id(id, filename):
    dados = ler(filename)
    return next((item for item in dados if item["id"] == id), None)