import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import webbrowser     

# 분리배출 정보 데이터
waste_data = {
    '플라스틱': {
        'name': '플라스틱',
        'description': '플라스틱은 깨끗이 씻고 라벨을 제거하여 배출하세요.',
        'image': 'images/plastic.png',
        'examples': [
            {
                'name': '페트병',
                'description': '페트병은 내용물을 비우고 다른 재질은 제거한 후 배출합니다.',
                'image': 'images/pet_bottle.jpg'
            },
            {
                'name': '비닐봉지',
                'description': '비닐봉지는 깨끗한 상태로 흩날리지 않도록 봉투에 모아서 배출합니다.',
                'image': 'images/plastic_bag.jpg'
            }
        ]
    },
    '종이': {
        'name': '종이',
        'description': '종이는 잘 펼쳐서 배출하세요.',
        'image': 'images/paper.png',
        'examples': [
            {
                'name': '우유팩',
                'description': '우유팩은 씻어서 배출합니다.',
                'image': 'images/milk_carton.jpg'
            },
            {
                'name': '상자류',
                'description': '테이프 등 종이류와 다른 재질은 제거하여 배출합니다.',
                'image': 'images/box.jpg'
            }
        ]
    },
    '유리': {
        'name': '유리병',
        'description': '유리병은 내용물을 비우고 배출하세요.',
        'image': 'images/glass.png',
        'examples': [
            {
                'name': '병류',
                'description': '병류는 내용물을 비우고 배출합니다.\n 깨진 유리제품은 신문지 등으로 싸서 종량제 봉투에 배출합니다.',
                'image': 'images/soju.jpg'
            }
        ]
    },
    '일반쓰레기': {
        'name': '일반쓰레기',
        'description': '일반쓰레기는 종량제 봉투에 넣어 배출합니다.',
        'image': 'images/general.png',
        'examples': [
            {
                'name': '계란 껍질',
                'description': '계란 껍질은 일반쓰레기로 배출합니다.',
                'image': 'images/egg.jpg'
            },
            {
                'name': '생선 뼈',
                'description': '생선 살을 제거한 생선 뼈는 일반쓰레기로 배출합니다.',
                'image': 'images/fish.jpg'
            },
        ]
    },
    '음식쓰레기': {
        'name': '음식물 쓰레기',
        'description': '음식물 쓰레기는 물기를 제거하고 배출합니다.',
        'image': 'images/food.png',
        'examples': [
            {
                'name': '과일 껍질',
                'description': '과일 껍질은 음식쓰레기로 배출합니다.',
                'image': 'images/fruit_peel.jpg'
            },
        ]
    },
    '기타': {
        'name': '기타',
        'description': '기타 물품은 각각의 배출 지침을 따릅니다.',
        'image': 'images/etc.png',
        'examples': [
            {
                'name': '건전지',
                'description': '건전지는 전용 수거함에 배출합니다.',
                'image': 'images/battery.jpg'
            },
            {
                'name': '형광등',
                'description': '형광등은 전용 수거함에 배출합니다.',
                'image': 'images/lamp.jpg'
            }
        ]
    }
}

class WasteManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("물품별 분리배출 정보")
        self.geometry("800x600")
        self.iconphoto(False, tk.PhotoImage(file='images/recycle.png'))  # 윈도우 아이콘 설정

        # 메뉴 버튼 생성
        self.create_menu_buttons()
        
        # 대표적인 폐기물 배출 방법 제목 추가
        title_label = tk.Label(self, text="대표적인 폐기물 배출 방법", font=('Arial', 24), background="#ffffff", fg="#000000")
        title_label.pack(pady=20)
        
        self.main_canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, background="#ffffff")
        self.main_frame = tk.Frame(self.main_canvas, background="#ffffff")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.main_canvas.yview)
        self.main_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.main_canvas.pack(side="left", fill="both", expand=True)
        self.main_canvas.create_window((4,4), window=self.main_frame, anchor="w", 
                                      tags="self.main_frame")

        self.main_frame.bind("<Configure>", self.on_frame_configure)

        self.create_main_buttons()
        
        # # Team DB 버튼 생성
        # self.create_team_db_button()
        
    def create_menu_buttons(self):
        menu_frame = tk.Frame(self, background="#ffffff")
        menu_frame.pack(side="top", fill="x")

        home_button = tk.Button(menu_frame, text="Home", command=self.go_to_home, background="#ffffff")
        home_button.pack(side="left", padx=(10, 0), pady=5)

        info_button = tk.Button(menu_frame, text="Info", command=self.go_to_info, background="#ffffff")
        info_button.pack(side="left", padx=10, pady=5)

        qna_button = tk.Button(menu_frame, text="Q&A", command=self.go_to_qna, background="#ffffff")
        qna_button.pack(side="left", padx=(0, 10), pady=5)

    def go_to_home(self):
        # 홈으로 이동하는 기능 추가
        messagebox.showinfo("Main", "메인 화면으로 이동합니다.")

    def go_to_info(self):
        # 현재 정보 페이지로 이동하는 기능 추가
        messagebox.showinfo("Info", "현재 정보 페이지에 있습니다.")

    def go_to_qna(self):
        # Q&A 페이지로 이동하는 기능 추가
        messagebox.showinfo("Q&A", "Q&A 페이지로 이동합니다.")
        url = "http://localhost:5000"
        webbrowser.open_new(url)
        
    # def create_team_db_button(self):
    #     team_db_button = tk.Button(self, text="Team DB", command=self.go_to_team_db, background="#ffffff")
    #     team_db_button.pack(side="bottom", anchor="s", padx=10, pady=10)

    # def go_to_team_db(self):
    #     # Team DB 페이지로 이동하는 기능 추가
    #     messagebox.showinfo("Team DB", "Team DB 페이지로 이동합니다.")

    def on_frame_configure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))

    def create_main_buttons(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        row = 1
        col = 1
        for waste_type in waste_data.keys():
            waste = waste_data[waste_type]
            button_frame = tk.Frame(self.main_frame, background="#ffffff")
            button_frame.grid(row=row, column=col, padx=20, pady=20)

            image = Image.open(waste['image'])
            image = image.resize((100, 100), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            button = tk.Button(button_frame, image=photo, command=lambda wt=waste_type: self.show_detail(wt), background="#ffffff", borderwidth=0)
            button.image = photo  # reference to avoid garbage collection
            button.pack()

            label = tk.Label(button_frame, text=waste['name'], background="#ffffff", fg="#000000")
            label.pack()

            col += 1
            if col > 3:  # 3 columns per row
                col = 1
                row += 1

        # Center the main frame in the canvas
        self.main_canvas.update_idletasks()
        self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))

        # Center the entire main_frame in the middle of the canvas
        canvas_width = self.main_canvas.winfo_width()
        canvas_height = self.main_canvas.winfo_height()
        frame_width = self.main_frame.winfo_width()
        frame_height = self.main_frame.winfo_height()
        x_offset = (canvas_width - frame_width) // 2
        y_offset = (canvas_height - frame_height) // 2
        self.main_canvas.coords("self.main_frame", x_offset, y_offset)

    def show_detail(self, waste_type):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        waste = waste_data[waste_type]
        
        back_button = tk.Button(self.main_frame, text="뒤로", command=self.back_to_main, background="#ffffff", fg="#000000")
        back_button.pack(pady=5)
        
        name_label = tk.Label(self.main_frame, text=waste['name'], font=('Arial', 18), background="#ffffff", fg="#000000")
        name_label.pack(pady=5, fill='x')

        description_label = tk.Label(self.main_frame, text=waste['description'], background="#ffffff", fg="#000000")
        description_label.pack(pady=5, fill='x')

        if os.path.exists(waste['image']):
            image = Image.open(waste['image'])
            image = image.resize((200, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(self.main_frame, image=photo, background="#ffffff")
            image_label.image = photo  # reference to avoid garbage collection
            image_label.pack(pady=5)
        else:
            print(f"Error: {waste['image']} not found")

        example_label = tk.Label(self.main_frame, text="예시 물품", font=('Arial', 16), background="#ffffff", fg="#000000")
        example_label.pack(pady=10)
        
        # max_name_length = max(len(example['name']) for example in waste['examples'])
        # max_description_length = max(len(example['description']) for example in waste['examples'])
 
        for example in waste['examples']:
            example_frame = tk.Frame(self.main_frame, background="#ffffff")
            example_frame.pack(pady=5, fill="x")

            example_image_label = tk.Label(example_frame, background="#ffffff")
            example_image_label.pack(side="left", padx=10)

            example_description_frame = tk.Frame(example_frame, background="#ffffff")
            example_description_frame.pack(side="left", padx=10, fill='x', expand=True)

            example_name_label = tk.Label(example_description_frame, text=example['name'], font=('Arial', 14), background="#ffffff", fg="#000000", anchor="w")
            example_name_label.pack(pady=5, fill='x', expand=True)

            example_description_label = tk.Label(example_description_frame, text=example['description'], background="#ffffff", fg="#000000", anchor="w")
            example_description_label.pack(pady=5, fill='x', expand=True)

            if os.path.exists(example['image']):
                example_image = Image.open(example['image'])
                example_image = example_image.resize((100, 100), Image.LANCZOS)
                example_photo = ImageTk.PhotoImage(example_image)
                example_image_label.config(image=example_photo)
                example_image_label.image = example_photo  # reference to avoid garbage collection
            else:
                print(f"Error: {example['image']} not found")

    def back_to_main(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.create_main_buttons()

if __name__ == "__main__":
    app = WasteManagementApp()
    app.mainloop()
