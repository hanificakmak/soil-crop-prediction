# soil-crop-prediction

# Sowing Success: How Machine Learning Helps Farmers Select the Best Crops

<img src="farmer_in_a_field.jpg" alt="Farmer in a field" width="530" height="354">

Measuring essential soil metrics such as nitrogen, phosphorous, potassium levels, and pH value is an important aspect of assessing soil condition. However, it can be an expensive and time-consuming process, which can cause farmers to prioritize which metrics to measure based on their budget constraints.

Farmers have various options when it comes to deciding which crop to plant each season. Their primary objective is to maximize the yield of their crops, taking into account different factors. One crucial factor that affects crop growth is the condition of the soil in the field, which can be assessed by measuring basic elements such as nitrogen and potassium levels. Each crop has an ideal soil condition that ensures optimal growth and maximum yield.

A farmer reached out to you as a machine learning expert for assistance in selecting the best crop for his field. They've provided you with a dataset called soil_measures.csv, which contains:
<ul>
  <li>"N": Nitrogen content ratio in the soil</li>
  <li>"P": Phosphorous content ratio in the soil</li>
  <li>"K": Potassium content ratio in the soil</li>
  <li>"pH" value of the soil</li>
  <li>"crop": categorical values that contain various crops (target variable).</li>
</ul>

Each row in this dataset represents various measures of the soil in a particular field. Based on these measurements, the crop specified in the "crop" column is the optimal choice for that field.

In this project, you will build multi-class classification models to predict the type of "crop" and identify the single most importance feature for predictive performance.
