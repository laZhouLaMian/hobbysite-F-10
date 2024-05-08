from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.forms import modelformset_factory

from commissions.models import Commission, Job, JobApplication

from .forms import CommissionForm, JobApplicationForm, JobForm


def commission_list(request):
    ctx = {
        "commission_list": Commission.objects.all(),
        "created_commission_list": Commission.objects.filter(
            author__username=request.user.profile.username
        ),
        "applied_commission_list": Commission.objects.filter(
            job__job_application__applicant__username=request.user.profile.username
        ),
    }

    return render(request, "commission_list.html", ctx)


def commission_detail(request, pk):
    commission = Commission.objects.get(pk=pk)
    ctx = {"commission": commission}

    return render(request, "commission_detail.html", ctx)
