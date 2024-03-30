import typer
import rich

__version__ = '0.000.01'

def version(arg):
    if arg:
        rich.print(f'CLI demonstração Versão:[b][green] {__version__}[/]')
        raise typer.Exit(code = 0)


def print_name(
    name:str = typer.Argument(),
    sobrenome:str= typer.Argument('Pythonico!'),
    version: bool = typer.Option(
        False,
        '--version','-v',
        callback=version,
        is_flag=True,
        is_eager=True,
    )
    ):
    rich.print(f'Olá [b][blue]{name} {sobrenome}[/]')


typer.run(print_name)