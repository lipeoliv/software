# Software Para Gerenciamento de Barbearia 

## Como usar

> Descompacte as fontes ou clone o repositório. Depois de obter o código, abra um terminal e navegue até o diretório de trabalho, com o código-fonte do produto.

```bash
$ # Obter o código
$ git clone https://github.com/creativetimofficial/soft-ui-dashboard-django.git
$ cd soft-ui-dashboard-django
$
$ # Instalação dos módulos do Virtualenv (sistemas baseados em Unix)
$ virtualenv env
$ source env/bin/activate
$
$ # Instalação dos módulos do Virtualenv (sistemas baseados em Windows)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Instalar módulos - Armazenamento SQLite
$ pip3 install -r requirements.txt
$
$ # Criar tabelas
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Iniciar a aplicação (modo de desenvolvimento)
$ python manage.py runserver # porta padrão 8000
$
$ # Inicie o aplicativo - porta personalizada
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Acesse o aplicativo da web no navegador: http://127.0.0.1:8000/
```

> Nota: Para usar o aplicativo, acesse a página de registro e crie um novo usuário. Após autenticação, o aplicativo desbloqueará as páginas privadas.

<br />

## Estrutura da Base de Código

O projeto é codificado usando uma estrutura simples e intuitiva apresentada abaixo:

```bash
<RAIZ DO PROJETO>
   |
   |-- core/                               # Implementa a configuração do aplicativo
   |    |-- settings.py                    # Define as configurações globais
   |    |-- wsgi.py                        # Inicia o aplicativo em produção
   |    |-- urls.py                        # Define os URLs servidos por todos os aplicativos/nós
   |
   |-- apps/
   |    |
   |    |-- home/                          # Um aplicativo simples que serve arquivos HTML
   |    |    |-- views.py                  # Serve páginas HTML para usuários autenticados
   |    |    |-- urls.py                   # Define rotas muito simples  
   |    |
   |    |-- authentication/                # Lida com rotas de autenticação (login e registro)
   |    |    |-- urls.py                   # Define rotas de autenticação  
   |    |    |-- views.py                  # Lida com login e registro  
   |    |    |-- forms.py                  # Define formulários de autenticação (login e registro) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, imagens>        # Arquivos CSS, arquivos Javascript
   |    |
   |    |-- templates/                     # Templates usados para renderizar páginas
   |         |-- includes/                 # Fragmentos e componentes HTML
   |         |    |-- navigation.html      # Componente de menu superior
   |         |    |-- sidebar.html         # Componente de barra lateral
   |         |    |-- footer.html          # Rodapé do aplicativo
   |         |    |-- scripts.html         # Scripts comuns a todas as páginas
   |         |
   |         |-- layouts/                   # Páginas mestre
   |         |    |-- base-fullscreen.html  # Usado por páginas de autenticação
   |         |    |-- base.html             # Usado por páginas comuns
   |         |
   |         |-- accounts/                  # Páginas de autenticação
   |         |    |-- login.html            # Página de login
   |         |    |-- register.html         # Página de registro
   |         |
   |         |-- home/                      # Páginas do Kit de UI
   |              |-- index.html            # Página inicial
   |              |-- 404-page.html         # Página 404
   |              |-- *.html                # Todas as outras páginas
   |
   |-- requirements.txt                     # Módulos de desenvolvimento - Armazenamento SQLite
   |
   |-- .env                                 # Injeta configuração via ambiente
   |-- manage.py                            # Inicia o aplicativo - Script padrão do Django
   |
   |-- ************************************************************************
```

<br />

> O fluxo de inicialização

- Django bootstrapper `manage.py` usa `core/settings.py` como o arquivo de configuração principal
- `core/settings.py` carrega a mágica do aplicativo do arquivo `.env`
- Redirecione os usuários convidados para a página de login
- Desbloqueie as páginas servidas pelo nó *app* para usuários autenticados

<br />

## Recompilar CSS

Para recompilar arquivos SCSS, siga esta configuração:

<br />

**Etapa #1** - Instalar ferramentas

- [NodeJS](https://nodejs.org/en/) 12.x ou superior
- [Gulp](https://gulpjs.com/) - globalmente
    - `npm install -g gulp-cli`
- [Fio](https://yarnpkg.com/) (opcional)

<br />

**Etapa #2** - Altere o diretório de trabalho para a pasta `assets`

```bash
$ cd apps/static/assets
```

<br />

**Etapa #3** - Instale os módulos (isso criará um diretório `node_modules` clássico)

```bash
instalação de $npm
// OU
$ fios
```

<br />

**Etapa #4** - Editar e recompilar arquivos SCSS

```bash
$ gulp scss
```

O arquivo gerado é salvo no diretório `static/assets/css`.

<br />
