from django.db import models
from django_countries.fields import CountryField

from main.abstract_models import CreatedAt, UpdatedAt, SoftDelete


# from DRF.main.abstract_models import CreatedAt, UpdatedAt, SoftDelete


class Offices(CreatedAt, UpdatedAt, SoftDelete):
    name = models.CharField(max_length=100)
    location = CountryField()
    company = models.ForeignKey('Company',
                                on_delete=models.CASCADE,
                                related_name='Office_company')

    def __str__(self):
        return self.name


class Company(CreatedAt, UpdatedAt, SoftDelete):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField('Employer',
                                       blank=True,
                                       related_name="Company_employees")
    cooperation = models.ManyToManyField('Company',
                                         blank=True,
                                         related_name="Company_cooperation")

    def __str__(self):
        return self.name

    @property
    def num_office(self):
        return Offices.objects.filter(company=self.id).count()

    @property
    def num_employees(self):
        return self.employees.count()


class Person(CreatedAt, UpdatedAt, SoftDelete):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, default=None)
    age = models.IntegerField()
    languages = models.ManyToManyField('Languages',
                                       blank=True,
                                       related_name='Person_languages')
    skills = models.ManyToManyField('Skills',
                                    blank=True,
                                    related_name='Person_skills')

    def __str__(self):
        return self.name


class Skills(models.Model):
    name = models.CharField(max_length=100)
    level = models.ForeignKey('Level',
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name="Skill_level")

    def __str__(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(max_length=100)
    level = models.ForeignKey('Level',
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name="Languages_level")

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employer(CreatedAt, UpdatedAt, SoftDelete):
    job_title = models.CharField(max_length=100)
    person_id = models.ForeignKey('Person',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  related_name="Employer_person_id")

    def __str__(self):
        return self.job_title
