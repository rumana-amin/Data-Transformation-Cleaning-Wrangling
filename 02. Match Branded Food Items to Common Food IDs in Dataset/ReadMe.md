
# **Matching Branded Food Items to Common Food IDs**  

## **Project Overview**  
This project involved developing a solution to match rows of information from two datasets and return corresponding values. The project was inspired by a job listing on Upwork. Using Python's **pandas** and **regular expression** libraries, the matching logic was implemented to achieve accurate results.  

---

## **Approach and Methodology**  

1. **Dataset Generation**  
   - Created sample datasets to replicate the problem:  
     - **Dataset 1**: 50 rows of branded food items.  
     - **Dataset 2**: 20 rows of common food items.  
   - Used ChatGPT to simulate realistic synthetic data.  

2. **Data Import and Preparation**  
   - Imported the sample datasets into Python using **pandas**, converting them into DataFrames for efficient manipulation.  

3. **Data Analysis**  
   - Examined the structure and format of both datasets to understand their alignment.  

4. **Matching Logic Implementation**  
   - Developed Python functions to match rows between the datasets based on specific criteria:  
     - Match names or categories in the branded food dataset with corresponding entries in the common food dataset.  

5. **Output Generation**  
   - Saved the matched results into a CSV file for easy review and further use.  

---

## **Code Snippet**  
```python
# Function to match branded food to common food
def match_common_food(branded_name, branded_category):
    # Try matching by name or category
    for _, common_food in common_foods.iterrows():     
        if common_food['name_cleaned'] in branded_name or common_food['category_cleaned'] in branded_category:
            return common_food['id']
    return None

# Apply the matching function to each row in the branded foods DataFrame
branded_foods['common_id'] = branded_foods.apply(
    lambda row: match_common_food(row['branded_name_cleaned'], preprocess(row['branded_category'])), axis=1
)
```  

### **Code Explanation**  
- Used **iterrows** to iterate through rows of the common food dataset.  
- Employed a **lambda function** to apply the matching logic to each row of the branded food dataset.  

---

## **Limitations**  
1. **Synthetic Data**  
   - The datasets were artificially generated, which might not fully capture real-world complexities.  
2. **Small Dataset Size**  
   - The datasets were intentionally kept small, limiting the validation scope to logical testing only.  

---

## **Deliverables**  
1. **TestDataset.xlsx**: Initial datasets for branded and common food items. [File Link](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/02.%20Match%20Branded%20Food%20Items%20to%20Common%20Food%20IDs%20in%20Dataset/TestDataset.xlsx)  
2. **Match_Rows.ipynb**: Python script used for data matching and transformation. [Python Script Link](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/02.%20Match%20Branded%20Food%20Items%20to%20Common%20Food%20IDs%20in%20Dataset/Match_Rows.ipynb)
3. **branded_foods_with_common_ids.csv**: Output file containing the matched results. [Output File Link](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/02.%20Match%20Branded%20Food%20Items%20to%20Common%20Food%20IDs%20in%20Dataset/branded_foods_with_common_ids.csv)
4. **Task Description.pdf**: Detailed job description and requirements. [Upwork Task Link](https://github.com/rumana-amin/Data-Transformation-Cleaning-Wrangling/blob/main/02.%20Match%20Branded%20Food%20Items%20to%20Common%20Food%20IDs%20in%20Dataset/Task%20Description.pdf)

This project demonstrates effective use of Python for data transformation, matching, and exportation while addressing a practical problem in data management.
