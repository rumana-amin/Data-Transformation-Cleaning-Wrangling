# Consolidating TSV Files Using Excel Power Query

## Overview
This project was initiated based on a job found on Upwork. This project demonstrates a step-by-step process to transform and consolidate multiple tab-separated values (TSV) files into a single table using Excel's Power Query. The methodology includes creating custom functions, applying transformations, and merging data effectively.
________________________________________
## Problem Statement
The task involves consolidating data from several TSV files. Each file requires transformation, alignment, and merging before producing the final output.
________________________________________
## Solution Outline
### 1.	Understand TSV Files
TSV files store tabular data, where rows are separated by newlines, and fields within rows are separated by tab characters. Rows 1 to 6 need to be transposed to align with the other columns in row 8.
![File format]( https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Power%20Query%20and%20TSV%20files/Images/01.%20Structure%20of%20TSV%20file.png)
### 2.	Transformation Steps
- Load Files: Import all TSV files using the "From Folder" option in Power Query.
![Load TSV Files]( https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Power%20Query%20and%20TSV%20files/Images/03.%20Load%20all%20tsv%20files.png)
-	Prepare a Sample File: Create a reference query for the structure of one TSV file. ![Sample File](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Power%20Query%20and%20TSV%20files/Images/04.%20Create%20Sample%20File.png)
-	Create Custom Functions: Transform sample queries into reusable functions for consistent data processing across files. ![Custom Function](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Power%20Query%20and%20TSV%20files/Images/08.%20Custom%20Function1.png)
-	Data Cleaning: Remove unnecessary rows, transpose headers, and standardize column structures.
### 3.	Combining Files
-	Apply custom functions to process each file. 
![Invoke Custom Function]( https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Power%20Query%20and%20TSV%20files/Images/12.%20Output1.png)
-	Merge transformed outputs into a single table.
-	Remove redundant columns, rename fields, and finalize the output.
________________________________________
## Key Steps
1.	Load TSV files into Power Query.
2.	Create and use parameters to streamline the transformation.
3.	Apply transformations like transposing, promoting headers, and removing unnecessary rows/columns.
4.	Create custom functions to automate repetitive transformations.
5.	Combine and merge outputs for a consolidated table.
![Consolidated Table](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Power%20Query%20and%20TSV%20files/Images/22.%20Merged%20%26%20Transformed.png)
________________________________________
## Final Output
The process results in a clean, consolidated table loaded into an Excel worksheet, ready for analysis or reporting.
![Final Output]( https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Power%20Query%20and%20TSV%20files/Images/23.%20Final%20Output.png)
________________________________________
## Applications
This approach can be applied to similar data consolidation tasks, ensuring consistency and efficiency in handling large datasets.
## Challenges
The most challenging part was to get all the columns in the same structure. The columns were in two formats. Rows 1 to 6 need to be transposed to align with the other columns in row 8. Initially, I was able to do it in Excel power query for a single file by duplicating the query and transforming each file before merging it into one. But I was unable to do so for multiple files. Finally, I used custom functions in power query to do so.

## Files
1.	Target File.xlsx: The power query file. [Link](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Power%20Query%20and%20TSV%20files/Target%20File.xlsx)
2.	TSV Files: Folder containing four TSV files. [Link](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/tree/main/Power%20Query%20and%20TSV%20files/TSV%20Files)

## Article Links
LinkedIn Article - [combining-tsv-files-using-excel-power-query](https://www.linkedin.com/pulse/transforming-combining-tsv-files-using-excel-power-query-rumana-amin-kuocc/?trackingId=Y3Aa81lpRLu4n8d24XZiKw%3D%3D) 


