import subprocess
import sys


def test_cli_help_exit_code():
    result = subprocess.run(
        [sys.executable, "-m", "nanosig.cli", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "NanoSig" in result.stdout
