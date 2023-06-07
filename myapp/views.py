from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from.models import*
from random import randint
import re


# Create your views here.

def index(request):
    return render(request,'index.html')

def message(request):
    if request.method=='POST':
        name=name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        message=contact.objects.create(name=name,email=email,subject=subject,message=message)
        show_message='Your message send successfully ..'
        return render(request,'index.html',{'msg':show_message})




def Signuppage(request):
    return render(request,'signup.html')

# Doctor and Patient Register


def register(request):
    if request.POST['role']=='Patient':
        name=request.POST.get('name')
        role=request.POST['role']
        email=request.POST['email']
        contact=request.POST.get('contact')
        pic=request.FILES.get('pic')
        passw=request.POST.get('password')
        cpassw=request.POST.get('cpassword')
        user=MasterTable.objects.filter(email=email)
        if user:
            message='you are already register'
            return render(request,'signup.html',{'msg':message})
        else:
            # email regex

            email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
                    
            if re.search (email_condition,email):

                # Password regex

                password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
                
                if re.match(password_pattern,passw):

                    if passw==cpassw:
                    

                        newuser=MasterTable.objects.create(email=email,password=passw,role=role)
                        newpatient=Patient.objects.create(user_id=newuser,email=email,name=name,contact=contact,pic=pic)
                        message='Register Successfully '

                        return render(request,'login.html',{'msg':message})


                    
                    else:
                        message =  "Password and Confirm Password does'nt Match"
                        return render(request,'signup.html',{'msg':message})                                
                else:
                    message =  "Weak Password"
                    return render(request,'signup.html',{'msg':message})            
            else:
                message ="Invalid Email"
                return render(request,'signup.html',{'msg':message})
           
           # Doctor role


    else:
        if request.POST['role']=='Doctor':
            role=request.POST['role']
            name=request.POST.get('name')
            email=request.POST['email']
            pic=request.FILES['pic']
            passw=request.POST['password']
            cpassw=request.POST['cpassword']
            user=MasterTable.objects.filter(email=email)
            if user:
                message='you are already register'
                return render(request,'signup.html',{'msg':message})
            else:
            # email regex

                email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
                        
                if re.search (email_condition,email):

                    # Password regex

                    password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
                    
                    if re.match(password_pattern,passw):

                        if passw==cpassw:
                            
                            newuser=MasterTable.objects.create(email=email,password=passw,role=role)
                            newpatient=Doctor.objects.create(user_id=newuser,email=email,name=name,pic=pic)
                            message='Register Successfully '

                            return render(request,'login.html',{'msg':message})

                        
                        else:
                            message =  "Password and Confirm Password does'nt Match"
                            return render(request,'signup.html',{'msg':message})                                
                    else:
                        message =  "Weak Password"
                        return render(request,'signup.html',{'msg':message})            
                else:
                    message ="Invalid Email"
                    return render(request,'signup.html',{'msg':message})

        
    return render(request,'signup.html')


def login(request):
    return render(request,'login.html')

# patient login

def userlogin(request):
    try:
        if request.POST['role']=='Patient':
            email=request.POST['email']
            password=request.POST['password']
            user=MasterTable.objects.get(email=email)
            if user:
                if user.password==password and user.role=='Patient':
                    patient=Patient.objects.get(user_id=user)
                    request.session['id']=user.id
                    request.session['email']=user.email
                    request.session['password']=user.password
                    request.session['name']=patient.name
                    return redirect('patienthomepage')
                else:
                    message='Incorrect Password !!!'
                    return render(request,'login.html',{'msg':message})
        else:
            if request.POST['role']=='Doctor':
                email=request.POST['email']
                password=request.POST['password']
                user=MasterTable.objects.get(email=email)
                if user:
                    if user.password==password and user.role=='Doctor':
                        doctor=Doctor.objects.get(user_id=user)
                        request.session['id']=user.id
                        request.session['email']=user.email
                        request.session['password']=user.password
                        request.session['name']=doctor.name
                        return render(request,'doctor/index.html',{'doct':doctor})
                    else:
                        message='Incorrect Password !!!'
                        return render(request,'login.html',{'msg':message})
    except Exception as e:
            return render(request,'404.html')
    
# Patient homepage and doctor list

def patienthomepage(request):
    all_doct=Doctor.objects.all()
    return render(request,'index1.html',{'all_doct':all_doct})



# Patient and Doctor logout 

def logout(request):
    del request.session['email']
    del request.session['password']
    return redirect('index')

# Patient profile create and update
def profilepage(request,pk):
    user=MasterTable.objects.get(id=pk)
    patient=Patient.objects.get(user_id=user)
    return render(request,'profile.html',{'user':user,'pat':patient})


