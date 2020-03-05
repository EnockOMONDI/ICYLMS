from django.contrib import admin
from account.models import PrivateMessage
from account.models import Student
from account.models import Teacher,Country,City
# from account.models import UserProfile

admin.site.register(PrivateMessage)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Country)
admin.site.register(City)


# admin.site.register(UserProfile)