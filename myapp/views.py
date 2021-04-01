# 애플리케이션의 '로직'을 넣는 곳
# 모델에서 필요한 정보를 받아와서 템플릿에 전달하는 역할 (모델-템플릿 : 연결)

from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'myapp/post_list.html', {'posts': posts})