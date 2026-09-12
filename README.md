# Healthcare Data Analysis Planning and Strategy

## 📌 Project Overview

This repository contains the Week 1 strategic plan for a healthcare data analytics project focused on understanding and predicting 30-day hospital readmission among patients with diabetes.

The project establishes a structured roadmap covering research background, objectives, data requirements, analytical methodology, measurable outcomes, project risks, tools, timeline, and evaluation criteria.

## 🎯 Objective

The primary objective is to develop a reproducible healthcare data-analysis strategy for identifying factors associated with hospital readmission within 30 days.

The plan considers:

- Healthcare background research
- Dataset identification
- Data-quality assessment
- Exploratory data analysis
- Feature preparation
- Predictive modelling
- Model evaluation
- Risk management
- Responsible healthcare analytics

## 📊 Proposed Dataset

The planned analysis uses the:

**Diabetes 130-US Hospitals for Years 1999–2008 dataset**

Key characteristics:

- 101,766 hospital encounters
- 47 original features
- 130 U.S. hospitals / integrated delivery networks
- Data period: 1999–2008

The dataset contains demographic, admission, diagnosis, medication, procedure and healthcare-utilisation variables.

## 🔬 Analytical Question

Can demographic, admission, medication, procedure and previous healthcare-utilisation information be used to identify hospital encounters associated with readmission within 30 days?

## 📈 Measurable Analytical Objectives

The project will:

1. Assess the quality and completeness of the healthcare dataset.
2. Identify important demographic, admission and healthcare-utilisation variables.
3. Explore patterns associated with 30-day readmission.
4. Develop classification models as a predictive prototype.
5. Compare models using precision, recall, F1-score, ROC-AUC and PR-AUC.
6. Examine the trade-off between false positives and false negatives.
7. Document limitations, fairness considerations and requirements for future validation.

## 🧪 Example Hypotheses

### H1
Higher prior inpatient utilisation may be associated with increased likelihood of 30-day readmission.

### H0
Prior inpatient utilisation has no meaningful association with 30-day readmission.

### H1
Machine-learning classification models can provide useful discrimination between encounters with and without 30-day readmission.

### H0
The proposed models do not provide useful discrimination beyond a baseline approach.

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook / Google Colab
- GitHub

## 🔄 Project Framework

```text
Research & Background
        ↓
Dataset Identification
        ↓
Data Quality Assessment
        ↓
Cleaning & Preprocessing
        ↓
Exploratory Data Analysis
        ↓
Feature Preparation
        ↓
Predictive Modelling
        ↓
Model Evaluation
        ↓
Interpretation
        ↓
Healthcare Recommendations
