import pandas as pd

def check_exposure(user_input):
    df = pd.read_csv("data/simulated_breaches.csv")
    matches = df[df["keyword"].str.contains(user_input, case=False, na=False)]
    return matches
