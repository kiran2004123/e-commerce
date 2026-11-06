import numpy as np
import pandas as pd

data = {
    "p_id": [101, 102, 103],
    "name": ["Lap", "Mouse", "Keyboard"],
    "price": [50000, 500, 1200],
    "q_avail": [20, 100, 50],
}

avail = pd.DataFrame(data)


cart =[]
def dis_catalog(data):
    print(avail)


def add_cart(p_id):
    temp = {}
    temp.add(q_avail['p_id','price'])

    carts.add(temp)

def check_out(cart):
    total =0
    for i in cart:
        total+=i['prices']

    return total

