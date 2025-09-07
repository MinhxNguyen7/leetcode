#
# Complete the 'processRequestQueueOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY operations
#  2. INTEGER_ARRAY values
#


def move_to_outstack_conditional(in_stack: list[int], out_stack: list[int]) -> None:
    """
    Moves all values of `in_stack` into `out_stack` in reverse order if `out_stack` is empty.
    Otherwise, does nothing.
    """
    if out_stack:
        return

    while in_stack:
        out_stack.append(in_stack.pop())


def processRequestQueueOperations(operations: list[str], values: list[int]):
    in_stack: list[int] = []
    out_stack: list[int] = []

    result: list[int] = []

    for operation, value in zip(operations, values):
        match operation:
            case "size":
                result.append(len(in_stack) + len(out_stack))

            case "enqueue":
                in_stack.append(value)

            case "peek":
                move_to_outstack_conditional(in_stack, out_stack)
                result.append(out_stack[-1])

            case "dequeue":
                move_to_outstack_conditional(in_stack, out_stack)
                result.append(out_stack.pop())

    return result


if __name__ == "__main__":
    print(
        processRequestQueueOperations(
            ["enqueue", "enqueue", "peek", "dequeue", "size", "dequeue"],
            [5, 3, 0, 0, 0, 0],
        )
    )  # [5, 5, 1, 3]
