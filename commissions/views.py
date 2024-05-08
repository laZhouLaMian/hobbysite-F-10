from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.forms import modelformset_factory

from commissions.models import Commission, Job

from .forms import CommissionForm, JobApplicationForm, JobForm


def commission_list(request):
    ctx = {
        "all_commission_list": Commission.objects.all(),
        "created_commission_list": Commission.objects.filter(
            author=request.user.profile
        ),
        "applied_commission_list": Commission.objects.filter(
            job__job_application__applicant=request.user.profile
        ),
    }

    return render(request, "commission_list.html", ctx)


@login_required
def commission_detail(request, pk):
    commission_detail = Commission.objects.get(pk=pk)
    commission_jobs = commission_detail.job
    total_manpower_required = (
        commission_jobs.aggregate(Sum("manpower_required"))["manpower_required__sum"]
        or 0
    )
    open_manpower = (
        total_manpower_required
        - commission_jobs.filter(job_application__status="1").aggregate(
            Count("job_application")
        )["job_application__count"]
    )

    form = JobApplicationForm()
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = Job.objects.get(role=request.POST.get("job"))
            application.applicant = request.user.profile
            application.status = "Pending"
            form.save()
            return redirect("commissions:list")

    ctx = {
        "commission_detail": commission_detail,
        "commission_jobs": commission_jobs.all(),
        "total_manpower_required": total_manpower_required,
        "open_manpower": open_manpower,
        "form": form,
    }

    return render(request, "commission_detail.html", ctx)


@login_required
def commission_create(request):
    commission_form = CommissionForm()
    job_form = JobForm()

    if request.method == "POST":
        commission_form = CommissionForm(request.POST)
        job_form = JobForm(request.POST)
        if commission_form.is_valid() and job_form.is_valid():
            commission = commission_form.save(commit=False)
            commission.author = request.user.profile
            commission = commission_form.save()
            job = job_form.save(commit=False)
            job.commission = commission
            job_form.save()
            return redirect("commissions:list")

    ctx = {"commission_form": commission_form, "job_form": job_form}

    return render(request, "commission_create.html", ctx)


@login_required
def commission_edit(request, pk):
    commission = Commission.objects.get(pk=pk)
    commission_jobs = commission.job
    commission_form = CommissionForm(instance=commission)
    job_formset = modelformset_factory(Job, extra=0, exclude=["commission"])
    job_forms = job_formset(queryset=Job.objects.filter(commission=commission))

    if request.method == "POST":

        commission_form = CommissionForm(request.POST, instance=commission)
        job_forms = job_formset(request.POST)

        if commission_form.is_valid() and job_forms.is_valid():

            commission = commission_form.save(commit=False)

            is_all_jobs_full = True
            for form_no in range(commission_jobs.count()):
                if request.POST[f"form-{form_no}-status"] is not "Full":
                    is_all_jobs_full = False
                    break

            if is_all_jobs_full:
                commission.status = "Full"

            commission.save()
            job_forms.save()
            return redirect("commissions:detail", pk=pk)

    ctx = {
        "commission_jobs": commission_jobs.all(),
        "commission_form": commission_form,
        "job_forms": job_forms,
    }
    return render(request, "commission_edit.html", ctx)
