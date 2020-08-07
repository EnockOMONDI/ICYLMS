from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.admin import ExportMixin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from account.models import PrivateMessage
from account.models import Student
from account.models import Teacher


# from account.models import UserProfile


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    fileds =('firts_name', 'last_name', 'email', 'age', 'country', 'interests')
    pass

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )

class UserAdmin(ExportMixin, UserAdmin):
    resource_class = UserResource
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(PrivateMessage)
admin.site.register(Teacher)


