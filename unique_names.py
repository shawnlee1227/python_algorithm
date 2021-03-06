def unique_names(names1, names2):
    ns = set(names1 + names2)
    nl = list(ns)
    return nl

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2))