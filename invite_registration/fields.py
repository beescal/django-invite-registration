# -*- coding: utf-8 -*-
'''
Created on Mar 20, 2012

@author: Mourad Mourafiq

@copyright: Copyright © 2012

other contributers: 
'''
from django import forms
from django.utils.translation import ugettext_lazy as _
from invite_registration.models import Invitation


class InvitationCodeField(forms.CharField):
    """Invitation code field"""

    def validate(self, value):
        """Validate against invitation code table"""
        super(InvitationCodeField, self).validate(value)

        try:
            invitation = Invitation.objects.get(code=value)
        except Invitation.DoesNotExist:
            raise forms.ValidationError(_("Ooops the invitation code is invalid."))