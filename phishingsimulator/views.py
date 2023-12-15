from django.shortcuts import render

# Create your views here.
def MailView(request):
    if request.method == "POST”:
        
         sender_email    = “sender email here”
         sender_name     = “sender name here”
         reply_to_email  = “reply to email here”
         reply_to_name   = “reply to name here”
         subject         = “this is subject”
         message         = “phishing template here” 
         email_list      = [“abc@example.com”,”bcd@example.com”]
                              
          m = Mails.objects.create(sender_email=sender_email, sender_name=sender_name, subject=subject, message=valid_message) 
                 
          for i in email_list:
            msg = EmailMessage(
                          subject,
                          message,
                          from_email=sender_name+ '<'+sender_email+'>',
                          to=[i],
                          reply_to=[reply_to_name+ '<'+reply_to_email+'>'],
                          connection=backend,
                           )
            msg.content_subtype = "html"
            msg.send()
            r = Recipient.objects.create(email=i, mail=m)
            PhishingData.objects.create(link=template_url, recipient= r)
 
          return HttpResponse({"res":"Email sent successfully"})