from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import s_registration
# Create your views here.
def home(request):
    return render(request,'home.html')
def admin_home(request):
    return render(request,'admin_home.html')

def login_p(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'sign_up.html')
def about(request):
     return render(request,'form.html')
def logout(request):
	auth.logout(request)
	return redirect('home') 
def login_page(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
                       
                 if user.is_staff:
                    login(request,user)
                    return redirect('admin_home')
                 else:
                    

                    auth.login(request,user)
                    messages.info(request, f'Welcome {username}')
                    return redirect('about')
       
                 
        
        
                

	

def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                #messages.info(request, 'SuccessFully completed.......')
                print("Successed...")
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('login_p')
    else:
        return render(request,'signup_page.html')


     

def profile(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        dob=request.POST['dob']
        img=request.FILES.get('image')
        phone=request.POST['phone']
        address=request.POST['address']
        paddress=request.POST['paddress']
        b_group=request.POST['blood']
        enumber=request.POST['enumber']
        ename=request.POST['ename']
        gname=request.POST['gname']
        relation=request.POST['relation']
        occupation=request.POST['occupation']
        gnumber=request.POST['gnumber']
        reg_no=request.POST['reg_no']
        select=request.POST['select']
        fee=request.POST['fee']
        pmnt=request.POST['pmnt1']
             
        n_emi=request.POST['n_emi']
        if n_emi==None:
             n_emi=0
        

        current_user=request.user
        
        
        student=s_registration(name=name,email=email,dob=dob,student_Photo=img,phone=phone,address=address,paddress=paddress,
                               b_group=b_group,e_number=enumber,e_name=ename,
                               g_name=gname,relation=relation,occupation=occupation,
                               g_number=gnumber,reg_no=reg_no,course=select,course_fee=fee,p_mode=pmnt,n_emi=n_emi,s_user=current_user

                               )
        student.save()
       # s=s_registration.objects.get(email=email)
        LastInsertId = (s_registration.objects.last()).id
        s=s_registration.objects.get(id=LastInsertId)
          
   
    return render(request,'profile.html',{'p':s})

def edit(request,pk):
     students=s_registration.objects.get(id=pk) 
     return render(request,'edit.html',{'student':students})

     


def edit_student_details(request,pk):
    if request.method=='POST':
        
        student = s_registration.objects.get(id=pk)
        old=student.student_Photo
        new=request.FILES.get('image')
        if old !=None and new==None:
            student.student_Photo=old
        else:
            student.student_Photo=new
            

        student.name=request.POST['name']
        student.email=request.POST['email']
        student.dob=request.POST['dob']
        student.phone=request.POST['phone']
        student.address=request.POST['address']
        student.paddress=request.POST['paddress']
        student.b_group=request.POST['blood']
        student.enumber=request.POST['enumber']
        student.ename=request.POST['ename']
        student.gname=request.POST['gname']
        student.relation=request.POST['relation']
        student.occupation=request.POST['occupation']
        student.gnumber=request.POST['gnumber']
        student.reg_no=request.POST['reg_no']
        student.select=request.POST['select']
        student.fee=request.POST['fee']
        student.pmnt=request.POST['pmnt']
             
        student.n_emi=request.POST['n_emi']
        student.save()
       
        return render(request,'edited_profile.html',{'p':student})
    return render(request, 'edit.html')
def show_students(request):
    student=s_registration.objects.all()
    return render(request,'show_students.html',{'student':student})
def delete_student(request,pk):
    student=s_registration.objects.get(id=pk)
    student.delete()
    return redirect('show_students')
def show_student(request,pk):
    student=s_registration.objects.get(id=pk)
    
    return render(request,'show_student.html',{'student':student})
    
