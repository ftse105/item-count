### Data Engineering Exercise

The objective of this exercise is to create a command line application that, given a directory of customer receipt files, can identify the top N best-selling products among all the receipts.  The solution must be implemented in Python, and it must function on Windows, Mac, and Linux.

**Deliverable requirements:**

Your solution should contain the following files:

* `cli.py` - single python file containing your solution
* `req.txt` - python requirements file (if non-standard modules were used)
* `readme.md` - description of your solution, including which python version and modules you used

You may submit your solution as a github/bitbucket repository, or a zipped folder.

**CLI Structure:**

CLI application should be called as shown below:

`python cli.py -d "<path_to_directory>" -n <number_of_products> -o "<output_filepath>"`

Arguments:

* "-d" - String filepath (absolute or relative) to the directory of receipt files
* "-n" - Integer number of best-selling products to return
* "-o" - String filepath (absolute or relative) to the output file

Note: arguments must be callable in any order

**Input files:**

The input receipt files contain JSON data for each customer transaction.  All of the files use the same JSON fields, although they may vary in size.  You must only process files ending with a ".json" extension  You do not need to traverse subdirectories within the directory.

There is a compressed sample folder of JSON receipt files in this repository called `data.tar.gz`

**Output:**

This application must output a single text file containing the following fields in JSON format:

* "source_folder": the directory of the recipt files
* "run_date": the date that the application was run, format "YYYY-MM-DD"
* "file_count": the number of files processed in the source folder
* "best_sellers": the list of best-selling products, with the total quantity sold and the rank

Below is an example of the output file structure:

```
{
  "source_folder": "/home/eataly/receipt_files",
  "run_date": "2017-01-06",
  "file_count": 999,
  "best_sellers": [
    {"product_id": "1234-1000", "qty_sold": 100, "rank": 1},
    {"product_id": "2345-1000", "qty_sold": 90, "rank": 2},
    {"product_id": "4567-1000", "qty_sold": 85, "rank": 3}
  ]
}
```
