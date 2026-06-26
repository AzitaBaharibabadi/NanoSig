import argparse
import sys

from nanosig import __version__


def build_parser():
    parser = argparse.ArgumentParser(
        prog="nanosig-cli",
        description="NanoSig: confidence-calibrated detection of low-abundance taxa in long-read metagenomic data.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"nanosig-cli {__version__}",
    )
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser(
        "run", help="Run the full NanoSig pipeline (not yet implemented)."
    )
    run_parser.add_argument(
        "--fastq", required=False, help="Input FASTQ file (placeholder, not yet wired up)."
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "run":
        print("nanosig-cli run: not implemented yet (Phase 8).")
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
