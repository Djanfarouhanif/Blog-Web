from django.shortcuts import render,redirect

from .models import Author, Article, Comment, Response
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required


def index(request):
    article = Article.objects.all()
    return render(request, 'index.html',{'articles':article})

def post(request, pk):
    article = Article.objects.get(article_id=pk)

    #comment = Comment.objects.get(article=article)


    
    context = {
        'article':article,
        'comments':comment

    }
    return render(request,'post.html', context)


@login_required(login_url='index')
def setting(request):
    
    if request.method=='POST':
        titre = request.POST['titre']
        content = request.POST['content']
        category = request.POST['category']
        if request.FILES.get('image') is None:
            article = Article.objects.create(category=category,titre=titre, body=content)
            article.save()
            return redirect('setting')
        else:
            image = request.FILES.get('image')
            article = Article.objects.create(category=category,titre=titre, body=content, article_img=image)
            article.save()
            return redirect('setting')
    return render(request, 'setting.html')

def comment(request,pk):
    article  = Article.objects.get(article_id=pk)
    if request.method=='POST':
        print("post")

        comment = request.POST['comment']
       

        new_comment = Comment.objects.create(article=article,comment=comment)
        new_comment.save()
        return redirect('post', pk=pk)
    else:
        return redirect('post',pk=pk)
       
    
