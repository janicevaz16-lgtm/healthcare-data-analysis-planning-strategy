# Healthcare Data Analysis: Heart Disease Risk Analytics

## Project Overview

This project demonstrates an end-to-end healthcare data analytics workflow using the UCI Heart Disease dataset, with a focus on the Cleveland dataset.

The project covers the complete analytical lifecycle from data-analysis planning and preprocessing through visualization, predictive analytics, data-quality assurance, compliance considerations, and final communication of findings.

The objective is to demonstrate how healthcare data can be transformed into structured analytical evidence while maintaining reproducibility, responsible interpretation, and awareness of data-quality and ethical considerations.
Model performance is only reported when reproduced from the project's actual modelling pipeline.
## Quick Navigation

| Component | Description |
|---|---|
| `notebooks/` | Executable exploratory analysis and modelling |
| `src/` | Reusable Python data and modelling functions |
| `docs/` | Six-stage analytical documentation |
| `figures/` | Workflows, diagrams, and dashboard mockups |
| `data/` | Dataset documentation and local data structure |

## My Analytical Contribution

This project demonstrates an end-to-end healthcare analytics workflow in which I:

- Defined the healthcare analytics problem and project objectives
- Assessed dataset structure and analytical requirements
- Designed data-cleaning and preprocessing procedures
- Developed a healthcare visualization and reporting strategy
- Planned and evaluated machine-learning classification approaches
- Defined data-quality and validation controls
- Incorporated healthcare privacy, ethics, and compliance considerations
- Documented analytical decisions and limitations
- Communicated the analytical lifecycle through a final stakeholder-style report
## Analytical Lifecycle

| Stage | Focus | Key Output |
|---|---|---|
| Week 1 | Planning | Analytical strategy and problem definition |
| Week 2 | Preprocessing | Data-cleaning and validation methodology |
| Week 3 | Visualization | Healthcare visualization and reporting strategy |
| Week 4 | Predictive Analytics | Classification modelling strategy |
| Week 5 | Data Quality | QA, governance, and compliance framework |
| Week 6 | Final Analysis | Stakeholder presentation and reflection |
## Dataset

**Source:** UCI Machine Learning Repository — Heart Disease

The Cleveland dataset contains **303 records** and **13 commonly used analytical features**, including demographic, physiological, and diagnostic variables.

The original target is represented on a 0–4 scale. For binary classification experiments in this project:

- `0` → no disease
- `1–4` → disease present

Target counts and missing-value statistics are generated from the exact dataset used by the notebooks rather than being hard-coded as project results.

**DOI:** 10.24432/C52P4X

## Business / Analytical Problem

Healthcare organisations generate complex clinical datasets containing demographic, physiological, and diagnostic information.

The analytical challenge addressed in this project is:

> How can patient-level clinical and demographic variables be analysed to identify patterns associated with heart-disease status while maintaining data quality, reproducibility, and responsible interpretation?

The project focuses on analytical decision support rather than clinical diagnosis.

---

### Example variables

- Age
- Sex
- Chest-pain type
- Resting blood pressure
- Cholesterol
- Fasting blood sugar
- Resting ECG
- Maximum heart rate
- Exercise-induced angina
- ST depression
- Slope
- Number of major vessels
- Thalassemia-related variable

---

## Project Workflow

The project follows an end-to-end healthcare analytics workflow:

1. Data Analysis Planning
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis
4. Data Visualization
5. Predictive Analytics Planning
6. Data Quality Assurance
7. Compliance and Ethical Review
8. Final Analysis and Reflection

---

## Analytical Evidence

The notebooks generate dataset-specific descriptive statistics,
data-quality checks, visualizations, and predictive-model evaluation
metrics directly from the project dataset.

This repository does not hard-code model performance or present
secondary-source statistics as project-generated results.

Key outputs include:

