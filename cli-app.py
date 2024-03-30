import typer
from typer import Typer
import rich

app = Typer()

__version__ = '0.000.01'

def version(arg):
    if arg:
        rich.print(f'CLI demonstração Versão:[b][green] {__version__}[/]')
        raise typer.Exit(code = 0)


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


@app.command()
def comando_a():
    ...


@app.command()
def comando_b():
    ...


app()