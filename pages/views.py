from django.shortcuts import render, redirect
from .models import Client , File, ClientGroup
from .forms import ClientForm, FileForm, ClientGroupForm
from django.contrib import messages
from django.http import HttpResponseRedirect

#Log In Page:
def login(request):
    return render(request, "login.html", {})

#Initial Search Page:
def search(request):
    all_items = Client.objects.all
    groups = ClientGroup.objects.all
    return render(request, "search.html", {'all_items': all_items, 'groups':groups})

#Search Page given Client Name selection:
def searchCN(request):
    all_items = Client.objects.all
    groups = ClientGroup.objects.all
    return render(request, "client_name.html", {'all_items': all_items, 'groups':groups, })

def searchCN_id(request, group_id):
    all_items = Client.objects.all
    groups = ClientGroup.objects.all
    group_id = ClientGroup.objects.get(pk=group_id)

    return render(request, "client_name_id.html", {'all_items': all_items, 'groups':groups, 'group_id':group_id,})

#Client Name Results:
def searchCN_q(request):
    if request.method == "POST":
        searched = request.POST['searched']
        clients = Client.objects.filter(
        client_name__contains=searched
        )
        return render(request, 'client_name_q.html', {'searched':searched, 'clients':clients})
    else:
        return render(request, 'client_name_q.html', {})

def searchCN_q_id(request, group_id):
    if request.method == "POST":
        searched = request.POST['searched']
        group = ClientGroup.objects.get(pk=group_id)
        clients = Client.objects.filter(
        client_name__contains=searched
        ).filter(
        client_group__contains=group
        )
        return render(request, 'client_name_q_id.html', {'searched':searched, 'clients':clients})
    else:
        return render(request, 'client_name_q_id.html', {})



#Search Page given Tax ID selection:
def searchTI(request):
    all_items = Client.objects.all
    groups = ClientGroup.objects.all
    return render(request, "tax_id.html", {'all_items': all_items, 'groups':groups})

def searchTI_id(request, group_id):
    all_items = Client.objects.all
    groups = ClientGroup.objects.all
    group_id = ClientGroup.objects.get(pk=group_id)

    return render(request, "tax_id_id.html", {'all_items': all_items, 'groups':groups, 'group_id':group_id,})

#Tax ID Results:
def searchTI_q(request):
    if request.method == "POST":
        searched = request.POST['searched']
        clients = Client.objects.filter(
        tax_id__contains=searched
        )
        return render(request, 'tax_id_q.html', {'searched':searched, 'clients':clients})
    else:
        return render(request, 'tax_id_q.html', {})

def searchTI_q_id(request, group_id):
    if request.method == "POST":
        searched = request.POST['searched']
        group = ClientGroup.objects.get(pk=group_id)
        clients = Client.objects.filter(
        tax_id__contains=searched
        ).filter(
        client_group__contains=group
        )
        return render(request, 'tax_id_q_id.html', {'searched':searched, 'clients':clients})
    else:
        return render(request, 'tax_id_q_id.html', {})

#Search Page given Project Manager selection:
def searchPM(request):
    groups = ClientGroup.objects.all
    all_items = Client.objects.all
    return render(request, "pm.html", {'all_items': all_items, 'groups':groups})

def searchPM_id(request, group_id):
    all_items = Client.objects.all
    groups = ClientGroup.objects.all
    group_id = ClientGroup.objects.get(pk=group_id)

    return render(request, "pm_id.html", {'all_items': all_items, 'groups':groups, 'group_id':group_id,})

#Project Manager Results:
def searchPM_q(request):
    if request.method == "POST":
        searched = request.POST['searched']
        clients = Client.objects.filter(
        project_manager__contains=searched
        )
        return render(request, 'pm_q.html', {'searched':searched, 'clients':clients})
    else:
        return render(request, 'pm_q.html', {})

def searchPM_q_id(request, group_id):
    if request.method == "POST":
        searched = request.POST['searched']
        group = ClientGroup.objects.get(pk=group_id)
        clients = Client.objects.filter(
        project_manager__contains=searched
        ).filter(
        client_group__contains=group
        )
        return render(request, 'pm_q_id.html', {'searched':searched, 'clients':clients})
    else:
        return render(request, 'pm_q_id.html', {})

