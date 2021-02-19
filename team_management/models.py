from django.db import models
from django.db.models.fields.related import ManyToManyField

class resource_type(models.Model):
    idresource_type = models.AutoField(primary_key=True)
    description_text = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.description_text + " "+str(self.date_created)

class project_type(models.Model):
    idproject_type = models.AutoField(primary_key=True)
    description_text = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    def __str__(self):
        return self.description_text
    

class task_type(models.Model):
    idtask_type = models.AutoField(primary_key=True)
    description_text = models.CharField(max_length=250)
    average_time = models.IntegerField(null=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField()
    def __str__(self):
        return self.description_text

class task_status(models.Model):
    idproject_type = models.AutoField(primary_key=True)
    description_text = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField()
    def __str__(self):
        return self.description_text

class customer(models.Model):
    idcustomer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField()
    def __str__(self):
        return self.name

class comment_type(models.Model):
    idcomment_type = models.AutoField(primary_key=True)
    description_text = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(null = True)
    def __str__(self):
        return self.description_text

class comments(models.Model):
    idcomment = models.AutoField(primary_key=True)
    idcomment_type = models.ForeignKey(comment_type,on_delete=models.DO_NOTHING)
    comment_text = models.TextField(null = True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(null = True)
    def __str__(self):
        return self.comment_text

class resource(models.Model):
    idresource = models.AutoField(primary_key=True)
    idresource_type = models.ForeignKey(resource_type, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_deleted = models.DateField(null=True, auto_now_add=True)
    ldap = models.CharField(max_length=100, null=True)
    active = models.SmallIntegerField(null=True)
    def __str__(self):
        return self.name


class project(models.Model):
    idproject = models.AutoField(primary_key=True)
    idproject_type = models.ForeignKey(project_type, on_delete=models.DO_NOTHING)
    idcostumer = models.ForeignKey(customer, on_delete=models.DO_NOTHING)
    description_text = models.CharField(max_length=250)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField()
    def __str__(self):
        return self.description_text

class task(models.Model):
    idtask = models.AutoField(primary_key=True)
    idresource = models.ForeignKey(resource, on_delete=models.DO_NOTHING)
    idtask_type = models.ForeignKey(task_type, on_delete=models.DO_NOTHING)
    idtask_status = models.ForeignKey(task_status, on_delete=models.DO_NOTHING)
    main_title = models.CharField(max_length=250)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    commit_date = models.DateField(null = True)
    def __str__(self):
        return self.main_title

class project_has_task(models.Model):
    idproject = models.ForeignKey(project, on_delete=models.DO_NOTHING)
    idtask = models.ForeignKey(task, on_delete=models.DO_NOTHING)
    class Meta:
        unique_together = [['idproject','idtask']]

class task_has_comments(models.Model):
    idcomment = models.ForeignKey(comments, on_delete=models.DO_NOTHING)
    idtask = models.ForeignKey(task, on_delete=models.DO_NOTHING)
    class Meta:
        unique_together = [['idcomment', 'idtask']]
