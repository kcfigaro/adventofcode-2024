def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    list1, list2 = [], []
    for line in lines:
        item1, item2 = line.strip().split()
        list1.append(item1)
        list2.append(item2)
    return list1, list2

def calculate_difference_sum(list1, list2):
    total_difference = 0
    for item1, item2 in zip(sorted(list1), sorted(list2)):
        total_difference += abs(int(item1) - int(item2))
    return total_difference

def count_common_items(list1, list2):
    from collections import Counter
    counter2 = Counter(list2)
    common_items_sum = 0
    for item in list1:
        if item in counter2:
            common_items_sum += int(item) * counter2[item]
    return common_items_sum

if __name__ == "__main__":
    file_path = './example.txt'
    list1, list2 = read_input(file_path)
    difference_sum = calculate_difference_sum(list1, list2)
    print(f"difference_sum: {difference_sum}")
    common_items_sum = count_common_items(list1, list2)
    print(f"sum of (common items x frequents): {common_items_sum}")
