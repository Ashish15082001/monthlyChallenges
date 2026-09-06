from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


challenges = {
        "january": "Eat no meat for the entire month.",
        "february": "Walk for at least 20 minutes every day.",
        "march": "Learn Django for at least 20 minutes every day.",
        "april": "Exercise for at least 30 minutes every day.",
        "may": "Read at least one book.",
        "june": "Learn a new programming language.",
        "july": "Write a blog post every week.",
        "august": "Take a photo every day.",
        "september": "Meditate for at least 10 minutes every day.",
        "october": "Learn a new skill.",
        "november": "Write a gratitude journal every day.",
        "december": "Reflect on the year and set goals for the next year."
}

# Create your views here.
def challenges_int(request, month):
    months = list(challenges.keys())
    if month > len(months) or month < 1:
        return HttpResponse("Invalid month.")
    else:
        month_name = months[month - 1]
        redirect_path = reverse("monthly-challenge", args=[month_name])
        return HttpResponseRedirect(redirect_path)

def challenges_string(request, month):
    return HttpResponse(f"STRING: {challenges.get(month, 'Invalid month.')}")