def summer(listi):
    try:
        for a in listi:
            if isinstance(a, str):
                new_list = "".join(listi)
            if isinstance(a, int):
                new_list = sum(listi)
        print(new_list)
        return new_list
    except TypeError:
        print("can't add string and number")

summer(["a", "b", "c"])
summer([1,3,10])
summer(["ag", "tr", "h"])
summer([1, "tr", "h"])