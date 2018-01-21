from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from core.helpers import Pagination, SendEmail
from home.models import Movie


class HomeView(ListView):
    template_name = 'index.html'
    URL = "home_index"

    def get_queryset(self, **kwargs):
        movies = Movie.objects.all().order_by('-rating_value')

        object_list = Pagination(
            query_set=movies,
            paginate_by=10,
            page=self.request.GET.get('page')).list()

        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Home'
        context['page'] = 'home'

        return context


class MovieView(DetailView):
    model = Movie
    slug_field = 'url'
    slug_url_kwarg = 'slug'
    template_name = 'movie.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Movies'
        context['page'] = 'movies'

        print(context)

        return context


class TestEmail(View):
    def get_context_data(self, **kwargs):
        kwargs['page_title'] = ''
        kwargs['page'] = 'home'
        return kwargs

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        SendEmail(
            template_name='email_test.html',
            subject='Test',
            to=['kovach.matej@gmail.com'],
            data={}
        )
        return render(self.request, 'index.html', context)
