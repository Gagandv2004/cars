from django.urls import path
from cbvapp import views

urlpatterns=[
    path('',views.AllCompaniesList.as_view(),name='list'),
    path('<int:pk>/',views.companydetails.as_view(),name='detail'),
    path('create/',views.AddNewCompany.as_view(),name='create'),
    path('edit/<int:pk>/',views.CompanyUpdate.as_view(),name='edit'),
    path('delete/<int:pk>/',views.DeleteCompany.as_view(),name='delete'),
    path('emi/<int:id>/',views.EMI_Calculator,name='emi'),
    path('product/<int:pk>/',views.productDetails.as_view(),name="product"),
   
]