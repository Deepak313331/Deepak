from django.shortcuts import render, redirect, get_object_or_404
from .models import UserDetailss
from .models import admindetails
from .models import ownersignup
from .models import category
from .models import sub_cat, view_room_db, image_upload
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.core.files.storage import FileSystemStorage
from .filters import search_view_room_db


def index(request):
    return render(request, "myapp/indexb.html")


def home(request):
    if request.session.has_key("skey"):
        if request.method == 'POST':
            return redirect("index")
        return render(request, "myapp/indexb.html", {'home_sesskey': request.session["skey"]})
    else:
        return redirect("index")


def about(request):
    return render(request, "myapp/aboutus2.html")


def contact(request):
    return render(request, "myapp/email1.html")


def signup(request):
    if request.method == 'POST':
        # s = UserDetails.objects.create_user(nname = nname, eemail = eemail, eephone = eephone)
        s = UserDetailss(nname=request.POST["name"], eemail=request.POST["email"],
                         eephone=int(request.POST["phone"]), epas=request.POST["pas"], eadd=request.POST["add"],
                         egen=request.POST["gen"], elook=request.POST["lookk"])
        s.save()
        return redirect("login")
    return render(request, "myapp/signupform.html")


def login(request):
    if request.method == "POST":
        r = UserDetailss.objects.filter(nname=request.POST["txtname"], epas=request.POST["txtpassword"])
        if r:
            request.session["skey"] = request.POST["txtname"]
            return render(request, "myapp/indexb.html", {'user_sesskey': request.session["skey"], 'res1': r})
        else:
            return render(request, "myapp/login_form.html", {'msg': "Invalid Credentials!!"})

    return render(request, "myapp/login_form.html")


def viewusersrecords(request):
    s = UserDetailss.objects.all()
    return render(request, "myapp/viewusersrecords.html", {'res': s})


def user_dashboard(request):
    if request.session.has_key("skey"):
        r = UserDetailss.objects.filter(nname=request.session["skey"])
        return render(request, "myapp/user_dash_board.html", {'user_sesskey': request.session["skey"], 'res1': r})
    return render(request, "myapp/user_dash_board.html")


def user_dash_board_view(request):
    if request.session.has_key("skey"):
        r = UserDetailss.objects.filter(nname=request.session["skey"])
        return render(request, "myapp/user_dash_board_view.html", {'user_sesskey': request.session["skey"], 'res1': r
                                                                   })
    return render(request, "myapp/user_dash_board_view.html")


def user_logout(request):
    del request.session["skey"]
    return redirect("index")


def user_check_email(request):
    s = request.GET["q"]
    chk = UserDetailss.objects.filter(eemail=s)
    if chk:
        return HttpResponse("Email already exist!!")
    else:
        return HttpResponse("")


'''def user_check_pass(request):
    pa = request.GET["c"]
    chk_pas = UserDetailss.objects.filter(epas=pa)
    if chk_pas
'''


def owner_check_email(request):
    s = request.GET["q"]
    ch = ownersignup.objects.filter(email=s)
    if ch:
        return HttpResponse("Email Already Exist!!")
    else:
        return HttpResponse("")


def owner(request):
    if request.method == 'POST':
        o = ownersignup(email=request.POST["txtsemail"], fullname=request.POST["txtsname"],
                        password=request.POST["txtspas"], phone=int(request.POST["txtsphone"]))
        o.save()
        return redirect("owner_login")
    return render(request, "myapp/signup&login.html")


def owner_login(request):
    if request.method == 'POST':
        res = ownersignup.objects.filter(fullname=request.POST["txtfullname"], password=request.POST["txtlpas"])
        if res:
            request.session["ownerD_key"] = request.POST["txtfullname"]
            return redirect("ownerD")
        else:
            return render(request, "myapp/signup&login.html", {'res': "INVALID CREDENTIALS!!"})
    return render(request, "myapp/signup&login.html")


def ownerD(request):
    if request.session.has_key("ownerD_key"):
        r = ownersignup.objects.filter(fullname=request.session["ownerD_key"])
        return render(request, "myapp/owner_dashboard.html", {'sesskey': request.session["ownerD_key"], 'res1': r})
    return render(request, "myapp/owner_dashboard.html")


def ownerrecords(request):
    s = ownersignup.objects.all()
    return render(request, "myapp/viewOWrec.html", {'res1': s})


