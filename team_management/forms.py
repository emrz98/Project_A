from django.forms import ModelForm
from team_management.models import task

class TaskForm(ModelForm):
    class Meta:
        model = task
        fields = ['idresource', 'idtask_type', 'idtask_status', 'main_title', 'start_date', 'end_date']

