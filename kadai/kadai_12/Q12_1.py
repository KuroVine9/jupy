"""
Q12.1 Answer.
"""
import pandas as pd

if __name__ == '__main__':
    w = pd.read_csv("../../resource/csv/weather.csv", encoding="EUC_KR", index_col=0)
    print("\n===1===")
    print(w.head())
    print(w.tail())

    print("\n===2===")
    print(w.loc["2015-06-06"])

    print("\n===3===")
    print(w["평균기온"].max())

    print("\n===4===")
    print(w[w["평균기온"] == w["평균기온"].max()])

    print("\n===5===")
    print(w[w["평균기온"] > 30.0])
