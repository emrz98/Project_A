from django.shortcuts import render
from team_management.models import resource_type,resource, task as t
def task(request):
    # resource_type.objects.create(description_text = "TC")
    # new_resource = resource_type(description_text = "PM")
    # new_resource.save()
    tasks_of_resource = t.objects.all()
    tasks = tasks_of_resource.values()
    
    resource_id = tasks[0]["idresource_id"]
    resource_in_charge = resource.objects.filter(idresource = resource_id)[0]
    print(resource_in_charge)
    cont = {"tasks": tasks,"resource": resource_in_charge}

    return render(request, "task.html", context=cont)

