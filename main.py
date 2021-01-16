from packages.util.input_generator import generate_random_list
from packages.sort import bubble_sort, merge_sort, quick_sort, sleep_sort

if __name__ == "__main__":
    target_list = generate_random_list(100)

    # スリープソート激重注意(なんかおかしくないか？)
    result_list_sleep = sleep_sort.sort(target_list)
    result_list_bubble = bubble_sort.sort(target_list)
    result_list_merge = merge_sort.sort(target_list)
    result_list_quick = quick_sort.sort(target_list)

    # スリープソート激重注意(なんかおかしくないか？)
    print(result_list_sleep == result_list_bubble ==
          result_list_merge == result_list_quick)
    print(result_list_quick)
