from django import forms
from django.contrib.auth.forms import UserCreationForm
from userapp.models import (
    Consumer,
    Provider,
    User,
    ChargingStation,
    Support,
    UserRecord,
    ChargePooler,
    User_convert_specs,
    DrivingEnv,
)


class UserSignUpForm(UserCreationForm):
    class Meta:
        fields = ["username", "email", "password1", "password2"]
        model = User


class ConsumerSignUpForm(forms.ModelForm):
    class Meta:
        fields = ["have_vehicle", "city"]
        model = Consumer
        labels = {"have_vehicle": "Do you have an EV?", "city": "City"}


class ProviderSignUpForm(forms.ModelForm):
    class Meta:
        fields = ["business_name", "image"]
        model = Provider
        labels = {"business_name": "Business Name", "image": "Logo"}


class UserUpdateForm(forms.ModelForm):
    class Meta:
        fields = ["username", "email"]
        model = User


class ChargingStationForm(forms.ModelForm):
    opening_time = widget = forms.TimeInput(format="%H:%M")
    closing_time = widget = forms.TimeInput(format="%H:%M")

    class Meta:
        fields = [
            "name",
            "lat",
            "lng",
            "no_of_ports",
            "fast_dc",
            "slow_ac",
            "price_kwh",
            "restroom",
            "cctv",
            "opening_time",
            "closing_time",
            "image",
        ]
        model = ChargingStation
        


class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ["subject", "description"]
        labels = {"subject": "Issue Title", "description": "Issue Description"}

        widgets = {
            "description": forms.Textarea(
                attrs={"placeholder": "Describe your issue here(max 200 words)"}
            )
        }


class SurveyForm(forms.ModelForm):
    class Meta:
        model = UserRecord
        fields = ["start_time", "stop_time", "vehicle", "port_type", "lat", "lng"]


class CharpoolerForm(forms.ModelForm):
    class Meta:
        model = ChargePooler
        fields = ["city", "local_area", "ph_no", "cost", "normal_port", "fast_port"]


class ConvertForm(forms.ModelForm):
    class Meta:
        model = User_convert_specs
        fields = ["fully_electric", "vehicle_type", "price_range", "dtd_sercive"]
        widgets = {
            "fully_electric": forms.HiddenInput(),
            "vehicle_type": forms.HiddenInput(),
            "price_range": forms.HiddenInput(),
            "dtd_sercive": forms.HiddenInput(),
        }


class DrivingEnv(forms.ModelForm):
    class Meta:
        model = DrivingEnv
        fields = ["consumption", "road_type", "consumption_per_100", "ac", "avg_speed"]
