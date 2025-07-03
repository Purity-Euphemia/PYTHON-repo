def main():
    scores = [[78, 45, 70, 59], [33, 80, 56, 47], [54, 20, 67]]
    for index, score in enumerate(scores):
        print(index) # to get the index of each list

def main():
    scores = [[78, 45, 70, 59], [33, 80, 56, 47], [54, 20, 67]]
    for index, score in enumerate(scores):
        for inner_index, inner_value in enumerate(score):
            print(f"index value: ", inner_value, end='\t')
            print(f"inner list: ", inner_index)

            print(f"inner list: ", score, end='\t')
            print(f"inner list index: ", index)


if __name__ == '__main__':
    main()

    days_per_month = {'january': 31, 'february': 28, 'march': 30, 'april': 31,}
    for month, days in days_per_month.items():
        print(f"{month}: {days}")
    for month_name in days_per_month.keys():
        print(month_name)
    for number_of_days in days_per_month.values():
        print(number_of_days)



number_dic = {1: "one", 2: "two", 3: "three", 4: "four", 5: "six"}
print(number_dic[3])

number_dic[5] = "five"
print(number_dic)

number_dic[7] = "seven"
print(number_dic)

del number_dic[4]
print(number_dic)















