import pickle
import pandas as pd

#load model
def main():
    with open(r"C:\\python calismalar\\modeli_cikarma\\diamond_model_complete.pkl", "rb") as f:
        saved_data = pickle. load(f)

    model = saved_data["model"]
    X_test_scaled = pd.read_csv(r"C:\\python calismalar\\modeli_cikarma\\diamond_testdatascaled.csv")
    print(model.predict(X_test_scaled))

if __name__ =="__main__":
    main()