#!/usr/bin/env python3
"""A tiny plugin-powered CLI.

Every .py file in the `plugins/` folder is loaded and its `fetch_data()`
function is called. The returned dictionary is printed in the terminal.
If one plugin breaks, the others keep running.
"""

import importlib.util
import sys
import traceback
from pathlib import Path

try:
    from rich.console import Console
    from rich.table import Table

    console = Console()
    HAS_RICH = True
except ImportError:  # rich is optional; fall back to plain text
    HAS_RICH = False

PLUGINS_DIR = Path(__file__).parent / "plugins"


def discover_plugins():
    """Return a sorted list of plugin file paths (ignores files starting with '_')."""
    if not PLUGINS_DIR.is_dir():
        return []
    return sorted(p for p in PLUGINS_DIR.glob("*.py") if not p.name.startswith("_"))


def load_plugin(path):
    """Import a single plugin file and return the module."""
    spec = importlib.util.spec_from_file_location(f"plugins.{path.stem}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_plugin(path):
    """Load a plugin and call fetch_data(). Returns (data, error_message)."""
    try:
        module = load_plugin(path)
        if not callable(getattr(module, "fetch_data", None)):
            return None, "no fetch_data() function found"
        data = module.fetch_data()
        if not isinstance(data, dict):
            return None, f"fetch_data() must return a dict, got {type(data).__name__}"
        return data, None
    except Exception as exc:  # one bad plugin must never crash the CLI
        return None, f"{type(exc).__name__}: {exc}"


def show_success(name, data):
    if HAS_RICH:
        table = Table(title=name, title_style="bold green", show_header=True)
        table.add_column("Key", style="cyan")
        table.add_column("Value", style="white")
        for key, value in data.items():
            table.add_row(str(key), str(value))
        console.print(table)
    else:
        print(f"\n== {name} ==")
        for key, value in data.items():
            print(f"  {key}: {value}")


def show_error(name, message):
    if HAS_RICH:
        console.print(f"[bold red]✗ {name} failed:[/bold red] {message}")
    else:
        print(f"\n✗ {name} failed: {message}", file=sys.stderr)


def main():
    plugins = discover_plugins()
    if not plugins:
        print(f"No plugins found in {PLUGINS_DIR}. Add a .py file with a fetch_data() function.")
        return 1

    ok, failed = 0, 0
    for path in plugins:
        data, error = run_plugin(path)
        if error:
            failed += 1
            show_error(path.stem, error)
        else:
            ok += 1
            show_success(path.stem, data)

    summary = f"\nDone: {ok} plugin(s) succeeded, {failed} failed."
    if HAS_RICH:
        console.print(summary, style="bold")
    else:
        print(summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
