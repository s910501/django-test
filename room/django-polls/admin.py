from django.contrib import admin
from .models import Question,Choice

# Register your models here.
#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    ## 显示数据、过滤等
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    ## 显示列表
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    ## 过滤列表
    list_filter = ['pub_date']
    ## 搜索
    search_fields = ['question_text']


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
