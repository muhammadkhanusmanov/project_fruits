def get_frutis_name(data:str)->list:
    """
    This function returns the name of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits names
    """
    row=data.split('\n')[1:]
    fruits=[]
    for i in range(len(row)):
        fruits.append(row[i].split(',')[0])

    return fruits

data = open('fruits.csv').read()

print(get_frutis_name(data))

    