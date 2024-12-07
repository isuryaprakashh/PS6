from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ownerapp.models import OwnerUser ,Property


# Create your views here.

def tenenthompage(request):
    return render(request,'tenentApp/tenentHomePage.html')

def about_us(request):
    return render(request,'tenentApp/about_us.html')


# tenentapp/views.py
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TenentProfile
from .forms import TenentProfileForm


@login_required
def tenent_profile(request):
    profile, created = TenentProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'email': request.user.email
        }
    )

    if request.method == 'POST':
        if 'update_profile' in request.POST:
            form = TenentProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                request.user.email = form.cleaned_data['email']
                request.user.save()
                profile.save()
                messages.success(request, 'Profile updated successfully! 🎉')
                return redirect('tenentapp:tenent_profile')
            else:
                messages.error(request, 'Please correct the errors below.')

        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password changed successfully! 🔐')
                return redirect('tenentapp:tenent_profile')
            else:
                messages.error(request, 'Please correct the password errors.')

    else:
        form = TenentProfileForm(instance=profile, initial={'email': request.user.email})
        password_form = PasswordChangeForm(request.user)

    context = {
        'form': form,
        'password_form': password_form,
        'profile': profile,
        'page_title': 'Profile Settings'
    }
    return render(request, 'tenentApp/tenentProfile.html', context)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q


@login_required
def property_list(request):
    # Check for reset parameter to clear filters
    if 'reset' in request.GET:
        return redirect('tenentapp:property_list')  # Redirect to clear search and filter queries

    search_query = request.GET.get('search', '')
    filter_option = request.GET.get('filter', '')

    # Fetch all properties
    properties = Property.objects.all()

    # Apply search filter (if any)
    if search_query:
        properties = properties.filter(
            Q(title__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Apply sorting based on filter option
    if filter_option == 'price_asc':
        properties = properties.order_by('price')  # Price low to high
    elif filter_option == 'price_desc':
        properties = properties.order_by('-price')  # Price high to low

    # Determine user type for rendering the correct navbar
    user_type = 'admin' if request.user.is_superuser else 'owner' if OwnerUser.objects.filter(user=request.user).exists() else 'tenant'

    context = {
        'properties': properties,
        'user_type': user_type,
        'search_query': search_query,
        'filter_option': filter_option,
    }

    return render(request, 'tenentApp/property_list.html', context)


@login_required
def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'tenentApp/property_detail.html', {'property': property})



from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template.loader import render_to_string


def contact_owner(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Render the email content using the HTML template
        email_content = render_to_string('tenentApp/email_template.html', {
            'name': name,
            'email': email,
            'message': message,
            'property': property  # Pass the entire property object to the template
        })

        # Set up the email with HTML content
        email_message = EmailMessage(
            subject=f"Inquiry about {property.title}",
            body=email_content,
            from_email=email,
            to=[property.email],
        )
        email_message.content_subtype = 'html'  # Set the email type to HTML

        # Send the email
        email_message.send()

        # Show success message and redirect
        # messages.success(request, 'Your message has been sent to the property owner.')
        return redirect('tenentapp:property_detail', property_id=property_id)

    return render(request, 'contact_owner.html', {'property': property})



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ownerapp.models import Message, Reply
from ownerapp.forms import MessageForm, ReplyForm



@login_required
def tenant_messages(request):
    # Fetch messages sent by the tenant and associated replies
    tenant_messages = Message.objects.filter(tenant=request.user).order_by('-timestamp')  # assuming tenant is logged in
    return render(request, 'tenentapp/messages.html', {'tenant_messages': tenant_messages})


@login_required
def reply_to_owner(request, message_id):
    # Get the message object
    message = get_object_or_404(Message, id=message_id)

    # Handle the reply submission
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.message = message
            reply.tenant = request.user  # The logged-in tenant
            reply.save()

            # messages.success(request, "Your reply has been sent.")
            return redirect('tenentapp:tenant_messages')  # Redirect to message listing page
    else:
        form = ReplyForm()

    return render(request, 'tenentapp/reply_form.html', {'form': form, 'message': message})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ownerapp.forms import MessageForm
from ownerapp.models import Property, Message

@login_required
def send_message(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Create the message
            message = form.save(commit=False)
            message.tenant = request.user  # Set the tenant as the logged-in user
            message.owner = property.owner  # Set the owner of the property
            message.property = property  # Set the related property
            message.save()  # Save the message to the database
            # messages.success(request, "Your message has been sent.")
            return redirect('tenentapp:property_detail', pk=property.id)  # Ensure you have this URL pattern
        # else:
        #     messages.error(request, "Please correct the errors below.")
    else:
        form = MessageForm()

    return render(request, 'tenentapp/send_message.html', {'form': form, 'property': property})


# views.py
from django.http import JsonResponse
from django.shortcuts import render
import google.generativeai as ai

# Configure the API
API_KEY = 'AIzaSyBzliAxdfyMS7Zo7Tjz0cdGQ4aKkQfhPlk'
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        if user_message.lower() == 'bye':
            return JsonResponse({'response': 'Goodbye!'})
        response = chat.send_message(user_message)
        return JsonResponse({'response': response.text})
    return render(request, 'tenentapp/chatbot.html')

