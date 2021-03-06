from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={'required': '이메일을 입력해주세요.'}, max_length=64, label='이메일')
    name = forms.CharField(
        error_messages={'required': '이름을 입력해주세요.'}, max_length=32, label='이름')
    password = forms.CharField(
        error_messages={'required': '비밀번호를 입력해주세요.'}, widget=forms.PasswordInput, label='비밀번호')
    re_password = forms.CharField(
        error_messages={'required': '비밀번호를 입력해주세요.'}, widget=forms.PasswordInput, label='비밀번호 확인')
