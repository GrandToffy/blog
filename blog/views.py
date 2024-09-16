from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

def post_list(request):
    num_items = request.GET.get('num_items', 5)  # По умолчанию 5 элементов на странице
    post_list = Post.objects.all()
    paginator = Paginator(post_list, num_items)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})
