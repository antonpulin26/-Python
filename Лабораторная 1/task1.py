numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

num_sum = sum(numbers[0:4])+sum(numbers[5:])
num_len = len(numbers)
num_avg = num_sum/num_len
numbers[4]=num_avg

print("Измененный список:", numbers)
