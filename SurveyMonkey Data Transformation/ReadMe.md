# Survey Monkey Data Transfomarion and Analysis
## Project Description
This Python script processes survey data exported from SurveyMonkey, transforming it into a clean and analysis-ready format. It performs a series of data cleaning, transformation, and merging steps to prepare the dataset for further analysis or visualization.

## Files Required

- `Data - Survey Monkey Output Edited.xlsx`  
  This Excel file must contain at least two sheets:
  - `Edited_Data`: The main survey response data.
  - `Question`: Metadata mapping for questions and subquestions.

## Steps Performed

1. **Initial Setup**  
   - Required packages: `pandas`, `openpyxl` (for handling Excel files).
   - Sets the working directory and loads input data.

2. **Data Cleaning**
   - Drops unnecessary columns such as `Start Date`, `End Date`, and identifying information.
   - Reshapes the dataset using `pd.melt()` to make it tidy and long-format.

3. **Merge with Question Metadata**
   - Loads and filters the `Question` sheet.
   - Merges melted survey data with question metadata on `Question+Subquestion`.

4. **Respondent Calculations**
   - Calculates the number of unique respondents per question.
   - Merges this data back into the main dataset.

5. **Same Answer Count**
   - For each combination of subquestion and answer, counts how many respondents gave the same answer.
   - Adds this information to the dataset.

6. **Renaming Columns**
   - Renames specific columns for better clarity and usability.

7. **Output**
   - Saves the cleaned and enriched dataset to `Output_Dataset.xlsx`.

## How to Run

1. Install dependencies (if not already installed):

   ```bash
   pip install pandas openpyxl

