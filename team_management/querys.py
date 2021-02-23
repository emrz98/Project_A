from team_management.models import resource_type,resource, task as t


def get_names_resources():
    all_resources = resource.objects.all().values()
    names = [resource["name"] for resource in all_resources]
    return names

def get_type_resources_names(type_resources):
    idresource_type = resource_type.objects.filter(description_text = type_resources).values()[0]["idresource_type"]
    all_names = [resource["name"] for resource in resource.objects.filter(idresource_type = idresource_type).values()]
    return all_names

def get_names_tcs():
    return get_type_resources_names("TC")
    
def get_names_pms():
    return get_type_resources_names("PM")