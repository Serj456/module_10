from multiprocessing import Pool
import time
def read_info(name):
    all_data_ = open('all_data','w')
    with open(name, 'r') as file:
        for i in file.readlines():
            all_data_.write(i)
    all_data_.close()

list_file = ['file 1.txt','file 2.txt','file 3.txt','file 4.txt']

start1 = time.time()
for i in list_file:
    read_info(i)
end1 = time.time()
work_time = end1 - start1
print(work_time)

start2 = time.time()
if __name__ == '__main__':
    with Pool(4) as p:
        p.map(read_info, list_file)
end2 = time.time()
work_time_multi = end2 - start2
print(work_time_multi)