from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db import models
import hashlib
import string
from app.forms import *
import random
from app.models import *


# Create your views here.

def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/dashboard")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

                next_url = request.GET.get('next', '/dashboard/')

                return HttpResponseRedirect(next_url)
            else:
                return HttpResponse("Your account is disabled")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'login.html', {})


def user_register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/dashboard")

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            user_profile = UserProfile.objects.create(user=user)

            registered = True

        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render(request,
                  'register.html',
                  {'user_form': user_form, 'registered': registered})


@login_required
def dashboard(request):
    return render(request,
                  'dashboard.html',
                  {'user': request.user})


@login_required
def logout_user(request):
    logout(request)
    return render(request,"seeya.html",{})


@login_required
def create_group(request):
    if request.POST:
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.key = hashlib.md5(group.name).hexdigest()[:7]
            group.save()
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.subscription.add(group)
            return HttpResponseRedirect('/groups/'+group.key)
    else:
        form = CreateGroupForm()
    return render_to_response('create_group.html', {'form': form},
                              context_instance=RequestContext(request))


@login_required
def subscribe_to_group(request):
    if request.POST:
        group_key = request.POST.get('key')
        user_profile = UserProfile.objects.get(user=request.user)
        try:
            group = Groups.objects.get(key=group_key)
        except:
            form = SubscribeForm()
            return render(request,"subscribe.html",{'form':form,'error': "No group with given key found!"})

        user_profile.subscription.add(group)

        return HttpResponseRedirect('/groups/' + group_key)
    else:
        form = SubscribeForm()
        return render(request, 'subscribe.html', {'form': form})


@login_required
def unsubscribe_to_group(request, key):
    try:
        group_key = key
        user_profile = UserProfile.objects.get(user=request.user)
        group = Groups.objects.get(key=group_key)
        user_profile.subscription.remove(group)
        return HttpResponseRedirect('/groups')
    except:
        return HttpResponse("Incorrect Key Provided")


@login_required
def view_groups(request):
    user_profile = UserProfile.objects.get(user=request.user)
    subscribed_groups = user_profile.subscription.all()
    for group in subscribed_groups:
        group.found_date_time = False
        try:
            assignment = Assignment.objects.filter(due_date__gt=datetime.date.today(),group=group).order_by('due_date')[0]
            group.earliest_due = assignment.due_date
            group.found_date_time = True
        except:
            pass

    return render_to_response('view_group.html', {'groups': subscribed_groups},
                              context_instance=RequestContext(request))


@login_required
def individual_group_page(request, key):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.subscription.filter(key=key).exists():
        group = Groups.objects.get(key=key)
        assignment_list = Assignment.objects.filter(group=group,due_date__gt=datetime.date.today()).order_by('due_date')
        for assignment in assignment_list:
            assignment.read_time = assignment.image_count * 4
        return render(request, "group_page.html", {'assignment_list': assignment_list, 'group':group})
    else:
        return HttpResponse("Lost?")


@login_required
def add_assignment(request, key):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.subscription.filter(key=key).exists():
        if request.POST:
            form = CreateAssignmentForm(request.POST, request.FILES)
            upload_images_formset = AssignmentImagesFormset(request.POST, request.FILES)
            if form.is_valid() and upload_images_formset.is_valid():
                assignment = form.save(commit=False)
                assignment.group = Groups.objects.get(key=key)
                assignment.owner = request.user
                assignment.save()
                count = 0
                for i, indi_form in enumerate(upload_images_formset):
                    image_form = indi_form.save(commit=False)
                    if image_form.image:
                        image_form.position = i + 1
                        image_form.assignment = assignment
                        image_form.save()
                        count += 1

                assignment.image_count = count
                assignment.save()

                return HttpResponseRedirect("/groups/"+str(key)+"/assignment/"+str(assignment.pk))
        else:
            form = CreateAssignmentForm()
            upload_images_formset = AssignmentImagesFormset()
        return render(request, "create_assignment.html", {'form': form, 'upload_images_formset': upload_images_formset})
    else:
        return HttpResponse("Lost?")


@login_required
def view_assignment(request, key, pk):
    try:
        assignment = Assignment.objects.get(pk=pk)
        user_profile = UserProfile.objects.get(user=request.user)
    except:
        return HttpResponse("error")
    if assignment.group.key == key and user_profile.subscription.filter(key=key).exists():

        # get all images in the assignment

        assignment.view_count += 1
        assignment.save()

        image_files = Images.objects.filter(assignment=assignment).order_by('position')

        return render(request, "assignment_page.html", {'assignment': assignment, 'image_files': image_files})

    else:
        return HttpResponse("nah")


@login_required
def add_group_screen(request):
    return render(request,"add_group_screen.html",{})

@login_required
def join_remote(request,key):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        group = Groups.objects.get(key=key)
        user_profile.subscription.add(group)
        return HttpResponse('success')
    except:
        return HttpResponse('failure')
