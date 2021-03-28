
def reformatDate(date):
    arr = date.split('/')
    if(len(arr) == 3):
        if len(arr[2]) < 4:
            return arr[0]+'/'+arr[1]+'/20'+arr[2]
    else:
        return "1/1/1970"
    return date

print(reformatDate("12/3/21"))
print(reformatDate("12/3/2021"))
