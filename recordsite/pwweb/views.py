from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.template import loader

from .models import WorkRecord

def index(request):
    latest_record_list = WorkRecord.objects.order_by("-date")
    context = {
        "latest_record_list": latest_record_list,
    }
    return render(request, "pwweb/index.html", context)

def submit_form(request):
    template = loader.get_template("pwweb/submit_form.html")
    return HttpResponse(template.render({}, request))

def create_record(request):
    record = request.POST
    workrecord = WorkRecord(
        game_type = record["gameType"],
        customer_name = record["customerName"],
        is_challenger_rank = record["isChallengerRank"],
        paid_amount = float(record["hourlyRate"]) * float(record["workHours"]),
        commission_rate = 0.75,
        date = timezone.now(),
        status = WorkRecord.TicketStatus.Pending
    )
    workrecord.save()     
    return HttpResponseRedirect(reverse("pwweb:index"))
