
import pandas as pd
import argparse
import json
import os
import sys
from datetime import date

#python3 cli.py -d "/Users/frankietse/Desktop/item-count-test/testdata" -n 5 -o "/Users/frankietse/Desktop/item-count-test/"

#------------------------- Sets up command line inputs and sets them to variables ------------------

parser = argparse.ArgumentParser(description='Inputs')
parser.add_argument("-d", default=1, type=str, help="String filepath (absolute or relative) to the directory of receipt files.")
parser.add_argument("-n", default=1, type=int, help="Integer number of best-selling products to return")
parser.add_argument("-o", default=1, type=str, help="String filepath (absolute or relative) to the output file")
args = parser.parse_args()
#adds the arguments to CLI

jsonFilesDir = args.d
nbrBestSelling = args.n
outputFileDir = args.o

#does some basic input formatting
if (jsonFilesDir.endswith('/') == False):
    jsonFilesDir = jsonFilesDir + "/"

if (outputFileDir.endswith('/') == False):
    outputFileDir = outputFileDir + "/"

# checks to see that path is valid
if (os.path.isdir(jsonFilesDir) == False):
    print("Invalid input path: " + jsonFilesDir)
    sys.exit()

# checks to see that path is valid
if (os.path.isdir(outputFileDir) == False):
    print("Invalid output path: " + outputFileDir)
    sys.exit()

#---------------------------- processes all json files in specified directory ----------------------

dataList = []   # used to house all data within all json files with all columns in list form.
fileCount = 0   # keeps track of number of files processed

# loops through all files that end in ".json"
for filename in os.listdir(jsonFilesDir):
    if filename.endswith(".json"):

        with open(jsonFilesDir + filename) as json_file:
            jsonData = json.load(json_file)

            fileCount = fileCount + 1
            print("Parsing file " + (jsonFilesDir + filename))

            #gets all fields of the json into a variable and inserts into panda Table/dataframe
            receipt_id = jsonData['receipt_id']
            transaction_time = jsonData['transaction_time']
            employee_name = jsonData['employee_name']


            for p in jsonData['products']:
                qty_sold = p['qty_sold']
                product_name = p['product_name']
                product_id = p['product_id']

                dataList.append([receipt_id, transaction_time, employee_name, product_id, qty_sold, product_name])

# converts all data stored in dataList into a panda table (dataframe) so we can do analysis
transactionsTbl = pd.DataFrame(dataList, columns = ['receiptid', 'transactiontime', 'employee_name', 'product_id', 'qty_sold', 'product_name'])
#print (dataList)
#print (transactionsTbl)


#--------------------------------- aggregate total items sold by product ID ---------------------------------

itemsSold = transactionsTbl.groupby(['product_id'])['qty_sold'].agg('sum').reset_index()    #total quantity sold by product id
itemsSold = itemsSold.sort_values(['qty_sold'], ascending=[False]).head(nbrBestSelling)     #sort by total sold and limit number of rows
outputList = itemsSold.values.tolist()
# print(outputList)



#------------------------------------------ create output json string ---------------------------------------

outputjson = "{\"source_folder\": \"" + jsonFilesDir + "\", \"run_date\": \"" + str(date.today()) + "\", \"file_count\": " + str(fileCount) + ",\"best_sellers\": ["

#append top sellers to the output json
for i in range(len(outputList)):
    outputjson = outputjson + "{\"product_id\": \"" + outputList[i][0] + "\", \"qty_sold\": " + str(outputList[i][1]) + ", \"rank\": " + str(i+1) + "},"

#removes last comma
if outputjson.endswith(','):
    outputjson = outputjson[:-1]

#closing json brackets
outputjson = outputjson + "]}"


#------------------------------------------ output to text file ---------------------------------------------

print("Writing output to file: " + outputFileDir + "output.json")
f = open(outputFileDir + "output.json", "w")
f.write(outputjson)
f.close()
