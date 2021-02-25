from django.shortcuts import render
from team_management.models import resource_type,resource, task as t
from team_management.queries import *
import json
from django.core.serializers.json import DjangoJSONEncoder

def calendar(request):
    print("This works")
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
    projects_resource = None
    project_dic = {}
    resources_names  = get_names_resources()
    if request.method == "GET":
        resource_selected = request.GET.get("resource")
        if(resource_selected != None):
            if(resource_selected == "All"):
                projects_resource = get_projects_resource(get_names_resources()) #doesnt_works
            else:
                projects_resource = get_projects_resource(resource_selected)
            
            for i in range(len(projects_resource)):
                projects_resource[i]["tasks"] = get_tasks_project_of_resource(resource_selected, projects_resource[i]["description_text"])
                projects_resource[i]["description_without_space"] = "-".join(projects_resource[i]["description_text"].split())
                project_dic[projects_resource[i]["description_without_space"]] = projects_resource[i]["tasks"]
            project_dic = json.dumps(project_dic, cls = DjangoJSONEncoder)
    data = {"resources_names":resources_names, 
            "elements_nav":"projects_nav", 
            "resource_selected":resource_selected, 
            "projects_resource":projects_resource,
            "project_dic":project_dic}
    return render(request, "projects.html", context=data)

def details(request):
    resources_names  = get_names_resources()
    all_tasks = []
    all_projects = []
    if request.method == "GET":
        resource_selected = request.GET.get("resource")
        if(resource_selected != None):
            all_tasks = get_all_tasks_resource(resource_selected)
            all_projects = get_projects_resource(resource_selected)
    data = {"resources_names":resources_names, 
            "element_nav":"details_nav",
            "resource_selected":resource_selected,
            "tasks":all_tasks,
            "projects":all_projects}
    return render(request, "details.html", context=data)



