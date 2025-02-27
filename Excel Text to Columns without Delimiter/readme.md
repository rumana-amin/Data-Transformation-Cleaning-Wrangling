# Excel File Transformation Without Delimiter

## Project Description
This project was initiated based on a problem found on Upwork. The client provided an image of an Excel file containing various types of information stored within a single column, without any delimiters. The primary objective was to extract and structure five specific types of data: **full name, address, zip code, city, and email**. However, some cells also contained additional information such as phone numbers, which needed to be handled carefully.

## Problem
The client provided a PNG image of an Excel file with data in a single column, lacking any delimiters to separate the required information. This presented a significant data extraction and structuring challenge.

![Sample Data Image](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Excel%20Text%20to%20Columns%20without%20Delimiter/sample_data.png)
## Data Transformation Process
To address this problem, the following steps were undertaken:
1. **Data Format Analysis**: Examined the structure and patterns of the provided data.
2. **Dataset Generation**: Generated 50 rows of sample data using ChatGPT to simulate the problem.
3. **Data Import and Transformation**: Imported the dataset into Power Query for preprocessing and cleaning.
4. **Custom Function Implementation**: Developed a custom function to accurately extract city and email information, which were the most challenging elements to separate.
5. **Validation and Refinement**: Verified the extracted data and performed necessary refinements to improve accuracy.
   
![Final Output](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Excel%20Text%20to%20Columns%20without%20Delimiter/Final%20Output.png)

## Challenges and Limitations
1. **Synthetic Data**: The dataset was generated using ChatGPT, leading to city names predominantly from Germany and Austria.
2. **Error Rate**: The automated process had an error rate of approximately 10%.
3. **Manual Adjustments**: Some manual transformations were required to ensure accuracy and completeness.

## Technologies Used
- Excel Power Query
- ChatGPT (for data generation)
- Data Cleaning and Transformation Techniques

## Important Links
- Sample Data.png: An image provided by the client of sample data. [Link Here](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Excel%20Text%20to%20Columns%20without%20Delimiter/Sample%20Data.png)
- Raw Data.xlsx: An Excel file containg raw dataset. [Link Here](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Excel%20Text%20to%20Columns%20without%20Delimiter/Raw%20Data.xlsx)
- Output Data.xlsx: Final output after transformation. [Link Here](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/Excel%20Text%20to%20Columns%20without%20Delimiter/Output%20Data.xlsx)

---
This repository serves as a reference for handling unstructured data within Excel files, showcasing the effectiveness of Power Query and custom transformations.
