from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name='Profile Picture')
    profession = models.CharField(max_length=150, default='Real Estate Agent')
    about = models.TextField(null=True, blank=True, verbose_name='About yourself')
    instagram = models.URLField(blank=True, null=True) 
    twitter = models.URLField(blank=True, null=True) 
    facebook = models.URLField(blank=True, null=True) 
    linkedin = models.URLField(blank=True, null=True) 
    your_cv = models.FileField(blank=True, null=True, 
    upload_to='uploads/pdf')

    def __str__(self): 
        return self.user.username
    
    
    
class Category(models.Model): 
    cat_name = models.CharField(verbose_name='Category Name', 
    max_length=100, unique=True) 
    description = models.TextField(verbose_name='Description', blank=True, 
    null=True) 
    def __str__(self): 
        return self.cat_name 

class Location(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        return super().save(*args, **kwargs)


class Property(models.Model):
    RENT = 'Rent'
    SALE = 'Sale'
    STATUS_CHOICE = [
         (RENT, 'Rent'),
         (SALE, 'Sale'),
    ]
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    price = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name='First Image')
    image2 = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name='Second Image')
    image3 = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name='Third Image')
    status = models.CharField(choices=STATUS_CHOICE, default=RENT, max_length=100)
    description = models.TextField()
    num_of_rooms = models.PositiveIntegerField()
    num_of_baths = models.PositiveIntegerField()
    agent = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address
    
    def get_absolute_url(self):
        return reverse('AppTwo:property_detail', args=[str(self.id)])
    
    def get_image_url(self):
        if self.image1:
            return self.image1.url
        elif self.image2:
            return self.image2.url
        elif self.image3:
            return self.image3.url
        
    
    

    
class Post(models.Model): 
    post_title = models.CharField(verbose_name='Post Title',
    max_length=150) 
    category = models.ManyToManyField(Category, verbose_name='Categories of Post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author') 
    post_img = models.ImageField(blank=True, null=True, 
    upload_to='uploads/post_img', verbose_name='Post Image') 
    create_date = models.DateTimeField(default=timezone.now)  
    published_date = models.DateTimeField(blank=True, null=True) 
    content = models.TextField() 
    def publish(self): 
        self.published_date = timezone.now() 
        self.save() 
    def approve_comment(self):
        return 
        self.comments.filter(approve_comment=True)
    def __str__(self): 
        return self.title 
    
    
class Comment(models.Model): 
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    author_poster = models.CharField(max_length=200) 
    comments = models.TextField() 
    create_date = models.DateTimeField(default=timezone.now)
    approve_comment = models.BooleanField(default=False) 
    def approve(self):
            self.approve_comment = True 
            self.save() 
    def __str__(self): 
            return self.comments    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.email