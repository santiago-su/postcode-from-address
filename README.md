# postcode-from-address

Small library to get postcodes from a csv with addresses, it has hardcoded logic on the csv/xls column names, might make this more generic in the future.

### Quick Start

#### Requirements:
-  `python3`

- `pip`

Run
```sh
$ pip install -r requirements.txt
```

To run the script we are passing three arguments in a prompt:

`--input-csv`: Relative path where your CSV/XLS/XLSX file is located.

`--output-csv`: Relative path and name of new file where your CSV/XLS/XLSX file will be returned.

`--timeout`: Time in seconds between requests to Nominatim APIs, try modifying if getting a lot of `Service timed out` errors

Please take into account Nominatim [usage policy](https://operations.osmfoundation.org/policies/nominatim/) when using this library which uses Nominatim on the background

**Example**:
```sh
python3 ./main.py --input-csv=./fulladdress.xlsx --output-csv=./newpostcodes.csv --timeout=10
```


