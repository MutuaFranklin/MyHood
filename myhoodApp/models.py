from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save




# Create your models here.
class Myhood(models.Model):
    
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    sample_hood_image = CloudinaryField('Hood_image', blank=True)
    description = models.TextField()
    police_contacts =models.CharField(max_length=60, blank=True, null=True)
    hood_admin = models.ForeignKey("Profile", on_delete=models.CASCADE)
    



    def __str__(self):
        return f'{self.name} hood'

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def update_hood(cls, hood_id, updated_description):
        myhood = cls.objects.filter(id = hood_id).update(description = updated_description)
        return myhood


class Profile(models.Model):
    gender_choice = ("Male", "Male"),("Female","Female")
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = CloudinaryField('Profile Pic', blank=True)
    family_name = models.CharField(max_length=56, blank=True)
    gender = models.TextField(blank=True, choices=gender_choice)
    mobile = models.CharField(max_length=18, blank=True)
    bio =  models.TextField(blank=True, default='Welcome to my world')
    general_location = models.CharField(max_length = 50,blank=True)
    hood = models.ForeignKey(Myhood, on_delete=models.DO_NOTHING, related_name='hood', blank=True, null=True)


    def __str__(self):
        return self.user.username

        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 

    @classmethod
    def update_profile(cls, prof_id, updated_bio):
        profile = cls.objects.filter(id = prof_id).update(family_name = updated_bio)
        return profile
    
    @classmethod
    def search_user(cls, username):
        return cls.objects.filter(user__username__icontains=username)




  

class UserPost(models.Model):
    post_pic = CloudinaryField('Post_image', blank=True)
    title = models.CharField(max_length=150, null=True)
    post = HTMLField()
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_user')
    hood = models.ForeignKey(Myhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title} hood'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def update_post(cls, post_id, updated_post):
        post = cls.objects.filter(id = post_id).update(post = updated_post)
        return post

    class Meta:
        ordering = ['-date_posted']

# Amenities

class Business(models.Model):
    biz_image = CloudinaryField('Business Image', blank=True)
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=18, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    description = models.TextField(blank=True)
    hood = models.ForeignKey(Myhood, on_delete=models.CASCADE, related_name='business')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='business', null=True)



    def __str__(self):
        return f'{self.name} Business'

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, business_name):
        return cls.objects.filter(name__icontains=business_name).all()
        
    @classmethod
    def update_biz(cls, biz_id, updated_biz):
        biz = cls.objects.filter(id = biz_id).update(description = updated_biz)
        return biz


class HealthFacilities(models.Model):
    hospital_image = CloudinaryField('Hospital Image', blank=True)
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=18, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    description = models.TextField(blank=True)
    hood = models.ForeignKey(Myhood, on_delete=models.CASCADE, related_name='health_facility')

    def __str__(self):
    
        return f'{self.name} Health Facility'

    def save_health_facility(self):
        self.save()

    def delete_health_facility(self):
        self.delete()
    @classmethod
    def update_hospital_details(cls, hos_id, updated_description):
        hospital = cls.objects.filter(id = hos_id).update(description = updated_description)
        return hospital

    @classmethod
    def search_health_facility(cls, name):
        return cls.objects.filter(name__icontains=name).all()


class PolicePosts(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=18)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    hood = models.ForeignKey(Myhood, on_delete=models.CASCADE, related_name='police_post')

    def __str__(self):
        return f'{self.name} Police Station'

    def save_police_post(self):
        self.save()

    def delete_police_post(self):
        self.delete()

    @classmethod
    def search_police_post(cls, name):
        return cls.objects.filter(name__icontains=name).all()


