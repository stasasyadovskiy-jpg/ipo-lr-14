import ImageEditor as img
def main():
    handler = None
    while True:
        img.clear_screen()
        img.print_menu()
        try:
            choice = int(input("\nВыберите операцию (1-11): "))
        except ValueError:
            print("Идиот от 1 до 11 выбери")
            input("\nНажмите Enter для продолжения")
            continue
        if choice == 1:
            image_path = input("Введите путь к изображению: ")
            handler = img.ImageHandler(image_path)
            if not handler.load_image():
                input("\nНажмите Enter для продолжения")
        elif choice == 2:
            if handler:
                handler.show_info()
            else:
                print("Загрузите изображение")
            input("\nНажмите Enter для продолжения")
        elif choice == 3:
            if handler and handler.image:
                handler.rotate_90()
            else:
                print("Загрузите изображение")
            input("\nНажмите Enter для продолжения")
        elif choice == 4:
            if handler and handler.image:
                handler.crop_150x150()
            else:
                print("Загрузите изображение")
            input("\nНажмите Enter для продолжения")
        elif choice == 5:
            if handler and handler.image:
                handler.resize()
            else:
                print("Загрузите изображение")
            input("\nНажмите Enter для продолжения")
        elif choice == 6:
            if handler and handler.image:
                handler.change_format()
            else:
                print("Загрузите изображение")
            input("\nНажмите Enter для продолжения")
        elif choice == 7:
            if handler and handler.image:
                handler.save_image()
            else:
                print("Загрузите изображение")
            input("\nНажмите Enter для продолжения")
        elif choice == 8:
            if handler and handler.image:
                processor = handler.get_processor()
                if processor:
                    processor.apply_grayscale()
                    handler.image = processor.get_processed_image()
            else:
                print("Загрузите изображение")
            input("\nНажмите Enter для продолжения")
        elif choice == 9:
            if handler and handler.image:
                processor = handler.get_processor()
                if processor:
                    text = input("Введите текст (по умолчанию: 'Вариант 2'): ")
                    if not text:
                        text = "Вариант 2"
                    
                    try:
                        font_size = int(input("Введите размер шрифта (по умолчанию 20): ") or "20")
                    except:
                        font_size = 20
                    
                    processor.add_text(text, font_size=font_size)
                    handler.image = processor.get_processed_image()
            else:
                print("Загрузите изображение")
            input("\nНажмите Enter для продолжения")
        elif choice == 10:
            if handler and handler.image:
                handler.show_preview()
            else:
                print("Загрузите изображение")
            input("\nНажмите Enter для продолжения")
        elif choice == 11:
            print("До встречи!")
            break
        else:
            print("Дура попросили же ввести число от 1 до 11")
            input("\nНажмите Enter для продолжения")
if __name__ == "__main__":
    main()