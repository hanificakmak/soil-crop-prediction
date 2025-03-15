# All required libraries are imported here for you.
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import f1_score

# Load the dataset
crops = pd.read_csv("soil_measures.csv")

# Check missing values
print(crops.isna().sum())

# Check unique values to decide it is multi-classification or binary
print(crops["crop"].unique())

# Define independent variables X and target variable y
X = crops.drop("crop", axis=1)
y = crops["crop"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify = y)

# Dictionary to store performance results of the features
features_dict = {}

# Evaluate each feature
for feature in ["N", "P", "K", "ph"] :
    log_reg = LogisticRegression(max_iter=100, multi_class="multinomial")
    
    # Train the model only one feature
    log_reg.fit(X_train[[feature]], y_train)
    
    # Make predictions
    y_pred = log_reg.predict(X_test[[feature]])
    
    # Calculate F1-score
    f1 = f1_score(y_test, y_pred, average = "weighted")
    
    # Store the result in the dictionary
    features_dict[feature] = f1

    # Print the F1-score for the feature
    print(f"F1-score for {feature}: {f1:.4f}")
    
# Identify the best predictive feature
best_feature = max(features_dict, key=features_dict.get)
best_score = features_dict[best_feature]

# Store the best feature and its performance
best_predictive_feature = {best_feature: best_score}

# Print the best predictive feature
print(f"Best predictive feature: {best_predictive_feature}")
