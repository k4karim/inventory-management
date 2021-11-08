from django.conf.urls import url
from inventory_mgmt import views

# SET THE NAMESPACE!
app_name = 'inventory_mgmt'

urlpatterns=[
    url(r'^$',views.prod_list,name='prod_list'),

    
    
    url(r'^new/$',views.prod_new,name='prod_new'),

    url(r'^prod/(?P<pk>\d+)/add/$',views.prod_add,name='prod_add'),
    url(r'^prod/(?P<pk>\d+)/remove/$',views.prod_remove,name='prod_remove'),
    url(r'^prod/(?P<pk>\d+)/delete/$',views.prod_delete,name='prod_delete'),
##
##    url(r'^med/(?P<pk>\d+)/delete/$',views.med_remove,name='med_remove'),

    
    
]
