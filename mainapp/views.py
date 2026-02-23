from django.shortcuts import render
from django.views import View


# Create your views here.
class HomePage(View):
    template_name = 'mainapp/homepage.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


def ballotBlitz(request):
    return render(request, 'mainapp/ballot_blitz.html')