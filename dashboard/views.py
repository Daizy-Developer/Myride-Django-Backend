from importlib.machinery import all_suffixes
from os import rename
from urllib import request, response
from django.shortcuts import render,redirect,HttpResponse
# from itsdangerous import Serializer
from dashboard.models import Driver, User,All_Ride_Historie,Ride_offer,Driver_offer,Saved_Destination,Earning
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
# import requests
# Modules For Crating Api
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.parsers import FormParser,MultiPartParser
from dashboard.serializer import Saved_Destination_Serializer, Driver_Rating_Serializer, Driver_Serializer,User_Serializer,User_Rating_Serializer,Driver_Rating_Serializer,All_Ride_Historie_Serializer,Status_Ride_Serializer,Cancel_Ride_Serializer,Fare_S,Km_S,Ride_Bike_Serializer,Ride_Car_Serializer,Offer_Price_Get ,Offer_Price_Post,Add_Carpool_Serializer,Driver_Offer_Serializer,Driver_Details_Serializer,Delivery_Serailizer,User_Message,Driver_Message,User_Messages_Serializer,Driver_Messages_Serializer,Add_Driver_Serializer,Add_Driver_Serializer ,Earning_Serializer,Driver_Image_Serializer,User_Image_Serializer
from  dashboard.forms import DriverForms,UserForms
import geopy.distance
import polyline
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
# Create your views here.
from django.shortcuts import render
luxury_fare = 12
mini_fare = 6
ac_fare = 8
bike_fare = 4
def update_fare(request):
        # user = User.objects.all()
    global luxury_fare,mini_fare,ac_fare,bike_fare
    bef_luxury_fare = luxury_fare
    bef_mini_fare = mini_fare
    bef_ac_fare = ac_fare
    bef_bike_fare = bike_fare
    # ac_fare =request.GET.get('Mini_Fare')
    # bike_fare =request.GET.get('Mini_Fare')
    upt_mini_fare =request.GET.get('Mini_Fare')
    upt_luxury_fare =request.GET.get('Luxury_Fare')
    upt_ac_fare =request.GET.get('Ac_Fare')
    upt_bike_fare =request.GET.get('Bike_Fare')
    print(upt_mini_fare)
    mini_fare =  upt_mini_fare
    luxury_fare =  upt_luxury_fare
    ac_fare =  upt_ac_fare
    bike_fare =  upt_bike_fare
    if mini_fare is None:
        mini_fare = bef_mini_fare
    if luxury_fare is None:
        luxury_fare = bef_luxury_fare
    if ac_fare is None:
        ac_fare = bef_ac_fare
    if bike_fare is None:
        bike_fare = bef_bike_fare
    return render(request,"fare.html",{"mini_fare":mini_fare,"luxury_fare":luxury_fare,"ac_fare":ac_fare,"bike_fare":bike_fare})

def fare_management(request):

    return render(request,"fare.html",{"mini_fare":mini_fare,"luxury_fare":luxury_fare,"ac_fare":ac_fare,"bike_fare":bike_fare})

@ensure_csrf_cookie
@csrf_protect
def index(request):
    driver_details = Driver.objects.all()
    app_users = User.objects.all()
    app_driver = Driver.objects.all()
    # USR = None
    if request.method=='POST' :
        # user = User.objects.all()
        USR_NAME = request.POST['username']
        PASSWORD = request.POST['password']
        USR = authenticate(username=USR_NAME,password= PASSWORD)
        if USR is not None:
            login(request,USR)
            return render(request,'dashboard.html',{'app_users':app_users,'app_driver':app_driver ,'driver':driver_details})
            
    
    if request.user.is_authenticated:
            return render(request,'dashboard.html',{'app_users':app_users,'app_driver':app_driver ,'driver':driver_details}) 
 
    return render(request,'user/user.html')

def USR_Logout(request):
    logout(request)
    return redirect('/')

def user(request):
    app_users = User.objects.all()

    if request.user.is_authenticated:
         return render(request,'Index.html',{'app_users':app_users}) 
    return HttpResponse("400 Bad Request")



def driver_detailss(request ,id):
    driver_profile = Driver.objects.filter(id=id)
    return render(request,'driver-details.html',{'driver_profile':driver_profile[0]})
