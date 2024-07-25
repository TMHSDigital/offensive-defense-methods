import numpy as np
from sklearn.ensemble import IsolationForest

# Generate synthetic data for demonstration
X = np.random.rand(100, 2)
X_outliers = np.random.uniform(low=-1, high=1, size=(20, 2))
X = np.concatenate([X, X_outliers], axis=0)

# Fit the model
clf = IsolationForest(random_state=42, contamination=0.1)
clf.fit(X)

# Predict anomalies
y_pred = clf.predict(X)

# Output the results
for i, pred in enumerate(y_pred):
    if pred == -1:
        print(f"Anomaly detected at index {i}: {X[i]}")
