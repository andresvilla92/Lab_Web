# coding=utf-8
from django import forms
from django.forms import ModelForm

from .models import *


TIPOS_CUENTA = (
    ('Cuenta de cheques', 'Cuenta de cheques'),
    ('Cuenta de ahorros', 'Cuenta de ahorros'),
    ('Certificado de depósito', 'Certificado de depósito'),
    ('Cuenta de mercado monetario', 'Cuenta de mercado monetario'),
    ('Cuentas de jubilación individual ', 'Cuentas de jubilación individual'),
)


class FormaCuenta(ModelForm):
    usuario = forms.CharField(widget=forms.HiddenInput(), required=True)
    banco = forms.ModelChoiceField(queryset=Banco.objects.all())
    numero_cuenta = forms.CharField(label='numero_cuenta')
    clabe = forms.CharField(label='clabe', max_length=18, help_text='Clave Bancaria Estandarizada (18 numeros).')  # maximo 18
    tipo_cuenta = forms.ChoiceField(choices=TIPOS_CUENTA, label="Tipo de cuenta", initial='', widget=forms.Select(), required=True)
    monto = forms.IntegerField(label='Monto en la cuenta')
    t_tarjeta_debito = forms.BooleanField(label='Tiene tarjet de debito?',initial=False, required=False)
    num_tarjeta = forms.CharField(label="Numero de tarjeta", help_text="Numero de la tarjeta de credito")
    tasa_inflacion = forms.FloatField(label="Tasa de Inflacion")
    plazo = forms.IntegerField(label="Plazo de inversion")

    class Meta:
        model = Cuenta
        fields = ['banco', 'numero_cuenta', 'clabe', 'tipo_cuenta',
                  'monto', 't_tarjeta_debito', 'num_tarjeta', 'tasa_inflacion',
                  'plazo']
        exclude = ('usuario',)


