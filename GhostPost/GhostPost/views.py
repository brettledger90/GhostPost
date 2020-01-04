from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def home(request):
    posts = Post.objects.order_by('-timestamp')

    return render(request, "home.html", {'posts': posts})

def post(request):
    if request.method == 'POST':
            form = PostForm(data=request.POST)

            if form.is_valid():
                
                data = form.cleaned_data
                print(data)
                boast = Post.objects.create(body=data['post'], typeOfPost=data['type_of_post'])
                
                redirecturl = request.POST.get('redirect', '/')

                return redirect(redirecturl)
    else:
        form = PostForm()

    return render(request, 'post.html', {'form': form})

def dislike(request, element_id):
    post = Post.objects.get(id=element_id)
    post.dislike += 1
    post.save()

    return redirect('/')

def like(request, element_id):
    post = Post.objects.get(id=element_id)
    post.like += 1
    post.save()
    
    return redirect('/')

def roasts(request):
    posts = Post.objects.filter(typeOfPost = 'Roast')
    
    return render(request, 'roast.html', {'posts': posts})

def boasts(request):
    posts = Post.objects.filter(typeOfPost = 'Boast')
    
    return render(request, 'boast.html', {'posts': posts})


def highestboasted(request):
    posts = Post.objects.order_by('-like')

    return render(request, 'highestboasted.html', {'posts': posts})

def delete(request, delete_id):
    ref = Post.objects.filter(delete=delete_id).delete()
    print(ref)
    

    return redirect("http://localhost:8000/deletesuccess")