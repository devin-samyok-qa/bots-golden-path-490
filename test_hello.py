import subprocess
import sys
from pathlib import Path

import hello


def test_main_prints_greeting(capsys):
    hello.main()
    assert capsys.readouterr().out == "Hello, Bots!\n"


def test_cli_prints_greeting():
    script = Path(__file__).parent / "hello.py"
    result = subprocess.run(
        [sys.executable, str(script)], capture_output=True, text=True, check=True
    )
    assert result.stdout == "Hello, Bots!\n"
