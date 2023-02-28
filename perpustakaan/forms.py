from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku


class FormBuku(ModelForm):
    class Meta:
        model = Buku
        # Memilihh field yang akan di tampilkan
        # fields = ['judul', 'penulis', 'kelompok_id']

        # Menampilkan semua field
        fields = '__all__'

        # Mengecualikan yang di tampilkan ke output
        # exclude = ['penerbit']

        widgets = {
            'judul': forms.TextInput({'class': 'form-control'}),
            'penulis': forms.TextInput({'class': 'form-control'}),
            'penerbit': forms.TextInput({'class': 'form-control'}),
            'jumlah': forms.NumberInput({'class': 'form-control'}),
            'kelompok_id': forms.Select({'class': 'form-control'}),

        }
