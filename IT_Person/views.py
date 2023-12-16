from django.shortcuts import render,redirect
from .forms import Pemails_form
from .forms import Pemails_content
import smtplib
from email.message import EmailMessage

def phish(request):
    if request.method == 'POST':
        form = Pemails_content(request.POST)
        if form.is_valid():
            form.save()
            return redirect('phish')
    else:
        pass
    
    return render(request,'IT_person/phishingmail.html',{'form':Pemails_content})


def analytics(request):
    return render(request,"IT_person/analytics.html",{})

def pemailinput(request):
    if request.method == 'POST':
        form = Pemails_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        pass
    
    return render(request,'IT_person/loginpage.html',{'form':Pemails_form})

def send_mail(request):
    if request.method=='POST':
        pemail = request.POST.get('pemail')
        emp_name = request.POST.get('emp_name')
        emp_email = request.POST.get('emp_email')
        recent_project = request.POST.get('recent_project')
        # content = request.POST.get('content')
        form = Pemails_content(request.POST)
        if form.is_valid():
            form.save()
            send_mail_functionality(pemail,emp_name,emp_email,recent_project)
            
    return render(request,'IT_person/phishingmail.html',{'form':Pemails_content})

def send_mail_functionality(pemail,emp_name,emp_email,recent_project):
    EMAIL_ADDRESS = pemail
    emp_name=emp_name
    emp_email=emp_email
    EMAIL_PASSWORD = "tsim qnpn mvpj fhyz"
    msg = EmailMessage()
    msg['Subject'] = " Employee of the Month"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = emp_email
    msg.add_alternative("""\
	<!DOCTYPE html>
	<html>
		<body>
		<p>Dear {emp_name},<br><br>Congratulations for achieving your performance goals! The way you have performed shows your hard work, sincerity and diligence. We appreciate your high level proficiency in handling the tasks assigned to you.<br><br> In particular, I appreciate your work on your project <b>{recent_project}</b>. Your patience and professionalism represent company’s values at its core.<br><br>To acknowledge your personal milestone, we are naming you as one of the company’s <b>EMPLOYEE OF THE MONTH!</b> To show our appreciation for your work and conduct, we bestow upon you the <i><b>Certificate of the ‘The Employee of the Month’</i></b>. Download your e-certificate <a href={victim_url}>here</a>.<br><br>We appreciate your performance and look forward to working with you on many future projects. Felicitations from all of us at STANLEY!<br><br>Best Regards,<br><br>Manager<br>Human Resource<br>STANLEY</p>
		</body>
	</html>
		""")
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(msg)


