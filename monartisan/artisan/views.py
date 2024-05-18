from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import pandas as pd 


# Dictionnaire pour mapper les types de données pandas aux types de champs Django
dtype_mapping = {
    'int64': 'models.IntegerField()',
    'float64': 'models.FloatField()',
    'object': 'models.CharField(max_length=255)',
    'bool': 'models.BooleanField()',
    'datetime64[ns]': 'models.DateTimeField()'
}

# Fonction pour deviner le type de champ Django basé sur le type de données pandas
def get_field_type(dtype):
    return dtype_mapping.get(dtype.name, 'models.CharField(max_length=255)')

# Générer les champs du modèle Django


def index(request):
    path = "/Users/sic/Documents/CodeSource/Python/MonArtisan/monartisan/artisan/excel_data.xlsx"
    data = pd.read_excel(path)
    columns = data.columns
    model_fields = []
    for column in columns:
        field_type = get_field_type(data[column].dtype)
        model_fields.append(f"    {column} = {field_type}")
    

    # for colonne in data.columns:
    #     print(colonne)
    # for index,ligne in data.iterrows():
    #     print("Index de ligne :",index)
    #     print("Contenu de la ligne :",ligne)
    
    
    print(len(data))
    return HttpResponse("Hello, world. You're at the polls index.")