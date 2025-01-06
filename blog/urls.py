from django.urls import path
from .views import BlogViewCreation,BlogDetailsView,BlogDeleteView,BlogUpdateView,TagCreationView,CategoryCreationView,SearchView,BlogFilterationView,BlogListView


urlpatterns = [
    path('create/', BlogViewCreation.as_view(), name='create'),
    path('details/<int:id>/',BlogDetailsView.as_view(),name='details'),
    path('update/<int:id>/',BlogUpdateView.as_view(),name='update'),
    path('delete/<int:id>/',BlogDeleteView.as_view(),name='delete'),
    path('tag/create/',TagCreationView.as_view(),name='tag_create'),
    path('category/create/',CategoryCreationView.as_view(),name='category_create'),
    path('search/',SearchView.as_view(),name='search'),
    path('filter/',BlogFilterationView.as_view(),name='filter'),
    path('list/',BlogListView.as_view(),name='list'),

]
