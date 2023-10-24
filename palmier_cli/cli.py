import click
import os 
import subprocess

@click.group()
def cli():
    "Palmier CLI - a web framwork for LLM Applications"
    pass
@cli.command()
@click.argument('projectname')
def startproject(projectname):
   '''
   Command used for creating projects with structure 
   '''
   created_text='''
        cd {projectname}
        palmier-cli run
    '''
   click.echo(f"Finished creating {projectname}")
   click.echo(created_text.format(projectname=projectname))

if __name__ == '__main__':
    cli()