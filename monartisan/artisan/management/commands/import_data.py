import pandas as pd
from artisan.models import Artisan  # Assurez-vous que ce chemin est correct par rapport à l'emplacement de votre modèle
from django.core.management.base import BaseCommand
import re
from django.utils import timezone
from django.db import models



class Command(BaseCommand):
    help = 'Import data from Excel file into Artisan model'

    def handle(self, *args, **kwargs):
        # Lire le fichier Excel
        df = pd.read_excel('/Users/sic/Documents/CodeSource/Python/MonArtisan/monartisan/artisan/base_epurer.xlsx')

        # Fonction pour transformer un nom de colonne en identificateur valide
        def to_valid_identifier(column_name):
            
            column_name = column_name.replace(' ', '_')
            if re.match(r'^\d', column_name):
                column_name = f'col_{column_name}'
            column_name = re.sub(r'\W|^(?=\d)', '_', column_name)
            column_name = re.sub(r'__+', '_', column_name)
            # Réduire la longueur du nom à 63 caractères maximum
            column_name = column_name[:63]
            # S'assurer que le nom ne se termine pas par un underscore
            column_name = column_name.rstrip('_')
            return column_name

    
        # Map columns to field names
        df.columns = [to_valid_identifier(col) for col in df.columns]

        # Obtenir les noms des champs du modèle Artisan
        model_fields = [f.name for f in Artisan._meta.get_fields()]

        # Insérer les données dans la base de données
        for index, row in df.iterrows():
            row_data = {}
            for key, value in row.to_dict().items():
                if key in model_fields:
                    field = Artisan._meta.get_field(key)
                    if isinstance(field, models.DateTimeField):
                        if pd.isna(value):
                            value = None
                        else:
                            value = timezone.make_aware(pd.to_datetime(value)) if not pd.isna(value) else None
                    row_data[key] = value

            artisan = Artisan(**row_data)
            artisan.save()
        
        self.stdout.write(self.style.SUCCESS('Données importées avec succès'))

# Pour exécuter ce script, placez-le dans un fichier de commande personnalisée dans Django
# Par exemple, placez ce fichier dans app_name/management/commands/import_data.py
# Ensuite, exécutez la commande suivante depuis le terminal : 
# python manage.py import_data
