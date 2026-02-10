from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import  HttpResponse
from cbvapp.models import Company,Products

# Create your views here.
# class Myclass(View):
#     def get(self,request):
#         return HttpResponse("<h2> this is class based view</h2>")

class Myclass(TemplateView):
    template_name="index.html"

class AllCompaniesList(ListView):
    model=Company
    context_object_name="allCompanies"

class companydetails(DetailView):
    model=Company
    context_object_name="company_details"

class AddNewCompany(CreateView):
    model=Company
    fields='__all__'

class CompanyUpdate(UpdateView):
    model=Company
    fields=['name','CEO','logo']

from django.urls import reverse_lazy

class DeleteCompany(DeleteView):
    model=Company
    success_url=reverse_lazy('list')


from cbvapp.forms import EMIFORM
from cbvapp.models import Products

def EMI_Calculator(request,id=0):
    product=Products.objects.get(id=id)
    form=EMIFORM(instance=product)

    if request.method=="POST":
        principal_amount=int(request.POST['principal'])
        tenure=int(request.POST['tenure'])

        if principal_amount<product.price:
            R=12/(12*100)
            N=tenure*12

            numerator=principal_amount*R*(1+R)**N
            denominator=(1+R)**N-1
            res=numerator/denominator
            print(res)
            return render(request,"cbvapp/emi_calculator.html",{'res':res,'form':form})
        else:
            return HttpResponse("<h1>The loan amount should be less than car price</h1>")

    return render(request,"cbvapp/emi_calculator.html",{'form':form})

class productDetails(DetailView):
    model=Products
    context_object_name="product_details"

