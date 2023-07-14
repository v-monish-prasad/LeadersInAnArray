def findLeadersInAnArray(array):
    if not array:
        return "Empty Array."

    maximum = array[-1]
    maxArray = [array[-1]]

    for i in range(len(array) - 2, -1 , -1):
        if array[i] > maximum:
            maximum = array[i]
            maxArray.append((array[i]))

    return maxArray[::-1]


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    print(findLeadersInAnArray(array))
