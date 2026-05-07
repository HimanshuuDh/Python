from functools import total_ordering

def file_to_list(file_name):
    data=[]


    try:
        file = open(file_name)
        for line in file:
            data.append(float((line)))

    except Exception as e:
        print("ERROR: ",str(e))
        return -1
    finally:
        file.close()

        return data

def compute_avg(data):
    total=0
    for item in data:
        total+=item
    avg=total/len(data)
    return avg

def main():
    rain_data=file_to_list("rainfall.txt")
    if rain_data==-1:
        print("no rainfall values found")
        return

    rainfall_avg=compute_avg(rain_data)
    print("rainfall_avg:",rainfall_avg)

main()