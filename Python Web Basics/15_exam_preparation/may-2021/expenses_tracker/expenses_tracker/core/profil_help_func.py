from expenses_tracker.tracker.models import Profile, Expense


def get_profile():
    profile = Profile.objects.first()
    return profile


def get_profile_and_budget():
    profile = Profile.objects.first()
    expenses = Expense.objects.all()
    profile.budget_left = profile.budget - sum(e.price for e in expenses)
    return profile