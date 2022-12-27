from rest_framework import serializers
from dashboard.models import Driver ,User , Promo_Code , All_Ride_Historie,Ride_offer,Driver_offer,User_Message,Driver_Message



class Driver_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['UId','name','date_of_birth','gender',
        'phone_number','home_address','ratings','total_rides']
class Promocode_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Promo_Code
        fields = '__all__'

class All_Ride_Historie_Serializer(serializers.ModelSerializer):
    class Meta:
        model = All_Ride_Historie
        fields = '__all__'

class Driver_Rating_Serializer(serializers.ModelSerializer):
    class Meta:
        model = All_Ride_Historie
        fields = ['Driver_ratings']
class User_Rating_Serializer(serializers.ModelSerializer):
    class Meta:
        model = All_Ride_Historie
        fields = ['User_ratings']
class Status_Ride_Serializer(serializers.ModelSerializer): 
    class Meta:
        model = All_Ride_Historie
        fields = ['status']
class Cancel_Ride_Serializer(serializers.ModelSerializer):
    class Meta:
        model = All_Ride_Historie
        fields = ['Cancel_Ride']
class Fare_S(serializers.ModelSerializer):
    class Meta:
        model = All_Ride_Historie
        fields = ['Km']


class Km_S(serializers.ModelSerializer):
    class Meta:
        model = All_Ride_Historie
        fields = ['Km']


class Offer_Price_Get(serializers.ModelSerializer):
    class Meta:
        model = Ride_offer
        fields = '__all__'
        
class Offer_Price_Post(serializers.ModelSerializer):
    class Meta:
        model = Ride_offer
        fields = '__all__'

class Ride_Bike_Serializer(serializers.ModelSerializer):
    class Meta:
        model = All_Ride_Historie
        fields = ['User_Uid','Ride','Date','Ride_Time','pickup_location_lat','pickup_location_long','drop_location_lat','drop_location_long','Address','Drop_Address','Km','Fare','User_ratings','Driver_ratings','Cancel_Ride','status']
class Ride_Car_Serializer(serializers.ModelSerializer):
    class Meta:
        model = All_Ride_Historie
        fields = ['User_Uid','Ride','Carpooling_User_1_Uid','Carpooling_User_2_Uid','Carpooling_User_3_Uid','Date','Ride_Time','pickup_location_lat','pickup_location_long','drop_location_lat','drop_location_long','Address','Drop_Address','Km','Fare','User_ratings','Driver_ratings','Cancel_Ride','status']

class Add_Carpool_Serializer(serializers.ModelSerializer):
    class Meta:
        model = All_Ride_Historie
        fields = ['Carpooling_User_1_Uid','Carpooling_User_2_Uid','Carpooling_User_3_Uid']

class Driver_Offer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Driver_offer
        fields = '__all__'
class Delivery_Serailizer(serializers.ModelSerializer):
    class Meta:
        model =  All_Ride_Historie
        fields = ['User_Uid','Ride_Type','Fragile','Date','Ride_Time','pickup_location_lat','pickup_location_long','drop_location_lat','drop_location_long','Km','Fare','User_ratings','Driver_ratings','Cancel_Ride','status']

class User_Img(serializers.ModelSerializer):
    # user_image = serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=False,use_url=True,required=True)
    class Meta:
        model = User
        fields = ['user_image']

class Driver_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Driver_Message
        fields = '__all__'
class User_Messages_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Message
        fields = '__all__'
class Driver_Messages_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Driver_Message
        fields = '__all__'
