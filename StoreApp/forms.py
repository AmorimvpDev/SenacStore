from django import forms
from StoreApp.models import Cliente

# criando um formulario baseado num model
class CadastroForm(forms.ModelForm):
                # ele herda isso
    class Meta:
        model = Cliente # model que eu quero q ele monte um formulario
        fields = '__all__' #Aqui puxa todos os campos em que vou cadastrar que tem no models.py, nome, cpf, etc
        
        #campos
        widgets = {
            'cpf': forms.TextInput(attrs={'class':'cpf'}),
            'cep': forms.TextInput(attrs={'class':'cep'}),
            'data_nascimento': forms.TextInput(attrs={'class':'date'}) #quero q o campo data de nascimento receba uma classe = date,
                                                                       # assim posso manipular de diversas maneiras
        }
    
class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    telefone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'cel_phone_with_ddd'}))
    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)
