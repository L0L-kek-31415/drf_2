from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin


from main.models import (Company, Employer, Offices,
                         Person, Skills, Level,
                         Languages)


class OfficeSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Offices
        exclude = ('is_active', )


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ('is_active', )


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        exclude = ('is_active', )


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        exclude = ('is_active', )

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = "__all__"


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = "__all__"
