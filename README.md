# Childhood Obesity Prediction Using Social Determinants

## Project Overview

**Project Title:** A Social Determinants-Based Machine Learning Framework for Childhood and Adolescent Obesity Prediction and Early Intervention

This project explores how social and household factors influence childhood and adolescent obesity. It uses machine learning to examine the relationship between demographic characteristics, household income, food security, dietary behaviour, and physical activity.

The project aims to support early identification of children who may be at risk of obesity and encourage evidence-based public health interventions.

## Objectives

- Examine the relationship between social determinants and childhood obesity.
- Develop machine learning models to predict obesity status among children and adolescents.
- Compare different classification algorithms.
- Build an interactive application for exploring obesity predictions.

## Dataset

The study uses data from the **National Health and Nutrition Examination Survey (NHANES) 2021–2023**.

- Source: [CDC NHANES 2021–2023](https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Cycle=2021-2023)
- Study population: Children and adolescents aged 2–19 years.
- Working dataset: 2,492 participants.
- Obesity group: 559 participants.
- Non-obesity group: 1,933 participants.

The data files were combined using the participant identification variable `SEQN`.

The selected features cover demographic, socioeconomic, household food security, dietary behaviour, and physical activity information.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Jupyter Notebook

## Methodology

The project followed these main steps:

1. Data collection from NHANES.
2. Data merging using the participant identification number.
3. Data cleaning and preprocessing.
4. Feature selection based on social determinants.
5. Creation of a binary obesity target variable.
6. Training and evaluation of machine learning models.
7. Development of an interactive Streamlit application.

## Machine Learning Models

The following classification algorithms were evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

Model performance was assessed using accuracy, precision, recall, F1-score, and ROC-AUC.

## Model Results

Gradient Boosting achieved the highest accuracy of **76.55%**.

Logistic Regression achieved the highest recall for the obesity class at **60.71%**, with an accuracy of 56.51%.

The results demonstrate the importance of considering multiple evaluation metrics, particularly when identifying the obesity class is a priority.

## Interactive Application

A Streamlit application was developed to provide an interactive interface for generating obesity-status predictions based on selected demographic, social, and behavioural characteristics.

The application is a research prototype and is not intended for clinical diagnosis.

## Project Structure

```text
childhood-obesity-prediction/
│
├── Childhood_Obesity.ipynb
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
```

## How to Run the Project

Clone the repository:

```bash
git clone https://github.com/mr-frank1216/childhood-obesity-prediction.git
```

Navigate into the project folder:

```bash
cd childhood-obesity-prediction
```

Install the required libraries:

```bash
pip install pandas numpy scikit-learn streamlit
```

Run the application:

```bash
streamlit run app.py
```

## Future Improvements

- Improve model performance and obesity-class prediction.
- Conduct independent validation using additional datasets.
- Assess model fairness across demographic groups.
- Improve the interactive application.
- Explore how findings can inform early intervention at household, school, and community levels.

## Research Significance

This project contributes to the use of data science and artificial intelligence in public health by examining childhood obesity through a social determinants perspective. It highlights how machine learning can support research, early identification, and the development of targeted prevention strategies.

## Author

**Franklin Chibueze Nwajuo**

Deep Tech/WESOnline Mentorship Program  
Group: C4 Data Science AI/ML 003

**Contact:** franklinchibs@gmail.com
