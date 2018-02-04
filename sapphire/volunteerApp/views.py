from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from utility.models import *
from feed.models import Feed_Entry
from groups.models import Group

def index(request):
    # Run processes to build dataset after login
    return redirect('eventNeeds')     # Redirects to /home/feed/


def calendar(request):
    if request.user.is_authenticated():
        return render(request, "volunteer/calendar.html")
    else:
        return redirect('login')

def eventNeeds(request):
    events = Event.objects.order_by('start')
    if request.user.is_authenticated():
        return render(request, 'volunteer/events.html', {'events':events})
    else:
        return redirect('login')

def event(request, event_id):
    event = Event.objects.get(id=event_id)
    is_organizer = Group.get_is_organzer(event.parentGroup, request.user)

    slots = Slot.objects.order_by('start')
    return render(request, 'volunteer/event.html', {'event':event, 'slots':slots, 'is_organizer':is_organizer})

def slot(request, slot_id):
    slot = Slot.objects.get(id=slot_id)
    is_organizer = Group.get_is_organzer(slot.parentEvent.parentGroup, request.user)
    user_slots = User_Slot.objects.filter(parentSlot=slot)
    return render(request, 'volunteer/slot.html', {'slot':slot, 'user_slots':user_slots, 'is_organizer':is_organizer})

def slotNeeds(request):
    slots = Slot.objects.order_by('start')
    if request.user.is_authenticated():
        return render(request, 'volunteer/slots.html', {'slots':slots})
    else:
        return redirect('login')

def volunteer(request, slot_id):
    #next = request.GET.get('next')
    slot = Slot.objects.get(id=slot_id)
    user_slot = User_Slot.objects.filter(parentSlot=slot, volunteer__isnull=True).first()
    if (user_slot == None):
        return redirect('/volunteer/slot/'+str(slot_id))

    user_slot.volunteer = request.user
    user_slot.save()

    name = slot.title
    event = slot.parentEvent.name


    feed_entry = Feed_Entry(
        user=request.user,
        datetime=datetime.now(),
        description="Volunteered for \"" + name + "\" in event \"" + event + "\"",
        url="/volunteer/slot/" + str(slot.id))
    feed_entry.save()
    return redirect('/volunteer/slot/'+str(slot.id))

def signin(request, user_slot_id):
    user_slot = User_Slot.objects.get(id=user_slot_id)
    user_slot.signin = datetime.now()
    user_slot.save()
    return redirect('/volunteer/slot/'+str(user_slot.parentSlot.id))

def signout(request, user_slot_id):
    user_slot = User_Slot.objects.get(id=user_slot_id)
    user_slot.signout = datetime.now()
    user_slot.save()
    return redirect('/volunteer/slot/'+str(user_slot.parentSlot.id))
