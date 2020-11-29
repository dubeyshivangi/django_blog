from django.urls import	path
from .import views
app_name	=	'myblog'

urlpatterns	=[
    # path('',views.post_list,name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:post_id>/share/',views.post_share,	name='post_share'),
    path('contact/',views.contact_us,	name='contact_us'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
]