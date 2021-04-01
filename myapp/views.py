# 애플리케이션의 '로직'을 넣는 곳
# 모델에서 필요한 정보를 받아와서 템플릿에 전달하는 역할

from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'myapp/post_list.html', {})