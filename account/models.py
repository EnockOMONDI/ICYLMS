from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from imagekit.models import ProcessedImageField


class PrivateMessage(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=127)
    text = models.TextField()
    sent_date = models.DateField(auto_now_add=True, null=True)
    to_address = models.CharField(max_length=255)
    from_address = models.CharField(max_length=255)
    
    def __str__(self):
        return "From: " + self.from_address + " To: " + self.to_address + " Title: " + self.title
    
    class Meta:
        db_table = 'at_private_messages'



class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
   

    
    class Meta:
        db_table = 'at_students'

# class Interest(models.Model):
#     name = models.CharField(max_length=60)
   

#     def __str__(self):
#         return self.name

# class Country(models.Model):
#     name = models.CharField(max_length=60)
   

#     def __str__(self):
#         return self.name



class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    
    def __str__(self):
        return self.user.first_name + " " + \
            self.user.last_name + " "
    
    class Meta:
        db_table = 'at_teachers'



# class County(models.Model):
#     name = models.CharField(max_length=60)
   

#     def __str__(self):
#         return self.name


# class Profile (models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     last_login = models.DateField(auto_now_add=True, null=True)
#     profilePic = models.ImageField(upload_to='profilepics',null=True,blank=True)
#     bio = models.CharField(max_length=150,blank=True)
#     country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
#     interests = models.ForeignKey(Interests, on_delete=models.SET_NULL, null=True) 
#     phone_number = models.IntegerField(blank =True, null = True)
#     birth_date = models.DateField(null =True, blank = True)
#     courses_enrolled = models.ManyToManyField('Courses', related_name='enrolled_courses', blank =True)

      
#     @receiver(post_save,sender = User)
#     def create_user_profile(sender,instance,created, **kwargs):
#         if created:
#           Profile.objects.create(user=instance)

#     @receiver(post_save,sender = User)
#     def save_user_profile(sender,instance,**kwargs):
#         instance.profile.save()


#     def get_number_of_courses_enrolled(self):
#         if self.courses_enrolled.count():
#             return self.courses_enrolled.count()
#         else:
#             return 0


#     def __str__(self):
#         return self.user.first_name + " " + \
#             self.user.last_name + " " 
