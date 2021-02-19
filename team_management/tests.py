from django.test import TestCase
from team_management.models import resource_type
# Create your tests here.
class ResourceTestCase(TestCase):
    def setUp(self):
        resource_type.objects.create(description_text = "TC")
        new_resource = resource_type(description_text = "PM")
        new_resource.save()

    def get_type_resources(self):
        obj = resource_type.objects.all()
        for i in obj:
            print(i)