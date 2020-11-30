from django.shortcuts import render

from django.views.generic import TemplateView


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class SkillsPageView(TemplateView):
    template_name = 'skills.html'


class WorksPageView(TemplateView):
    template_name = 'work.html'


class ResumePageView(TemplateView):
    template_name = 'resume.html'


def bar_chart_view(request):
    y = [90,90,80,75,20,40,90,65]
    x = ['DS', 'DJ', 'CSS', 'HT', 'BS', 'JS', 'RF', 'AD']
    plt.bar(y)
    bar = plt.show()
    plt.savefig('bar')
    return render(request, 'skills.html', {'bar': bar})

