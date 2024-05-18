from django.db import models

class Tutor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)

    create_at = models.DateTimeField("date of creation",auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField()
    
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    
    create_at = models.DateTimeField("date of creation",auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField()

COMPANY_DEPARTMENT = [
    ("CEO","Dierecteur général"),
    ("CP","Coordinateur de projet"),
    ("DS","Directeur de service"),
    ("DP","Directeur de département"),
    ("CS","Chef de service"),
    ("CL","Collaborateur"),
]
UVCI_SPECIALITY = [
    ("DAS","Dévéloppement d'application et E-services"),
    ("RSI","Réseaux et sécurité informatique "),
    ("BD","Base de donnée"),
    ("BD","Base de donnée"),
    ("MMX","Multi médias et communication"),
    ("CMD","Communication marqueting digital"),
    ("ATD","..."),
]

class Staff(models.Model):
    first_name = models.CharField(max_length=200)
    last_name  = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    speciality = models.CharField(choices=UVCI_SPECIALITY)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    is_ceo = models.BooleanField(default=False)
    department = models.CharField(choices=COMPANY_DEPARTMENT)
    
    create_at = models.DateTimeField("date of creation",auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField()
    

