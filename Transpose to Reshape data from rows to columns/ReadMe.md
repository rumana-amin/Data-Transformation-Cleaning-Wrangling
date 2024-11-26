# Transpose and Reshape Data from Rows to Columns
## Project Overview
This project began with a job posting on Upwork, involving data reshaping and retrieving telephone codes for various countries. The task required reformatting data from an Excel file with a unique structure: two columns, where the first contains repeated headers and the second holds corresponding values. Each record spans seven rows, and the goal was to transform these row-based records into a more readable table format, with each header as a column. Additionally, an HTML table containing country codes was imported and merged with the structured data. 

I approached this task in two ways. In the first script [(Script 1)](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Transpose%20to%20Reshape%20data%20from%20rows%20to%20columns/Transpose%20Rows_script1.ipynb)
, I used Python’s Pandas library, combining a custom function and a for loop to reshape the data. In the second script [(Script 2)](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Transpose%20to%20Reshape%20data%20from%20rows%20to%20columns/Data_processing_script2.ipynb), I employed Pandas along with the transpose and pivot functions to achieve the desired format.
### Data Structure Overview
The input file overview:
- **Format**: Excel file (`.xlsx`)
- **Structure**: Two columns:
  - **Column 1**: Header names (repeated every 7 rows for each new record)
  - **Column 2**: Corresponding values for each header
- **Data blocks**: Each unique record occupies a block of exactly 7 rows.

 Input structure:
| Column 1 (Header) | Column 2 (Value) |
|-------------------|------------------|
| NAME:          	| francisca lopez vera           |
| ADRESS:         	 | calle herreria nº 27 calle herreria nº25|
|CITY: | el burgo, |
| ...               | ...              |
| TELEPHONE: | 34956370762|
| NAME: | Miguel |
| ADRESS:| Camino Ca'n Duran nº15 (PIVITA)|
| ...               | ...              |

### Output Structure

The output DataFrame (`df_transposed`) will contain:
- A single row for each 7-row block from the input file.
- Headers as columns, with corresponding values filled in for each row.

Output structure:
| NAME | ADRESS| CITY | ... | TELEPHONE |
|---------|---------|---------|-----|---------|
| francisca lopez vera  | calle herreria nº 27 calle herreria nº25| el burgo| ... | 645465703|
| Miguel | Camino Ca'n Duran nº15 (PIVITA) | Palma de Mallorca (El Arenal), |…| 658888909|


## How It Works in Script1
To address this problem, the following steps were undertaken among many others:
1. **Read Excel Data**:  Reads an Excel file with unstructured data (no headers) in blocks of 7 rows.
   
2. **Transpose Data Blocks**: Organizes the data by transposing each 7-row block into a single row
### Code
   ```python
# Number of headers (each block contains 7 headers)
n = 7

# Create an empty DataFrame for the final output
df_final = pd.DataFrame()

# Loop through the DataFrame in chunks of 7 rows to create rows in the final DataFrame
for i in range(0, len(df), n):
    # Select a chunk of 7 rows
    chunk = df.iloc[i:i+n]
    
    # Transpose the chunk so that column 1 becomes the headers and column 2 becomes values
    chunk_transposed = chunk.set_index(0).T
    
    # Append the transposed chunk to the final DataFrame
    df_final = pd.concat([df_final, chunk_transposed], ignore_index=True)

```

3. **Retrieve Country Codes**: Imports an HTML table with country codes.

4. **Data Merge**: The transposed data is merged with the country code table using a left join on the `Country: ` column to add relevant country codes.

```python
df_merged = pd.merge(df_transposed, df_code, left_on="Country", right_on="COUNTRY", how="left")
```

5. **Column Renaming**: Renames columns to fit known header names.

6. **Merging Two Columns**: Telephone and Country Code is merged into one column.
  



### Output
This process is particularly useful for converting long-format data with repeating headers into a more practical wide-format table. The result is a DataFrame where each row represents a unique record, with columns for address, city, country, name, postal code, province, telephone, and an added country code.

## File List
- **1. 03-12.xlsx**: The input Excel file containing unstructured data. [file link]( https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Transpose%20to%20Reshape%20data%20from%20rows%20to%20columns/03-12.xlsx)
- **2. output_data.csv**: The final merged DataFrame containing structured data with country codes. [file link](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Transpose%20to%20Reshape%20data%20from%20rows%20to%20columns/output_data.csv)
- **3. Transpose Rows_script1.ipynb**: Python script 1, where custom function and for loop are used. [Python Script 1](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Transpose%20to%20Reshape%20data%20from%20rows%20to%20columns/Transpose%20Rows_script1.ipynb)
- **4. Data processing_script2.ipynb**: Python script 2, where transpose and pivot function are used. [Python Script 2](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Transpose%20to%20Reshape%20data%20from%20rows%20to%20columns/Data_processing_script2.ipynb)
