from django.shortcuts import render
from django.forms import forms
from DjangoUeditor.forms import UEditorField
from  DjangoUeditor.widgets import UEditorWidget

from .models import Blog

# Create your views here.


class TestUEditorForm(forms.Form):
	Description=UEditorField("test-ueditor",initial="这是一个测试的富文本编辑器！！",width=600,height=800)


# 测试前端富文本
def ueditor_test(request):
	forms = TestUEditorForm()

	return render(request,'ueditor_test.html',{'forms':forms})


# 测试富文本数据库的前后端交互
def ueditor_blog(request):
	title = Blog.objects.all().values('name')
	desc = Blog.objects.all().values('desc')
	detail = Blog.objects.all().values('detail')

	cons = {'title':title,'desc':desc,'detail':detail}

	return render(request,'ueditor_blog.html',cons)

