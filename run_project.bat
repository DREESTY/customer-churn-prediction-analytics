@echo off
echo === Customer Churn Prediction & Retention Analytics ===
echo.
python src\make_eda.py
python src\train_model.py
echo.
echo Done. Open data\processed and outputs\figures.
pause
