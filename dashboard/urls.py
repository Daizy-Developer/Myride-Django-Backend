from . import views
from django.urls import path , include
urlpatterns = [
    # path('accounts/', include('allauth.urls')),  
    path('',views.index),
    path('update-fare',views.update_fare),
    path('fare-management',views.fare_management),
  
    path("user" ,views.user),
    path("driver-details/<int:id>/" ,views.driver_detailss),
    path('Ride-logs',views.ride_logs),
    path('logout',views.USR_Logout),
    path('update_driver/<int:id>',views.updatedriver),
    path('user-details/<int:id>',views.updateuser),
    
    # Api's
    # Driver's Api Urls
    path('user-data/<str:UId>',views.user_details),
    path('driver-data/<str:UId>',views.driver_details),
    path('drivers_api/', views.driver_api),# GET ,POST
    path('driver_api_put_delete/<int:pk>/',views.driver_api_put_delete),#GET, PUT ,DELETE
    path('driver_api_patch/<int:pk>/',views.driver_patch),#PATCH
    # User's Api Urls
    path('user_api/', views.user_api),# GET ,POST
    path('user_api_put_delete/<int:pk>/',views.user_api_put_delete), #GET, PUT ,DELETE
    path('user_api_patch/<int:pk>/',views.user_patch),#PATCH
 
    # Promocode 
    # path('promocode/<str:Promocode>',views.promocode_api,name="Promocode Api"),
    # path('add-promocode/',views.add_promocode,name="Promocode Api "),
    path('ride_history/<str:User_Uid>',views.Ride_History, name="Ride_History"),
    path('ride_history/driver/<str:Driver_Uid>',views.Driver_Ride_History, name="Ride_History"),
    # path('new-ride',views.New_Ride, name="New Ride"),
    path("Driver-ratings/<int:id>",views.Driver_Ratings, name="Driver-ratings"),
    path("User-ratings/<int:id>",views.User_Ratings, name="Driver-ratings"),
    path("status/<int:id>",views.Trip_Status),
    path("Cancellation-Reason/<int:id>",views.Cancellation_Reason),
    path("Mini_Fare/<int:Km>",views.Get_Mini_Fare),
    path("Luxury_Fare/<int:Km>",views.Get_Luxury_Fare),
    path("Ac_Fare/<int:Km>",views.Get_Ac_Fare),
    path("Bike_Fare/<int:Km>",views.Get_Bike_Fare),
    path("Update_Fare/<int:id>/<str:Car>/<int:Km>/",views.Update_Fare),
    path("Kms/<int:id>",views.Km),
    path('bike-ride',views.Bike_Ride, name="New Ride"),
    path('car-ride',views.Car_Ride, name="New Ride"),
    path("offer_ride_get/<str:User_Uid>/<str:Date>/<str:Ride_Time>",views.Ride_Offer_Get),
    path("offer_ride_post/",views.Ride_Offer_Post),
    path("driver_offer_ride/<int:Ride_id>",views.Driver_Ride_Offer_Get),
    path("driver_offer_ride",views.Driver_Ride_Offer_Post),
    path("add_carpool/<int:id>",views.Add_Carpool_Ride),
    path("Ride-Details/<int:id>",views.Ride_Details),
    path('new-ride/<str:vehicle>',views.New_Ride, name="New Ride"),
    path('delivery',views.New_Delivery, name="New Ride"),
    path('User-Ride-Message/<int:Ride_id>',views.User_Ride_Message),
    path('Driver-Ride-Message/<int:Ride_id>',views.Driver_Ride_Message),
    path('User-Specific-Message/<int:id>',views.User_Specific_Message),
    path('Driver-Specific-Message/<int:id>',views.Driver_Specific_Message),
    path('Driver-Message',views.DriverMessage),
    path('User-Message',views.UserMessage),
    path("Location/<int:id>/<str:pickup_location_lat>/<str:pickup_location_long>/<str:drop_location_lat>/<str:drop_location_long>",views.Location),


    ]
