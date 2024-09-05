from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import PortfolioItem
from .forms import PortfolioItemForm

@login_required
def portfolio_list(request):
    items = PortfolioItem.objects.filter(user=request.user)
    return render(request, 'portfolio/portfolio.html', {'items': items})

@login_required
def portfolio_create(request):
    if request.method == 'POST':
        form = PortfolioItemForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio_item = form.save(commit=False)
            portfolio_item.user = request.user
            portfolio_item.save()
            return redirect('portfolio_list')
    else:
        form = PortfolioItemForm()
    return render(request, 'portfolio_form.html', {'form': form})

@login_required
def portfolio_edit(request, pk):
    portfolio_item = get_object_or_404(PortfolioItem, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PortfolioItemForm(request.POST, request.FILES, instance=portfolio_item)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
    else:
        form = PortfolioItemForm(instance=portfolio_item)
    return render(request, 'portfolio_form.html', {'form': form})

@login_required
def portfolio_delete(request, pk):
    portfolio_item = get_object_or_404(PortfolioItem, pk=pk, user=request.user)
    if request.method == 'POST':
        portfolio_item.delete()
        return redirect('portfolio_list')
    return render(request, 'portfolio_confirm_delete.html', {'portfolio_item': portfolio_item})
