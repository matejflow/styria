from django.conf.urls import url

from .views import HomeView, MovieView, TestEmail

urlpatterns = [
    url(r'^$', HomeView.as_view(), name=HomeView.URL),
    url(r'^movie/(?P<slug>[_\w]+)/$', MovieView.as_view(), name="movie_details"),
    url(r'^test_email/$', TestEmail.as_view(), name="test_email"),

]
