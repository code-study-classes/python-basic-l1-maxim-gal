import random

nums = [random.randint(1, 100) for _ in range(random.randint(7, 10))]
print("Исходные баллы:", nums)

min_num = min(nums)
max_num = max(nums)
print(f"Удаляем минимум ({min_num}) и максимум ({max_num}).")

nums_copy = nums.copy()
nums_copy.remove(min_num)
nums_copy.remove(max_num)

print("Оставшиеся баллы:", nums_copy)

average = sum(nums_copy) / len(nums_copy)
print(f"Средний рейтинг: {average}")