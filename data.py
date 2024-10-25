from pathlib import Path

def total_salary(path):
    try: 
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file: 
                try:
                    name, salary = line.strip().split(',')
                    salaries.append(float(salary))
                except ValueError:
                    print(f"Помилка у рядку: {line.strip()}")
                    continue
            
            if not salaries:
                return (0, 0)
            
            total = sum(salaries)
            average = total / len(salaries) 
            return total, average 
    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return (0, 0)

total, average = total_salary("/Users/mac/Desktop/goit-algo-hw-04/salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")