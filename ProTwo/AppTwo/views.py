from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from .forms import PropertySearchForm
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


# Create your views here.
class AboutView(TemplateView):
    
    template_name='about.html'


def myfunc(request):
    property = Property.objects.all().order_by('-created_at')[:4]
    prop_rent = Property.objects.filter(status='Rent')
    prop_sale = Property.objects.filter(status='Sale')
    total_prop = Property.objects.all()
    agents = UserProfile.objects.all()
    if request.method == 'POST':
        form = PropertySearchForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            properties = Property.objects.filter(location__name__icontains=location)
            return render(request, 'search-result.html', {'form':form, 'properties':properties})
    else:
        form = PropertySearchForm()
    context = {
        'form': form,
        'property': property,
        'prop_rent':prop_rent,
        'prop_sale':prop_sale,
        'total_prop':total_prop,
        'agents':agents,
    }
    return render(request, 'index.html', context)

def rent(request):
    rent = Property.objects.filter(status='Rent')
    page = request.GET.get('page')
    num_of_items = 3
    paginator = Paginator(rent, num_of_items)
    try:
        rent = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        rent = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        rent = paginator.page(page)
    context = {
        'rents': rent,
        'paginator': paginator,
    }
    return render(request, 'rent.html', context)

def sale(request):
    sale = Property.objects.filter(status='Sale')
    page = request.GET.get('page')
    num_of_items = 3
    paginator = Paginator(sale, num_of_items)
    try:
        sale = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        sale = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        sale = paginator.page(page)
    context = {
        'sales': sale,
        'paginator': paginator,
    }
    return render(request, 'sale.html', context)

def myContact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        mail_subject = f'{subject} from Real Estate App website'
        email_data = {
            'name': name,
            'email':email,
            'subject':subject,
            'message': message
        }
        html_message = render_to_string('mail-template.html', email_data)
        plain_text = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        send = mail.send_mail(mail_subject, plain_text, from_email, ['ogungburemayowa2019@gmail.com', ], html_message=html_message)
        if send:
            data.save()
            send = mail.send_mail(mail_subject, plain_text, from_email, ['ogungburemayowa2019@gmail.com', ], html_message=html_message)
            messages.success(request, 'Message sent Successfully')
        else:
            messages.error(request, 'Your message was not sent. Please try again.')
    return render(request, 'contact.html')

# def myAbout(request):
    
#     return render(request, 'about.html')

def myService(request):
    
    return render(request, 'services.html')

def myProperties(request):
    featured = Property.objects.filter(featured=True).order_by('-created_at')
    property = Property.objects.all().order_by('-created_at')
    page = request.GET.get('page')
    num_of_items = 3
    paginator = Paginator(property, num_of_items)
    try:
        property = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        property = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        property = paginator.page(page)
    context = {
        'featured':featured,
        'property':property,
        'paginator': paginator,
    }
    return render(request, 'properties.html', context)

def property_detail(request, property_id):
    prop_detail = get_object_or_404(Property, id=property_id)
    context = {
        'detail': prop_detail,
    }
    return render(request, 'property-single.html', context)

