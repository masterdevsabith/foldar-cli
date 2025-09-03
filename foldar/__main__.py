from .code_templates import (
    NAVBAR_CODE,
    BUTTON_CODE,
    THEME_PROVIDER,
    THEME_SWITCHER,
    TYPES_CODE,
    HERO_CODE,
    APP_PAGE_CODE,
)
import typer
from pathlib import Path

app = typer.Typer()


@app.command()
def next_create(path: Path = typer.Argument(..., help="project folder path")):
    path.mkdir(parents=True, exist_ok=True)

    folders = [
        path / "components" / "ui",
        path / "components" / "includes",
        path / "types",
        path / "public" / "assets",
        path / "about",
        path / "contact",
        path / "blogs",
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

    (path/"components"/"includes"/"Navbar.tsx").write_text(NAVBAR_CODE)
    (path/"components"/"ui"/"Button.tsx").write_text(BUTTON_CODE)

    (path/"types"/"uiTypes.ts").write_text(TYPES_CODE)

    (path/"components"/"ui"/"theme-provider.tsx").write_text(THEME_PROVIDER)
    (path/"components"/"ui"/"theme-switcher.tsx").write_text(THEME_SWITCHER)

    (path/"components"/"Hero.tsx").write_text(HERO_CODE)

    (path/"page.tsx").write_text(APP_PAGE_CODE)


@app.command()
def version():
    """Show version information."""
    typer.echo("seta v0.1.0")


def main():
    app()


if __name__ == "__main__":
    main()


# pip uninstall foldar -y
# pip install -e .
