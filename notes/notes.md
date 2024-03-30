# CLI (command line interface)

É um artifício que nos permite criar linhas de comando para utilizar em nossos projetos. Ao seguir uma documentação e boas práticas, podemos criar uma interface no terminal poderosa para ser utilizada


## Alguns conceitos

### Comando
Geralmente é o nome da aplicação e uma das maneiras que você pode chamar ele na aplicação, ex:

- git
- node
- pip

### Subcomando
São complementos ao seu comando, podendo definir quais ações serão feitas pelo seu terminal, ex:

- git <mark style="background: #00ced1">commit</mark>
- poetry <mark style="background: #00ced1">add</mark>
- pip <mark style="background: #00ced1">install</mark>

### Argumentos
São as especificações e complementos a um subcomando, é o argumento que será utilizado dentro do sub comando, ex:

- git switch <mark style="background: #00ced1">master</mark>
- pip install <mark style="background: #00ced1">typer</mark>
- poetry remove <mark style="background: #00ced1">pandas</mark>

### Flags
Flags são argumentos opcionais que incorporam seu comando, ex:

- pip install <mark style="background: #00ced1">--upgrade</mark> pip
- git push <mark style="background: #00ced1">-f</mark>

### Redirecionamento (pipes)
Eles pegam o retorno de um comando anterior e com base nessa resposta redirecionam para um outro comando e criando uma composição entre elas, ex:

- cat [arquivo] <mark style="background: #00ced1">|</mark> grep teste
- pip freeze <mark style="background: #00ced1">></mark> requirements.txt

<small><strong>Nota:</strong>Geralmente o maior ">" escreve em um arquivo</small>

### Condutores
especificar

- stdin: Entrada padrão
- stdout: Saída padrão
- stderr: Saída de erro

## Opções que são boas práticas em um CLI
- Flags de ajuda
- - git <mark style="background: #00ced1">-h</mark>
- - git <mark style="background: #00ced1" >-help</mark>
- - git <mark style="background: #00ced1">-version</mark>

- Manuais no terminal
- - <mark style="background: #00ced1">info</mark> http
- - <mark style="background: #00ced1">man</mark> http 

- Obtendo mais informações
- - pipx upgrade-all <mark style="background: #00ced1">--verbose</mark>
- - pytest <mark style="background: #00ced1">-vvv</mark> [verbose x4]


# Typer

## Run()
O run é o método que chama o cli e dá comportamentos a linha de comando

nota: o typer usa os parametros como argumentos e sempre quando tiver um parametro default, ex: color=blue, eçe se torna uma flag, sendo necessário escrever --color blue [MELHORAR] 

Nota: O typer faz casting dos parâmetros, isto é, pode converter um tipo em outro assim que possível, ex:

```python
stdin: python cli.py 1

my_function(name):
    print(type(name))
    ...

typer.run()
stdout: <class: 'str'>
```

## Argument()


- Argument(...): Requerido
- Argument(valueHere) = Argumento com valor default, dessa maneira, valores defult não são mais flags!
- Argument(uma_func): Algo que gera o argumento padrão
- Argument(..., help='Mensagem de ajuda')
- Argument(..., metavar='customização de exibição')
- Argument(..., envvar='VARIAVEL_DE_AMBIENTE')


```python
import typer
import rich

def print_name(
    name:str = typer.Argument(),
    sobrenome:str= typer.Argument('Pythonico!')
    ):
    rich.print(f'Olá [b][blue]{name} {sobrenome}[/]')


typer.run(print_name)
```

Saída:

![help argumento default](images_md/help%20argumento%20default.png)


## Opitons()

Para passar flags para o CLI podemos utilizar o objeto Options, fornecendo vários parâmetros desde ser passado no Prompt até mesmo se será visível ao digitar ou não.

Além disso, podemos passar mais de uma forma de chamar uma flag, ex:

```python
    ...
    version: bool = Option(
        False,
        '--version', '-v', '--versao',
        ...
    )
    
```

## Criando Callbacks

Os Callbacks são maneiras que podemos direcionar um argumento ou flag para a execução de outras funções, por exemplo a versão do CLI:

```python
__version__ = '0.000.01'

def version(arg):
    if arg:
        rich.print(f'CLI demonstração Versão:[b][green] {__version__}[/]')
        raise typer.Exit(code = 0)


def print_name(
    ...
    version: bool = typer.Option(
        False,
        '--version','-v',
        callback=version,
        is_flag=True,
        is_eager=True,
    )
    ):
    ...
```

Notas

- O is_eager é um parâmetro utilizado para que essa linha seja executada primeiro, que nesse caso chama o callback;
- Ou sejam, o callback da version sempre acontece mas como o parâmetro version é False por default, ele não executa;
- Por fim, após executar a flag, queremos que o usuário saia do CLI, que o código termine, para isso utilizamos o `typer.Exist(code = 0)` indicando que o fim do código
- <strong>IMPORTANTE:</strong> Devemos levantar uma exceção com `raise` 

## Subcomandos

Para criar subcomandos utlizando o typer, vamos usar decoradores e uma premissa semelhante ao flask ou fastAPI:

```python
from typer import Typer

app = Typer() #instância nosso app

@app.command() #decorador que incorpora o subcomando ao app
def comando_a(): #função do subcomando
    ...


@app.command()
def comando_b():
    ...


app() #chamada do app
```

Notas:
- Ao fazer um comando, ele não necessariamente vai ter o mesmo nome da função;
- No caso de usar o underline `_` o subcomando no CLI vai converter para traçõ `-` ex: `comand-a`
- Podemos também nomear o comando pelo decorador, dessa forma ele não terá o nome da função abaixo, ex:

```python

@app.command(name='sub-command')
def comando_b():
    ...

#chamando o CLI: python <name-cli>.py sub-command
```

- Também podemos passar o help específico do subcomando, basta passar um `help=` como parâmetro dentro do decorador 

```python

@app.command(name='sub-command',help='Cria um arquivo ...')
def comando_b():
    ...

#chamando o CLI: python <name-cli>.py sub-command
```

### Boilerplate para o app

Ao utilizar um `app`, temos um problema ao executar o cli sem nenhum subcomando específico, ele não especifica ou informa para o usuário o que pode ser feito. Apenas retorna uma mensagem de `Missing command.` mesmo que existem subcomando contidos no app. Ex:

![app sem especificar o stdout](images_md/app%20sem%20info%20de%20comandos.png)

Além disso, outras informações do CLI ficam restritas, como por exemplo a sua versão.

Para que possamos contornar este problema, e criar essas informações, será necessário gerar uma função callback para o próprio `app` de forma que seja mostrada apenas quando o comando for iniciado sozinho e também ganhe as flags de `--version`.

Tendo isso em mente, é necessário utilizar este Boilerplate, para que nosso CLI receba esse comportamento desejado:


```python
import typer
from typer import Typer
import rich

app = Typer()

__version__ = '00.000.01'

def version(arg):
	if arg:
        	rich.print(f'CLI demonstração Versão:[b][green] {__version__}[/]')
		raise Exit(code=0)


@app.callback(invoke_without_command=True)
def typer_callback(
	ctx: typer.Context,
	version: bool = typer.Option( False,
				'--version','-v',
				is_eager=True,
				is_flag=True,
				callback=version)
):
	if ctx.invoked_subcommand:
		return
	rich.print('Use um dos comandos! `comando_a` ou `comando_b`')

app()
```