def owner_add_room(request):
    if request.session.has_key("ownerD_key"):
        if request.method == 'POST':
            file = request.FILES["txtfile"]
            obj = FileSystemStorage()
            f = obj.save(file.name, file)
            url = obj.url(f)
            add_room = view_room_db(location=request.POST["txtloc"], category=request.POST["txtcat"],
                                    description=request.POST["txtarea"], sub_category=request.POST["txtsubcat"],
                                    file_upload=url, room_price=request.POST["txtprice"],
                                    room_facility=request.POST["txtfac"])
            add_room.save()
            return render(request, "myapp/view_room_owner.html")
        r = ownersignup.objects.filter(fullname=request.session["ownerD_key"])
        return render(request, "myapp/owner_add_room.html", {'sesskey': request.session["ownerD_key"], 'res1': r})
    return render(request, "myapp/owner_add_room.html")


def view_booking_owner(request):
    if request.session.has_key("ownerD_key"):
        r = ownersignup.objects.filter(fullname=request.session["ownerD_key"])
        return render(request, "myapp/view_booking_owner.html", {'sesskey': request.session["ownerD_key"], 'res1': r})
    return render(request, "myapp/view_booking_owner.html")


def view_room_owner(request):
    if request.session.has_key("ownerD_key"):
        r = ownersignup.objects.filter(fullname=request.session["ownerD_key"])
        return render(request, "myapp/view_room_owner.html", {'sesskey': request.session["ownerD_key"], 'res1': r})
    return render(request, "myapp/view_room_owner.html")


def owner_view_room(request):
    if request.session.has_key("ownerD_key"):
        if owner_login(request):
            view = view_room_db.objects.all()
            return render(request, "myapp/view_room_owner.html",
                          {'sesskey': request.session["ownerD_key"], 'view_room_res': view})
    return render(request, "myapp/view_room_owner.html")


def search_property(request):
    if request.method == 'POST':
        search = view_room_db.objects.filter(location=request.POST["loc"], category=request.POST["cat_name"])
        if search:
            return render(request, "myapp/user_dash_board_view.html", {'show_details': search})
        else:
            return HttpResponse("No Property Found at that location!!")
    return render(request, "myapp/user_dash_board_view.html")


def test(request):
    if request.session.has_key("skey"):
        r = UserDetailss.objects.filter(nname=request.session["skey"])
        return render(request, "myapp/test.html", {'user_sesskey': request.session["skey"], 'res1': r
                                                   })
    return render(request, "myapp/test.html")


def add_room_cat(request):
    res = category.objects.all()
    return render(request, "myapp/owner_add_room.html", {'cat_res': res})


def add_room_subcat(request):
    res = sub_cat.objects.filter(cat_id=int(request.GET["q"]))
    return render(request, "myapp/add_room_subcat.html", {'sub_res': res})


def owner_logout(request):
    del request.session["ownerD_key"]
    return redirect("home")


def al(request):
    if request.method == 'POST':
        res = admindetails.objects.filter(email=request.POST["txtaemail"], password=request.POST["txtapass"])
        if res:
            if res:
                request.session["admin_session_key"] = request.POST["txtaemail"]
                return redirect("admin_dashboard")
        else:
            return render(request, "myapp/admin_login.html", {'res': "INVALID CREDENTIALS!!"})

    return render(request, "myapp/admin_login.html")


def admin_dashboard(request):
    if request.session.has_key("admin_session_key"):
        res = admindetails.objects.filter(email=request.session["admin_session_key"])
        return render(request, "myapp/admindash.html",
                      {'admin_key': request.session["admin_session_key"], 'admin_res': res})
    return render(request, "myapp/admin_login.html")


def admin_logout(request):
    del request.session["admin_session_key"]
    return redirect("al")


def cat(request):
    res = category.objects.all()
    return render(request, "myapp/indexb.html", {'cat_res': res})


def subcat(request):
    res = sub_cat.objects.filter(cat_id=int(request.GET["q"]))
    return render(request, "myapp/sub_cate.html", {'sub_res': res})


'''def add_room_owner(request):
    if request.method == 'POST':
        add_room = view_room_db(location=request.POST["txtloc"], category=request.POST["txtcat"],
                                sub_category=request.POST["txtsub"], description=request.POST["txtarea"],
                                fileup=request.POST["txtfile"], room_price=int(request.POST["txtprice"]),
                                room_facility=request.POST["txtfac"])
        add_room.save()
        return render(request, "myapp/owner_add_room.html", {'details': "Details Inserted Successfully!!"})'''


def delete_owner_add_room(request):
    if request.method == "POST":
        s1 = view_room_db.objects.get(pk=request.POST["txtid"])
        s1.delete()
        return redirect("owner_view_room")
    else:
        s = view_room_db.objects.get(pk=request.GET["q"])
        return render(request, "myapp/delete_owner_room.html", {"res": s})
