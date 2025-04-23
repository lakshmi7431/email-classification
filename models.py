import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib

def train_model():
    # Load your dataset
    data = pd.read_csv('emails.csv')  # Replace with your dataset path
    X = data['email_body']
    y = data['category']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train a model
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, 'your_model.pkl')

if __name__ == "__main__":
    train_model()