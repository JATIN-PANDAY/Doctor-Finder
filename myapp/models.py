from django.db import models

# Create your models here.

class MasterTable(models.Model):
    role=models.CharField(max_length=40)    
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=40)
    is_active=models.BooleanField(default=True)
    is_created=models.DateTimeField(auto_now_add=True)
    is_verified=models.BooleanField(default=False,null=True)
    is_updated=models.DateTimeField(auto_now_add=True)
        
def __str__(self):
    return self.role

class Patient(models.Model):
    user_id=models.ForeignKey(MasterTable,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=40,null=True)
    state=models.CharField(max_length=40,null=True)
    city=models.CharField(max_length=30,null=True)
    dob=models.CharField(max_length=20,null=True)
    pic=models.ImageField(upload_to='myapp/image/Patient')
    bloodgroup=models.CharField(max_length=30,null=True)
    gender=models.CharField(max_length=20,null=True)
    contact=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name


class Doctor(models.Model):
    user_id=models.ForeignKey(MasterTable,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=40,null=True)
    state=models.CharField(max_length=40,null=True)
    city=models.CharField(max_length=30,null=True)
    dob=models.CharField(max_length=20,null=True)
    pic=models.ImageField(upload_to='myapp/image/Doctor')
    contact=models.CharField(max_length=12,null=True)
    qualification=models.CharField(max_length=40,null=True)
    Experience=models.CharField(max_length=100,null=True)
    Department=models.CharField(max_length=100,null=True)
    department_id=models.CharField(max_length=10,default=0)
    def __str__(self):
        return self.name

# Patient request to doctor for appointment
class Appointment(models.Model):
    pat_id=models.ForeignKey(Patient,on_delete=models.CASCADE , default=0)
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    contact=models.CharField(max_length=50,null=True)
    department=models.CharField(max_length=50,null=True)
    # doctor=models.CharField(max_length=50,null=True)
    message=models.CharField(max_length=400,null=True)
    # date = models.DateField(null=True)

    def __str__(self):
        return self.name



# doctor send appointment schedule to patient
class doctorappointment(models.Model):
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE , default=0)
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    department=models.CharField(max_length=100,null=True)
    appointment_day=models.CharField(max_length=20,null=True)
    appointment_time=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

    
class PatientContact(models.Model):
    patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE , default=0)
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    subject=models.CharField(max_length=100,null=True)
    message=models.CharField(max_length=300,null=True)
    
    def __str__(self):
        return self.name


class contact(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    subject=models.CharField(max_length=100,null=True)
    message=models.CharField(max_length=300,null=True)
   
    def __str__(self):
        return self.name

