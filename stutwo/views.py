from django.shortcuts import render


def student_register_view(request):
    if request.method == "GET":
        return render(request, "student_register.html")
    else:
        return None
