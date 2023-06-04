"""
Q12.3 Answer.
"""
import pandas as pd

if __name__ == '__main__':
    p_car = pd.DataFrame(
        {
            "name": [chr(ch) for ch in range(ord('A'), ord('G') + 1)],
            "horse power": [130, 250, 190, 300, 210, 220, 170],
            "weight": [1900, 2600, 2200, 2900, 2400, 2300, 2200],
            "efficiency": [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2]
        }
    ).set_index("name")
    q_car = pd.DataFrame(
        {
            "name": ["A", "B", "C", "D"],
            "horse power": [120, 220, 120, 200],
            "weight": [1900, 2100, 1500, 2900],
            "efficiency": [18.3, 19.2, 21.1, 17.3]
        }
    ).set_index("name")

    print("\n===1===")
    print(q_car)

    print("\n===2===")
    print(pd.concat([p_car, q_car]))

    print("\n===3===")
    p_car["com"] = "P"
    q_car["com"] = "Q"
    print(pd.concat([p_car, q_car]))

    print("\n===4===")
    print(pd.DataFrame(
        {
            "com": ["P", "Q"],
            "avg": [
                (p_car["horse power"] * p_car["efficiency"]).mean(),
                (q_car["horse power"] * q_car["efficiency"]).mean()
            ]
        }
    ).set_index("com"))
