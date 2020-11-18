from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger






def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)

	page = request.GET.get('page', 1)
	paginator = Paginator(products, 8)
	try:
		product_list = paginator.page(page)
	except PageNotAnInteger:
		product_list = paginator.page(1)
	except EmptyPage:
		product_list = paginator.page(paginator.num_pages)






	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=category)

		page = request.GET.get('page', 1)
		paginator = Paginator(products, 8)
		try:
			product_list = paginator.page(page)
		except PageNotAnInteger:
			product_list = paginator.page(1)
		except EmptyPage:
			product_list = paginator.page(paginator.num_pages)

	context = {
		'category': category,
		'categories': categories,
		'product_list': product_list
	}
	return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	cart_product_form = CartAddProductForm()
	context = {
		'product': product,
		'cart_product_form': cart_product_form
	}
	return render(request, 'shop/product/detail.html', context)
