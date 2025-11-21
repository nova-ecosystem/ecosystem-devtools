import argparse
import sys
# Import your submodules here
from nova_cli.commands import version

def main():
    parser = argparse.ArgumentParser(
        prog="nova", 
        description="Nova Ecosystem Developer Tools"
    )
    
    subparsers = parser.add_subparsers(dest="main_command", help="Available commands")

    # Register subcommands from modules
    version.register_subcommand(subparsers)

    # Parse arguments
    args = parser.parse_args()

    # Route to the correct module
    if args.main_command == "version":
        version.execute(args)
    else:
        # If no command is provided, print help
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()