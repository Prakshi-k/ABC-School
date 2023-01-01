from django.contrib import admin
from .models import contactnow, kindergarten, student, teacher,staff


# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display=['stuid','rollno','dob','std','fname','lname','mobno']
    list_filter=['std']

class teacherAdmin(admin.ModelAdmin):
    list_display=['fname','lname','mobno']

class staffAdmin(admin.ModelAdmin):
    list_display=['fname','lname','mobno']

class kindergartenAdmin(admin.ModelAdmin):
    list_display=['stuid','fname','lname','section','rollno','mobno']
    list_filter=['section']

class contactnowAdmin(admin.ModelAdmin):
    list_display=['name','email','message']


admin.site.register(student,studentAdmin)
admin.site.register(teacher,teacherAdmin)
admin.site.register(kindergarten,kindergartenAdmin)
admin.site.register(staff,staffAdmin)
admin.site.register(contactnow,contactnowAdmin)


admin.site.site_title="ABC School"

admin.site.site_header="ABC School Admin Panel"