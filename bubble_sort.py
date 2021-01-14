from util.input_generator import generate_random_list

if __name__ == "__main__":
    target_list = generate_random_list(1000)

    for i in range(len(target_list)):
        if i == 0:
            continue
        else:
            for j in reversed(range(0, i)):
                if target_list[i] < target_list[j]:
                    target_list[i], target_list[j] = target_list[j], target_list[i]
                    i = j
                else:
                    break

    print(f"Result list: {target_list}")
