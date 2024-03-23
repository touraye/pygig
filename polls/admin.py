from django.contrib import admin

from .models import Question

# make poll app modifiable by admin
admin.site.register(Question)