from django.shortcuts import render
from team_management.models import resource_type
def main_menu(request):
    data = {"template":"task.html"}
    tc = TestPersona("EmmanuelTC", "TC", ["A", "B", "C"])
    pm = TestPersona("EmmanuelPM", "PM", ["A", "B", "C"]) 
    data["tc"] = tc
    data["pm"] = pm
    print(data["pm"])
    resource_type.objects.create(description_text = "TC")
    new_resource = resource_type(description_text = "PM")
    new_resource.save()
    obj = resource_type.objects.all()
    for i in obj:
        print(i.date_created)
        print(i.date_modified)

    return render(request, "main_menu.html", context=data)



def tasks(request):
    data = {"templat:task.html "}
    return render(request, "task.html",context=data)




class TestPersona:
    def __init__(self, nombre, puesto, proyectos):
        self.nombre = nombre
        self.puesto = puesto
        self.proyectos = proyectos