def updatedriver(request ,id):
    driver_profile = Driver.objects.get(pk=id)
    form =  DriverForms(request.POST or None,instance=driver_profile )

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'driver_profile':driver_profile,'form':form})

def updateuser(request ,id):
    user_profile = User.objects.get(pk=id)
    form =  UserForms(request.POST or None,instance=user_profile )
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'user-details.html',{'user_profile':user_profile,"form":form})
def ride_logs(request):
    ride_log = All_Ride_Historie.objects.all()
    return render(request ,'ride-history.html',{'ride':ride_log})
# Api
# Driver
@api_view(['GET','POST','PUT'])
def driver_api(request):

    if request.method == 'GET':
        drivers = Driver.objects.all()
        serializer = Driver_Serializer(drivers,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Driver_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def driver_api_put_delete(request, pk):

    try:
        snippet = Driver.objects.get(pk=pk)
    except Driver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Driver(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Driver_Serializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(['PATCH'])
def driver_patch(request,pk):
    try:
        snippet = Driver.objects.get(pk=pk)
    except Driver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PATCH':
        serializer = Driver_Serializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED) 
    return Response(status=status.HTTP_400_BAD_REQUEST) 

# User API
@api_view(['GET'])
def driver_details(request,UId):
   
    if request.method == 'GET':
        driver= Driver.objects.filter(UId=UId).first()
        serializer = Driver_Serializer(driver)
        return Response(serializer.data)

@api_view(['GET'])
def user_details(request,UId):
    if request.method == 'GET':
        driver= User.objects.filter(UId=UId).first()
        serializer = User_Serializer(driver)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def user_api(request):

    if request.method == 'GET':
        user = User.objects.all()
        serializer = User_Serializer(user,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = User_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_api_put_delete(request, pk):

    try:
        snippet = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = User(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = User_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(['PATCH'])
def user_patch(request,pk):
    try:
        snippet = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PATCH':
        serializer = User_Serializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED) 
    return Response(status=status.HTTP_400_BAD_REQUEST) 


# Ride Details 





# Promocode 

# Promocode 


# @api_view()

# User Trip History.

@api_view(['GET'])
def Ride_History(request,User_Uid):
    try:
        Passenger = All_Ride_Historie.objects.filter(User_Uid=User_Uid)

    except All_Ride_Historie.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        user= All_Ride_Historie.objects.filter(User_Uid=User_Uid)
        serializer = All_Ride_Historie_Serializer(user, many=True)
        return Response(serializer.data)

# Driver Ride History
@api_view(['GET'])
def Driver_Ride_History(request,Driver_Uid):
    if request.method == 'GET':
        driver= All_Ride_Historie.objects.filter(Driver_Uid=Driver_Uid)
        serializer = All_Ride_Historie_Serializer(driver, many=True)
        return Response(serializer.data)


@api_view([ 'GET','PATCH'])
def User_Ratings(request,id):
    try:
        # snippet = All_Ride_Historie.objects.filter(otp=otp,Date=Date)
        snippet = All_Ride_Historie.objects.get(id=id)
    except All_Ride_Historie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        # driver= All_Ride_Historie.objects.filter(Driver_Detail=Driver_Detail)
        # serializer = Driver_Rating_Serializer(snippet, many=True)
        serializer = User_Rating_Serializer(snippet)
        print("Get new User details", serializer)
        return Response(serializer.data)
    elif request.method=="PATCH":
        new_serializer=User_Rating_Serializer(snippet, data=request.data)
        if new_serializer.is_valid():
            new_serializer.save()
            print("after patch request", new_serializer)
        return Response(new_serializer.data) # ERROR 
    return Response(new_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view([ 'GET','PATCH'])    
def Driver_Ratings(request,id):
    try:
        # snippet = All_Ride_Historie.objects.filter(otp=otp,Date=Date)
        snippet = All_Ride_Historie.objects.get(id=id)
    except All_Ride_Historie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        # driver= All_Ride_Historie.objects.filter(Driver_Detail=Driver_Detail)
        # serializer = Driver_Rating_Serializer(snippet, many=True)
        serializer = Driver_Rating_Serializer(snippet)
        print("Get new driver details", serializer)
        return Response(serializer.data)
    elif request.method=="PATCH":
        new_serializer=Driver_Rating_Serializer(snippet, data=request.data)
        if new_serializer.is_valid():
            new_serializer.save()
            print("after patch request", new_serializer)
        return Response(new_serializer.data) # ERROR 
    return Response(new_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view([ 'GET','PATCH'])
def Trip_Status(request,id):
    try:
        snippet = All_Ride_Historie.objects.get(id=id)
    except All_Ride_Historie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        # driver= All_Ride_Historie.objects.filter(Driver_Detail=Driver_Detail)
        serializer = Status_Ride_Serializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = Status_Ride_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("---------- calling", serializer)
            return Response(serializer.data) # ERROR 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view([ 'GET','PATCH'])
def Cancellation_Reason(request,id):
    try:
        snippet = All_Ride_Historie.objects.get(id=id)
    except All_Ride_Historie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        # driver= All_Ride_Historie.objects.filter(Driver_Detail=Driver_Detail)
        # serializer = Cancel_Ride_Serializer(snippet, many=True)
        serializer = Cancel_Ride_Serializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        #snippet = All_Ride_Historie.objects.all()
        #snippet = All_Ride_Historie.objects.filter()
        serializer = Cancel_Ride_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("---------- calling", serializer)
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view([ 'GET'])
def Get_Mini_Fare(request,Km):
    try:
        # snippet = All_Ride_Historie.objects.filter(otp=otp,Date=Date).first()
        Kilometre = Km*int(mini_fare)
    except All_Ride_Historie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(Kilometre)

@api_view([ 'GET'])
def Get_Luxury_Fare(request,Km):
    try:
        # snippet = All_Ride_Historie.objects.filter(otp=otp,Date=Date).first()
        Kilometre = Km*int(luxury_fare)
    except All_Ride_Historie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(Kilometre)

@api_view([ 'GET'])
def Get_Ac_Fare(request,Km):
    try:
        # snippet = All_Ride_Historie.objects.filter(otp=otp,Date=Date).first()
        Kilometre = Km*int(ac_fare)
    except All_Ride_Historie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(Kilometre)
@api_view([ 'GET'])
def Get_Bike_Fare(request,Km):
    try:
        # snippet = All_Ride_Historie.objects.filter(otp=otp,Date=Date).first()
        Kilometre = Km*int(bike_fare)
    except All_Ride_Historie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(Kilometre)


@api_view([ 'PATCH'])
def Update_Fare(request,id,Car,Km):
    try:
        snippet = All_Ride_Historie.objects.get(id=id)
        if Car == "Luxury":
            Kilometre = Km*int(luxury_fare)
        elif Car == "Ride Mini":
            Kilometre = Km*int(mini_fare)
        elif Car == "Ride AC":
            Kilometre = Km*int(ac_fare)
        elif Car == "Bike":
            Kilometre = Km*int(bike_fare)
        else:return Response(status=status.HTTP_404_NOT_FOUND)

    except All_Ride_Historie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(Kilometre)
    if request.method == 'PATCH':
        serializer = Fare_S(snippet, data={"Km":Kilometre})
        if serializer.is_valid():
            serializer.save()
            print("---------- calling", serializer)
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view([ 'GET'])
def Ride_Offer_Get(request,User_Uid,Date,Ride_Time):
    try:
        snippet = Ride_offer.objects.filter(Date=Date,Ride_Time=Ride_Time,User_Uid=User_Uid,).first()    
    except Ride_offer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Offer_Price_Get(snippet)
        # return Response(Km*6)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#@api_view([ 'POST'])
@api_view(['POST'])
def Driver_Ride_Offer_Post(request, Ride_id,UId,Offer):
    if request.method == 'POST':
        Ride_Driver = Driver.objects.filter(UId=UId).first()
        Ride = All_Ride_Historie.objects.filter(id=Ride_id).first()
        serializer = Driver_Offer_Serializer(data={
            "Ride_id": Ride_id,
            "Driver_Uid": UId,
            "pickup_location_lat": Ride.pickup_location_lat,
            "pickup_location_long": Ride.pickup_location_long,
            "drop_location_lat": Ride.drop_location_lat,
            "drop_location_long": Ride.drop_location_long,
            "Address": Ride.Address,
            "Drop_Address": Ride.  Drop_Address,
            "drop_location_long": Ride.drop_location_long,
            "Driver_offer": Offer,
            "Date": Ride.Date,
            "Ride_Time": Ride.Ride_Time,
            "name":Ride_Driver.name,
            "phone_number":Ride_Driver.phone_number,
            "date_of_birth":Ride_Driver.date_of_birth,
            "gender":Ride_Driver.gender,
            "vehicle_no":Ride_Driver.vehicle_no,
            "vehicle_name":Ride_Driver.vehicle_name,
            "license_no":Ride_Driver.license_no,
            "insurance_no":Ride_Driver.insurance_no,
            "ratings":Ride_Driver.ratings,
            "Carpooling_User_1_Uid":Ride.Carpooling_User_1_Uid,
            "Carpooling_User_2_Uid":Ride.Carpooling_User_2_Uid,
            "Carpooling_User_3_Uid":Ride.Carpooling_User_3_Uid,


            })
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    return Response(status=status.HTTP_400_BAD_REQUEST)


    return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['PATCH'])
def Add_Carpool_Ride(request, id):
    try:
        snippet = All_Ride_Historie.objects.get(id=id)
    except All_Ride_Historie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PATCH':
        #snippet = All_Ride_Historie.objects.all()
        #snippet = All_Ride_Historie.objects.filter()
        serializer = Add_Carpool_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("---------- calling", serializer)
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view([ 'GET'])
def Km(request,id):

    try:
        snippet = All_Ride_Historie.objects.get(id=id)
    except All_Ride_Historie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':

        serializer = Km_S(snippet)
        # return Response(Km*6)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view([ 'GET'])
def Driver_Ride_Offer_Get(request,Ride_id):
    try:
        snippet = Driver_offer.objects.filter(Ride_id=Ride_id)
    except Driver_offer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Driver_Offer_Serializer(snippet,many=True)
        # return Response(Km*6)
        return Response(serializer.data)

@api_view([ 'GET','PATCH'])
def Ride_Details(request,id):
    try:
        snippet = All_Ride_Historie.objects.get(id=id)
    except All_Ride_Historie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        # driver= All_Ride_Historie.objects.filter(Driver_Detail=Driver_Detail)
        # serializer = Cancel_Ride_Serializer(snippet, many=True)
        serializer = All_Ride_Historie_Serializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        User_details  = snippet.Driver_Uid
        Driver_Fetch = Driver.objects.filter(UId=User_details)
        
        serializer = Driver_Details_Serializer(snippet, data={"Driver_Detail":Driver_Fetch})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def New_Ride(request,vehicle):
    if request.method == 'POST':
        if vehicle=='Luxury':
            serializer = Ride_Car_Serializer(data=request.data)
        elif vehicle=='Ride Mini':
            serializer = Ride_Car_Serializer(data=request.data)
        elif vehicle=='Ride AC':
            serializer = Ride_Car_Serializer(data=request.data)
        elif vehicle=='Bike':
            serializer = Ride_Bike_Serializer(data=request.data)
        # request_body = json.dumps(request.data)

        

        Date = request.data['Date']
        Fare = request.data['Fare']
        if 'Driver_Uid' in request.data:
            if serializer.is_valid():
                Driver_Uid = request.data['Driver_Uid']
                driver_ = Driver.objects.filter(UId=Driver_Uid).first()
                driver_pk =  driver_.id
                serializer1 = Earning_Serializer(data={
                "date": Date,
                "earnings": Fare,
                "driver":driver_pk
            })
            
                if serializer1.is_valid():
                    serializer1.save()    
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
@api_view(['POST'])
def New_Delivery(request):
    if request.method == 'POST':
       
        serializer = Delivery_Serailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def User_Ride_Message(request,Ride_id):
    try:
        Ride_id_User= User_Message.objects.filter(ride=Ride_id)
    
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':        
        user_serializer = User_Messages_Serializer(Ride_id_User,many=True)
        
        return Response(user_serializer.data)
        
@api_view(['GET'])
def Driver_Ride_Message(request,Ride_id):
    try:
        
        Ride_id_Driver= Driver_Message.objects.filter(ride=Ride_id)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':        
        driver_serializer = Driver_Messages_Serializer(Ride_id_Driver,many=True)
        return Response(driver_serializer.data)

@api_view(['GET'])
def User_Specific_Message(request,id):
    try:
        Ride_id_User= User_Message.objects.get(id=id) 
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':        
        user_serializer = User_Messages_Serializer(Ride_id_User)
        return Response(user_serializer.data)
        
@api_view(['GET'])
def Driver_Specific_Message(request,id):
    try:
        
        Ride_id_Driver= Driver_Message.objects.get(id=id)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':        
        driver_serializer = Driver_Messages_Serializer(Ride_id_Driver)
        return Response(driver_serializer.data)
        
        
@api_view(['POST'])
def UserMessage(request):
    if request.method == 'POST':
       
        serializer = User_Messages_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def DriverMessage(request):
    if request.method == 'POST':
       
        serializer = Driver_Messages_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view([ 'GET'])
def Location(request,id,pickup_location_lat,pickup_location_long,drop_location_lat,drop_location_long):
    try:
        Ride= All_Ride_Historie.objects.get(id=id)
        pickup_location_lat = float(pickup_location_lat)
        pickup_location_long = float(pickup_location_long)
        drop_location_lat = float(drop_location_lat)
        drop_location_long = float(drop_location_long)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        pool_coords_1 = (pickup_location_lat, pickup_location_long)
        pool_coords_2 = (drop_location_lat, drop_location_long)
        POOL_KM =geopy.distance.geodesic(pool_coords_1, pool_coords_2).km
        Ride_Coords_1 = (Ride.pickup_location_lat,Ride.pickup_location_long)
        Ride_Coords_2 = (Ride.drop_location_lat,Ride.drop_location_long)
        RIDE_KM = geopy.distance.geodesic(Ride_Coords_1, Ride_Coords_2).km
        print(POOL_KM)
        print(RIDE_KM)
        if POOL_KM <=RIDE_KM+1:
            location_encode =polyline.encode([(pickup_location_lat,pickup_location_long),(drop_location_lat,drop_location_long)])
            location_decode = polyline.decode(location_encode)
            return Response(location_decode)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def customer_lists(request):
    if request.method == 'GET':
        lists= All_Ride_Historie.objects.filter(status="BOOKED")
        serializer = All_Ride_Historie_Serializer(lists,many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view([ 'POST'])
def Ride_Offer_Post(request):
    if request.method == 'POST':
        serializer = Offer_Price_Post(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view([ 'PATCH'])
def Add_Driver(request,id):
    try:
        snippet = All_Ride_Historie.objects.get(id=id)
    except All_Ride_Historie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PATCH':
        Driver_Uid = request.data['Driver_Uid']
        serializer =  Add_Driver_Serializer(snippet,data={
            "Driver_Uid":Driver_Uid,
            "status":"ARRIVING"
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def saved_destination(request,user):
    if request.method == 'GET':
        lists= Saved_Destination.objects.filter(user=user)
        serializer = Saved_Destination_Serializer(lists,many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_saved_destination(request):
    if request.method == 'POST':
        # lists= Saved_Destination.objects.filter(user=user)
        serializer = Saved_Destination_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def Driver_Statastics(request,UId):
    if request.method == 'GET':
        driver_ = Driver.objects.filter(UId=UId).first()
        earnings = Earning.objects.filter(driver=driver_)
        serializer = Earning_Serializer(earnings,many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Driver_Img(viewsets.ModelViewSet):
    lookup_field = 'UId'
    serializer_class = Driver_Image_Serializer
    parser_classes = (MultiPartParser,FormParser)

    def get_queryset(self):
        return Driver.objects.filter(UId=self.kwargs['UId'])
    def perform_update(self, serializer):
        serializer.save(driver_image=self.request.data.get('driver_image'))

class User_Img(viewsets.ModelViewSet):
    lookup_field = 'UId'
    serializer_class = User_Image_Serializer
    parser_classes = (MultiPartParser,FormParser)

    def get_queryset(self):
        return User.objects.filter(UId=self.kwargs['UId'])
    def perform_update(self, serializer):
        serializer.save(user_image=self.request.data.get('user_image'))



