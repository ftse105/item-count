#Version etc

-Python3
-pandas

#Arguments

Lines 13-39
-Created the arguments that allows user to enter in CLI

#Input Files

Lines 43-70
-Made a list of all json files
-Iterated through the list
-Flatten "products" to include "receipt_id", "transaction_time" and "employee_name"

-Used pandas to convert list into a table
(Can see list view and table view by uncommenting out lines 71 and 72)

#Sum or Sort

Lines 77-79
-Sums quantity sold by product id
-Soft by total and limit the number of rows

#Output Files

Lines 86-97
-Outputs the list to JSON format given
-Append top sellers to the output

Lines 102-105
-Outputs JSON to text file
