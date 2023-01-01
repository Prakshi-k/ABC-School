from django.urls import path
from . import views


urlpatterns = [
         path('',views.index,name="index"),
         path('index',views.index,name="index"),
         path('about',views.about,name="about"),
         path('vehicle',views.vehicle,name="vehicle"),
         path('teacher',views.teacher,name="teacher"),
         path('contact',views.contact,name="contact"),
         path('contactnow_form',views.contactnow_form,name="contactnow_form"),
         
         path('login',views.user_login,name="user_login"),
         path('logout',views.user_logout,name="user_logout"),
         path('signup',views.register,name="register"),
         path('profile',views.user_profile,name="user_profile"),
         path('profile/student_rec_p/primary',views.get_student_primary,name="get_student_primary"),
         path('profile/student_rec_s/secondary',views.get_student_secondary,name="get_student_secondary"),
         path('profile/student_rec_kg/kindergarten',views.get_student_kindergarten,name="get_student_kindergarten"),

         path('juniorkg_std',views.juniorkg_std,name="juniorkg_std"),
         path('seniorkg_std',views.seniorkg_std,name="seniorkg_std"),
         path('first_std',views.first_std,name="first_std"),
         path('second_std',views.second_std,name="second_std"),
         path('third_std',views.third_std,name="third_std"),
         path('fourth_std',views.fourth_std,name="fourth_std"),
         path('fifth_std',views.fifth_std,name="fifth_std"),
         path('sixth_std',views.sixth_std,name="sixth_std"),
         path('seventh_std',views.seventh_std,name="seventh_std"),
         path('eighth_std',views.eighth_std,name="eighth_std"),
         path('ninth_std',views.ninth_std,name="ninth_std"),
         path('tenth_std',views.tenth_std,name="tenth_std"),
]
