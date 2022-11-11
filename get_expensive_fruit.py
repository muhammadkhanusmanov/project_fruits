def get_expensive_fruit(data:str)->str:
    """
    This function returns the name of the most expensive fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the most expensive fruit
    """
    row=data.split('\n')[1:]
    values=[]
    ids=[]
    for i in range(len(row)):
        values.append(float(row[i].split(',')[1]))
        ids.append(row[i].split(',')[0])
    m=values[0]
    for j in values:
        if m<j:
            m=j
    idindex=values.index(m)

    return ids[idindex]



    # your code here
f = open('fruits.csv').read()
print(get_expensive_fruit(f))

