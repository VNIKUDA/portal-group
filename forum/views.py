from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post

def forum_home(request):
    threads = Thread.objects.all()
    return render(request, 'forum/forum_home.html', {'threads': threads})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    return render(request, 'forum/thread_detail.html', {'thread': thread})

def new_thread(request):
    if request.method == 'POST':
        title = request.POST['title']
        thread = Thread.objects.create(title=title, created_by=request.user)
        return redirect('thread_detail', id=thread.id)
    return render(request, 'forum/new_thread.html')

def new_post(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == 'POST':
        message = request.POST['message']
        Post.objects.create(thread=thread, message=message, created_by=request.user)
        return redirect('thread_detail', id=thread_id)
    return render(request, 'forum/new_post.html', {'thread': thread})

