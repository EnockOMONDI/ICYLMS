from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from cloudinary.models import CloudinaryField
# from imagekit.models import ProcessedImageField

INTERESTS_CATEGORY_TYPES = (
('Leadership', 'Leadership'),

)
COUNTRY_CATEGORY_TYPES = (
('Algeria', 'Algeria'),
('Angola', 'Angola'),
('Benin', 'Benin'),
('Botswana', 'Botswana'),
('Burkina Faso', 'Burkina Faso'),
('Burundi', 'Burundi'),
('Cape Verde', 'Cape Verde'),
('Cameroon', 'Cameroon'),
('Central African Republic', 'Central African Republic'),
('Chad', 'Chad'),
('Comoros', 'Comoros'),
('Congo Democratic Republic', 'Congo Democratic Republic'),
('Congo, Republic of the', 'Congo, Republic of the'),
('Cote dIvoire', 'Cote dIvoire'),
('Djibouti', 'Djibouti'),
('Egypt', 'Egypt'),
('Equatorial Guinea', 'Equatorial Guinea'),
('Eritrea', 'Eritrea'),
('Eswatini', 'Eswatini'),
('Ethiopia', 'Ethiopia'),
('Gabon', 'Gabon'),
('Gambia', 'Gambia'),
('Ghana', 'Ghana'),
('Guinea', 'Guinea'),
('Guinea-Bissau', 'Guinea-Bissau'),
('Kenya', 'Kenya'),
('Lesotho', 'Lesotho'),
('Liberia', 'Liberia'),
('Libya', 'Libya'),
('Madagascar', 'Madagascar'),
('Malawi', 'Malawi'),
('Mali', 'Mali'),
('Mauritania', 'Mauritania'),
('Mauritius', 'Mauritius'),
('Morocco', 'Morocco'),
('Mozambique', 'Mozambique'),
('Namibia', 'Namibia'),
('Niger', 'Niger'),
('Nigeria', 'Nigeria'),
('Rwanda', 'Rwanda'),
('Sao Tome and Principe', 'Sao Tome and Principe'),
('Senegal', 'Senegal'),
('Seychelles', 'Seychelles'),
('Sierra Leone', 'Sierra Leone'),
('Somalia', 'Somalia'),
('South Africa', 'South Africa'),
('South Sudan', 'South Sudan'),
('Sudan', 'Sudan'),
('Tanzania', 'Tanzania'),
('Togo', 'Togo'),
('Tunisia', 'Tunisia'),
('Uganda', 'Uganda' ),
('Zambia', 'Zambia' )
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic =  CloudinaryField('image', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    country = models.CharField(max_length=127, choices=COUNTRY_CATEGORY_TYPES,  blank=True,null=True,  default='Kenya')
    age = models.PositiveSmallIntegerField(default='18', null=True)
    interests = models.CharField(max_length=70,null=True, choices=INTERESTS_CATEGORY_TYPES,default='Leadership' )
  
 
    
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
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