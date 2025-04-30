
def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5, 67, 32)")
    return 

def get_user_input():
    x = input()
    list = x.split(',')
    floatlist = [float(num) for num in list]
    print(floatlist)
    return floatlist

def calc_average(floatlist):
    average = sum(floatlist) / len(floatlist)
    print(average)
    return average

def find_min_max(floatlist):
    if len(floatlist)== 0:
        print("No numbers provided.")
        return None , None
    min_temp = min(floatlist)
    max_temp = max(floatlist)
    print("Minimum Temperature:", min_temp)
    print("Maximum Temperature:", max_temp)
    return min_temp , max_temp

def sort_temperature(floatlist):
    sorted_list = sorted(floatlist)
    print("Sorted Temperatures:", sorted_list)
    return sorted_list

def calc_median_temperature(floatlist, sorted_list):
    if len(floatlist) == 0:
        print("No numbers provided.")
        return None
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_list[mid -1] + sorted_list[mid])/2
    else:
        median = sorted_list[mid]
    print("Median Temperature:", median)
    return median
    

def main():
    display_main_menu()
    floatlist = get_user_input()
    calc_average(floatlist)
    find_min_max(floatlist)
    sorted_list = sort_temperature(floatlist)
    calc_median_temperature(floatlist, sorted_list)

if __name__ == "__main__":
    main()
