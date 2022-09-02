from django.shortcuts import render
import apps.config as cf
import pymysql

# Tupla = (1,2,3,4,5,6,7,8)
# Array = []
# Diccionario = {}
def multiform(form):
    """
    Toma un diccionario de la forma {'a[b][c]': 'd', 'e[f][g]': 'h'} y devuelve {'a': {'b': {' c':
    'd'}}, 'e': {'f': {'g': 'h'}}}
    
    :param form: Los datos del formulario que desea convertir en un diccionario
    """
    data = {}
    for url_k in form:
        v = form[url_k]
        ks = []
        while url_k:
            if '[' in url_k:
                k, r = url_k.split('[', 1)
                ks.append(k)
                if r[0] == ']':
                    ks.append('')
                url_k = r.replace(']', '', 1)
            else:
                ks.append(url_k)
                break
        sub_data = data
        for i, k in enumerate(ks):
            if k.isdigit():
                k = int(k)
            if i+1 < len(ks):
                if not isinstance(sub_data, dict):
                    break
                if k in sub_data:
                    sub_data = sub_data[k]
                else:
                    sub_data[k] = {}
                    sub_data = sub_data[k]
            else:
                if isinstance(sub_data, dict):
                    sub_data[k] = v
    return data

def get_connection ():
    return pymysql.connect (host=cf.DB_HOST, database=cf.DB_SCHEMA, user=cf.DB_USER, password=cf.DB_PASS)

def getDashboard (request):
    return render(request, "dashboard.html")