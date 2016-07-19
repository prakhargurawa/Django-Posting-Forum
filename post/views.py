from urllib import quote_plus

from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render ,get_object_or_404,redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from django.utils import timezone

from .forms import PostForm


from .models import Post
# Create your views here.

def posts_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	#if not request.user.is_authenticated():
		#raise Http404

	form=PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.user=request.user
		print form.cleaned_data.get("title")
		instance.save()
		messages.success(request,"Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())  
	
		  
	#if request.method =="POST":
		#print request.POST.get("content")
		#print request.POST.get("title")
	
	context={
		"form":form,
	}
	return render(request,"post_form.html",context)


def posts_detail(request,id=None):
	#instance=Post.objects.get(id=100)
	#instance=get_object_or_404(Post,title="myfirstpost")
	instance=get_object_or_404(Post,id=id)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string=quote_plus(instance.content)
	context = {
		"title":instance.title,
		"instance":instance,
		"share_string":share_string,
	}
	return render(request,"post_detail.html",context)
	#return HttpResponse("<h1>Hello Prakhar this is detail</h1>")




def posts_list(request):
	today=timezone.now().date()
	queryset_list=Post.objects.active()
	if request.user.is_staff or request.user.is_superuser:
		queryset_list=Post.objects.all()
	#queryset_list = Post.objects.filter(draft=False).filter(publish__lte=timezone.now())#all().order_by("-timestamp")
	query=request.GET.get("q")
	if query:
		queryset_list=queryset_list.filter(title__icontains=query)
	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	page_request_var="page"
	page=request.GET.get(page_request_var)
    	#page = request.GET.get('page')
    	try:
        	queryset = paginator.page(page)
    	except PageNotAnInteger:
        	# If page is not an integer, deliver first page.
        	queryset = paginator.page(1)
    	except EmptyPage:
        	# If page is out of range (e.g. 9999), deliver last page of results.
        	queryset = paginator.page(paginator.num_pages)



	#if request.user.is_authenticated():
	#	context = {
	#	"title":"My User List"
	#	}
	#else:
	context = {
		"object_list":queryset,
		"title":"List",
		"page_request_var":page_request_var,
		"today":today,
	}
	return render(request,"post_list.html",context)
	
	#return HttpResponse("<h1><center>Hello Prakhar this is list</center></h1>")







def posts_update(request,id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance=get_object_or_404(Post,id=id)
	form=PostForm(request.POST or None,request.FILES or None,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully Saved",extra_tags='some-tags')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title":instance.title,
		"instance":instance,
		"form":form,
	}
	return render(request,"post_form.html",context)


def posts_delete(request,id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance=get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request,"Successfully deleted");
	return redirect("post:list")

