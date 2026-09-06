from django.http import HttpResponse

# Create your views here.
def index(request, month):
    challenges = {
        "january": "These are the challenges for January.",
        "february": "These are the challenges for February.",
        "march": "These are the challenges for March.",
        "april": "These are the challenges for April.",
        "may": "These are the challenges for May.",
        "june": "These are the challenges for June.",
        "july": "These are the challenges for July.",
        "august": "These are the challenges for August.",
        "september": "These are the challenges for September.",
        "october": "These are the challenges for October.",
        "november": "These are the challenges for November.",
        "december": "These are the challenges for December.",
    }
    return HttpResponse(challenges.get(month, "Invalid month."))