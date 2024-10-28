import sys
from pathlib import Path 
from colorama import Fore, Style, init

init(autoreset=True) 

def display_directory_structure(directory_path, indent=""):
    try:
        for item in directory_path.iterdir():
            if item.is_dir():
                # Виведення директорії зеленим кольором
                print(f"{indent}{Fore.GREEN}📂 {item.name}")
                # Рекурсивний виклик для відображення вмісту піддиректорії
                display_directory_structure(item, indent + "    ")
            else:
                # Виведення файлу синім кольором
                print(f"{indent}{Fore.BLUE}📜 {item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Немає доступу до {directory_path}")

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії як аргумент.")
        sys.exit(1)
    directory_path = Path(sys.argv[1])
    if not directory_path.exists() or not directory_path.is_dir():
        print("Вказаний шлях не існує або не є директорією.")
        sys.exit(1)
    print(f"{Fore.YELLOW}Структура директорії {directory_path}:\n")
    display_directory_structure(directory_path)

if __name__ == "__main__":
    main()


