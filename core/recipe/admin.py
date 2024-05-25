from django.contrib import admin
from recipe.models import *

# Register your models here.


admin.site.register(student)
admin.site.register(studentID)
admin.site.register(Department)
admin.site.register(Recipes)
admin.site.register(subject)


class subjectnameAdmin(admin.ModelAdmin):
    list_display= ['student','subject', 'marks','show_total_marks'  ]
admin.site.register(sunjectmarks, subjectnameAdmin)

