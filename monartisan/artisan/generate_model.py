import pandas as pd
import re

# Lire les colonnes du fichier Excel
df = pd.read_excel('/Users/sic/Documents/CodeSource/Python/MonArtisan/monartisan/artisan/excel_data.xlsx')

# Récupérer les noms des colonnes
columns = df.columns

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

# Fonction pour transformer un nom de colonne en identificateur valide
def to_valid_identifier(column_name):
    # Remplacer les espaces par des underscores
    column_name = column_name.replace(' ', '_')
    # Ajouter un préfixe si le nom commence par un chiffre
    if re.match(r'^\d', column_name):
        column_name = f'col_{column_name}'
    # Supprimer ou remplacer les caractères non alphanumériques restants
    column_name = re.sub(r'\W|^(?=\d)', '_', column_name)
    # Remplacer les doubles underscores par un seul underscore
    column_name = re.sub(r'__+', '_', column_name)
    
    # Réduire la longueur du nom à 63 caractères maximum
    column_name = column_name[:63]
    # S'assurer que le nom ne se termine pas par un underscore
    column_name = column_name.rstrip('_')
    return column_name

# Générer les champs du modèle Django
model_fields = []
for column in columns:
    field_name = to_valid_identifier(column)
    field_type = get_field_type(df[column].dtype)
    verbose_name = column  # Conserver le nom original pour verbose_name
    model_fields.append(f"    {field_name} = {field_type} # verbose_name='{verbose_name}'")

# Nom du modèle
model_name = "ENQArtisan"

# Générer le modèle Django
model_code = f"""
from django.db import models

class {model_name}(models.Model):
"""
model_code += "\n".join(model_fields)
model_code += """

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.metier}"
"""

# Écrire le modèle dans un fichier
with open('/Users/sic/Documents/CodeSource/Python/MonArtisan/monartisan/artisan/models.py', 'w') as f:
    f.write(model_code)

print("Modèle Django généré avec succès.")
