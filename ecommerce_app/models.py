from django.db import models
from registrar.models import Course
from django.contrib.auth.models import User
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
import os
from account.models import Student
from account.models import Teacher


STATUS = (
    (0,"Offline"),
    (1,"Online")
)

SHORT_COURSE_CATEGORY_TYPES = (
    ('leadership', 'leadership'),
    ('SDGs', 'SDGs'),

)

class ShortCourse(models.Model):
    name = models.CharField(max_length=191)
    sub_title = models.CharField(max_length=127)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    Validator_image = CloudinaryField('image', blank=True, null=True)
    Validator_name = models.CharField(max_length=191, blank=True, null=True)
    Course_module_file = CloudinaryField('file', blank=True, null=True)
    duration = models.CharField(max_length=191)
    category = models.CharField(max_length=127, choices=SHORT_COURSE_CATEGORY_TYPES, default='General Education')
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    finish_date = models.DateField(null=True)
    is_official = models.BooleanField(default=False)
    status = models.PositiveSmallIntegerField(default=settings.SHORT_COURSE_UNAVAILABLE_STATUS)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name
    @property
    def lectures_in_shortcourse(self):
        return self.shortcourselectures.count()
    
    @property
    def students_in_shortcourse(self):
        return self.shortcoures.students.count()

    

class ShortCourseLecture(models.Model):
    lecture_id = models.AutoField(primary_key=True)
    lecture_num = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        default=1
    )
    week_num = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        default=1
    )
    title = models.CharField(max_length=63, default='', null=True)
    description = models.TextField(default='', null=True)
    youtube_url = models.URLField(null=True, blank=True)
    vimeo_url = models.URLField(null=True, blank=True)
    bliptv_url = models.URLField(null=True, blank=True)
    VIDEO_PLAYER_CHOICES = (
        (settings.YOUTUBE_VIDEO_PLAYER, 'YouTube'),
        (settings.VIMEO_VIDEO_PLAYER, 'Vimeo')
    )
    preferred_service = models.CharField(
        max_length=1,
        choices=VIDEO_PLAYER_CHOICES,
        default=settings.YOUTUBE_VIDEO_PLAYER
    )
    shortcourse = models.ForeignKey(ShortCourse, on_delete=models.CASCADE, related_name='shortcourselectures')
   

    def __str__(self):
        return 'Week: ' + str(self.week_num) + ' ShortCourseLecture: ' + str(self.lecture_num) + ' Title: ' +self.title;
    
   

class ShortCourseModules(models.Model):
    ShortCourse = models.ForeignKey(ShortCourse,on_delete=models.CASCADE,related_name='modules')
    Module_name = models.CharField(max_length=80)
    Module_duration = models.CharField(max_length=191)
    module_image = CloudinaryField('image', blank=True, null=True)
    module_file = CloudinaryField('file', blank=True, null=True)
    module_description = models.TextField()

    
    def __str__(self):
        return self.Module_name

class Product(models.Model):
    # course = models.OneToOneField(Course,default=1, on_delete=models.PROTECT )
    name = models.CharField(max_length=191)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    slug = models.SlugField()
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    Validator_image = CloudinaryField('image', blank=True, null=True)
    Validator_name = models.CharField(max_length=191)
    Course_module_file = CloudinaryField('file', blank=True, null=True)
    duration = models.CharField(max_length=191)
    Delivery = models.CharField(max_length=191, blank=True, null=True)
   

    def __str__(self):
        return self.name

# class Modules(models.Model):
#     Product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='modules')
#     Module_name = models.CharField(max_length=80)
#     Module_duration = models.CharField(max_length=191)
#     module_image = CloudinaryField('image', blank=True, null=True)
#     module_file = CloudinaryField('file', blank=True, null=True)
#     module_description = models.TextField()

    
#     def __str__(self):
#         return self.Module_name

# class Units(models.Model):
#     Modules = models.ForeignKey(Modules,on_delete=models.CASCADE,related_name='units')
#     Unit_number = models.CharField(max_length=80)
#     Unit_name = models.CharField(max_length=191)
#     unit_duration = models.CharField(max_length=191)
#     Month =  models.CharField(max_length=80) 
#     unit_description = models.TextField()
    
#     def __str__(self):
#         return self.Unit_name
    


class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return "{}:{}".format(self.product.name, self.id)

    def update_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        self.save()

    def total_cost(self):
        return self.quantity * self.price


class Order(models.Model):
    name = models.TextField(max_length=50, blank=True, null=True)
    email = models.TextField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
 

    def __str__(self):
        return "{}:{}".format(self.id, self.email)

    def total_cost(self):
        return sum([ li.cost() for li in self.lineitem_set.all() ] )


class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}:{}".format(self.product.name, self.id)

    def cost(self):
        return self.price * self.quantity