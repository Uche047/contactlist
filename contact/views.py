from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index_view(request):
	contact = Contact.objects.all()
	
	search = request.GET.get('search-area')
	if search:
		contact = Contact.objects.filter(name__icontains=search)
		
	
	else:
		contact = Contact.objects.all()
		search = ""
	
	context = {
		'uche': contact,
		'search': search
	}	
	return  render(request, 'index.html', context)

def addContact_view(request):
	if request.method == 'POST':
		print(request.POST.values())
		new_contact = Contact(
			name = request.POST['fullname'],
			relationship = request.POST['relationship'],
			phoneNumber = request.POST['phone-number'],
			address= request.POST['address'],
			email= request.POST['email'],


			)
		
		new_contact.save()
		return redirect("/index")
	return render(request, 'new.html')

def profile_view(request, id):
	contact = Contact.objects.get(id=id)
	context = {
		'uche': contact
	}
	return render(request, 'contact-profile.html', context)

def editContact_view(request, id):
	contact = Contact.objects.get(id=id)
	context = {
		'uche': contact
	}
	if request.method == 'POST':
		contact.name = request.POST['fullname']
		contact.relationship = request.POST['relationship']
		contact.phoneNumber = request.POST['phone-number']
		contact.address = request.POST['address']
		contact.email = request.POST['email']
		contact.save()

		return redirect('/edit/' + str(contact.id))


	return render(request, 'edit.html', context)

def delete_view(request, id):
	contact = Contact.objects.get(id=id)
	context = {
		'uche':contact
		}
	if request.method == 'POST':
		contact.delete()
		return redirect('/index/')
		
	return render(request, 'delete.html', context)
