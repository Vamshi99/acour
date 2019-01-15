from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from . import mail
from . import services
from . import send_sms

from .models import Package

def index(request):
    p_list = Package.objects.all()
    return render(request, 'track/index.html', {'packages': p_list})

def detail(request,package_id):
    package = get_object_or_404(Package, pk=package_id)
    return render(request, 'track/detail.html', {'package': package})

def entry(request):
    return render(request, 'track/main.html')

def submit(request):
    try:
        package = Package.objects.create(order_id=request.POST['order_id'],roll_no=request.POST['roll_no'],delivery_service=request.POST['agent'])
    except (KeyError, RuntimeError):
        return render(request, 'track/error.html', {
             'error_message': "Some error in response",
        })
    else:
        #TO-DO    return HttpResponse("Added entry for " % package.id)
        entry_message = "Order No: {} by \"{}\" is received by the courier office. OTP number to receive this order is {}".format(package.order_id,package.delivery_service,package.otp)
        mail.mail_notify(entry_message)
        send_sms.sms_notify(entry_message)
        return HttpResponseRedirect(reverse('track:entry'))

def search(request):
    return render(request, 'track/search.html')

#TO-DO
def validate(request):
    package = get_object_or_404(Package, id=request.POST['id'])
    if int(package.otp) == int(request.POST['otp']):
            up=Package.objects.filter(pk=package.id).update(status='DE', delivered_time=timezone.now())
            del_message = "Order No: {} by \"{}\" is delivered to you.".format(package.order_id,package.delivery_service)
            mail.mail_notify(del_message)
            send_sms.sms_notify(del_message)
            return HttpResponseRedirect(reverse('track:deliver', args=(package.id,)))
    else:
        #To-do give error notification
        return render(request, 'track/error.html', {
            'error_message': "Wrong OTP, authentiation failed.",
        })
        return HttpResponseRedirect(reverse('track:deliver', args=(package.id,)))

def deliver(request,package_id):
    package = get_object_or_404(Package, id=package_id)
    return render(request, 'track/pile.html', {'package': package})

def sclick(request):
    p_list = Package.objects.filter(roll_no=request.POST['search'])
    return render(request, 'track/results.html', {'packages': p_list})


def scan(request):
    text = services.get_text()
#    text = services.get_imText('C:\\Users\\Vamshi\\hack\\acour\\track\\demo.png')
    if text['orderid'] and text['rollno'] and text['agent']:
            try:
                package = Package.objects.create(order_id=text['orderid'],roll_no=text['rollno'],delivery_service=text['agent'])
            except KeyError:
                return render(request, 'track/error.html', {
                    'error_message': "Some error in input, try manually",
                })
            else:
                #TO-DO    return HttpResponse("Added entry for " % package.id)
                return HttpResponseRedirect(reverse('track:search'))