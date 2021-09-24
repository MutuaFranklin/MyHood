from myhoodApp.models import Business, HealthFacilities, Myhood, Profile, UserPost
from django.contrib.auth.models import User
from django.db.models.fields import PositiveSmallIntegerField
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterBizForm, RegisterHoodHospital, RegisterMyhoodForm, UserRegistrationForm, UpdatePostForm, HoodMemberPostForm, UpdateUserProfileForm
from .email import send_welcome_email
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy



# Create your views here.

def register(request):
    reg_form = UserRegistrationForm()

    if request.method == 'POST':
        reg_form = UserRegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            user = reg_form.cleaned_data.get('username')
            email = reg_form.cleaned_data['email']
            messages.success(request, 'Account was created for ' + user)
            send_welcome_email(user,email)
            return redirect('login')
        else:
            reg_form = UserRegistrationForm()

    
    return render(request, 'registration/sign_up.html', {'reg_form': reg_form})


def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'registration/login.html')


def index(request):
    

    return render(request, 'myhood/index.html')

    



def home(request):
    current_user = request.user
    myhood = Profile.objects.get(user=current_user)
    posts = UserPost.objects.filter(hood=current_user.profile.hood).all()
    business = Business.objects.filter(hood=current_user.profile.hood).all()
    admin = Myhood.objects.filter(hood_admin=current_user.profile).all()
    hospitals = HealthFacilities.objects.filter(hood=myhood.hood).all()

    print(hospitals)

    hoods= Myhood.objects.all()

     #Register myhood
    if request.method == 'POST':
        hForm = RegisterMyhoodForm(request.POST, request.FILES)
        if hForm.is_valid():
            hood = hForm.save(commit=False)
            print(hForm)
            hood.hood_admin = current_user.profile
            hood.save()
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        hForm = RegisterMyhoodForm()

    # Make a Post
    if request.method == 'POST':
        pForm = HoodMemberPostForm(request.POST, request.FILES)
        if pForm.is_valid():
            post = pForm.save(commit=False)
            post.posted_by = current_user.profile
            post.hood= myhood.hood
            post.save()
            return redirect('home')
    else:
        pForm = HoodMemberPostForm()



    # Register a business
    if request.method == 'POST':
        bForm = RegisterBizForm(request.POST, request.FILES)
        if bForm.is_valid():
            biz = bForm.save(commit=False)
            biz.owner = current_user.profile
            biz.hood= myhood.hood
            biz.save()
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        bForm = RegisterBizForm()

    hosForm = RegisterHoodHospital()
   
    context ={
        
        "pForm":pForm,
        "myhood":myhood,
        "posts":posts,
        "business":business,
        "bForm":bForm,
        "hForm":hForm,
        "hosForm":hosForm,
        "hoods":hoods,
        "admin":admin,
        "hospitals":hospitals       
                  
       
      
    }

    return render(request, 'myhood/home.html', context)

def registerHealthFacility(request):
    current_user = request.user
    myhood = Profile.objects.get(user=current_user)



     # Register health facility
    if request.method == 'POST':
        hosForm = RegisterHoodHospital(request.POST, request.FILES)
        if hosForm.is_valid():
            hos = hosForm.save(commit=False)
            hos.hood= myhood.hood
            hos.save()
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        hosForm = RegisterHoodHospital()

    context ={
        "myhood":myhood,
        "hosForm":hosForm,


    }

    return render(request, 'myhood/home.html', context)



def userProfile(request, username):
    current_user = request.user
    otherUser = get_object_or_404(User, username=username)
    userProfile = Profile.objects.get(user=otherUser)
    posts = UserPost.objects.filter(posted_by = otherUser.profile)
    myhood = Profile.objects.get(user=current_user)
    business = Business.objects.filter(owner=otherUser.profile).all()
    neighbors = Profile.objects.filter(hood=userProfile.hood).all()
    # print(neighbors)




    if request.method == 'POST':
        bForm = RegisterBizForm(request.POST, request.FILES)
        if bForm.is_valid():
            biz = bForm.save(commit=False)
            biz.owner = current_user.profile
            biz.hood= myhood.hood
            biz.save()
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        bForm = RegisterBizForm()


    context ={
        "otherUser":otherUser,
        "profile":userProfile,
        "posts": posts,
        "bForm":bForm,
        "business":business ,
        "neighbors":neighbors,       
                  
    }


    return render(request, 'profile/userProfile.html', context)


class NewProfileUpdateView(UpdateView):
        model=Profile
        slug_field = "username"
        form_class =UpdateUserProfileForm
        template_name ='profile/editProfile.html'
        
        def get_queryset(self): 
            return Profile.objects.all()


        def get_success_url(self):
        
            # return reverse_lazy('userProfile',args=[self.request.user.username]) 
            return reverse_lazy('home',) 

class UpdateProfileView(UpdateView):
        model=Profile
        slug_field = "username"
        form_class =UpdateUserProfileForm
        template_name ='profile/editProfile.html'
        
        def get_queryset(self): 
            return Profile.objects.all()


        def get_success_url(self):
        
            return reverse_lazy('userProfile',args=[self.request.user.username]) 
            # return reverse_lazy('home',) 

def search(request):
    current_user = request.user
    neighbor = Profile.objects.filter(hood=current_user.profile.hood).all()

    if 'search_query' in request.GET and request.GET["search_query"]:
        # form data
        search_business = request.GET.get("search_query")
        search_neighbor = request.GET.get("search_query")
        # print(search_business)

        # search results
        searched_business =Business.search_business(search_business)
        searched_neighbor =Profile.search_user(search_neighbor)


        # print(searched_business)
        business_message = f"{search_business}"
        neighbor_message = f"{search_business}"


        context = {
            "b_message":business_message,
            "n_message":neighbor_message,
            "business": searched_business,
            "neighbors": searched_neighbor,
            "hood_member":neighbor
        }


        return render(request, 'myhood/search.html', context)

    else:
        message = "You haven't searched for any term"
        return render(request, 'myhood/search.html',{"message":message})
        

