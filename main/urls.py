from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import BookViewSet, JournalViewSet
router = DefaultRouter()
router.register('books', viewset=BookViewSet, basename='books')
router.register('journals', viewset=JournalViewSet, basename='journals')


urlpatterns = [
    path('', include(router.urls))
]
