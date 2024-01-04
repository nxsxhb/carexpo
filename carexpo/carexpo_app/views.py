
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Car
from . forms import CarForm

# Create your views here.
def index(request):
    car = Car.objects.all()
    contents = { 'car_list': car }

    return render(request, "index.html", contents)

def detail(request, car_id):
    carID=Car.objects.get(id=car_id)
    return render(request, "details.html", {'car_id':carID})

def add(request):
    if request.method=="POST":
        brand_name = request.POST.get('brand_name',)
        model_name = request.POST.get('model_name',)
        type = request.POST.get('type',)
        year = request.POST.get('year',)
        image = request.FILES['image']

        car=Car(brand_name=brand_name,model_name=model_name,type=type,year=year,image=image)
        car.save()
        
    return render(request, 'add.html')

def update(request,id):
    car=Car.objects.get(id=id)
    form=CarForm(request.POST or None, request.FILES, instance=car)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'car': car})

def delete(request, id):
    if request.method=='POST':
        car = Car.objects.get(id=id)
        car.delete()
        return redirect('/')
    return render(request, 'delete.html')
