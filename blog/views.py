from django.http import HttpResponse
from django.shortcuts import render
from . models import Blogpost

# Create your views here.
def index(request):
    blogs = Blogpost.objects.all()
    print(blogs)
    
    return render(request,'blog/index.html',{'blogs':blogs})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id=id)[0]
    print(post)
    all_post = Blogpost.objects.all()
    total = len(all_post)
    print(total)
    
    return render(request,'blog/blogpost.html',{'post':post, 'total':total})






# from django.http import HttpResponse
# from django.shortcuts import render
# from shop.models import Product, Contact, Order, OrderUpdate
# from django.contrib import messages
# import math
# import json
# # Create your views here.


# def index(request):
#     # products = Product.objects.all()
#     # print(products)
#     # print(type(products))
#     # n = len(products)
#     # nSlides = n//4 + math.ceil(n/4 - n // 4)
#     # params = {'no_of_slides' : nSlides, 'range': range(1,nSlides), 'product':products}
    
#     # Created List of Lists fro displaying multiple sliders
#     # allProducts = [[products, range(1, nSlides)],
#     #                [products, range(1, nSlides)]]
    
#     allproducts = []
#     categoryproducts = Product.objects.values('category') # Get the categories of all the objects
    
    
# # Filtered all the products based on the Categories and created a new Queryset for each type of Category. 
# # This means No. of categories = Number of Querysets

#     # Created a SET and iterate through each categoryproducts and stored the values in item['category'] 
#     # SET is used to avoid Duplication of element
#     categories = {item['category'] for item in categoryproducts} 
#     for category in categories:
#         print(category)
#         product = Product.objects.filter(category=category) #Filtered all the products with current category(For loop)
#         n = len(product)
#         print(len(product))
#         nSlides = n//4 + math.ceil(n/4 - n // 4) # Calculated the no. of slides
#         allproducts.append([product, range(1,nSlides)]) # Added product and range of slides in allproducts[] list
    
#     # Made Dictionary of the products as key:value pair
#     params = {'allproducts': allproducts}                                            
#     print(params)            
#     # Passed the dictionary to the view                  
#     return render(request, 'shop/index.html', params)             

# def about(request):
#     return render(request, 'shop/about.html')


# def contact(request):
#     if request.method == 'POST':
#         print(request)
#         name = request.POST.get('name','')
#         email = request.POST.get('email','')
#         phone = request.POST.get('phone','')
#         desc = request.POST.get('desc','')
#         print(name,email,phone,desc)
        
#         contact = Contact(name=name,email=email,phone=phone,desc=desc)
#         print(contact)
#         contact.save()
#         messages.success(request, 'Form submitted successfully...')
        
#     return render(request,'shop/contact.html')


# def tracker(request):
    
#     if request.method == 'POST':
#         order_id = request.POST.get('order_id','')
#         email = request.POST.get('email','')
        
#         try:
#             # Checks that the given order_id ane email is present in the Orders Table and 
#             # filters all the data related to the given order_id and email
#             order = Order.objects.filter(order_id=order_id, email=email) 
            
#             if len(order) > 0:
#                 # If the order is present in the OrderUpdates Table then filter all the data 
#                 # related with the given Order_id
#                 update = OrderUpdate.objects.filter(order_id=order_id)
#                 updates = []
#                 for item in update:
#                     updates.append({'text': item.update_desc , 'time': item.timestamp})
#                     response = json.dumps([updates,order[0].items_json],default=str)
#                 return HttpResponse(response)
#             else:
#                 return HttpResponse('{}')
#         except Exception as e:
#             return HttpResponse('{}')
#     return render(request,'shop/tracker.html')


# def search(request):
#     return render(request,'shop/search.html')


# def prodView(request, myid):
#     # return HttpResponse("We are at Product view page")
#     product = Product.objects.filter(product_id=myid)
#     print(product)
#     return render(request, 'shop/prodview.html',{'product':product})

# def checkout(request):
#     if request.method == 'POST':
#         print(request)
#         items_json = request.POST.get('items_json','')
#         name = request.POST.get('name','')
#         email = request.POST.get('email','')
#         address = request.POST.get('address','')
#         city = request.POST.get('city','')
#         state = request.POST.get('state','')
#         zip_code = request.POST.get('zip_code','')
#         phone = request.POST.get('phone','')
        
#         order = Order(items_json=items_json, name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
#         print(order)
#         order.save()
#         update = OrderUpdate(order_id=order.order_id, update_desc="The order has been Placed")
#         update.save()
#         thank = True
#         order_id = order.order_id
#         return render(request,'shop/checkout.html',{'thank' :thank, 'order_id':order_id})
#     return render(request,'shop/checkout.html')
                           