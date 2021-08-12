from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from accounts.forms import UserCreateForm, UserUpdateForm, CustomerUpdateForm, AddressUpdateForm, AddressCreateForm
from accounts.models import Address
# Create your views here.


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup_page.html'

    def form_valid(self, form):
        messages.success(self.request, f'Account created successfully. You can log in now using your details.')
        return super().form_valid(form)


@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        c_form = CustomerUpdateForm(request.POST, instance=request.user.customer)

        if u_form.is_valid() and c_form.is_valid():
            u_form.save()
            c_form.save()
    else:
        u_form = UserUpdateForm(instance=request.user)
        c_form = CustomerUpdateForm(instance=request.user.customer)

    total_price = request.session['total_price']

    context = {
        'u_form': u_form,
        'c_form': c_form,
        'total_price': total_price,
    }
    return render(request, 'accounts/profile.html', context)


class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'accounts/address_page.html'
    success_url = reverse_lazy('accounts:address_view')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        # context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the addresses currently logged user
        address_list = Address.objects.filter(customer=self.request.user.customer)

        total_price = self.request.session['total_price']

        context = {
            'address_list': address_list,
            'total_price': total_price,
        }
        return context


class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = Address
    form_class = AddressUpdateForm
    success_url = reverse_lazy('accounts:address_view')
    template_name = 'accounts/address_update_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_price = self.request.session['total_price']
        context['total_price'] = total_price
        return context


class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = Address
    success_url = reverse_lazy('accounts:address_view')
    template_name = 'accounts/address_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_price = self.request.session['total_price']
        context['total_price'] = total_price
        return context


class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    form_class = AddressCreateForm
    success_url = reverse_lazy('accounts:address_view')
    template_name = 'accounts/address_create.html'

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer
        return super(AddressCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_price = self.request.session['total_price']
        context['total_price'] = total_price
        return context
