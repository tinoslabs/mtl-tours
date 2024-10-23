from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    heading = models.CharField(max_length=255, verbose_name='Category Heading')
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    # description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.heading

class Package(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None, related_name='packages', verbose_name=('Category'))
    name = models.CharField(max_length=255, verbose_name=('Package Name'), unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=('Price'))
    description = RichTextField(null=True, blank=True, verbose_name=('Description'))

    def __str__(self):
        return self.name

class PackageImage(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='images', verbose_name=('Package'))
    image = models.ImageField(upload_to='image/', verbose_name=('Image'))

    def __str__(self):
        return f"Image for {self.package.name}"



    

class Booking(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    time = models.TimeField()
    date = models.DateField()
    num_people = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name}'s Booking"


class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name