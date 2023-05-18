"""
Q7.3 Answer.
"""

if __name__ == '__main__':
    list1 = ["I like", "I love"]
    list2 = ["pancakes.", "kiwi juice.", "espresso."]

    print("\n".join((f"{prefix} {suffix}" for prefix in list1 for suffix in list2)))
