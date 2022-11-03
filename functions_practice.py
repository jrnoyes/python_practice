def hello():
    print("Hello!")

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(list):
    if len(list) == 0:
        print("my lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[0]}")
            else:
                print(f"Next I eat{list[i]}")

hello()
print(pack("arg1", "arg2", "arg3"))
eat_lunch([])