#All records in the database:
def records(request):
    all_items = Client.objects.all
    return render(request, "records.html", {'all_items': all_items})


#Add Client Page:
def client(request):
    submitted = False

    if request.method == 'POST':

                       #check for input
        form = ClientForm(request.POST)           #save user input

        if form.is_valid():                        #check if input is valid
            form.save()                            #save input to our database
            messages.info(request, request.POST['client_name']+ ' has been added to the Records!')
            return HttpResponseRedirect('/search?submitted=True')

    else:
        groups = ClientGroup.objects.all
        ct_message = 'Choose Client Type'
        form = ClientForm(initial = {'client_type': ct_message})
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "addclient.html", {'form': form, 'submitted':submitted, 'groups':groups})

#edit client
def edit(request, list_id):
    if request.method == 'POST':
        item = Client.objects.get(pk=list_id)

        form = ClientForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.info(request, request.POST['client_name']+ ' record has been edited!')
            return redirect('search')

    else:
        form = ClientForm()
        groups = ClientGroup.objects.all
        item = Client.objects.get(pk=list_id)
        return render(request, "edit.html", {'item': item, 'form': form, 'groups':groups})

#Add document given id
def document_id(request, list_id):
    if request.method == 'POST':
        item = Client.objects.get(pk=list_id)

        form = ClientForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.info(request, request.POST['client_name']+ ' record has been edited!')
            return redirect('search')

    else:
        documents = Client.objects.get(pk=list_id)
        groups = ClientGroup.objects.all
        document_list = File.objects.filter(client=list_id)
        form = FileForm()
        formC = ClientForm()
        context = {'form':form, 'formC':formC, 'documents':documents, 'document_list':document_list, 'groups':groups, }

    return render(request, 'add_document_id.html', context)

def document_id_add(request, list_id):
    if request.method == 'POST':
        documents = Client.objects.get(pk=list_id)
        form = FileForm(request.POST or None,request.FILES)

        if form.is_valid():

            form.save()
            messages.info(request, 'The document has been added to the Database!')
            return redirect('document_id', list_id)

    else:
        documents = Client.objects.get(pk=list_id)
        form = FileForm()

    return render(request, 'add_document_submit.html', {'form':form, 'documents':documents})

#delete client
def delete(request, list_id):
    item = Client.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'The Record has been deleted!')
    return redirect('search')

#delete file
def delete_file(request, list_id, file_id):
    item = File.objects.get(pk=file_id)
    item.delete()
    return redirect('document_id', list_id)

#add document:
def document(request):
     if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'The document has been added to the Database!')
            return redirect('search')
     else:
        form = FileForm()
        context = {'form':form,}
     return render(request, 'add_document.html', context)

#View Documents
def document_list(request):
    documents = Client.objects.all
    document_list = File.objects.all

    context = {'documents':documents, 'document_list':document_list, }

    return render(request, 'documents.html', context)

def groups(request):
    all_items = ClientGroup.objects.all
    return render(request, 'groups.html', {'all_items':all_items, })

def group_delete(request, group_id):
    item = ClientGroup.objects.get(pk=group_id)
    item.delete()
    return redirect('groups')

def group(request):
    submitted = False
    if request.method == 'POST':                   #check for input
        form = ClientGroupForm(request.POST)            #save user input

        if form.is_valid():                        #check if input is valid
            form.save()                            #save input to our database
            return redirect('groups')

    else:
        form = ClientGroupForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "add_group.html", {'form': form, 'submitted':submitted})

def group_search(request, group_id):
    group = ClientGroup.objects.get(pk=group_id)
    clients = Client.objects.filter(
    client_group__contains=group
    )
    return render(request, 'group_q.html', {'clients':clients})


def edit_document(request, list_id, file_id):
    if request.method == 'POST':

        item = File.objects.get(pk=file_id)
        form = FileForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            return redirect('document_id', list_id)

    else:
        document = File.objects.get(pk=file_id)
        client = Client.objects.get(pk=list_id)
        form = FileForm()

    return render(request, 'edit_document.html', {'form':form,  'document':document, 'client':client, })
