def get_smallest_integer(my_list):
    smallest = my_list[0]
    for n in my_list:
        if n < smallest:
            smallest = n
    return smallest


if __name__ == "__main__":
    my_list = [4, 14, 23, 94, 27, 24, 32]
    smallest = get_smallest_integer(my_list)
    print(f"The smallest integer in the list is: {smallest}")    