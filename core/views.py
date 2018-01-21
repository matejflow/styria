from django.views.generic import ListView

from home.models import Movie

from .helpers import Pagination
from .mixins import StaffLoginMixin


class HomeView(StaffLoginMixin, ListView):
    model = Movie
    template_name = 'admin_index.html'
    URL = "admin_index"

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

        print(context)
        return context
