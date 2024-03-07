from django.contrib import admin
from.models import Patient,Doctor,Appointment,Department,Login

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Department)
admin.site.register(Login)
