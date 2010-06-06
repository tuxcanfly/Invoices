# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from bills.models import Invoice, InvoiceForm, UserForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.conf import settings

@login_required
def dashboard(request):
		invoices = Invoice.objects.filter(user=request.user).order_by('-date')
		return render_to_response('invoices.html', {
			'invoice_list': invoices,
			'username': request.user.username,
		}) 

@login_required
def showinvoice(request, id):
		invoice = get_object_or_404(Invoice, pk=id)
		error = None
		if (invoice.user != request.user) and not request.user.is_staff:
			error = 'Permission Denied'
			invoice = None
		return render_to_response('invoice.html', {
			'username': request.user.username, 
			'invoice': invoice,
			'error': error,
		})

def userlogout(request):
	return logout(request)

@login_required
def invoiceform(request):
	if request.user.is_staff:
		if request.method == 'POST':
			form = InvoiceForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/bills/')
		else:
			form = InvoiceForm()
		return render_to_response('invoiceform.html', {
			'form': form,
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/bills/login/')

@login_required
def userform(request):
	if  request.user.is_staff:
		if request.method == 'POST':
			form = UserForm(request.POST)
			if form.is_valid():
				newuser = form.save(commit=False)
				newuser.set_password(settings.PASSWORD)
				form.save()
				return HttpResponseRedirect('/bills/')
		else:
			form = UserForm()
		return render_to_response('userform.html', {
			'form': form,
		}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/bills/login/')
