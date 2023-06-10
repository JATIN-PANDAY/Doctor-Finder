from django.urls import path,include
from myapp import views

urlpatterns = [
    path("",views.index,name='index'),
    path('contact',views.message,name='contact'),
    path('signup',views.Signuppage,name='signup'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('logout',views.logout,name='logout'),
    path('profilepage/<int:pk>',views.profilepage,name='profilepage'),
    path('patientprofileupdate/<int:pk>',views.patientprofileupdate,name='patientprofileupdate'),
    path('doctorprofilepage/<int:pk>',views.doctorprofilepage,name='doctorprofilepage'),
    path('doctorprofileupdate/<int:pk>',views.doctorprofileupdate,name='doctorprofileupdate'),
    path('patienthomepage',views.patienthomepage,name='patienthomepage'),
    path('appointment/<int:pk>',views.appointment,name='appointment'),
    path('checkdepartment/<int:pk>',views.checkdepartment,name='checkdepartment'),
    path('doctorshowappointment/<int:pk>',views.doctorshowappointment,name='showappointment'),
    path('doctorsendappointmentpage/<int:pk>',views.doctorsendappointmentpage,name='doctorsendappointmentpage'),
    path('doctorsendappointment',views.doctorsendappointment,name='doctorsendappointment'),
    path('patientcheckdepartment/<int:pk>',views.patientcheckdepartment,name='patientcheckdepartment'),
    path('patientshowappointment/<int:pk>',views.patientshowappointment,name='patientshowappointment'),
    path('Patientcontact/<int:pk>',views.Patientcontact,name='Patientcontact'),


]
