from util.input_generator import generate_random_list
from util.stop_watch import stop_watch


@stop_watch
def sort(input_list: list) -> list:
    """入力されたリストをソートする"""
    work_list = input_list.copy()
    for i in range(len(work_list)):
        if i == 0:
            continue
        else:
            for j in reversed(range(0, i)):
                if work_list[i] < work_list[j]:
                    work_list[i], work_list[j] = work_list[j], work_list[i]
                    i = j
                else:
                    break
    return work_list


if __name__ == "__main__":
    target_list = generate_random_list(1000)
    result_list = sort(target_list)

    print(f"Result list: {result_list}")
