import typer
from pathlib import Path

app = typer.Typer()


BUTTON_CODE = """\
import React from 'react';

type ButtonProps = {
  label: string;
  onClick?: () => void;
};

export function Button({ label, onClick }: ButtonProps) {
  return <button onClick={onClick}>{label}</button>;
}
"""


@app.command()
def next_create(path: Path = typer.Argument(..., help="project folder path")):
    path.mkdir(parents=True, exist_ok=True)
    print("hi")


@app.command()
def version():
    """Show version information."""
    typer.echo("seta v0.1.0")


@app.command()
def notify():
    print("created")


def main():
    app()


if __name__ == "__main__":
    main()


# pip uninstall foldar -y
# pip install -e .
