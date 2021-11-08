from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from .models import Inventory

  
# Create your views here.
def prod_list(request):
    prod_list = Inventory.objects.filter().order_by('quantity')

    return render(request, 'prod_list.html', {'prod_list': prod_list})


def prod_new(request):
    if request.method=="POST":
        user_prod_title= str(request.POST.get('prod_title')).strip()
        user_quantity= str(request.POST.get('quantity')).strip()
    
        try:
            new_inv = Inventory(prod_title=user_prod_title, quantity=user_quantity,created_date=timezone.now())
        
            new_inv.save()
            
            messages.success(request, 'You have Successfully added: '+str(user_prod_title), extra_tags='alert')
        except:
            messages.success(request, str(user_prod_title)+ ' already exist in our dattabase', extra_tags='alert')
    
        return redirect('inventory_mgmt:prod_list')
    

def prod_delete(request,pk):
    prod=get_object_or_404(Inventory,pk=pk)
    
    _prod_title= prod.prod_title
    if request.method == 'POST':
        
        
        Inventory.objects.filter(id = pk).delete()
        
        
        messages.error(request, 'You have Successfully Deleted: '+str(_prod_title), extra_tags='alert')
       
        return redirect('inventory_mgmt:prod_list')



def prod_add(request,pk):

    
     prod=get_object_or_404(Inventory,pk=pk)

     existing_quantity=prod.quantity
    
     _prod_title= prod.prod_title

     if request.method == 'POST':
        
        
        user_input_quantity= str(request.POST.get('prod-quantity')).strip()
       

        total=int(existing_quantity)+int(user_input_quantity)
        
        Inventory.objects.filter(id = pk).update(quantity = total)
        
        messages.success(request, 'You have Successfully added  '+str(user_input_quantity)+' quantity to ' +str(_prod_title), extra_tags='alert')
        
       
        return redirect('inventory_mgmt:prod_list')



def prod_remove(request,pk):
    prod=get_object_or_404(Inventory,pk=pk)
    existing_quantity=prod.quantity

    _prod_title= prod.prod_title

    if request.method == 'POST':
        user_input_quantity= str(request.POST.get('prod-quantity')).strip()
        total=int(existing_quantity)-int(user_input_quantity)
        Inventory.objects.filter(id = pk).update(quantity = total)
        messages.error(request, 'You have Successfully removed  '+str(user_input_quantity)+' quantity from ' +str(_prod_title), extra_tags='alert')
        return redirect('inventory_mgmt:prod_list')    

