from argparse import ArgumentParser

def cli(*args) -> dict:
    """
    Returns:
      args  : a dictionary of arguments with names and values
    """

    parser = ArgumentParser(
        description="Arguments needed for getting postcodes from a CSV"
    )

    parser.add_argument(
        "--input-csv",
        help="Relative path where your CSV/XLS/XLSX file is located",
        required=True,
        type=str,
    )

    parser.add_argument(
        "--output-csv",
        help="Relative path and name of new file where your CSV/XLS/XLSX file will be returned",
        required=True,
        type=str,
    )

    parser.add_argument(
        "--timeout",
        help="Time in seconds between requests to Nominatim APIs",
        required=True,
        type=str,
    )

    return parser.parse_args(*args).__dict__