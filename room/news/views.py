from django.shortcuts import render,HttpResponse

# Create your views here.
from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

def blog_articles(request,avg1,avg2):
    return HttpResponse('6666avg1%savg2%s' %(avg1,avg2))

def comments(request,page_number):
    return HttpResponse('5555555'+page_number)
    #return HttpResponse('6666avg1%savg2%s' %(avg1,avg2))
