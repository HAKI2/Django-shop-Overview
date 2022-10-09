from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'userprofile/profile.html')

@login_required
def settings(request):
    pass

@login_required
def favourite(request):
    fav = request.user.favourite_set.all()
    pr = fav[0].product.all()
    return render(request, 'userprofile/favourite.html', context={"pr": pr,
                                                                  "section": "favourite"})