from django.contrib import admin
from .models import Myhood,Profile, Business, HealthFacilities, PolicePosts, UserPost

# Register your models here.



admin.site.register(Profile)
admin.site.register(Myhood)
admin.site.register(UserPost)
admin.site.register(Business)
admin.site.register(HealthFacilities)
admin.site.register(PolicePosts)


