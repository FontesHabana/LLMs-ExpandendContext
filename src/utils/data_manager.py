import csv

csv_file_path='data/raw/murder_mystery.csv'

data_list=[]

try:
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        dict_reader=csv.DictReader(file, delimiter=',')
        print(f"Nombres de columnas: {dict_reader.fieldnames}")
        for row_dict in dict_reader:
            data_list.append(row_dict)
except FileNotFoundError:
    print("archivo no encontrado")
except Exception as e:
    print(f"Error: {e}")

