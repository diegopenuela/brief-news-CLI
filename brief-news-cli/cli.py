# cli.py Typer-based CLI entry point
import typer
from config import NYTimes_API_KEY
from api import fetch_top_stories 

app = typer.Typer()

@app.command()
def dummy(arg1: str, arg2: int):
    """
    My CLI command description.
    """
    typer.echo(f"Argument 1: {arg1}")
    typer.echo(f"Argument 2: {arg2}")

@app.command()
def top_stories():
    """
    Fetch and display top stories from the New York Times API.
    """
    # Check if the NYTimes_API_KEY is available
    if not NYTimes_API_KEY:
        typer.echo("Error: New York Times API key is missing. Please set it in your config.py file.")
        return

    # Fetch top stories
    top_stories_data = fetch_top_stories()

    if top_stories_data:
        typer.echo("Top Stories:")
        for i, story in enumerate(top_stories_data, start=1):
            typer.echo(f"{i}. {story['title']}")
    else:
        typer.echo("Failed to fetch top stories. Check your API key and network connection.")


@app.callback()
def main(ctx: typer.Context):
    """
    Non-commercial use. A CLI based on Python and Typer. 
    Connects to trusted news sources like the New York Times APIs, fetch today's news, 
    and then uses Hugging Face AI tools to summarize the news in a simple paragraph.
    """
    print(f"About to execute command: {ctx.invoked_subcommand}")

if __name__ == "__main__":
    app()