def print_triangle(n):
    if n > 0:
        print_triangle(n - 1)
        for i in range(n):
            print('*', end="")
        print()


def print_oposite_triangles(n):
    if n > 0:
        for i in range(n):
            print('*', end="")
        print()
        print_oposite_triangles(n - 1)
        for i in range(n):
            print('*', end="")
        print()


def print_ruler(n):
    if n > 0:
        print_ruler(n - 1)
        for i in range(n):
            print('-', end="")
        print()
        print_ruler(n - 1)


# print_triangle(4)
# print_oposite_triangles(4)
# print_ruler(4)

