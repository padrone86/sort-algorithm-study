from util.input_generator import generate_random_list
from util.stop_watch import stop_watch


def get_pivot_item(input_list: list) -> list:
    """
    リスト内の先頭要素から二つの異なる要素を取り出し、大きい方を軸要素として返却する。
    すべて同じ値の時はNoneを返す。
    """
    pivot_item = None
    for item in input_list:
        if pivot_item == None:
            pivot_item = item
        elif pivot_item < item:
            return item
        elif pivot_item == item:
            continue
        else:
            return pivot_item

    return None


def quick_sort(input_list: list, pivot_item) -> (list, list):
    """指定された軸要素を使いクイックソートでソートしたリストを返す"""
    if pivot_item == None:
        return input_list
    else:
        pivot_item_count = 0
        left, right = [], []

        for item in input_list:
            if item < pivot_item:
                left.append(item)
            elif item > pivot_item:
                right.append(item)
            else:
                pivot_item_count += 1

        left = quick_sort(left, get_pivot_item(left))
        right = quick_sort(right, get_pivot_item(right))

        return left + [pivot_item] * pivot_item_count + right


@stop_watch
def sort(input_list: list) -> list:
    """入力されたリストをソートする"""
    return quick_sort(input_list, get_pivot_item(input_list))


if __name__ == "__main__":
    target_list = generate_random_list(10)
    result_list = sort(target_list)

    print(f"Result list: {result_list}")
