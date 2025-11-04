import time
# import numpy
import pandas as pd
import pynput

data = {
    "a":[1,2,3,4,5],
    "b":[5,3,6,2,2],
    "c":[9,9,2,2,2]
}
df = pd.DataFrame(data)

print(df)
time.sleep(2)

def pirnt():
    print("Hello world2")
def main():

    with pynput.keyboard.GlobalHotKeys({
        '<f11>': pirnt()

    }) as h:
        h.join()      

if __name__ == "main":
    main()


