from main.models import *
from main.forms import *

class FilmsMixin:
    def get_user_context(self, *, object_list=None, **kwargs):
        context = kwargs
        context['form'] = Search_vid()
        context['auth'] = False
        return context