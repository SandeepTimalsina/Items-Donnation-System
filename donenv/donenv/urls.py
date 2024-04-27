"""donvol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("gallery/", views.gallery, name="gallery"),
    path("login-admin/", views.login_admin, name="login_admin"),
    path("login-donor/", views.login_donor, name="login_donor"),
    path("login-volunteer/", views.login_volunteer, name="login_volunteer"),
    path("signup-donor/", views.signup_donor, name="signup_donor"),
    path("signup-volunteer/", views.signup_volunteer, name="signup_volunteer"),
    path("index-admin/", views.index_admin, name="index_admin"),
    # admin dashboard
    path("pending-donation/", views.pending_donation, name="pending_donation"),
    path("accepted-donation/", views.accepted_donation, name="accepted_donation"),
    path("rejected-donation/", views.rejected_donation, name="rejected_donation"),
    path(
        "volunteerallocated-donation/",
        views.volunteerallocated_donation,
        name="volunteerallocated_donation",
    ),
    path("donationrec-admin/", views.donationrec_admin, name="donationrec_admin"),
    path(
        "donationnotrec-admin/", views.donationnotrec_admin, name="donationnotrec_admin"
    ),
    path(
        "donationdelivered-admin/",
        views.donationdelivered_admin,
        name="donationdelivered_admin",
    ),
    path("all-donations/", views.all_donations, name="all_donations"),
    path("manage-donor/", views.manage_donor, name="manage_donor"),
    path("new-volunteer/", views.new_volunteer, name="new_volunteer"),
    path("accepted-volunteer/", views.accepted_volunteer, name="accepted_volunteer"),
    path("rejected-volunteer/", views.rejected_volunteer, name="rejected_volunteer"),
    path("all-volunteer/", views.all_volunteer, name="all_volunteer"),
    path("add-area/", views.add_area, name="add_area"),
    path("edit-area/<int:pid>", views.edit_area, name="edit_area"),
    path("manage-area/", views.manage_area, name="manage_area"),
    path("changepwd-admin/", views.changepwd_admin, name="changepwd_admin"),
    path("logout/", views.logout, name="logout"),
    # view details
    path(
        "accepted-donationdetail/<int:pid>",
        views.accepted_donationdetail,
        name="accepted_donationdetail",
    ),
    path(
        "view-volunteerdetail/<int:pid>",
        views.view_volunteerdetail,
        name="view_volunteerdetail",
    ),
    path("view-donordetail/<int:pid>", views.view_donordetail, name="view_donordetail"),
    path(
        "view-donationdetail/<int:pid>",
        views.view_donationdetail,
        name="view_donationdetail",
    ),
    # donar dashboard
    path("index-donor/", views.index_donor, name="index_donor"),
    path("donate-now/", views.donate_now, name="donate_now"),
    path("donation-history/", views.donation_history, name="donation_history"),
    path("profile-donor/", views.profile_donor, name="profile_donor"),
    path("changepwd-donor/", views.changepwd_donor, name="changepwd_donor"),
    # volunteer dashboard
    path("index-volunteer/", views.index_volunteer, name="index_volunteer"),
    path("collection-req/", views.collection_req, name="collection_req"),
    path(
        "donationrec-volunteer/",
        views.donationrec_volunteer,
        name="donationrec_volunteer",
    ),
    path(
        "donationnotrec-volunteer/",
        views.donationnotrec_volunteer,
        name="donationnotrec_volunteer",
    ),
    path(
        "donationdelivered-volunteer/",
        views.donationdelivered_volunteer,
        name="donationdelivered_volunteer",
    ),
    path("profile-volunteer/", views.profile_volunteer, name="profile_volunteer"),
    path("changepwd-volunteer/", views.changepwd_volunteer, name="changepwd_volunteer"),
    # vew details
    path(
        "donationdetail-donor/<int:pid>",
        views.donationdetail_donor,
        name="donationdetail_donor",
    ),
    path(
        "donationrec-detail/<int:pid>",
        views.donationrec_detail,
        name="donationrec_detail",
    ),
    path(
        "donationcollection-detail/<int:pid>",
        views.donationcollection_detail,
        name="donationcollection_detail",
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
