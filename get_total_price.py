def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits total price
    """
    row=data.split('\n')[1:]
    values=[]
    sums=0
    for i in range(len(row)):
        sums+=(float(row[i].split(',')[1]))
    return sums
    
data = open('fruits.csv').read()

print(get_total_price(data))

    