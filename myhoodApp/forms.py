
from . models import Profile, Business,Myhood, PolicePosts, HealthFacilities, UserPost
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
      
        def __init__(self, *args, **kwargs):
            super(UserRegistrationForm, self).__init__(*args, **kwargs)

            for fieldname in ['username', 'password1', 'password2']:
                self.fields[fieldname].help_text = None

        fields = ('first_name', 'last_name', 'email','username',  'password1', 'password2')
        widgets = {
            'first_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"First Name", 'label': 'First Name'}),
            'last_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Second Name", 'label': 'Second Name'}),
            'email':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Email Address", 'label': 'Email Address'}),
            'username':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Username", 'label': 'Username'}),
            'password1':forms.PasswordInput(attrs = {'class':'form-control ', 'placeholder':"Password", 'label': 'Password'}),
            'password2':forms.PasswordInput(attrs = {'class':'form-control', 'type':'password', 'placeholder':"Confirm Password", 'label': 'Confirm Password'}),
        }


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'profile_pic','family_name', 'bio','gender','general_location', 'mobile','hood' ]
        widgets = {
            'profile_pic': forms.FileInput(attrs={'class':'form-control'}),
            'family_name':forms.TextInput(attrs={'class': 'form-control'}),
            'bio':forms.Textarea(attrs={'class': 'form-control'}),
            'gender':forms.Select(attrs={'class': 'form-control'}),
            'general_location':forms.TextInput(attrs={'class': 'form-control'}),
            'hood':forms.Select(attrs={'class': 'form-control'}),


            
        }


class HoodMemberPostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ('title', 'post')





class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = [  'post_pic', 'title','post']
        widgets = {
            'project_pic':forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}), 
            'post':forms.Textarea(attrs={'class': 'form-control'}),
            
            
        
        }

class RegisterBizForm(forms.ModelForm):
    class Meta:
        model =  Business
        fields = [ 'biz_image', 'name', 'description','phone','email']
        widgets = {
            'biz_image':forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}), 
            'description':forms.TextInput(attrs={'class': 'form-control'}),
            'phone':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),

            
            
        
        }


class RegisterMyhoodForm(forms.ModelForm):
    class Meta:
        model =  Myhood
        fields = [ 'name','location','sample_hood_image', 'description','police_contacts']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class': 'form-control'}), 
            'sample_hood_image':forms.FileInput(attrs={'class': 'form-control'}),
            'description':forms.TextInput(attrs={'class': 'form-control'}),
            'police_contacts':forms.TextInput(attrs={'class': 'form-control'}),

            
            
        
    }

class RegisterHoodHospital(forms.ModelForm):
    class Meta:
        model =  HealthFacilities
        fields = [ 'hospital_image','name','phone','email', 'description']
        widgets = {
            'hospital_image':forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class': 'form-control'}), 
            'email':forms.TextInput(attrs={'class': 'form-control'}), 
            'description':forms.TextInput(attrs={'class': 'form-control'}),

            
            
        
    }

    

    


  



