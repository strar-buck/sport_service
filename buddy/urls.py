from django.conf.urls import include, url
from buddy.forms import LoginForm
from views import *

urlpatterns = [
    url(r'^task/$', TaskView.as_view(), name='task'),
	url(r'^assign/$', AssignmentView.as_view(), name='assign'),
]