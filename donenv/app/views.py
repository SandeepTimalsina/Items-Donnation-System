from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request, "index.html")


def gallery(request):
    return render(request, "gallery.html")


def login_admin(request):
    return render(request, "login-admin.html")


def login_donor(request):
    return render(request, "login-donor.html")


def login_volunteer(request):
    return render(request, "login-volunteer.html")


def signup_donor(request):
    return render(request, "signup_donor.html")


def signup_volunteer(request):
    return render(request, "signup_volunteer.html")


def index_admin(request):
    return render(request, "index-admin.html")


# admin dashboard
def pending_donation(request):
    return render(request, "pending-donation.html")


def accepted_donation(request):
    return render(request, "accepted-donation.html")


def rejected_donation(request):
    return render(request, "rejected-donation.html")


def volunteerallocated_donation(request):
    return render(request, "volunteerallocated-donation.html")


def donationrec_admin(request):
    return render(request, "donationrec-admin.html")


def donationnotrec_admin(request):
    return render(request, "donationnotrec-admin.html")


def donationdelivered_admin(request):
    return render(request, "donationdelivered-admin.html")


def all_donations(request):
    return render(request, "all-donations.html")


def manage_donor(request):
    return render(request, "manage-donor.html")


def new_volunteer(request):
    return render(request, "new-volunteer.html")


def accepted_volunteer(request):
    return render(request, "accepted-volunteer.html")


def rejected_volunteer(request):
    return render(request, "rejected-volunteer.html")


def all_volunteer(request):
    return render(request, "all-volunteer.html")


def add_area(request):
    return render(request, "add-area.html")


def edit_area(request, pid):
    return render(request, "edit-area.html")


def manage_area(request):
    return render(request, "manage-area.html")


def changepwd_admin(request):
    return render(request, "changepwd-admin.html")


def logout(request):
    return redirect("index")


# admin view details
def accepted_donationdetail(request, pid):
    return render(request, "accepted-donationdetail.html")


def view_volunteerdetail(request, pid):
    return render(request, "view-volunteerdetail.html")


def view_donordetail(request, pid):
    return render(request, "view-donordetail.html")


def view_donationdetail(request, pid):
    return render(request, "view-donationdetail.html")


# donor dashboard
def index_donor(request):
    return render(request, "index-donor.html")


def donate_now(request):
    return render(request, "donate-now.html")


def donation_history(request):
    return render(request, "donation-history.html")


def profile_donor(request):
    return render(request, "profile-donor.html")


def changepwd_donor(request):
    return render(request, "changepwd-donor.html")


# volunteer dashboard
def index_volunteer(request):
    return render(request, "index-volunteer.html")


def collection_req(request):
    return render(request, "collection-req.html")


def donationrec_volunteer(request):
    return render(request, "donationrec-volunteer.html")


def donationnotrec_volunteer(request):
    return render(request, "donationnotrec-volunteer.html")


def donationdelivered_volunteer(request):
    return render(request, "donationdelivered-volunteer.html")


def profile_volunteer(request):
    return render(request, "profile-volunteer.html")


def changepwd_volunteer(request):
    return render(request, "changepwd-volunteer.html")


# view details
def donationdetail_donor(request, pid):
    return render(request, "donationdetail-donor.html")


def donationcollection_detail(request, pid):
    return render(request, "donationcollection-detail.html")


def donationrec_detail(request, pid):
    return render(request, "donationrec-detail.html")
