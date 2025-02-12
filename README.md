Here's the updated **README.md** with **Binning** included in the data preprocessing section:  

---

# Heart Disease Prediction using Random Forest  

## Project Overview  
This project aims to predict heart disease using the **Random Forest Classifier**. It uses the **Heart Disease 2020 Cleaned dataset**, performs data preprocessing (including binning), and applies machine learning to classify individuals based on their health attributes.  

---

## Dataset  
The dataset used is `heart_2020_cleaned.csv`, which contains health-related features like age, BMI, smoking habits, physical activity, and general health condition. The target variable is `HeartDisease`, indicating whether a person has heart disease (`Yes` or `No`).  

---

## Data Preprocessing  
1. **Handling Categorical Data**: Encoded categorical variables using `LabelEncoder`.  
2. **Replacing Values**: Converted `Yes/No` responses into `1/0`, transformed age ranges into numerical values.  
3. **Feature Scaling**: Used `MinMaxScaler` to normalize numerical data.  
4. **Binning**: Applied binning on continuous features like `BMI` and `AgeCategory` to reduce noise and group values into intervals.  
   - **AgeCategory** was binned into ranges such as `Young`, `Middle-aged`, and `Senior`.  
   - **BMI** was grouped into categories like `Underweight`, `Normal`, `Overweight`, and `Obese`.  
5. **Feature Selection**: Selected correlated features based on Pearson correlation.  

---

## How Random Forest Works  
Random Forest is an ensemble learning method that operates by constructing multiple decision trees during training and outputs the class that is the mode of the classes predicted by individual trees.  

Key steps:  
1. **Bootstrapping**: The algorithm selects multiple random subsets of data to train decision trees.  
2. **Feature Selection**: Each tree is trained on a random subset of features, ensuring diversity.  
3. **Voting Mechanism**: For classification tasks, the final prediction is determined by majority voting.  
4. **Averaging**: For regression, the final prediction is the average of outputs from individual trees.  

---

## Pros and Cons of Random Forest  

### **Pros**  
- **High Accuracy**  
- **Handles Missing Values**  
- **Feature Importance**  
- **Resistant to Noise**  
- **Scales Well with Large Datasets**  

### **Cons**  
- **Computationally Expensive**  
- **Harder to Interpret**  
- **Slow Prediction Time**  
- **Possible Overfitting**  

---

## Model Training  
- **Random Forest Classifier** with `100` estimators.  
- Dataset split: **70% Training, 30% Testing**.  
- **Accuracy Achieved**: **91.2%**  

---

## How to Run the Project  

### Prerequisites  
Ensure you have Python installed along with the required dependencies.  

### Install Dependencies  
```bash  
pip install pandas numpy scikit-learn  
```  

### Run the Notebook  
1. Navigate to the `src` folder.  
2. Open `index.ipynb` in Jupyter Notebook.  
3. Run the notebook cells step by step.  

---

## Model Evaluation  
- **Metric Used**: Accuracy Score  
- **Accuracy Achieved**: `91.2%`  

---

## Repository Structure  
```
|-- data/                    # Folder containing dataset  
|   |-- heart_2020_cleaned.csv  
|  
|-- src/                     # Folder containing source code  
|   |-- index.ipynb  
|  
|-- model/                   # Folder containing trained model  
|   |-- saved_model.pkl  
|  
|-- README.md                # Documentation  
```  

---

## Future Improvements  
- Implement other classifiers like Logistic Regression and SVM for comparison.  
- Optimize feature selection to improve performance.  
- Deploy the model using Flask or Streamlit for real-world applications.  

---

## Author  
**Safwan Ali** – Data Science Enthusiast  

### Connect with Me  
- **GitHub**: [Safwan2003](https://github.com/Safwan2003)  
- **LinkedIn**: [Safwan Ali](https://www.linkedin.com/in/safwan-ali-281aa1275/)  

---
