from django.shortcuts import render
from commissions.models import Commission


def commission_list(request):
    commissions = Commission.objects.all()
    ctx = {
        'commissions': commissions
    }

    return render(request, 'commission_list.html', ctx)


def commission_detail(request, pk):
    commission = Commission.objects.get(pk=pk)
    ctx = {
        'commission': commission
    }

    return render(request, 'commission_detail.html', ctx)