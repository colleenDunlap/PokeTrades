from django.urls import path

from . import views

urlpatterns = [
        path("", views.index, name = "index"),
        path("team/<int:team_id>/",views.team_details, name = "team_details"),
        path("trade/submit", views.SubmitTrade.as_view(), name = "SubmitTrade"),
        ]


