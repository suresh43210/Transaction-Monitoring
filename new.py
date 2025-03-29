import pickle
from joblib import dump

# Load the model from the .pkl file
with open(
    "/Users/sureshneupane/Documents/suresh/data-analysis/Transaction-Monitoring/final_model.pkl",
    "rb",
) as f:
    model = pickle.load(f)

# Save the model as .joblib
dump(
    model,
    "/Users/sureshneupane/Documents/suresh/data-analysis/Transaction-Monitoring/final_model.joblib",
)
print("Model saved as final_model.joblib")
