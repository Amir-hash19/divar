from django.shortcuts import render
from django.http.response import HttpResponse,FileResponse
import os

def download_cookies(request):
    file = os.path.join("/home/amirykta/Desktop/divar/divar/account/cookies.pdf")
    return FileResponse(
        open(file, "rb"),
        as_attachment=True
    )

def print_page_user(request):
    return render(request, "account/user_page.html")