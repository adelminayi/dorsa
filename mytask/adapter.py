import os
import random

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site

from allauth.account.adapter import DefaultAccountAdapter


class MyAdapter(DefaultAccountAdapter):
    def send_confirmation_mail(self, request, emailconfirmation, signup):
        current_site = get_current_site(request)
        ctx = {
            "user": emailconfirmation.email_address.user,
            "current_site": current_site,
        }
        if signup:
            email_template = "account/email/email_confirmation_signup"
        else:
            email_template = "account/email/email_confirmation_message"
        self.send_mail(email_template, emailconfirmation.email_address.email, ctx)