def patientprofileupdate(request,pk):
    user=MasterTable.objects.get(id=pk)
    if user.role=='Patient':
        if user:
            patient=Patient.objects.get(user_id=user)
            patient.name=request.POST['name']
            patient.email=request.POST['email']
            patient.contact=request.POST['contact']        
            patient.state=request.POST['state']        
            patient.city=request.POST['city']        
            patient.dob=request.POST['dob']        
            patient.bloodgroup=request.POST['bloodgroup']        
            patient.gender=request.POST['gender']        
            patient.pic=request.FILES.get('pic') 
            patient.save()
            url=f"/profilepage/{pk}"
            return redirect(url)              


# Doctor profile create
def doctorprofilepage(request,pk):
    user=MasterTable.objects.get(id=pk)
    doctor=Doctor.objects.get(user_id=user)
    return render(request,'doctor/profile.html',{'user':user,'doct':doctor})

# Doctor Profile Update

def doctorprofileupdate(request,pk):
    user=MasterTable.objects.get(id=pk)
    if user.role=='Doctor':
        user.email=request.POST['email']
        if user:
            doctor=Doctor.objects.get(user_id=user)
            doctor.name=request.POST.get('name')
            doctor.email=request.POST.get('email')
            doctor.state=request.POST.get('state')      
            doctor.city=request.POST.get('city')        
            doctor.dob=request.POST.get('dob') 
            doctor.Experience=request.POST.get('experience')
            doctor.qualification=request.POST.get('qualification')
            doctor.Department=request.POST.get('department')
            doctor.contact=request.POST.get('contact')
            doctor.pic=request.FILES.get('pic')
            doctor.save()
            url=f"/doctorprofilepage/{pk}"
            return redirect(url)              

def checkdepartment(request):
    return render(request,'doctor/department.html')


# Patient send appointment request

def appointment(request,pk):
    user=request.session['id']
    if user:
        patient=Patient.objects.get(user_id=user)
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        dept=request.POST['department']
        # doct=request.POST['doctor']
        messa=request.POST['message']
        appointment=Appointment.objects.create(pat_id=patient,name=name,email=email,contact=contact,department=dept,message=messa)
        message='Your appointment request has been sent successfully. Thank you! '
        return render(request,'index1.html',{'msg':message})
    


# Doctor see patient appointment request

def checkdepartment(request,pk):
    user=MasterTable.objects.get(id=request.session['id'])
    if user:
        doctor=Doctor.objects.get(user_id=user)
        return render(request,'doctor/department.html')

def doctorshowappointment(request,pk):
    user=MasterTable.objects.get(id=request.session['id'])
    if user:
        doct=Doctor.objects.get(user_id=user)
        department=request.POST.get('department')
        if doct.Department==department:
            appointment=Appointment.objects.filter(department=department)
            return render(request,'doctor/appointment.html',{'appoi':appointment})
        else:
            message='Enter correct department name'
            return render(request,'doctor/department.html',{'msg':message})
    


# Doctor send appointment schedule
def doctorsendappointmentpage(request,pk):
    user=MasterTable.objects.get(id=request.session['id'])
    if user:
        if user.role=='Doctor':
            doctor=Doctor.objects.get(user_id=user)
            return render(request,'doctor/ui-forms.html')
def doctorsendappointment(request):
    user=MasterTable.objects.get(id=request.session['id'])
    if user:
        if user.role=='Doctor':
            doctor=Doctor.objects.get(user_id=user)
            name=request.POST.get('name')
            email=request.POST.get('email')
            day=request.POST.get('day')
            time=request.POST.get('time')
            department=request.POST.get('department')
            address=request.POST.get('address')
            new_appointment=doctorappointment.objects.create(doctor_id=doctor,name=name,email=email,address=address,appointment_day=day,appointment_time=time,department=department)
            message='Appointment Send Successfully...'
            return render(request,'doctor/ui-forms.html',{'msg':message})

# Patient see Appointment schedule

def patientcheckdepartment(request,pk):
    user=MasterTable.objects.get(id=request.session['id'])
    if user:
        patient=Patient.objects.get(user_id=user)
        return render(request,'checkdepartment.html')

def patientshowappointment(request,pk):
    try:
        user=MasterTable.objects.get(id=request.session['id'])
        if user:
            if user.role=='Patient':
                patient=Patient.objects.get(user_id=user)
                name=request.POST.get('name')
                department=request.POST.get('department')
                
                appointment_schedule=doctorappointment.objects.get(department=department)
                if appointment_schedule.department==department and name==patient.name:
                    return render(request,'appointmentschedule.html',{'app_sch':appointment_schedule})
    except Exception as e:
        message='No appointment in this department.'
        return render(request,'checkdepartment.html',{'msg':message})


    return render(request,'checkdepartment.html')



            
        
def Patientcontact(request,pk):
    user=MasterTable.objects.get(id=request.session['id'])
    if user:
        if user.role=='Patient':
            patient=Patient.objects.get(user_id=user)
            name=request.objects.get('name')
            email=request.objects.get('email')
            subject=request.objects.get('subject')
            message=request.objects.get('message')
            new_contact=PatientContact.objects.create(patient_id=patient,name=name,email=email,subject=subject,message=message)
            show_message='Your message sent...'
            return render(request,'index1.html',{'msg':show_message})