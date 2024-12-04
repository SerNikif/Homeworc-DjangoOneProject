from django.shortcuts import render
from django.views.generic import TemplateView


def function_view(request):
    return render(request, 'func_template.html')


class ClassView(TemplateView):
    template_name = 'class_template.html'
