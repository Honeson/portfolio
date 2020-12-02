from django.urls import path
from .views import HomePageView, SkillsPage, WorksPage, ResumePage, HomePage, successView

urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    path('', HomePage, name='home'),
    path('success/', successView, name='success'),
    path('skills/', SkillsPage, name='skills'),
    path('works/', WorksPage, name='works'),
    path('resume/', ResumePage, name='resume'),
]