- Dataset structure and descriptive statistics
- Missing-value and duplicate analysis
- Target distribution
- Numerical feature distributions
- Categorical feature analysis
- Correlation analysis
- Confusion matrices
- ROC curves
- Classification metrics

## Data Quality

Data-quality controls include:

- Missing-value analysis
- Duplicate detection
- Data-type validation
- Numerical range checks
- Categorical consistency checks
- Target validation
- Transformation tracking
- Data provenance
- Reproducibility checks
- Data leakage prevention

The project also includes a formal quality-assurance workflow and risk-management framework.

---

## Visualization

The project uses visualization techniques appropriate to the variable type and analytical question.

Examples include:

- Target-distribution charts
- Bar charts
- Histograms
- Box plots
- Correlation heatmaps
- Confusion matrices
- ROC curves
- Dashboard-style reporting

Visualization decisions are justified according to audience, data type, readability, and analytical purpose.
## Technical Skills Demonstrated

**Programming:** Python, Pandas, NumPy, scikit-learn

**Data Analytics:** Data cleaning, EDA, statistical summaries,
feature analysis, classification

**Visualization:** Matplotlib, Seaborn, Power BI, Excel

**Machine Learning:** Logistic Regression, Decision Trees,
Random Forest, model evaluation

**Data Quality:** Missing-value analysis, validation,
data integrity, leakage prevention, reproducibility

**Healthcare Analytics:** Privacy, ethics, governance,
compliance awareness, responsible reporting
**Version Control:** Git, GitHub, repository organization

---

## Predictive Analytics

Potential classification approaches include:

- Logistic Regression
- Decision Tree
- Random Forest

Evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1-score
- Specificity
- ROC-AUC
- PR-AUC

Model performance is only reported when reproduced from the project's actual modelling pipeline.

---

## Technical Skills Demonstrated

### Programming & Analytics

- Python
- Pandas
- NumPy
- scikit-learn
- Jupyter Notebook

### Data Analysis

- Data cleaning
- Missing-value analysis
- Exploratory data analysis
- Statistical summaries
- Feature analysis
- Classification methodology

### Visualization

- Matplotlib
- Seaborn
- Power BI
- Excel
- Dashboard design

### Data Governance

- Data-quality assurance
- Validation rules
- Risk management
- Compliance awareness
- Reproducibility
- Documentation

### Version Control

- Git
- GitHub
- Repository organization
- Versioned documentation

---

## Healthcare Data Responsibility

This project treats healthcare analytics as a high-responsibility analytical domain.

The methodology considers:

- Privacy
- Data minimisation
- Human oversight
- Bias and representation
- Transparency
- Responsible visualization
- Data security
- Reproducibility
- Avoidance of unsupported clinical claims

The project is educational and analytical and should not be interpreted as a clinical diagnostic system.

---

## Project Deliverables

### Week 1
Data Analysis Planning and Strategy

### Week 2
Data Cleaning and Preprocessing Methodology

### Week 3
Data Visualization and Reporting

### Week 4
Predictive Analytics Strategy and Modeling Plan

### Week 5
Data Quality Assurance and Compliance Analysis

### Week 6
Final Data Analysis Presentation and Reflection

---

## Repository Structure

```text

healthcare-data-analysis-planning-strategy/

├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   │   └── README.md
│   └── processed/
│       └── README.md
│
├── docs/
│   ├── Week 1 ...
│   ├── Week 2 ...
│   ├── Week 3 ...
│   ├── Week 4 ...
│   ├── Week 5 ...
│   └── Week 6 ...
│
├── figures/
│   ├── Week 2 ...
│   ├── Week 3 ...
│   ├── Week 4 ...
│   ├── Week 5 ...
│   └── Week 6 ...
│
├── notebooks/
│   ├── 01_heart_disease_eda.ipynb
│   └── 02_heart_disease_modeling.ipynb
│
└── src/
    ├── __init__.py
    ├── data_loader.py
    ├── preprocessing.py
    ├── modeling.py
    └── metrics.py
