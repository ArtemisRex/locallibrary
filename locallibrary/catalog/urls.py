
# This is where we will add our patterns as we build the application
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]

#urlpatterns += [
#    path('catalog/', include('catalog.urls')),
#]
