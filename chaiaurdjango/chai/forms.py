from django import forms
from .models import ChaiVariety


class ChaiVarietyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(
        queryset=ChaiVariety.objects.order_by("name"),
        label="Select Chai Variety",
        required=False,
        empty_label="All Chai Variety",
        widget=forms.Select(
            attrs={
                "class": (
                    "w-full rounded-md bg-slate-900 border border-slate-700 "
                    "text-slate-200 px-4 py-2 text-sm "
                    "focus:outline-none focus:ring-2 focus:ring-sky-500 "
                    "focus:border-sky-500"
                )
            }
        )
    )
