from django.shortcuts import render

def main_menu(request):
    data = {"template":"task.html"}
    tc = TestPersona("EmmanuelTC", "TC", ["A", "B", "C"])
    pm = TestPersona("EmmanuelPM", "PM", ["A", "B", "C"]) 
    data["tc"] = tc
    data["pm"] = pm
    print(data["pm"])
    return render(request, "main_menu.html", context=data)



def tasks(request):
    data = {"templat:task.html "}
    return render(request, "task.html",context=data)




class TestPersona:
    def __init__(self, nombre, puesto, proyectos):
        self.nombre = nombre
        self.puesto = puesto
        self.proyectos = proyectos