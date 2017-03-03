# -*- coding: utf-8 -*- 
from django.db import models

class WorkExperience(models.Model):
    position = models.CharField(verbose_name="Stanowisko", max_length=30)
    position_en = models.CharField(verbose_name="Stanowisko EN", max_length=30)
    company_name = models.CharField(verbose_name="Nazwa firmy", max_length=50)
    date_start = models.DateField(verbose_name="Rozpoczęcie pracy")
    date_end = models.DateField(vebose_name="Zakończenie pracy", null = True, blank=True, default=True)
    description = models.TextField(verbose_name="Opis stanowiska")
    description_en = models.TextField(verbose_name="Opis stanowiska")
    www = models.CharField(verbose_name="Strona WWW", max_length=100, null=True, blank=True)
    
class Education(models.Model):
    faculty = models.CharField(verbose_name="Wydział", max_length=50)
    faculty_en = models.CharField(verbose_name="Wydział EN", max_length=50)
    field_of_study = models.CharField(verbose_name="Kierunek", max_length=50)
    field_of_study_en = models.CharField(verbose_name="Kierunek EN", max_length=50)
    specialization = models.CharField(verbose_name="Specjalizacja", max_length=50)
    specialization_en = models.CharField(verbose_name="Specjalizacja EN", max_length=50)
    date_start = models.DateField(verbose_name="Rozpoczęcie nauki")
    date_end = models.DateField(vebose_name="Zakończenie zakończenie", null = True, blank=True, default=True)
    
class ProgrammingSkills(models.Model):
    name = models.CharField(verbose_name="Nazwa", max_length=50)
    value = models.IntegerField(verbose_name="Wartość %", min_value=1, max_value=100)