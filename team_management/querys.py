from team_management.models import resource_type,resource, task as t


def get_names_resources():
    all_resources = resource.objects.all().values()
    names = [resource["name"] for resource in all_resources]
    return names