from rest_framework import routers
from main.views import (OfficeViewSet, CompanyViewSet,
                                PersonViewSet, EmployerViewSet,
                                SkillViewSet, LanguagesViewSet,
                                LevelViewSet)


router = routers.SimpleRouter()
router.register(r'office', OfficeViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'person', PersonViewSet)
router.register(r'employer', EmployerViewSet)
router.register(r'skill', SkillViewSet)
router.register(r'language', LanguagesViewSet)
router.register(r'level', LevelViewSet)
