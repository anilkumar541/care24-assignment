from django.urls import path
from rest_framework.routers import DefaultRouter
from mainapp.views import  ContentViewSet, AuthorRegistrationView, AuthorLoginView



router = DefaultRouter()
router.register(r'content', ContentViewSet, basename='content')


urlpatterns = [

    path('author-register/', AuthorRegistrationView.as_view(), name='author-register'),
    path('author-login/', AuthorLoginView.as_view(), name='author-login'),


]+router.urls



# pip install djangorestframework djangorestframework-simplejwt pytest-django
# check this
