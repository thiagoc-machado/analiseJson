
from datetime import datetime
import json, os
from functools import wraps
from django.core.cache import cache

def openfile():
    """
        Lê o arquivo JSON e armazena no cache.
        Retorna os dados do arquivo.
    """
    cache_key = 'usuarios_json'
    usuarios = cache.get(cache_key)

    if usuarios is not None:
        print('Retornando do cache')
        return usuarios

    # Lê o arquivo
    print('Lendo o arquivo JSON')
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, 'usuarios.json')

    with open(file_path, 'r') as file:
        usuarios = json.load(file)
    print('Arquivo lido com sucesso')
    # Armazena no cache por 10 minutos (600 segundos)
    cache.set(cache_key, usuarios, timeout=600)
    print('Dados armazenados no cache')
    return usuarios

def processingTime(func):
    """
        Decorador para medir o tempo de processamento de uma função.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        processing_time = datetime.now() - start_time
        processing_time = (f'{processing_time.total_seconds()} miliseconds')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return result, processing_time, timestamp
    return wrapper



    