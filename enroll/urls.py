from django.urls import path
from .views import StuCreView, StuUpdView, StuDelView, StudentListView

urlpatterns = [
    path('', StuCreView.as_view(template_name ='enroll/add.html'), name='add'),
    path('show/', StudentListView.as_view(template_name='enroll/show.html'), name='show'),
    path('update/<int:pk>/', StuUpdView.as_view(template_name='enroll/update.html'), name='update'),
    path('delete/<int:pk>/', StuDelView.as_view(template_name='enroll/addshow.html'), name='delete')
]
