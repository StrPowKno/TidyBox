import click
from tidybox.organizer import scan, clean
from tidybox.undo import undo_last
from tidybox.watcher import watch as watch_dir

@click.group()
def cli():
    """TidyBox — A smart file organizer."""
    pass

@cli.command()
@click.argument("directory")
def scan(directory):
    """Preview files grouped by type."""
    from tidybox.organizer import scan as do_scan
    do_scan(directory)

@cli.command()
@click.argument("directory")
@click.option("--dry-run", is_flag=True, help="Preview without moving anything.")
@click.option("--recursive", is_flag=True, help="Include subdirectories.")
def clean(directory, dry_run, recursive):
    """Organize files into folders."""
    from tidybox.organizer import clean as do_clean
    do_clean(directory, dry_run=dry_run, recursive=recursive)

@cli.command()
def undo():
    """Undo the last organization."""
    undo_last()

@cli.command()
@click.argument("directory")
def watch(directory):
    """Watch a directory and auto-organize."""
    watch_dir(directory)