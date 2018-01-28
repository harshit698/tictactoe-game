from django.conf.urls import url
from django.contrib.auth.views import Loginview,Logoutview


from .views import home

urlpatterns=[
	url(r'home$',home,name="player_home")
	url(r'login$',
		Loginview.as_view(template_name="player/login_form.html"),
		name="player_login"),
	url(r'logout$',
		Logoutview.as_view(),
		name="player_logout"),
]