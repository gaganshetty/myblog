from django.views import generic
from blogger.models import Entry

class BlogIndex(generic.ListView):
	queryset = Entry.objects.published()
	template_name = "index.html"
	
class BlogDetail(generic.DetailView):
	model =  Entry
	template_name = 'details.html'

