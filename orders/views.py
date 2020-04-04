from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import User
from django.db import IntegrityError
from .models import Regular_Pizza, Sicilian_Pizza, Topping, Sub, Dinner_Platter, Pasta, Salad, Order, Placed_Order, AddOn
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


def index(request):
    return render(request, 'orders/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'orders/signup.html')

    else:
        if request.POST['password1'] == request.POST['password2']:

            password = request.POST['password1']
            if len(password) > 4:
                try:
                    user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                    user.first_name = request.POST['firstname']
                    user.last_name = request.POST['lastname']
                    user.email = request.POST['email']
                    user.save()
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                except IntegrityError:
                    return render(request, 'orders/signup.html', {'error': 'Username already exist'})

            else:
               return render(request, 'orders/signup.html', {'error': 'Passwords length must be greater than 4'}) 

        else:
            return render(request, 'orders/signup.html', {'error': 'Passwords does not match'})


@login_required
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'orders/login.html')

    else:
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'orders/login.html', {'error': 'Invalid Credentials'})

        else:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))


@login_required
def menu(request):
    if request.method == 'GET':
        context = {
            "Regular_Pizzas": Regular_Pizza.objects.all(),
            "Sicilian_Pizzas": Sicilian_Pizza.objects.all(),
            "Toppings": Topping.objects.all(),
            "Subs": Sub.objects.all(),
            "Pastas": Pasta.objects.all(),
            "Salads": Salad.objects.all(),
            "Dinner_Platters": Dinner_Platter.objects.all(),
        }
        return render(request, 'orders/menu.html', context)

    else:
        order = Order()
        order.name = request.POST['name']
        order.typeof = request.POST['typeof']
        order.size = request.POST['size']
        order.quantity = request.POST['quantity']
        order.topping1 = request.POST['topping1']
        order.topping2 = request.POST['topping2']
        order.topping3 = request.POST['topping3']
        order.total = request.POST['total']
        order.status = request.POST['status']
        order.orderedby = request.user
        order.time = timezone.datetime.now()
        order.save()

        context = {
            "Regular_Pizzas": Regular_Pizza.objects.all(),
            "Sicilian_Pizzas": Sicilian_Pizza.objects.all(),
            "Toppings": Topping.objects.all(),
            "Subs": Sub.objects.all(),
            "Pastas": Pasta.objects.all(),
            "Salads": Salad.objects.all(),
            "Dinner_Platters": Dinner_Platter.objects.all(),
        }
        return render(request, 'orders/menu.html', context)


@login_required
def customise0(request, name):
    context = {
        "regular": Regular_Pizza.objects.get(name=name),
        "sicilian": Sicilian_Pizza.objects.get(name=name)
    }
    return render(request, 'orders/customise0.html', context)


@login_required
def customise1(request, name):
    if name == '1 topping':
        sname = '1 item'

    if name == '2 toppings':
        sname = '2 items'

    if name == '3 toppings':
        sname = '3 items'
    context = {
        "regular": Regular_Pizza.objects.get(name=name),
        "sicilian": Sicilian_Pizza.objects.get(name=sname),
        "toppings": Topping.objects.all()
    }
    return render(request, 'orders/customise1.html', context)


@login_required
def customise2(request, name):
    try:
        sub = Sub.objects.get(name=name)
    except Sub.DoesNotExist:
        context = {
            "dinner": Dinner_Platter.objects.get(name=name)
        }
        return render(request, 'orders/customise2.html', context)

    context = {
        "sub": sub,
        "addon": AddOn.objects.get(id=1)
    }
    return render(request, 'orders/customise2.html', context)


@login_required
def customise3(request, name):
    try:
        pasta = Pasta.objects.get(name=name)
    except Pasta.DoesNotExist:
        context = {
            "salad": Salad.objects.get(name=name)
        }
        return render(request, 'orders/customise3.html', context)

    context = {
        "pasta": pasta,
    }
    return render(request, 'orders/customise3.html', context)


@login_required
def cart(request):
    if request.method == 'GET':
        orders = Order.objects.filter(orderedby=request.user, status="Cart")

        total_cost = 0
        for order in orders:
            total_cost += order.total

        context = {
            "orders": orders,
            "total_cost": total_cost
        }
        return render(request, 'orders/cart.html', context)


@login_required
def discard(request, order_id):
    order = get_object_or_404(Order, pk=order_id, orderedby=request.user)
    if request.method == 'POST':
        order.delete()
        return HttpResponseRedirect(reverse('cart'))


@login_required
def placeorder(request):
    if request.method == 'POST':
        orders = Order.objects.filter(orderedby=request.user, status="Cart")
        placedorder = Placed_Order()
        total_price = 0
        for order in orders:
            placedorder.detail += f"[{order.name} {order.typeof} {order.size} {order.topping1} {order.topping2} {order.topping3}]X{order.quantity} "
            total_price += order.total
            order.delete()

        placedorder.totalprice = total_price
        placedorder.status = "In Progress"
        placedorder.time = timezone.datetime.now()
        placedorder.orderedby = request.user
        placedorder.save()
        return render(request, 'orders/cart.html')


@login_required
def order(request):
    if request.user.is_superuser:
        orderspro = Placed_Order.objects.filter(status="In Progress")
        orderscom = Placed_Order.objects.filter(status="Completed")
    else:
        orderspro = Placed_Order.objects.filter(
            status="In Progress", orderedby=request.user)
        orderscom = Placed_Order.objects.filter(
            status="Completed", orderedby=request.user)

    context = {
        "orderspro": orderspro,
        "orderscom": orderscom
    }
    return render(request, 'orders/order.html', context)


@permission_required('polls.add_choice')
def complete(request, order_id):
    order = get_object_or_404(Placed_Order, pk=order_id)
    if request.method == 'POST':
        order.status = "Completed"
        order.save()
        return HttpResponseRedirect(reverse('order'))
