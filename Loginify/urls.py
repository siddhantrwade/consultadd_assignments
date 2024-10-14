from django.urls import path
from .views import hello_world
from .views import login_view
from .views import signup_view
from .views import home_view # for some reason this import is not working as it should, debug later
from . import views # import all view functions created within this app


urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name = 'login'), # the template for this url path is nested inside loginify folder within templates
    path('home/', views.home_view, name = 'home'),
         
]