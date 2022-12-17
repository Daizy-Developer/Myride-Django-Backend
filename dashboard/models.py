from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import CharField
# Create your models here.
GENDER_CHOICES = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
    ("OTHER","OTHER"),
    )
STATUS_CHOICES = (
    ("ARRIVED","ARRIVED"),
    ("ARRIVING","ARRIVING"),
    ("CANCELLED","CANCELLED"),
    ("ENDED","ENDED"),
    ("ADVANCE BOOKING","ADVANCE BOOKING"),
)
RIDE_TYPE = (
    ("RIDE","RIDE"),
    ("DELIVERY","DELIVERY")
)
CAR_CHIOCES = (
    ("Luxury","Luxury"),
    ("Ride Mini","Ride Mini"),
    ("Ride AC","Ride AC"),
    ("Bike","Bike"),
)

CANCELLATION_REASON = (
    ("NONE","NONE"),
    ("DRIVER DENIED TO COME","DRIVER DENIED TO COME"),
    ("ASKING FOR EXTRA MONEY","ASKING FOR EXTRA MONEY"),
    ("BOOKED FROM SOMEWHERE ELSE","BOOKED FROM SOMEWHERE ELSE"),
    ("CHANGE OF PLAN","CHANGE OF PLAN"),
    ("OTHER","OTHER"),

)


class Driver(models.Model ):
    UId  =  models.CharField(max_length=30 , blank=True , null=True )
    # id_ = models.AutoField() 
    name = models.CharField(max_length=50,default="")
    date_of_birth = models.DateField()
    gender = models.CharField(max_length = 20,choices = GENDER_CHOICES,default = "MALE")
    phone_number = models.CharField(max_length=12)
    driver_image = models.ImageField(upload_to="driver/images",null=True,blank=True,default="def_img.png")
    vehicle_no = models.CharField(max_length=10)
    vehicle_name = models.CharField(max_length=50,default='')
    license_no = models.CharField(max_length=10)
    insurance_no = models.CharField(max_length=10)
    earnings = models.IntegerField()
    last_location_lat =models.DecimalField(max_digits = 40 ,decimal_places = 8)
    last_location_long = models.DecimalField(max_digits = 40 ,decimal_places = 8)
    current_location_lat = models.DecimalField(max_digits = 40 ,decimal_places = 8)
    current_location_long = models.DecimalField(max_digits = 40 ,decimal_places = 8)
    def __str__(self):
        return self.name
        
class User(models.Model):
    UId=  models.CharField(max_length=30 , blank=True , null=True )

    name = models.CharField(max_length=50,default="")
    date_of_birth = models.DateField()
    gender = models.CharField(max_length = 20,choices = GENDER_CHOICES,default = "MALE")
    phone_number = models.CharField(max_length=12)
    user_image = models.ImageField(upload_to="driver/images",null=True,blank=True,default="def_img.png")
    home_address = models.CharField(max_length=400)
    ratings = models.DecimalField(default=0.0,decimal_places = 2,max_digits=3)
    total_rides = models.IntegerField(blank=True , null=True)
   # work_address = models.CharField(max_length=400)
    # def __str__(self):
    #     return self.name



class All_Ride_Historie(models.Model):
  #  otp = models.IntegerField()
    
    User_Detail =  models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    User_Uid = models.CharField(max_length=100)
    Ride_Type =models.CharField(max_length = 20,choices = RIDE_TYPE , default="RIDE")
    Ride = models.CharField(max_length = 20,choices = CAR_CHIOCES,null=True,blank=True)
    Carpooling_User_1_Uid = models.CharField(max_length=100,null=True,blank=True)
    Carpooling_User_2_Uid = models.CharField(max_length=100,null=True,blank=True)
    Carpooling_User_3_Uid = models.CharField(max_length=100,null=True,blank=True)
    Fragile = models.BooleanField(null=True,blank=True)
    # User_Detail =  models.ManyToManyField(User, on_delete=models.CASCADE)
    Driver_Detail =  models.ForeignKey(Driver,on_delete=models.CASCADE,null=True)
    Driver_Uid = models.CharField(max_length=50,null=True,blank=True)
    # Driver_Detail =  models.ManyToManyField(Driver, on_delete=models.CASCADE)
    Date = models.DateField()
    Ride_Time =  models.TimeField(null=True)
    pickup_location_lat = models.DecimalField(max_digits = 40 ,decimal_places = 8)
    pickup_location_long = models.DecimalField(max_digits = 40 ,decimal_places = 8)
    drop_location_lat =  models.DecimalField(max_digits = 40 ,decimal_places = 8)
    drop_location_long = models.DecimalField(max_digits = 40 ,decimal_places = 8)
    Km = models.IntegerField(default=1)
    Fare =  models.IntegerField()
    User_ratings = models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(1)])
    Driver_ratings = models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(1)])
    Cancel_Ride = models.CharField(max_length=50,choices = CANCELLATION_REASON,default = "NONE")
    status = models.CharField(max_length = 20,choices = STATUS_CHOICES,default = "ARRIVED")

    def __str__(self):
        # return "Passenger "+self.User_Detail.first_name# +" Driver "+self.Driver_Detail.first_name + " " +str(self.otp)+" "+ str(self.Date)
        return str(self.id)+" "+ str(self.Date)


class Ride_offer(models.Model):
    User_Uid = models.CharField(max_length=100)
    Driver_Uid = models.CharField(max_length=100,null=True,blank=True)
    pickup_location_lat = models.DecimalField(max_digits = 40 ,decimal_places=8)
    pickup_location_long = models.DecimalField(max_digits = 40 ,decimal_places=8)
    drop_location_lat =  models.DecimalField(max_digits = 40 ,decimal_places=8)
    drop_location_long = models.DecimalField(max_digits = 40 ,decimal_places=8)
    Driver_offer = models.IntegerField()
    Date = models.DateField(null=True,blank=True) #Remove Null
    Ride_Time =  models.TimeField(null=True,blank=True) #Remove Null

class Promo_Code(models.Model):
    Title = models.CharField(max_length =70,null=True,blank=True)
    Promocode = models.CharField(max_length=30)
    Description = models.TextField(null=True,blank=True)
    def __str__(self):
        return"Promocode "+self.Promocode

class Driver_offer(models.Model):
    Ride_id = models.ForeignKey(All_Ride_Historie,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default="")
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length = 20,choices = GENDER_CHOICES,default = "MALE")
    phone_number = models.CharField(max_length=12)
    driver_image = models.ImageField(upload_to="driver/images",null=True,blank=True,default="def_img.png")
    vehicle_no = models.CharField(max_length=10)
    vehicle_name = models.CharField(max_length=50,default='')
    license_no = models.CharField(max_length=10)
    insurance_no = models.CharField(max_length=10)
    Driver_offer = models.IntegerField()

class User_Message(models.Model):
    ride = models.ForeignKey(All_Ride_Historie,null=False,blank=False,on_delete=models.CASCADE)
    sender = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    reciever = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True)
    message = models.TextField()
    Time =  models.TimeField()

class Driver_Message(models.Model):
    ride = models.ForeignKey(All_Ride_Historie,null=False,blank=False,on_delete=models.CASCADE)
    sender = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True)
    reciever = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    message = models.TextField()
    Time =  models.TimeField()
