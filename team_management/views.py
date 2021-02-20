from django.shortcuts import render
from team_management.models import resource_type,resource, task as t
from team_management.querys import *
def task(request):
    # resource_type.objects.create(description_text = "TC")
    # new_resource = resource_type(description_text = "PM")
    # new_resource.save()
    tasks_of_resource = t.objects.all()
    tasks = tasks_of_resource.values()
    resource_id = tasks[0]["idresource_id"]
    resources_names  = get_names_resources()
    resource_in_charge = resource.objects.filter(idresource = resource_id)[0]

    data = {"template" : "task.html", "resources_names":resources_names , "tasks": tasks,"resource": resource_in_charge, }
    return render(request, "main.html", context=data)

def calendar(request):
    resources_names  = get_names_resources()
    data = {"template": "calendar.html", "resources_names":resources_names}
    return render(request, "main.html", context=data)




