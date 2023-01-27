from django.urls import path
from . import views
from django.views.generic.base import TemplateView 

urlpatterns = [

    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('<int:pk>/', views.post, name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',views.AuthorDetailView.as_view(), name='author-detail'),
]

urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]

urlpatterns += [
    path('book/create/', views.create_book, name='book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    path('book/<int:pk>/addcart/', views.SaveCart, name ='add-cart'),
    path('cart/', views.CartView, name ='cart'),


]

urlpatterns +=[
    path('register/', views.register, name = 'register'),
]