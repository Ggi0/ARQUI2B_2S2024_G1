import sys
import requests

def get_collections():
    # x = requests.get('http://34.29.61.196:8000/api/data/')
    x = requests.get('http://34.29.61.196:8000/api/colecciones/')

    if x.status_code != 200:
        print(x)
        return []

    collections = []

    total_data = 0
    for item in x.json():
        if item.get('id') not in collections:
            collections.append({
                'id': item.get('id'),
                'nombre': item.get('nombre')
            })
        # print(item.get('data')[0])
        total_data += len(item.get('data'))

    print(f'Data en colecciones: {total_data}')
    return collections


def get_records_counter():
    x = requests.get('http://34.29.61.196:8000/api/data/')

    if x.status_code != 200:
        print(x)
        return 0
    
    return len(x.json())

print(f'Colecciones: {get_collections()}')
print(f'Registros: {get_records_counter()}')
