from django.shortcuts import render,redirect

from .models import Author, Article, Comment
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required


def index(request):
    
    return render(request, 'index.html')

def post(request, pk):
    article = Article.objects.get(article_id=pk)


    
    context = {
        'article':article
    }
    return render(request,'post.html', context)


@login_required(login_url='index')
def setting(request):
    if request.method=='POST':
        titre = request.POST['titre']
        content = request.POST['content']
        category = request.POST['category']
        if request.FILE.get('image') is None:
            article = Article.objects.create(category=category,titre=titre, body=content)
            article.save()
            return redirect('setting')
        else:
            image = request.FILE.get('image')
            article = Article.objects.create(category=category,titre=titre, body=content, article_img=image)
            article.save()
            return redirect('setting')
    return render(request, 'setting.html')