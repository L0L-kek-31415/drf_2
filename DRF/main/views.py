from rest_framework import generics, viewsets, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from main.models import (Company, Employer,
                             Offices, Person, Skills,
                             Languages,  Level)
from main.permissions import IsAdminOrReadOnly
from main.serializers import (OfficeSerializer, CompanySerializer,
                                  PersonSerializer, EmployerSerializer,
                                  SkillSerializer, LanguagesSerializer,
                                  LevelSerializer)


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.soft_delete()
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OfficeViewSet(BaseViewSet):
    queryset = Offices.objects.filter(is_active=True)
    serializer_class = OfficeSerializer
    permission_classes = (AllowAny,)




class CompanyViewSet(BaseViewSet):
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanySerializer


class PersonViewSet(BaseViewSet):
    queryset = Person.objects.filter(is_active=True)
    serializer_class = PersonSerializer
    permission_classes = (IsAdminOrReadOnly,)


class EmployerViewSet(BaseViewSet):
    queryset = Employer.objects.filter(is_active=True)
    serializer_class = EmployerSerializer
    permission_classes = (IsAdminOrReadOnly,)


class SkillViewSet(BaseViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (IsAdminOrReadOnly,)


class LevelViewSet(BaseViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = (AllowAny,)


class LanguagesViewSet(BaseViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer
    permission_classes = (IsAdminOrReadOnly,)
