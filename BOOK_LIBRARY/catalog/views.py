 
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .form import CreateBookForm, RegistrationForm, CommentForm
from .models import Book, Author, Genre, Cart, CartItem
from django.http import HttpResponseRedirect



def SaveCart(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == "POST":
        if Cart.objects.filter(buyer = request.user):
            cart = Cart.objects.get(buyer = request.user)
        else:
            cart = Cart.objects.create(buyer = request.user)

        cart_item = CartItem.objects.create(quantity = request.POST['quantity'], book = book)
        cart.items.add(cart_item)
        

    
    return render(request, 'catalog/add_cart.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'register.html', {'form': form})

class BookListView(generic.ListView):
    model = Book
    paginate_by = 30
    
class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

class AuthorDetailView(generic.DetailView):
    model = Author



from catalog.models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/06/2020'}

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__' # Not recommended (potential security issue if more fields added)

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

def create_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST, request.FILES)
        if form.is_valid():
            
            # file is saved
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CreateBookForm()
    return render(request, 'catalog/book_form.html', {'form': form})

class BookUpdate(UpdateView):
    model = Book
    fields ='__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')


def CartView(request):
    if Cart.objects.filter(buyer = request.user):
        cart = Cart.objects.get(buyer = request.user)
    else:
        cart = Cart.objects.create(buyer = request.user)
    context = {"cart": cart}
    return render(request,'catalog/cart_detail.html', context)

def post(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, assessor=request.user, book=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = CommentForm()
    return render(request, 'catalog/book_detail.html', {"book": book, "rate_form": form})
