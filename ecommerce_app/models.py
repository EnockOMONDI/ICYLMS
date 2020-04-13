from django.db import models
from registrar.models import Course
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = (
    (0,"Offline"),
    (1,"Online")
)

class Product(models.Model):
    # course = models.OneToOneField(Course,default=1, on_delete=models.PROTECT )
    name = models.CharField(max_length=191)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    slug = models.SlugField()
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    Course_module_file = CloudinaryField('file', blank=True, null=True)
    duration = models.CharField(max_length=191)
    Validation = models.CharField(max_length=191)
    Delivery = models.CharField(max_length=191, blank=True, null=True)

   

    def __str__(self):
        return self.name

class Modules(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='modules')
    Module_name = models.CharField(max_length=80)
    Module_duration = models.CharField(max_length=191)
    module_image = CloudinaryField('image', blank=True, null=True)
    module_file = CloudinaryField('file', blank=True, null=True)
    module_description = models.TextField()

    
    def __str__(self):
        return self.Module_name

class Units(models.Model):
    Modules = models.ForeignKey(Modules,on_delete=models.CASCADE,related_name='units')
    Unit_number = models.CharField(max_length=80)
    Unit_name = models.CharField(max_length=191)
    unit_duration = models.CharField(max_length=191)
    Month =  models.CharField(max_length=80) 
    unit_description = models.TextField()
    
    def __str__(self):
        return self.Unit_name
    


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