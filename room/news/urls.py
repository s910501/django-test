from django.conf.urls import url

from . import views

urlpatterns = [
    ## 嵌套参数
    url(r'blog/(page-(\d+)/)?$', views.blog_articles),                  # bad
    url(r'comments/(?:page-(?P<page_number>\d+)/)?$', views.comments),  # good
    ## 额外参数
    url(r'^articles/([0-9]{4})/$', views.year_archive,{'foo':'bar'}),


    #url(r'^articles/2003/$', views.special_case_2003),
    #url(r'^articles/([0-9]{4})/$', views.year_archive),
    #url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    #url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
]
