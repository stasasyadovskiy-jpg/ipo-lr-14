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
            print(f"Изображение загружено: {self.image_path}")
            return True
        except Exception as e:
            print(f"Ошибка загрузки изображения")
            return False
    def rotate_90(self):
        if self.image:
            self.image = self.image.rotate(90, expand=True)
            print("Изображение повернуто на 90 градусов")
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
                print(f"Изображение слишком маленькое! Оно всего лишь {width}*{height}")
    def resize(self):
        if self.image:
            try:
                width = int(input("Введите новую ширину: "))
                height = int(input("Введите новую высоту: "))
                self.image = self.image.resize((width, height))
                print(f"Размер изменен на {width}x{height}")
            except ValueError:
                print("Введи число дура")
    def change_format(self):
        if self.image:
            print("\nДоступные форматы:")
            print("1. JPEG (.jpg, .jpeg)")
            print("2. PNG (.png)")
            print("3. GIF (.gif)")
            try:
                choice = int(input("Выберите формат (1-3): "))
                formats = {
                    1: ('JPEG', '.jpg'),
                    2: ('PNG', '.png'),
                    3: ('GIF', '.gif'),
                }
                if choice in formats:
                    format_name, extension = formats[choice]
                    base_name = os.path.splitext(self.image_path)[0]
                    default_name = f"{base_name}_converted{extension}"
                    new_path = input(f"Введите путь для сохранения (по умолчанию: {default_name}): ")
                    
                    if not new_path:
                        new_path = default_name
                    try:
                        self.image.save(new_path, format=format_name)
                        print(f"Изображение сохранено в формате {format_name}: {new_path}")
                        self.image_path = new_path
                        self.image = Image.open(new_path)
                        return True
                    except Exception as e:
                        print(f"Ошибка сохранения в формате {format_name}: {e}")
                else:
                    print("Неверный выбор формата")
            except ValueError:
                print("Ошибка: введите число от 1 до 3")
        else:
            print("Загрузите изображение")
        return False
    def show_info(self):
        if self.image:
            width, height = self.image.size
            mode = self.image.mode
            format_info = self.image.format if self.image.format else "Неизвестно"
            size_kb = os.path.getsize(self.image_path) / 1024 if os.path.exists(self.image_path) else "Неизвестно"
            
            print(f"Информация об изображении:")
            print(f"  Размер: {width}x{height} пикселей")
            print(f"  Режим: {mode}")
            print(f"  Формат: {format_info}")
            print(f"  Путь: {self.image_path}")
        else:
            print("Изображение не загружено")
    def save_image(self, output_path=None):
        if self.image:
            if not output_path:
                base_name = os.path.splitext(self.image_path)[0]
                default_name = f"{base_name}_edited.jpg"
                output_path = input(f"Введите путь для сохранения (по умолчанию: {default_name}): ")
                
                if not output_path:
                    output_path = default_name
            try:
                format_name = None
                ext = os.path.splitext(output_path)[1].lower()
                if ext in ['.jpg', '.jpeg']:
                    format_name = 'JPEG'
                elif ext == '.png':
                    format_name = 'PNG'
                elif ext == '.gif':
                    format_name = 'GIF'
                
                if format_name:
                    self.image.save(output_path, format=format_name)
                else:
                    self.image.save(output_path)
                
                print(f"Изображение сохранено: {output_path}")
                print(f"Полный путь: {os.path.abspath(output_path)}")
                return True
            except Exception as e:
                print(f"Ошибка сохранения: {e}")
                return False
        print("Нет изображения для сохранения")
        return False
    
    def get_processor(self):
        if self.image:
            self.processor = ImageProcessor(self.image)
            return self.processor
        print("Загрузите изображение")
        return None
    
    def get_image(self):
        return self.image
    
    def show_preview(self):
        if self.image:
            try:
                self.image.show()
                print("Предпросмотр открыт")
            except:
                print("Не удалось открыть предпросмотр")
        else:
            print("✗ Нет изображения для просмотра")

class ImageProcessor:
    def __init__(self, image):
        self.image = image
    
    def apply_grayscale(self):
        if self.image:
            self.image = self.image.convert('L')
            self.image = self.image.convert('RGB')
            print("Применен черно-белый фильтр")
            return True
        print("Нет изображения для обработки")
        return False
    
    def add_text(self, text="Вариант 2", position=(10, 10), font_size=20, color="white"):
        if self.image:
            try:
                draw = ImageDraw.Draw(self.image)
                try:
                    font = ImageFont.truetype("arial.ttf", font_size)
                except:
                    font = ImageFont.load_default()
                
                draw.text(position, text, fill=color, font=font)
                print(f"Текст '{text}' добавлен в позицию {position}")
                return True
            except Exception as e:
                print(f"Ошибка при добавлении текста: {e}")
                return False
        print("Нет изображения для обработки")
        return False
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
    print("6. Изменить формат изображения")
    print("7. Сохранить изображение")
    print("="*30)
    print("ОБРАБОТКА через ImageProcessor:")
    print("8. Черно-белый фильтр")
    print("9. Добавить текст")
    print("="*30)
    print("10. Показать текущее изображение")
    print("11. Выход")
    print("="*50)