#Задача "Многопроцессное считывание"
import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            if line != "":
                all_data.append(line)
            else:
                break

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start1 = datetime.datetime.now()

for file in filenames:
    read_info(file)

end1 = datetime.datetime.now()
print(end1 - start1) #0:00:06.694201

# Многопроцессный

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)
    #0:00:03.030173





