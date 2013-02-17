from django.db import models
from django.contrib import admin
from django.contrib.auth.models import Group

class Cred(models.Model):
	title = models.CharField(max_length=64)
	username = models.CharField(max_length=250, blank=True, null=True)
	password = models.CharField(max_length=250)
	description = models.TextField(blank=True, null=True)
	group = models.ForeignKey(Group)	

class CredAdmin(admin.ModelAdmin):
	list_display = ('title', 'username')

admin.site.register(Cred, CredAdmin)