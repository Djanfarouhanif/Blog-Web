from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Author, Article, Comment, Response
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from  itertools import chain
import random


def index(request):
    article_sugg = []
    if request.method == 'POST':
        if request.POST.get('categorie'):
            current_article = request.POST.get('categorie')
            article= Article.objects.filter(category__icontains=current_article)
           
            for  i in article:
                article_sugg.append(i)

        elif request.POST.get('search'):
            search = request.POST.get('search')
            article = Article.objects.filter(category__icontains=search)
            for i in article:
                article_sugg.append(i)
        
    else:

        article = Article.objects.all()
        for i in article:
            article_sugg.append(i)
    random.shuffle(article_sugg)
    print(article_sugg, '=============================')
    return render(request, 'index.html',{'articles':article_sugg})


def post(request, pk):
    article = Article.objects.get(article_id=pk)

    if request.method == 'POST':
        comment_text = request.POST['comment']
        new_comment = Comment.objects.create(article=article, comment=comment_text)
        new_comment.save()
        
        
        return redirect('post', pk=pk)

    comment_current = Comment.objects.filter(article=article)
    comment_response = {}

    for existing_comment in comment_current:
        response = Response.objects.filter(id_response=existing_comment.id)
        comment_response[existing_comment] = response

    context = {
        'article': article,
        'comment_response': comment_response,
    }

    return render(request, 'post.html', context)

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

def response(request):
    comment_id = request.GET.get('comment_id')
    comment = Comment.objects.get(id=comment_id)
    comment_uuid = comment.article.article_id
    if request.method == 'POST':
        response = request.POST['response']
        new_response = Response.objects.create(id_response=comment_id, response=response, comment_parent=comment)
        new_response.save()
        return redirect(f'post/{comment_uuid}')
    else:
        return redirect(f'post/{comment_uuid}')
    


