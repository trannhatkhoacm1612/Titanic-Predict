from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Generate some fake data
X = np.random.rand(100,2)
y = np.random.randint(0,2,100)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize and fit the model
clf = LogisticRegression().fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the predictions
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)