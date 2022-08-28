from rest_framework import generics, viewsets, permissions
from rest_framework.permissions import AllowAny

from main.models import (Company, Employer,
                             Offices, Person, Skills,
                             Languages,  Level)
from main.permissions import IsAdminOrReadOnly
from main.serializers import (OfficeSerializer, CompanySerializer,
                                  PersonSerializer, EmployerSerializer,
                                  SkillSerializer, LanguagesSerializer,
                                  LevelSerializer)


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Offices.objects.filter(is_active=True)
    serializer_class = OfficeSerializer
    permission_classes = (AllowAny,)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanySerializer
    permission_classes = (IsAdminOrReadOnly,)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.filter(is_active=True)
    serializer_class = PersonSerializer
    permission_classes = (IsAdminOrReadOnly,)


class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.filter(is_active=True)
    serializer_class = EmployerSerializer
    permission_classes = (IsAdminOrReadOnly,)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAdminOrReadOnly,)


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = (AllowAny,)


class LanguagesViewSet(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer
    permission_classes = (IsAdminOrReadOnly,)
