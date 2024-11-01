# ReadMe

## Project Overview

This script reshapes data from an Excel file with a specific structure: it contains two columns, where the first column represents repeated headers, and the second column holds corresponding values. Each unique record is spread across blocks of 7 rows, and the goal is to convert these row-based records into a more readable table format, with each header as a column.

### Input File Requirements

The input file should meet these criteria:
- **Format**: Excel file (`.xlsx`)
- **Structure**: Two columns:
  - **Column 1**: Header names (repeated every 7 rows for each new record)
  - **Column 2**: Corresponding values for each header
- **Data blocks**: Each unique record occupies a block of exactly 7 rows.

Example input structure:
| Column 1 (Header) | Column 2 (Value) |
|-------------------|------------------|
| Header1           | Value1           |
| Header2           | Value2           |
| Header3           | Value3           |
| ...               | ...              |
| Header7           | Value7           |
| Header1           | Value8           |
| Header2           | Value9           |
| ...               | ...              |

### Output Structure

The output DataFrame (`df_final`) will contain:
- A single row for each 7-row block from the input file.
- Headers as columns, with corresponding values filled in for each row.

Example output structure:
| Header1 | Header2 | Header3 | ... | Header7 |
|---------|---------|---------|-----|---------|
| Value1  | Value2  | Value3  | ... | Value7  |
| Value8  | Value9  | Value10 | ... | Value14 |

### Code Explanation

The following steps explain the code functionality:

1. **Read the Excel File**:
   ```python
   df = pd.read_excel('03-12.xlsx', header=None)
   ```
   - Reads the Excel file without predefined headers, allowing the original structure to remain unchanged.
   
2. **Set Parameters and Initialize Final DataFrame**:
   ```python
   n = 7
   df_final = pd.DataFrame()
   ```
   - Defines `n`, the number of rows in each data block.
   - Initializes an empty DataFrame, `df_final`, to store the reshaped data.

3. **Loop through the Data in Blocks of 7 Rows**:
   ```python
   for i in range(0, len(df), n):
       chunk = df.iloc[i:i+n]
   ```
   - Iterates through `df` in steps of 7 rows to handle each data block individually.

4. **Transpose Each Block**:
   ```python
   chunk_transposed = chunk.set_index(0).T
   ```
   - Transposes each 7-row block so that headers in column 1 become columns in `chunk_transposed`.
   - Sets column 1 as the index, which becomes the column headers upon transposing.

5. **Concatenate Transposed Chunks**:
   ```python
   df_final = pd.concat([df_final, chunk_transposed], ignore_index=True)
   ```
   - Appends each transposed chunk as a new row in `df_final`, incrementally building the output DataFrame.
   
### Requirements

- **Python Packages**: `pandas`
- **Python Version**: Any version that supports pandas and basic file I/O operations.

### Usage

1. Ensure that the Excel file meets the input format requirements.
2. Place the Excel file in the same directory as the script.
3. Run the script to output the reshaped data in a DataFrame format (`df_final`).

### Example

For an input file named `03-12.xlsx`, running this script will produce a `df_final` DataFrame with the desired table structure. 

This process is especially useful for converting long-format data with repeating headers into a more usable, wide-format table.
