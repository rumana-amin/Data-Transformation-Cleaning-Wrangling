# Install required packages
#!pip install pandas
#!pip install openpyxl  # required for handling Excel files with Pandas

# Import necessary libraries
import pandas as pd
import os

# Get the current working directory
pwd = os.getcwd()

# Load the dataset from Excel
survey_data_path = os.path.join(pwd, "Data - Survey Monkey Output Edited.xlsx")
dataset = pd.read_excel(survey_data_path, sheet_name="Edited_Data")

# Make a copy of the dataset
dataset_modified = dataset.copy()

# Drop unnecessary columns
columns_to_drop = ['Start Date', 'End Date', 'Email Address', 'First Name', 'Last Name', 'Custom Data 1']
dataset_modified.drop(columns=columns_to_drop, inplace=True)

# Melt the dataset to make it tidy
id_vars = list(dataset_modified.columns)[:8]
value_vars = list(dataset_modified.columns)[8:]
dataset_melted = dataset_modified.melt(id_vars=id_vars, value_vars=value_vars, var_name="Question+Subquestion", value_name="Answer")

# Load the questions dataset
question_data_path = os.path.join(pwd, "Data - Survey Monkey Output Edited.xlsx")
question_import = pd.read_excel(question_data_path, sheet_name="Question")

# Make a copy of the dataset
question = question_import.copy()

# Drop unnecessary columns from the questions dataset
question.drop(columns=["Raw_Questions", "Raw_Subquestions", "Subquestions"], inplace=True)

# Merge the melted dataset with the questions dataset
dataset_merged = pd.merge(left=dataset_melted, right=question, how="left", on="Question+Subquestion")

# Print lengths of original and merged datasets
print("Original Data Length:", len(dataset_melted))
print("Merged Data Length:", len(dataset_merged))

# Group by questions and count the number of unique respondents
respondents = dataset_merged[dataset_merged["Answer"].notna()].groupby("Questions")["Respondent ID"].nunique().reset_index()
respondents.rename(columns={"Respondent ID": "Respondents"}, inplace=True)

# Merge the dataset with the number of respondents
dataset_merged_two = pd.merge(left=dataset_merged, right=respondents, how="left", on="Questions")

# Print lengths of original and merged datasets
print("Original Data Length:", len(dataset_merged))
print("Merged Data Length:", len(dataset_merged_two))

# Group by question+subquestion and answer to count the number of respondents with the same answer
same_answer = dataset_merged.groupby(["Question+Subquestion", "Answer"])["Respondent ID"].nunique().reset_index()
same_answer.rename(columns={"Respondent ID": "Same Answer"}, inplace=True)

# Merge the dataset with the number of respondents with the same answer
dataset_merged_three = pd.merge(left=dataset_merged_two, right=same_answer, how="left", on=["Question+Subquestion", "Answer"])
dataset_merged_three["Same Answer"].fillna(0, inplace=True)

# Print lengths of original and merged datasets
print("Original Data Length:", len(dataset_merged_two))
print("Merged Data Length:", len(dataset_merged_three))

# Rename columns for clarity
output_dataset = dataset_merged_three.rename(columns={
    "Identify which division you work in.-Response": "Division Primary",
    "Identify which division you work in.-Other (please specify)": "Division Secondary",
    "Which of the following best describes your position level?-Response": "Position",
    "Which generation are you apart of?-Response": "Generation",
    "Please select the gender in which you identify.-Response": "Gender",
    "Which duration range best aligns with your tenure at your company?-Response": "Tenure",
    "Which of the following best describes your employment type?-Response": "Employment Type"
})

# Save the output dataset to Excel
output_dataset.to_excel(os.path.join(pwd, "Output_Dataset.xlsx"), index=False)
