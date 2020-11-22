from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required
def home(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	# category_id = Category.objects.filter(name=new)
	products = Product.objects.filter(available=True)
	new_products = Product.objects.filter(category_id='12')
	sale_products = Product.objects.filter(category_id='13')
	recommend = Product.objects.filter(category_id='5')

	page = request.GET.get('page', 1)
	page2 = request.GET.get('page', 1)
	page3 = request.GET.get('page', 1)
	page4 = request.GET.get('page', 1)

	paginator = Paginator(products, 12)
	paginator2 = Paginator(new_products, 2)
	paginator3 = Paginator(sale_products, 1)
	paginator4 = Paginator(recommend, 3)


	try:
		product_list = paginator.page(page)
		product_list2 = paginator2.page(page2)
		product_list3 = paginator3.page(page3)
		product_list4 = paginator4.page(page4)



	except PageNotAnInteger:
		product_list = paginator.page(1)
		product_list2 = paginator2.page(1)
		product_list3 = paginator3.page(1)
		product_list4 = paginator4.page(1)


	except EmptyPage:
		product_list = paginator.page(paginator.num_pages)
		product_list2 = paginator2.page(paginator2.num_pages)
		product_list3 = paginator3.page(paginator3.num_pages)
		product_list4 = paginator4.page(paginator4.num_pages)






	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=category)
		new_products = Product.objects.filter(category_id='12')
		sale_products = Product.objects.filter(category_id='13')
		recommend = Product.objects.filter(category_id='5')




		page = request.GET.get('page', 1)
		page2 = request.GET.get('page', 1)
		page3 = request.GET.get('page', 1)
		page4 = request.GET.get('page', 1)


		paginator = Paginator(products, 8)
		paginator2 = Paginator(new_products, 2)
		paginator3 = Paginator(sale_products, 1)
		paginator4 = Paginator(recommend, 3)

		try:
			product_list = paginator.page(page)
			product_list2 = paginator2.page(page2)
			product_list3 = paginator3.page(page3)
			product_list4 = paginator4.page(page4)


		except PageNotAnInteger:
			product_list = paginator.page(1)
			product_list2 = paginator2.page(1)
			product_list3 = paginator3.page(1)
			product_list4 = paginator4.page(1)





		except EmptyPage:
			product_list = paginator.page(paginator.num_pages)
			product_list2 = paginator2.page(paginator2.num_pages)
			product_list3 = paginator3.page(paginator3.num_pages)
			product_list4 = paginator4.page(paginator4.num_pages)

	context = {
		'category': category,
		'categories': categories,
		'product_list': product_list,
		'product_list2': product_list2,
		'product_list3': product_list3,
		'product_list4': product_list4
	}
	return render(request, 'shop/product/real_list.html', context)




def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	# category_id = Category.objects.filter(name=new)
	products = Product.objects.filter(available=True)
	new_products = Product.objects.filter(category_id='12')
	sale_products = Product.objects.filter(category_id='13')
	recommend = Product.objects.filter(category_id='5')

	page = request.GET.get('page', 1)
	page2 = request.GET.get('page', 1)
	page3 = request.GET.get('page', 1)
	page4 = request.GET.get('page', 1)

	paginator = Paginator(products, 8)
	paginator2 = Paginator(new_products, 3)
	paginator3 = Paginator(sale_products, 3)
	paginator4 = Paginator(recommend, 3)


	try:
		product_list = paginator.page(page)
		product_list2 = paginator2.page(page2)
		product_list3 = paginator3.page(page3)
		product_list4 = paginator4.page(page4)



	except PageNotAnInteger:
		product_list = paginator.page(1)
		product_list2 = paginator2.page(1)
		product_list3 = paginator3.page(1)
		product_list4 = paginator4.page(1)


	except EmptyPage:
		product_list = paginator.page(paginator.num_pages)
		product_list2 = paginator2.page(paginator2.num_pages)
		product_list3 = paginator3.page(paginator3.num_pages)
		product_list4 = paginator4.page(paginator4.num_pages)






	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=category)
		new_products = Product.objects.filter(category_id='12')
		sale_products = Product.objects.filter(category_id='13')
		recommend = Product.objects.filter(category_id='5')




		page = request.GET.get('page', 1)
		page2 = request.GET.get('page', 1)
		page3 = request.GET.get('page', 1)
		page4 = request.GET.get('page', 1)


		paginator = Paginator(products, 8)
		paginator2 = Paginator(new_products, 3)
		paginator3 = Paginator(sale_products, 3)
		paginator4 = Paginator(recommend, 3)

		try:
			product_list = paginator.page(page)
			product_list2 = paginator2.page(page2)
			product_list3 = paginator3.page(page3)
			product_list4 = paginator4.page(page4)


		except PageNotAnInteger:
			product_list = paginator.page(1)
			product_list2 = paginator2.page(1)
			product_list3 = paginator3.page(1)
			product_list4 = paginator4.page(1)





		except EmptyPage:
			product_list = paginator.page(paginator.num_pages)
			product_list2 = paginator2.page(paginator2.num_pages)
			product_list3 = paginator3.page(paginator3.num_pages)
			product_list4 = paginator4.page(paginator4.num_pages)

	context = {
		'category': category,
		'categories': categories,
		'product_list': product_list,
		'product_list2': product_list2,
		'product_list3': product_list3,
		'product_list4': product_list4
	}
	return render(request, 'shop/product/list.html', context)

@login_required
def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	recommend = Product.objects.filter(category_id='5')

	page4 = request.GET.get('page', 1)
	paginator4 = Paginator(recommend, 3)

	cart_product_form = CartAddProductForm()

	try:
		product_list4 = paginator4.page(page4)

	except PageNotAnInteger:
		product_list4 = paginator4.page(1)
	except EmptyPage:

		product_list4 = paginator4.page(paginator4.num_pages)


	context = {
		'product': product,
		'cart_product_form': cart_product_form,
		'product_list4': product_list4

	}
	return render(request, 'shop/product/detail.html', context)
