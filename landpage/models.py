from django.db import models
from registrar.models import Course
# from django.urls import reverse
# from django.contrib.auth.models import User

# Create your models here.

# Developers Note:
#     (1) Database
#     Once you make a change, go to /src/academicstoday_project and type:
#     $ python manage.py makemigrations landpage
#     $ python manage.py migrate landpage
#
#     (2) Field Types
#     https://docs.djangoproject.com/en/1.7/ref/models/fields/#field-types
#
#     (3) Meta Options
#     https://docs.djangoproject.com/en/1.7/ref/models/options/
#
#     (4) Query Sets
#     https://docs.djangoproject.com/en/1.7/ref/models/querysets/
#
#     (5) Models
#     https://docs.djangoproject.com/en/1.7/topics/db/models/
#
#     (6) Model Instances
#     https://docs.djangoproject.com/en/1.7/ref/models/instances/
#


class LandpageTeamMember(models.Model):
    id = models.AutoField(primary_key=True)
    image_filename = models.CharField(max_length=31)
    full_name = models.CharField(max_length=31)
    role = models.CharField(max_length=31)
    twitter_url = models.CharField(max_length=255, null=True)
    facebook_url = models.CharField(max_length=255, null=True)
    image_filename = models.CharField(max_length=255, null=True)
    linkedin_url = models.CharField(max_length=255, null=True)
    github_url = models.CharField(max_length=255, null=True)
    google_url = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'at_landpage_team_members'


class LandpageCoursePreview(models.Model):
    id = models.AutoField(primary_key=True)
    image_filename = models.CharField(max_length=31)
    title = models.CharField(max_length=127)
    category = models.CharField(max_length=31)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'at_landpage_course_previews'

class LandpageTopPickCourse(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course)
    
    def __str__(self):
        return self.course
    
    class Meta:
        db_table = 'at_landpage_top_pick_courses'


class CoursePreview(models.Model):
    id = models.AutoField(primary_key=True)
    image_filename = models.CharField(max_length=31)
    title = models.CharField(max_length=63)
    sub_title = models.CharField(max_length=127)
    category = models.CharField(max_length=31)
    description = models.TextField()
    summary = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'at_course_previews'


class LandpageContactMessage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=127)
    email = models.EmailField()
    phone = models.CharField(max_length=63)
    message = models.TextField()
    posted_date = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.name + " " + self.email + " " + self.phone
    
    class Meta:
        db_table = 'at_landpage_contact_message'


class LandpagePartner(models.Model):
    id = models.AutoField(primary_key=True)
    image_filename = models.CharField(max_length=31)
    title = models.CharField(max_length=127)
    url = models.URLField()
    
    def __str__(self):
        return self.title + ' ' + self.url
    
    class Meta:
        db_table = 'at_landpage_partners'


# class Graduant(models.Model):
#     id = models.AutoField(primary_key=True)
#     course_taken = 
#     year_of_graduation = 

# class County(models.Model):
#     name = models.CharField(max_length=60)
   

#     def __str__(self):
#         return self.name


# class Profile(models.Model):
#     profilePic = models.ImageField(upload_to='profile/',null=True,blank=True)
#     bio = models.CharField(max_length=150,blank=True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True)
    
    
#     def __str__(self):
#         return self.bio

#     def save_profile(self):
#         self.save()

#     def delete_profile(self):
#         self.delete()

#     @classmethod
#     def get_profile(cls):
#         profile = Profile.objects.all()
#         return profile

#     @classmethod
#     def find_profile(cls,search_term):
#         profile = cls.objects.filter(user__username__icontains=search_term)
#         return profile

#     @classmethod
#     def update_profile(cls,id,bio):
#         updated = Image.objects.filter(id=id).update(bio = bio)
#         return updated




# class Image(models.Model):
#     image = models.ImageField(upload_to='uploads/', blank=True, null=False)
#     caption = models.CharField(max_length = 60)
#     upload_date = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
#     likes = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         return self.caption
#     class Meta:
#         ordering = ['-upload_date']

#     def save_image(self):
#         self.save()

#     def delete_image(self):
#         self.delete()

#     @classmethod
#     def update_caption(cls,id,caption):
#         captioned = Image.objects.filter(id=id).update(caption = caption)
#         return captioned

#     @classmethod
#     def get_images(cls):
#         image = Image.objects.all()
#         return image

#     @classmethod
#     def get_image_by_id(cls,id):
#         image = Image.objects.filter(id=Image.id)
#         return image

# class Comment(models.Model):
#     comment = models.CharField(max_length=60,blank=True,null=True)
#     comment_date = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User)
#     image = models.ForeignKey(Image,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.comments

#     class Meta:
#         ordering = ['-comment_date']

#     def save_comment(self):
#         return self.save()

#     def delete_comment(self):
#         self.delete()

#     @classmethod
#     def get_comment(cls):
#         comment = Comment.objects.all()
#         return comment

