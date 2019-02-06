from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

class Blog(models.Model):
	
	name = models.CharField(max_length=20, verbose_name='博客标题')
	desc = models.TextField(verbose_name='博客摘要')
	detail = UEditorField(verbose_name='博客内容',width=800, height=300, toolbars="full", imagePath="upload/ueditor/", filePath="upload/ueditor/", upload_settings={"imageMaxSize":1204000},default='')

	class Meta:
		verbose_name_plural = '博客数据库'
