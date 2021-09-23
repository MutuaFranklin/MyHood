from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Business, Myhood, UserPost

# Create your tests here.
class ReviewAppTestClass(TestCase):

    def setUp(self):
        self.new_user = User(id = 1, first_name = 'Frank', last_name = 'Mutua', username = 'frank', email = 'frankmutua@gmail.com')
        # self.new_user.save()

        self.new_hood = Myhood(id = 1, name = 'Hood', location = 'Location', description='My home')
        # self.new_hood.save()

        self.new_profile = Profile(id =1, user = self.new_user, family_name = 'family', mobile = '0703761111', profile_pic = 'mypic.jpg', hood = self.new_hood)
        # self.new_profile.save()

        self.new_business = Business(id = 1, name = 'Hood Business', biz_image = 'hood.jpg', description = 'hood biz', owner = self.new_profile, hood = self.new_hood, email = 'hoodbiz@gmail.com')
        # self.new_business.save()


        self.new_post = UserPost(id = 1, title = 'Welcome', post = 'Welcome to hood App', hood = self.new_hood, posted_by = self.new_profile)
        # self.new_review.save()

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        UserPost.objects.all().delete()
        Business.objects.all().delete()
        Myhood.objects.all().delete()

# instances
    def test_instance_user(self):
        self.assertTrue(isinstance(self.new_user, User))

    def test_instance_post(self):
        self.assertTrue(isinstance(self.new_post, UserPost))

    def test_instance_business(self):
        self.assertTrue(isinstance(self.new_business, Business))

    def test_instance_profile(self):
        self.assertTrue(isinstance(self.new_profile, Profile))
    
    def test_instance_hood(self):
        self.assertTrue(isinstance(self.new_hood, Myhood))
# save method
    def test_save_profile(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)
    
    def test_save_business(self):
        self.new_business.save_business()
        biz = Business.objects.all()
        self.assertTrue(len(biz) > 0)

    def test_save_hood(self):
        self.new_hood.save_hood()
        hood = Myhood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_save_post(self):
        self.new_post.save_post()
        post = UserPost.objects.all()
        self.assertTrue(len(post) > 0)

# delete method
    def test_delete_profile(self):
        profile = self.new_profile
        profile.save_profile()
        profile.delete_profile()        
        self.assertTrue(len(Profile.objects.all()) == 0)

    def test_delete_hood(self):
        hood = self.new_hood
        hood.save()
        hood.delete_hood()
        self.assertTrue(len(Myhood.objects.all()) == 0)

    def test_delete_business(self):
        biz = self.new_business
        biz.save_business()
        biz.delete_business()        
        self.assertTrue(len(Business.objects.all()) == 0)

    def test_delete_post(self):
        post = self.new_post
        post.save_post()
        post.delete_post()        
        self.assertTrue(len(UserPost.objects.all()) == 0)


# update method
    def test_update_profile(self):
        self.new_profile.save()
        profile_id = Profile.objects.last().id
        Profile.update_profile(profile_id, 'Mutua')
        new = Profile.objects.get(id = profile_id)
        self.assertEqual(new.family_name, 'Mutua')

    def test_update_neighborhood(self):
        self.new_hood.save()
        hood_id = Myhood.objects.last().id
        Myhood.update_hood(hood_id, 'Welcome gentlemen and Ladies')
        new = Myhood.objects.get(id = hood_id)
        self.assertEqual(new.description, 'Welcome gentlemen and Ladies')

    
    
    def test_update_business(self):
        self.new_business.save()
        biz_id = Business.objects.last().id
        Business.update_biz(biz_id, 'New business')
        new = Business.objects.get(id = biz_id)
        self.assertEqual(new.description, 'New business')

# search

    # def test_hood_search_by_name(self):
    #     self.new_hood.save()
    #     hood = Myhood.s('TestArea')
    #     self.assertTrue(len(hood)== 1)

    def test_profile_search_by_username(self):
        self.new_user.save()
        profile = Profile.search_user('frank')
        self.assertTrue(len(profile)== 1)

    def test_business_search_by_name(self):
        self.new_business.save()
        biz = Business.search_business('Hood Business')
        self.assertTrue(len(biz)== 1)