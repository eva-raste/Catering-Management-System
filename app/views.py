from django.shortcuts import redirect, render
from .models import Customer,Event
from .forms import CustomerForm, EventForm
from django.shortcuts import get_object_or_404

# Create your views here.
def home(req):
    return render (req,'index.html')

def login(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = CustomerForm()
    return render(request, 'login.html', {'form': form})

def customer_list(req):
    list=Customer.objects.all()
    return render(req,'customer_list.html',{'list':list})
    
def event_list(req):
    list = Event.objects.order_by('-date') 
    return render(req, 'event_list.html', {'list': list})

def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})


def event_edit(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'event_form.html', {'form': form})


def event_delete(request, event_id):
    event=get_object_or_404(Event,pk=event_id)
    if request.method=="POST":
        event.delete()
        return redirect('event_list')
    return render(request,'event_confirm_delete.html',{'event':event})