from django.urls import path
from .views import register,success_view,login_view,fleet_manager_home_view,driver_home_view,introduction_to_ev,dataset,distribution,relationship,vehicle_status,redirect_to_distribution,prediction_view,relationship_view,predict_electric_range,home_view

urlpatterns = [
    path("", home_view, name="home"),
    path("register/", register, name='register'),
    path('success/', success_view, name='success_url'),  # Success URL
    path('login/', login_view, name='login'),
    # Define other URLs for fleet manager and driver pages
    path('fleet_manager_home/', fleet_manager_home_view, name='fleet_manager_home'),
    path('driver_home/', driver_home_view, name='driver_home'),
    #Fleet Manager Dashboard
    path('introduction_to_ev/', introduction_to_ev, name='introduction_to_ev'),
    path('dataset/', dataset, name='dataset'),
    path('distribution/', distribution, name='distribution'),
    path('relationship/', relationship, name='relationship'),
    path('vehicle_status/', vehicle_status, name='vehicle_status'),
    # path('distribution/', distribution_view, name='distribution'),
    path('distribution/', redirect_to_distribution, name='distribution'),
    path('prediction/', prediction_view, name='prediction'),
    path('relationship/', relationship_view, name='relationship'),
    path('predict/', predict_electric_range, name='predict')
]

