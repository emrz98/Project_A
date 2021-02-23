from django.shortcuts import render
from team_management.models import resource_type,resource, task as t
from team_management.querys import *

tc_names = get_names_tcs()
pm_names = get_names_pms()
print("lo hizo")

def calendar(request):
    resources_names  = get_names_resources()
    data = {"resources_names":resources_names, "element_nav":"calendar_nav"}
    return render(request, "calendar.html", context=data)


def task(request):
    # resource_type.objects.create(description_text = "TC")
    # new_resource = resource_type(description_text = "PM")
    # new_resource.save()
    if request.method == "GET":
        resources_names = request.GET.getlist("resource")
        if("All" in resources_names):
            resources_names = get_names_resources()        
        obj_resources = [resource.objects.filter(name = name).values() for name in resources_names]
        ids_resources = [resource[0]["idresource"] for  resource in obj_resources]
        tasks_per_resource ={}
        for i in range(len(obj_resources)):
            tasks  =t.objects.filter(idresource = ids_resources[i])
            tasks_per_resource[resources_names[i]] = tasks
    resources_names  = get_names_resources()
    data = {"resources_names":resources_names , "element_nav":"task_nav", "tasks": tasks_per_resource}
    return render(request, "task.html", context=data)

def projects(request):
    resources_names  = get_names_resources()
    if request.method == "GET":
        resource_selected = request.GET.get("resource")
    data = {"resources_names":resources_names, "elements_nav":"projects_nav", "resource_selected":resource_selected}
    return render(request, "projects.html", context=data)

def details(request):
    resources_names  = get_names_resources()
    data = {"resources_names":resources_names, "element_nav":"details_nav"}
    return render(request, "details.html", context=data)



