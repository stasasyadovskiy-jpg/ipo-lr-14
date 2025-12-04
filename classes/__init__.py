from PIL import Image, ImageDraw, ImageFont
import os

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.processor = None
    
    def load_image(self):
        try:
            self.image = Image.open(self.image_path)
            print(f"✓ Изображение загружено: {self.image_path}")
            return True
        except Exception as e:
            print(f"✗ Ошибка загрузки изображения: {e}")
            return False
    
    def rotate_90(self):
        if self.image:
            self.image = self.image.rotate(90, expand=True)
            print("✓ Изображение повернуто на 90 градусов")
    
    def crop_150x150(self):
        if self.image:
            width, height = self.image.size
            if width >= 150 and height >= 150:
                left = (width - 150) // 2
                top = (height - 150) // 2
                right = left + 150
                bottom = top + 150
                self.image = self.image.crop((left, top, right, bottom))
                print("✓ Изображение обрезано до 150x150")
            else:
                print("✗ Изображение слишком маленькое для обрезки 150x150")
    
    def resize(self):
        if self.image:
            try:
                width = int(input("Введите новую ширину: "))
                height = int(input("Введите новую высоту: "))
                self.image = self.image.resize((width, height))
                print(f"✓ Размер изменен на {width}x{height}")
            except ValueError:
                print("✗ Ошибка: введите числа")
    
    def show_info(self):
        if self.image:
            width, height = self.image.size
            mode = self.image.mode
            format_info = self.image.format if self.image.format else "Неизвестно"
            print(f"Информация об изображении:")
            print(f"  Размер: {width}x{height}")
            print(f"  Режим: {mode}")
            print(f"  Формат: {format_info}")
            print(f"  Путь: {self.image_path}")
        else:
            print("✗ Изображение не загружено")
    
    def save_image(self, output_path=None):
        if self.image:
            if not output_path:
                output_path = input("Введите путь для сохранения: ")
            try:
                self.image.save(output_path)
                print(f"✓ Изображение сохранено: {output_path}")
                return True
            except Exception as e:
                print(f"✗ Ошибка сохранения: {e}")
                return False
        print("✗ Нет изображения для сохранения")
        return False
    
    def get_processor(self):
        if self.image:
            self.processor = ImageProcessor(self.image)
            return self.processor
        print("✗ Сначала загрузите изображение")
        return None
    
    def get_image(self):
        return self.image

class ImageProcessor:
    def __init__(self, image):
        self.image = image
    
    def apply_grayscale(self):
        self.image = self.image.convert('L')
        print("✓ Применен черно-белый фильтр")
    
    def add_text(self):
        text = input("Введите текст: ")
        try:
            font_size = int(input("Введите размер шрифта: "))
        except:
            font_size = 20
        
        try:
            draw = ImageDraw.Draw(self.image)
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                font = ImageFont.load_default()
            draw.text((10, 10), text, fill="white", font=font)
            print(f"✓ Текст '{text}' добавлен")
        except Exception as e:
            print(f"✗ Ошибка при добавлении текста: {e}")
    
    def apply_sharpen(self):
        from PIL import ImageFilter
        self.image = self.image.filter(ImageFilter.SHARPEN)
        print("✓ Применена резкость")
    
    def get_processed_image(self):
        return self.image

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    print("\n" + "="*50)
    print("ОБРАБОТЧИК ИЗОБРАЖЕНИЙ - МЕНЮ")
    print("="*50)
    print("1. Загрузить изображение")
    print("2. Показать информацию об изображении")
    print("3. Повернуть на 90 градусов")
    print("4. Обрезать до 150x150")
    print("5. Изменить размер")
    print("6. Сохранить изображение")
    print("="*30)
    print("ОБРАБОТКА:")
    print("7. Черно-белый фильтр")
    print("8. Добавить текст")
    print("9. Резкость")
    print("="*30)
    print("10. Выполнить все операции из варианта 2")
    print("11. Показать текущее изображение")
    print("12. Выход")
    print("="*50)

def show_preview(image):
    try:
        image.show()
        print("✓ Предпросмотр открыт")
    except:
        print("✗ Не удалось открыть предпросмотр")

def execute_variant2(handler):
    print("\n" + "="*50)
    print("ВЫПОЛНЕНИЕ ВАРИАНТА 2")
    print("="*50)
    
    if not handler.image:
        print("✗ Сначала загрузите изображение")
        return
    
    print("1. Поворот на 90 градусов...")
    handler.rotate_90()
    
    print("2. Обрезка до 150x150...")
    handler.crop_150x150()
    
    print("3. Черно-белый фильтр...")
    processor = handler.get_processor()
    if processor:
        processor.apply_grayscale()
    
    print("4. Добавление текста 'Вариант 2'...")
    if processor:
        try:
            draw = ImageDraw.Draw(handler.image)
            try:
                font = ImageFont.truetype("arial.ttf", 20)
            except:
                font = ImageFont.load_default()
            draw.text((10, 10), "Вариант 2", fill="white", font=font)
            print("✓ Текст добавлен")
        except Exception as e:
            print(f"✗ Ошибка при добавлении текста: {e}")
    
    print("✓ Все операции варианта 2 выполнены")
    
    save_choice = input("Сохранить результат? (д/н): ").lower()
    if save_choice == 'д':
        handler.save_image()

def main():
    handler = ImageHandler("")
    
    while True:
        print_menu()
        choice = input("\nВыберите действие (1-12): ")
        
        if choice == '1':
            clear_screen()
            path = input("Введите путь к изображению: ")
            if os.path.exists(path):
                handler = ImageHandler(path)
                handler.load_image()
            else:
                print("✗ Файл не найден")
        
        elif choice == '2':
            clear_screen()
            handler.show_info()
        
        elif choice == '3':
            clear_screen()
            if handler.image:
                handler.rotate_90()
            else:
                print("✗ Сначала загрузите изображение")
        
        elif choice == '4':
            clear_screen()
            if handler.image:
                handler.crop_150x150()
            else:
                print("✗ Сначала загрузите изображение")
        
        elif choice == '5':
            clear_screen()
            if handler.image:
                handler.resize()
            else:
                print("✗ Сначала загрузите изображение")
        
        elif choice == '6':
            clear_screen()
            handler.save_image()
        
        elif choice == '7':
            clear_screen()
            if handler.image:
                processor = handler.get_processor()
                if processor:
                    processor.apply_grayscale()
            else:
                print("✗ Сначала загрузите изображение")
        
        elif choice == '8':
            clear_screen()
            if handler.image:
                processor = handler.get_processor()
                if processor:
                    processor.add_text()
            else:
                print("✗ Сначала загрузите изображение")
        
        elif choice == '9':
            clear_screen()
            if handler.image:
                processor = handler.get_processor()
                if processor:
                    processor.apply_sharpen()
            else:
                print("✗ Сначала загрузите изображение")
        
        elif choice == '10':
            clear_screen()
            if handler.image:
                execute_variant2(handler)
            else:
                print("✗ Сначала загрузите изображение")
        
        elif choice == '11':
            clear_screen()
            if handler.image:
                show_preview(handler.image)
            else:
                print("✗ Сначала загрузите изображение")
        
        elif choice == '12':
            clear_screen()
            print("Выход из программы...")
            break
        
        else:
            print("✗ Неверный выбор. Попробуйте снова.")
        
        input("\nНажмите Enter для продолжения...")
        clear_screen()

if __name__ == "__main__":
    clear_screen()
    print("Добро пожаловать в обработчик изображений!")
    print("Для начала работы выберите '1. Загрузить изображение'")
    main()