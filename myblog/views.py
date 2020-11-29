from django.shortcuts import render, get_object_or_404
from .models import Post , Comment , Contactus
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms	import	EmailPostForm , CommentForm , ContactusForm
from django.core.mail import send_mail

def	post_share(request,	post_id):
    post	=	get_object_or_404(Post,	id=post_id,	status='published') #	Retrieve	post	by	id
    sent =False
    if	request.method	==	'POST':    #	Form	was	submitted
        form	=	EmailPostForm(request.POST)
        if	form.is_valid():  #	Form	fields	passed	validation
            cd	=	form.cleaned_data 
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject	='{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message	='Read "{}"	at {}\n\n{}\'s comments:{}'.format(post.title, post_url,cd['name'],cd['comments'])
            send_mail(subject,	message, 'dubeyshivangi1910@gmail.com',[cd['to']])
            sent = True
            # print(sent)
    else:
        form	=	EmailPostForm()
    # print(sent)
    return	render(request,	'myblog/post/share.html',	{'post':	post,'form':	form,'sent':sent})


class PostListView(ListView):
    queryset	=	Post.published.all()
    context_object_name	=	'posts'
    paginate_by	=	5
    template_name	=	'myblog/post/list.html'

def	post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status='published',publish__year=year,            publish__month=month,publish__day=day)
    comments	=	post.comments.filter(active=True)     
    new_comment	=	None
    if	request.method	==	'POST':                        
        comment_form = CommentForm(data=request.POST) 	
        if	comment_form.is_valid():   
            new_comment	=comment_form.save(commit=False) 
            new_comment.post	=	post             
            new_comment.save()             
    else:
        comment_form	=	CommentForm()
    return	render(request,'myblog/post/detail.html',{'post':	post, 'comments':	comments,'new_comment':	new_comment,'comment_form':	comment_form})

def contact_us(request):
    s = False
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactusForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            s = True
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactusForm()

    return render(request, 'myblog/post/contact.html', {'form': form , 's':s})
# Create your views here.
