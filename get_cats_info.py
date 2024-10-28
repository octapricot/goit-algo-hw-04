def get_cats_info(path):
    cats_info = []
    try: 
        with open(path, 'r', encoding='utf-8') as file: 
            for line in file: 
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_info = {
                        "id": cat_id, 
                        "name": name, 
                        "age": age
                    }
                    cats_info.append(cat_info)
                except ValueError:
                    print("Помилилась в рядку {line.strip()}")
                    continue
        return cats_info
    
    except FileNotFoundError:
        print(f"Файл у {path} відсутній")
        return []
    except Exception as e:
        print(f"Помилка виникла тут: {e}")
        return []
    
cats_info = get_cats_info("/Users/mac/Desktop/goit-algo-hw-04/cats_info.txt")
print(cats_info)