from django.urls import path
from .views import BlogViewCreation,BlogDetailsView,BlogDeleteView,BlogUpdateView,TagCreationView,CategoryCreationView,SearchView


urlpatterns = [
    path('create/', BlogViewCreation.as_view(), name='create'),
    path('details/<int:id>/',BlogDetailsView.as_view(),name='create'),
    path('update/<int:id>/',BlogUpdateView.as_view(),name='create'),
    path('delete/<int:id>/',BlogDeleteView.as_view(),name='delete'),
    path('tag/create/',TagCreationView.as_view(),name='tag_create'),
    path('category/create/',CategoryCreationView.as_view(),name='category_create'),
    path('search/',SearchView.as_view(),name='search'),

]
