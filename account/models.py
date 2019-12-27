from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
# from imagekit.models import ProcessedImageField

COUNTRY_CATEGORY_TYPES = (
    ('Aeronautics & Astronautics', 'Aeronautics & Astronautics'),
    ('Anesthesia', 'Anesthesia'),
    ('Anthropology', 'Anthropology'),
    ('Applied Physics', 'Applied Physics'),
    ('Art or Art History', 'Art & Art History'),
    ('Astrophysics', 'Astrophysics'),
    ('Biochemistry', 'Biochemistry'),
    ('Bioengineering', 'Bioengineering'),
    ('Biology', 'Biology'),
    ('Business', 'Business'),
    ('Cardiothoracic Surgery', 'Cardiothoracic Surgery'),
    ('Chemical and Systems Biology', 'Chemical and Systems Biology'),
    ('Chemical Engineering', 'Chemical Engineering'),
    ('Chemistry', 'Chemistry'),
    ('Civil and Environmental Engineering', 'Civil and Environmental Engineering'),
    ('Classics', 'Classics'),
    ('Communication', 'Communication'),
    ('Comparative Literature', 'Comparative Literature'),
    ('Comparative Medicine', 'Comparative Medicine'),
    ('Computer Science', 'Computer Science'),
    ('Dermatology', 'Dermatology'),
    ('Developmental Biology', 'Developmental Biology'),
    ('East Asian Languages and Cultures', 'East Asian Languages and Cultures'),
    ('Economics', 'Economics'),
    ('Education', 'Education'),
    ('Electrical Engineering', 'Electrical Engineering'),
    ('English', 'English'),
    ('French', 'French'),
    ('Genetics', 'Genetics'),
    ('General Eduction', 'General Education'),
    ('Geological and Environmental Sciences', 'Geological and Environmental Sciences'),
    ('Geophysics', 'Geophysics'),
    ('Health', 'Health'),
    ('History', 'History'),
    ('Latin American Cultures', 'Latin American Cultures'),
    ('Law School', 'Law School'),
    ('Linguistics', 'Linguistics'),
    ('Management', 'Management'),
    ('Materials Science', 'Materials Science'),
    ('Mathematics', 'Mathematics'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
    ('Medicine', 'Medicine'),
    ('Microbiology and Immunology', 'Microbiology and Immunology'),
    ('Molecular and Cellular Physiology', 'Molecular and Cellular Physiology'),
    ('Music', 'Music'),
    ('Neurobiology', 'Neurobiology'),
    ('Neurology', 'Neurology'),
    ('Neurosurgery', 'Neurosurgery'),
    ('Obstetrics and Gynecology', 'Obstetrics and Gynecology'),
    ('Ophthalmology', 'Ophthalmology'),
    ('Orthopaedic Surgery', 'Orthopaedic Surgery'),
    ('Other', 'Other'),
    ('Otolaryngology', 'Otolaryngology'),
    ('Pathology', 'Pathology'),
    ('Pediatrics', 'Pediatrics'),
    ('Philosophy', 'Philosophy'),
    ('Physics', 'Physics'),
    ('Political Science', 'Political Science'),
    ('Psychiatry', 'Psychiatry'),
    ('Psychology', 'Psychology'),
    ('Radiation Oncology', 'Radiation Oncology'),
    ('Radiology', 'Radiology'),
    ('Religious Studies', 'Religious Studies'),
    ('Slavic Languages and Literature', 'Slavic Languages and Literature'),
    ('Sociology', 'Sociology'),
    ('Statistics', 'Statistics'),
    ('Surgery', 'Surgery'),
    ('Theater and Performance Studies', 'Theater and Performance Studies'),
    ('Urology', 'Urology'),
)

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
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_pic = models.ImageField(upload_to= '/profile_pic', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    country = models.CharField(max_length=127, choices=COUNTRY_CATEGORY_TYPES,  blank=True,null=True,  default='Kenya')
    age = models.PositiveSmallIntegerField(default='18', null=True)
    interests = models.CharField(max_length=30,null=True)
    
    def __str__(self):
        return self.user.first_name + " " + \
                          self.user.last_name 
    
    class Meta:
        db_table = 'at_students'

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Student.objects.create(user=instance)
    

    # @receiver(post_save, sender=User)
    # def update_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Student.objects.create(user=instance)
    #     instance.student.save()
    def create_student_profile(sender, **kwargs):
        if kwargs['created']:
            student = Student.objects.create(user=kwargs['instance'])

    post_save.connect(create_student_profile, sender=User)
    






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
