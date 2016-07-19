from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

from django.conf import settings

#Post.objects.all()
#Post.objects.create(user=user,title="Some time")

class PostManager(models.Manager):
	def active(self,*args,**kwargs):
		return super(PostManager,self).filter(draft=False).filter(publish__lte=timezone.now())




# Create your models here.

#MVC MODEL

class Post(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	title=models.CharField(max_length=120)
	
	image=models.FileField(null=True,blank=True)
	draft=models.BooleanField(default=False)
	publish=models.DateField(auto_now=False,auto_now_add=False)
	content=models.TextField()
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)


	objects=PostManager()


	def __unicode__(self):
		return self.title
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		#return "/post/%s" %(self.id)
		return reverse("post:detail",kwargs={"id":self.id})	
	class Meta:
		ordering=["-timestamp","-updated"]
