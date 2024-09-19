from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Do a hand-stand every day",
    "may": "Stretch for at least 20 minutes every day",
    "june": "Learn spanish for at least 20 minutes every day",
    "july": "Call your mom once a week",
    "august": "Learn a new fact about python every day",
    "september": "Go to the gym at least 3 times per week",
    "october": "Eat home-made food every day",
    "november": "Reach out to an old friend or acquaintance at least once a week",
    "december": "Build a new project from scratch by the end of the month",
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Invalid month</h1>")


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"""
          <li>
            <a href=\"{month_path}\">{capitalized_month}</a>
          </li>
        """

    response_data = f"""
      <h1>Months</h1>
      <ol>
        {list_items}
      </ol>
    """

    return HttpResponse(response_data)
