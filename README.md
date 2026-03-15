# Predicting a Composite Player Performance Index

Machine learning project using season-level soccer statistics from the Big 5 European leagues to predict a constructed player performance index.

---

## Project Summary

This project explores how well player-level season statistics can predict a broader summary of on-field performance. Instead of relying on a single metric like goals or assists, I built a composite **performance index** from multiple standardized statistics and compared several supervised regression models to predict it.

The final dataset included **1,072 outfield players** after filtering out goalkeepers and players with fewer than 900 minutes played.

---

## Why This Project Matters

Player evaluation is a multidimensional problem. In practice, scouting and recruitment decisions often require combining attacking output, efficiency, defensive contributions, and overall involvement rather than relying on one statistic.

This project demonstrates how to:
- clean and preprocess sports data
- engineer a custom target variable
- compare multiple machine learning models
- evaluate predictive performance using train/test splits and cross-validation

---

## Methodology

### Data Source
- Kaggle: *Football Players Stats 2025–2026*
- Based on FBref data from the Big 5 European leagues

### Preprocessing
- removed goalkeepers
- filtered players with fewer than 900 minutes
- cleaned missing values
- built a final model-ready dataset

### Target Variable
The response variable was a constructed **performance index** based on:
- Goals
- Assists
- Shots on target per 90
- Goals per shot
- Tackles won
- Interceptions
- Fouls drawn

These features were standardized and averaged to create a continuous season-level performance measure.

### Models Compared
- Linear Regression
- KNN Regression
- Ridge Regression
- Random Forest Regression

### Validation Strategy
- 80/20 train-test split
- 5-fold cross-validation on the training set
- evaluation using RMSE, MAE, and R²

---

## Results

**Best model:** Linear Regression

| Model | Test RMSE |
|------|----------:|
| Linear Regression | **0.3124** |
| Ridge Regression | 0.3143 |
| Random Forest | 0.3288 |
| KNN Regression | 0.3693 |

The results suggest that the selected predictors captured the constructed performance index well using a relatively simple linear relationship.

---

## Key Takeaways

- Linear regression outperformed more flexible models on this dataset
- Ridge regression performed almost identically, suggesting limited benefit from regularization
- Random forest was competitive but did not beat the linear models
- KNN regression produced the weakest predictive performance
- The project shows how domain-specific feature engineering and careful model comparison can produce useful predictive insight from sports data

---

## Skills Demonstrated

- Data cleaning and preprocessing
- Feature engineering
- Composite metric construction
- Supervised machine learning
- Cross-validation and model selection
- Regression model comparison
- Data visualization
- Reproducible analysis in R Markdown

---

## Future Improvements

- add multiple seasons of player data
- build position-specific performance indices
- expand the feature set with passing and defensive metrics
- extend the project into a squad-fit or recruitment recommendation tool

---

## Tech Stack

**Python**
- pandas
- scikit-learn

**R**
- tidyverse
- tidymodels
- glmnet
- ranger
- kknn
- plotly

---

## Project Files

- `finalProject131/finalProject131.Rmd` — full written report
- `finalProject131/finalProject131.html` — knitted report output
- `python/data.py` — preprocessing and performance index construction
- `data/processed/model.csv` — final model-ready dataset
- `docs/codebook.txt` — variable definitions

---

## Author

**Kaydon Lee**
