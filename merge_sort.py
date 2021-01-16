from util.input_generator import generate_random_list
from util.stop_watch import stop_watch


def merge(left_sorted: list, right_sorted: list) -> list:
    """2つのリスト要素を整列して1つのリストにする"""
    result = []

    while len(left_sorted) > 0 and len(right_sorted) > 0:
        if left_sorted[0] < right_sorted[0]:
            result.append(left_sorted[0])
            left_sorted = left_sorted[1:]
        else:
            result.append(right_sorted[0])
            right_sorted = right_sorted[1:]

    if len(left_sorted) > 0:
        result.extend(left_sorted)
    else:
        result.extend(right_sorted)

    return result


def merge_sort(input_list: list) -> list:
    """入力されたリストをソートする"""
    center_index = int(len(input_list) / 2)
    left, right = input_list[:center_index], input_list[center_index:]

    left_sorted = left if len(left) == 1 else merge_sort(left)
    right_sorted = right if len(right) == 1 else merge_sort(right)
    return merge(left_sorted, right_sorted)


@stop_watch
def sort(input_list: list) -> list:
    return merge_sort(input_list)


if __name__ == "__main__":
    target_list = generate_random_list(10)
    result_list = sort(target_list)

    print(f"Result list: {result_list}")
