from django import forms
from .models import Details, Course


class DateInput(forms.DateInput):
    input_type = 'date'


class DetailsForm(forms.ModelForm):
    genders = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
    gender = forms.ChoiceField(choices=genders, widget=forms.RadioSelect)
    purpose = (('Enquiry', 'Enquiry'), ('Place Order', 'Place Order'), ('Return', 'Return'))
    purposes = forms.CharField(label='Purpose', widget=forms.Select(choices=purpose))
    date_of_birth = forms.DateField(widget=DateInput)

    class Meta:
        model = Details
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('course')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('course')
