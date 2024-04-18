from django.shortcuts import render
from StoreApp.models import Departamento, Produto
from StoreApp.forms import CadastroForm, ContatoForm
from django.core.mail import send_mail

# Create your views here.
def index(request):
    produtos_destaque = Produto.objects.filter(destaque = True)

    context = {
        'produtos' : produtos_destaque
    }

    return render(request, 'index.html', context)

def produto_lista(request):
    produtos_lista = Produto.objects.all()

    context = {
        'produtos' : produtos_lista,
        'titulo' : 'Todos Produtos'

    }
    return render(request, 'produtos.html', context)

def produto_lista_por_departamento(request, id):
                                        #la no models, foreingkey, puxa o nome do lugar mais o seu id
    produtos_lista = Produto.objects.filter(departamento_id = id)
    departamento = Departamento.objects.get(id = id)

    context = {
        'produtos' : produtos_lista,
        'titulo' : departamento.nome
    }

    return render(request, 'produtos.html', context)

def produto_detalhe(request, id):
    produto = Produto.objects.get(id = id)                                                #: significa os 4 primeiros 
    produtos_relacionados = Produto.objects.filter(departamento_id = produto.departamento).exclude(id = id)[:4]
    #pega todos produto do departamento q to definindo

    context = {
        'produto' : produto,
        'produtos_relacionados' : produtos_relacionados
    }

    return render(request, 'produto_detalhes.html', context)

def sobre_empresa(request):


    return render(request, 'sobre_empresa.html')

def cadastro(request):

    #Armazenar mensagem de Correct ou Error
    mensagem = '' 

    #Se o formulário receber algum dado:
    if request.method == 'POST':
        formulario = CadastroForm(request.POST) # montando o formulario com os dados

        #Fazendo uma verificação se ta tudo batendo
        if formulario.is_valid():
            formulario.save() 
            formulario = CadastroForm() # deixar na tela o cadastro vazio
                            #e exibe a mensagem abaixo:
            mensagem = 'Cliente cadastrado com sucesso.'
        else:
            mensagem = 'Verifique os erros abaixo: '


    #Se n recebi nenhum dado e entrei pelo menu, o formulario deve vir vazio.
    else:
        formulario = CadastroForm()

        
    context = {
        'formulario_cadastro' : formulario,
        'mensagem' : mensagem
    }   
    return render(request, 'cadastro.html', context)

def contato(request):
    mensagem = ''

    if request.method == "POST":
        #recuperando os dados do formulário
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        assunto = request.POST['assunto']
        mensagem = request.POST['mensagem']
        remetente = request.POST['email']
        destinatario = ['arthuramorimn1ofc@gmail.com', 'murilobraz22@gmail.com']
        corpo = f"Nome: {nome} \nTelefone: {telefone}  \nMensagem: {mensagem}"
    
        #try == tenta executar isso, caso der erro, cai no except.
        try:
            #fazer o envio do e-mail
            send_mail(assunto, corpo, remetente, destinatario)
            mensagem = 'Mensagem enviada com sucesso :)'
        except:
            mensagem = 'Erro ao enviar a Mensagem :('
    formulario = ContatoForm()
    context = {
        'mensagem' : mensagem,
        'formulario_contato' : formulario

    }
    return render(request, 'contato.html', context)