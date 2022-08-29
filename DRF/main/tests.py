import pytest
from rest_framework.test import APIClient, APITestCase


from main.models import Level, Company


client = APIClient()


@pytest.mark.django_db(True)
class Base_test(APITestCase):
    def setUp(self):
        Level.objects.create(name='test 1')
        Company.objects.create(name='kek lol')

    def test_admin_add_company(self):
        client.login(username='admin', password='admin')

        response = self.client.post('/company/', {
            'name': 'second company',
            'cooperation': '1'
        })
        print(response.status_code, response.data)

    def test_create_office(self):
        response = self.client.post('/office/', {
            'name': 'test office',
            'location': 'BH',
            'company': '1'
        })
        print(response.data)
        self.assert_(response.data['name'] == 'test office')

    def test_fail_create_office(self):
        response = self.client.post('/office/', {
            'name': 'test office',
            'location': 'BH',
            'company': '5'
        })
        self.assert_(response.status_code == 400)

    def test_add_level(self):
        response = self.client.post('/level/', {'name':'kek'})
        print(response.status_code)
        self.assert_(response.status_code == 201)
        self.assert_(response.data['name'] == 'kek')
    def test_office_list(self):
        response = self.client.get('/level/')
        print(response.data)
        assert response.status_code == 200


    def test_company_list(self):

        response = self.client.get('/company/')
        print(response.data)
        assert response.status_code == 200


