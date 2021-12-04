from django.urls import path,include
from .import views
import employee

urlpatterns = [
    path('',views.employee_form,name = 'employee_insert'),
    
    path('list/', views.employee_list,name = 'employee_list'),

    path('<int:id>/',views.employee_form,name = 'create_emp'),
    path('update_emp/<str:pk>/',views.update_emp,name = 'update_emp'),
    path('employee_delete/<str:pk>/',views.employee_delete,name='employee_delete'),

    path('logout/', views.logout_page, name='logout'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
]
