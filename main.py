from packages.util.input_generator import generate_random_list
from packages.sort import bubble_sort, merge_sort, quick_sort

if __name__ == "__main__":
    target_list = generate_random_list(10000)

    result_list_bubble = bubble_sort.sort(target_list)
    result_list_merge = merge_sort.sort(target_list)
    result_list_quick = quick_sort.sort(target_list)

    print(result_list_bubble)
