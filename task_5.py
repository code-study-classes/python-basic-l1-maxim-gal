load = [10, 50, 20, 80, 30, 90, 40, 60, 10, 20]
print("Исходная нагрузка:", load)

smoothed_load = []

for i in range(len(load) - 2):
    a = load[i]
    b = load[i+1]
    c = load[i+2]
    
    total = a + b + c
    
    average = int(total / 3)
    
    smoothed_load.append(average)

print("Сглаженный тренд:", smoothed_load)