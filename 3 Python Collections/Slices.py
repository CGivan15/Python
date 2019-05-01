def first_4(List):
    list_copy = List[:]
    print(list_copy[0:4])
    return


def first_and_last_4(List):
    list_copy = List[:]
    result = list_copy[0:4] + list_copy[-4:]
    print(result)
    return


def odds(List):
    list_copy = List[:]
    print(list_copy[1::2])
    return


def reverse_evens(List):
    list_copy = List[0::2]
    print(list_copy[-1::-1])
    return


def sillycase(String):
    half = round(len(String)/2)
    print(String[:half].lower() + String[half:].upper())
    return


List_Nums = [1,2,3,4,5]
name = "Treehouse"

List_Nums)
first_4(List_Nums)
first_and_last_4(List_Nums)
odds(List_Nums)
reverse_evens(List_Nums)
sillycase(name)