from django.views import View
from django.shortcuts import redirect
from django.shortcuts import render

class HomeView(View):
    template_name = 'pages/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)