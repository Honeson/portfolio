from django.urls import path
from .views import HomePageView, SkillsPageView, WorksPageView, ResumePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('skills/', SkillsPageView.as_view(), name='skills'),
    path('works/', WorksPageView.as_view(), name='works'),
    path('resume/', ResumePageView.as_view(), name='resume'),
]