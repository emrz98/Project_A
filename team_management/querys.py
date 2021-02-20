from team_management.models import resource_type,resource, task as t


def get_names_resources():
    names = []
    all_resources = resource.objects.all()
    values_all_resources = all_resources.values()
    for item in values_all_resources:
        name = item["name"]
        names.append(name)
    return names