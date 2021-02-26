from team_management.models import project, resource_type,resource, task, project_has_task

'''
Query functions
get_names_resources(): This function return the names of all the resources in the database
                        doesnt matter the type of resource


get_type_resources_names(): This function return the names of all the resources with the
                            type of resource given in the parameter of the function.


'''

def get_names_resources():
    '''
    This function return the names of all the resources in the database
    doesnt matter the type of resource.

    Parameters:
    None
    '''
    all_resources = resource.objects.all().values()
    names = [resource["name"] for resource in all_resources]
    return names

def get_type_resources_names(type_resources):
    '''
    This function return the names of all the resources with the
    type of resource given in the parameter of the function.

    Parameters:
    type_resources --- String
    '''
    idresource_type = resource_type.objects.filter(description_text = type_resources).values()[0]["idresource_type"]
    all_names = [resource["name"] for resource in resource.objects.filter(idresource_type = idresource_type).values()]
    return all_names

def get_names_tcs():
    return get_type_resources_names("TC")
    
def get_names_pms():
    return get_type_resources_names("PM")

def get_all_tasks_resource(resource_name):
    id_res = resource.objects.filter(name = resource_name).values()[0]["idresource"]
    all_task = task.objects.filter(idresource = id_res).values()
    return all_task

def get_idprojects_from_tasks(all_task):
    id_all_task = [task["idtask"] for task  in all_task]
    all_project_id = [project_has_task.objects.filter(idtask_id = id_task) for id_task in id_all_task]
    all_project_id = list(set([queryset.values()[0]["idproject_id"] for queryset in all_project_id if queryset.exists()]))
    return all_project_id

def get_projects_resource(resource_name):
    all_task = get_all_tasks_resource(resource_name)
    all_project_id = get_idprojects_from_tasks(all_task)
    all_projects = [project.objects.filter(idproject = id).values()[0] for id in all_project_id] 
    return all_projects


def get_tasks_project_of_resource(resource_name ,project_description):
    all_task = get_all_tasks_resource(resource_name)
    id_project = project.objects.filter(description_text = project_description).values()[0]["idproject"]
    id_tasks_project =[has_task["idtask_id"] for has_task in project_has_task.objects.filter(idproject = id_project).values()]
    task_source_project=[task for task in all_task if task["idtask"] in id_tasks_project]
    return task_source_project
    
def create_new_task():
    pass