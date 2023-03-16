from django.urls import path, include
from django.contrib import admin

from empapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),

    path('api', include('api.urls')),


    path('', views.emp, name='emp'),
    path('addEmployee', views.addEmployee, name='addEmployee'),
    path('rememp', views.rememp, name='rememp'),
    path('rememp/<int:emp_id>', views.rememp, name='rememp'),
    path('viewEmployee', views.viewEmployee, name='viewEmployee'),
    # path('editEmployee/<int:empId>', views.editEmployee, name='editEmployee'),
    path('editEmployee', views.editEmployee, name='editEmployee'),

    path('UPDATE/<int:id>', views.UPDATE, name='editEmployee'),
    path('filter', views.filter, name='filter'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
