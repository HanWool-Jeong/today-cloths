import tkinter as tk
import json
import tkinter.ttk
from tkinter import *
from tkinter import messagebox
import datetime
import urllib.request as URL
import random
import tkinter.font

#날씨 api
##dt = datetime.datetime.now()
##
##today = dt.strftime("%Y%m%d")
####print(today)
##
##api = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?&ServiceKey=XyZeCgl2DLqczBQQf4z3mG%2B6rGhxnJ7Y5yh%2FAFeJsDXZnRqOPXLhMQeekq7rHUIcvLDefnpRQkc%2Br%2FjiGGYrug%3D%3D&base_time=0500&nx=60&ny=125&_type=json"
##
##api = api + "&base_date=" + today
##
##api = str(api)
##        # print(api)
##
##data = URL.urlopen(api)
##result = data.read()
##
##j = json.loads(result)
##weather_raw = j["response"]["body"]["items"]["item"]
##
##for i in weather_raw:
##    print(i)
##
##pop =0
##sky =0
##t3h =0
##
##for i in weather_raw:
##    if i["category"] == "POP":
##        pop = i["fcstValue"]
##
##    if i["category"] == "SKY":
##        sky = i["fcstValue"]
##
##    if i["category"] == "T3H":
##        t3h = i["fcstValue"]
##
##if sky == 1:
##    sky = "맑음"
##elif sky == 2:
##    sky = "구름조금"
##elif sky == 3:
##    sky = "구름많음"
##elif sky == 4:
##    sky = "흐림"
##
##todaysky = "오늘 흑석동의 날씨는 '%s'입니다" % (sky)
##todaypop = " / 강수확률 %d 퍼센트" % (pop)
##todayt3h = " / 기온 %d도" % (t3h)

LARGE_FONT = ("Verdana", 12)
filename = 'data.json'

class Lists(tk.Tk):
    def __init__(self):
        # 옷 종류 세부 항목 기존 리스트 m 은 남성, f 은 여성, u 는 상의, l 은 하의, o 는 외투
        self.values_m_u = ['Shirts', 'Knit', 'Sleeved T-Half', 'Sleeved T-Long', 'Man-to-Man', 'Hood', 'Sleeveless']
        self.values_m_l = ['Denim-Skinny', 'Denim-Straight', 'Denim-Wide', 'Cotton-Skinny', 'Cotton-Straight', 'Cotton-Wide', 'Slacks', 'Half-Pants', 'Training-Pants']
        self.values_m_o = ['Jacket-Denim', 'Jacket-Cotton', 'Jacket-Leather', 'Jacket-Suit', 'Mustang', 'Coat-Short',
                           'Coat-Long', 'Jumper', 'Padding-Short', 'Padding-Long', 'Hoodie', 'Kardigan']

        self.values_f_u = ['Shirts & Blouse', 'Knit', 'Sleeved T-Half', 'Sleeved T-Long', 'Man-to-Man', 'Hood',
                           'Sleeveless', 'One-Piece']
        self.values_f_l = ['Denim-Skinny', 'Denim-Straight', 'Denim-Wide', 'Denim-Boots-Cut', 'Cotton-Skinny', 'Cotton-Straight', 'Cotton-Wide','Cotton-Boots-Cut', 'Slacks', 'Shorts', 'Skirt-Mini', 'Skirt-Midi', 'Skirt-Long', 'Training-Pants']
        self.values_f_o = ['Jacket-Denim', 'Jacket-Cotton', 'Jacket-Leather', 'Jacket', 'Mustang', 'Coat-Short',
                           'Coat-Long', 'Jumper', 'Padding-Short', 'Padding-Long', 'Hoodie', 'Kardigan']

        # 색 세부항목
        self.values_color = ['Black','Grey', 'White', 'Ivory', 'Beige', 'Brown', 'Red', 'Wine', 'Hot Pink', 'Indi Pink', 'Orange', 'Light Yellow', 'Yellow', 'Light Green',
                             'Deep Green', 'Olive/Kaki', 'Light Blue', 'Deep Blue', 'Navy', 'Light Purple', 'Purple']
        self.c_total = []

        self.c_red = ['Black', 'White', 'Grey', 'Navy', 'Beige', 'Brown', 'Ivory', 'Light Blue', 'Blue']
        self.c_wine = ['Black', 'Beige', 'Brown', 'Ivory', 'Light Blue', 'Blue', 'Grey', 'Navy']
        self.c_hot_pink = ['Black', 'White', 'Blue', 'Grey', 'Ivory', 'Light Blue']
        self.c_indi_pink = ['White', 'Ivory', 'Black', 'Beige', 'Light Blue', 'Grey', 'Brown']
        self.c_orange = ['Black', 'White', 'Blue', 'Beige', 'Grey', 'Ivory', 'Light Blue', 'Brown']
        self.c_light_yellow = ['Light Blue', 'Black', 'White', 'Beige', 'Ivory']
        self.c_yellow = ['Black', 'Light Blue', 'Blue', 'Navy', 'White', 'Beige', 'Grey', 'Ivory', 'Brown']
        self.c_light_green = ['Black', 'White', 'Beige', 'Ivory', 'Brown', 'Grey', 'Light Blue', 'Blue']
        self.c_deep_green = ['Black', 'White', 'Beige', 'Navy', 'Brown', 'Ivory', 'Grey', 'Light Blue', 'Blue']
        self.c_olive_kaki = ['Black', 'Brown', 'Beige', 'Grey', 'Ivory', 'Light Blue', 'Blue', 'Navy']
        self.c_light_blue = ['Black', 'White', 'Ivory', 'Red', 'Wine', 'Hot Pink', 'Indi Pink', 'Orange', 'Yellow', 'Light Green',
                'Deep Green', 'Olive/Kaki', 'Light Blue', 'Blue', 'Navy', 'Light Purple', 'Purple', 'Beige', 'Brown']
        self.c_blue = ['Black', 'White', 'Beige', 'Ivory', 'Red', 'Wine', 'Hot Pink', 'Orange', 'Yellow', 'Light Green',
                'Deep Green', 'Olive/Kaki', 'Light Blue', 'Blue', 'Navy', 'Purple', 'Light Purple', 'Grey', 'Brown']
        self.c_navy = ['Black', 'White', 'Grey', 'Ivory', 'Red', 'Wine', 'Yellow', 'Deep Green', 'Olive/Kaki', 'Light Blue',
                'Blue', 'Brown']
        self.c_light_purple = ['Black', 'White', 'Light Blue', 'Ivory', 'Blue']
        self.c_purple = ['Black', 'White', 'Beige', 'Light Blue', 'Blue', 'Grey', 'Ivory']
        self.c_beige = ['Black', 'Brown', 'Red', 'Wine', 'Indi Pink', 'Orange', 'Light yellow',
                 'Yellow', 'Light green', 'Deep Green', 'Olive Green', 'Light Blue', 'Blue', 'Navy', 'Purple', 'Grejy']
        self.c_brown = ['Black', 'Red', 'Wine', 'Light green', 'Deep Green', 'Olive/Kaki', 'Ivory', 'Indi Pink', 'Orange',
                 'Yellow', 'Light Blue', 'Brown', 'Navy', 'Beige']
        self.c_grey = ['Black', 'Red', 'Wine', 'Indi Pink', 'Hot Pink', 'Orange', 'Yellow', 'Light Green', 'Deep Green',
                'Olive/Kaki', 'Navy', 'Deep Purple', 'Beige']
        self.c_white = ['Black', 'White', 'Red', 'Wine', 'Indi Pink', 'Hot Pink', 'Orange', 'Light yellow', 'Yellow',
                 'Light Green', 'Deep Green', 'Olive/Kaki', 'Light Blue', 'Deep Blue', 'Navy', 'Light Purple', 'Purple',
                 'Beige', 'Brown', 'Grey', 'Ivory']
        self.c_ivory = ['Red', 'Wine', 'Hot Pink', 'Indi Pink', 'Orange', 'Light Yellow', 'Yellow', 'Light Green',
                 'Deep Green', 'Olive/Kaki',
                 'Light Blue', 'Deep Blue', 'Navy', 'Light Purple', 'Purple', 'Brown', 'Grey', 'Black']
        self.c_black = ['Black', 'White', 'Grey', 'Red', 'Wine', 'Indi Pink', 'Hot Pink', 'Orange', 'Light Yellow', 'Yellow',
                 'Light Green',
                 'Deep Green', 'Oilve/Kaki', 'Light Blue', 'Purple', 'Navy', 'Beige']
        self.c_total.append(self.c_red)
        self.c_total.append(self.c_wine)
        self.c_total.append(self.c_hot_pink)
        self.c_total.append(self.c_indi_pink)
        self.c_total.append(self.c_orange)
        self.c_total.append(self.c_light_yellow)
        self.c_total.append(self.c_yellow)
        self.c_total.append(self.c_light_green)
        self.c_total.append(self.c_deep_green)
        self.c_total.append(self.c_olive_kaki)
        self.c_total.append(self.c_light_blue)
        self.c_total.append(self.c_blue)
        self.c_total.append(self.c_navy)
        self.c_total.append(self.c_light_purple)
        self.c_total.append(self.c_purple)
        self.c_total.append(self.c_beige)
        self.c_total.append(self.c_brown)
        self.c_total.append(self.c_grey)
        self.c_total.append(self.c_white)
        self.c_total.append(self.c_ivory)
        self.c_total.append(self.c_black)

        self.first_item = dict()
        self.second_item = dict()
        self.third_item = dict()
        self.recommendation = str()
        self.thickness = list()

        #반팔
        self.values_banpal_m = ['Shirts', 'Sleeved T-Half', 'Sleeveless']
        self.values_banpal_f = ['Shirts & Blouse', 'Sleeved T-Half', 'Sleeveless']
        self.values_ginpal = ['Knit', 'Sleeved T-Long', 'Man-to-Man', 'Hood']
        self.values_banbaji_m = ['Shorts']
        self.values_banbaji_f = ['Shorts', 'Mini Skirt', 'Midi Skirt']
        self.values_ginbaji_m = ['Denim-Skinny', 'Denim-Straight', 'Denim-Wide', 'Cotton-Skinny', 'Cotton-Straight',
                           'Cotton-Wide', 'Slacks', 'Training-Pants']
        self.values_ginbaji_f = ['Denim-Skinny', 'Denim-Straight', 'Denim-Boots-Cut', 'Denim-Wide', 'Cotton-Skinny',
                           'Cotton-Straight', 'Cotton-Boots-Cut', 'Cotton-Wide', 'Slacks', 'Long Skirt', 'Training-Pants']
        self.values_without_padding_f = ['Jacket-Denim', 'Jacket-Cotton', 'Jacket', 'Jacket-Leather', 'Mustang', 'Coat-Short',
                           'Coat-Long', 'Jumper', 'Hoodie', 'Kardigan']
        self.values_without_padding_m = ['Jacket-Denim', 'Jacket-Cotton', 'Jacket-Leather', 'Mustang', 'Jacket-Suit', 'Coat-Short',
                           'Coat-Long', 'Jumper', 'Hoodie', 'Kardigan']


        #온도별 리스트
        self.lst_5l = []
        self.lst_6to9 = []
        self.lst_10to17 = []
        self.lst_17to19 = []
        self.lst_20to22 = []
        self.lst_23to27 = []
        self.lst_27h = []

        #임시 리스트
        self.temp_lst1 = []
        self.temp_lst2 = []

        # 임시 리스트를 만들어, 상의, 하의, 외투를 구별
        self.temp_upper = []
        self.temp_lower = []
        self.temp_over = []
        self.c_temp_upper = []
        self.c_temp_lower = []
        self.c_temp_over = []


class SetVars(tk.Tk):
    def __init__(self):
        self.var_g = tk.IntVar()
        self.var_t1 = tk.IntVar()
        self.var_t2 = tk.IntVar()
        self.var_thick = tk.IntVar()
        self.var_situation = tk.IntVar()

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "오늘 이 옷 어때?")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        

        #메뉴바 생성
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="홈으로", command=lambda: self.show_frame(StartPage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="메뉴", menu=filemenu)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, PageReg, PageDel, PageCode):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= 'white')

        font13 = tkinter.font.Font(family='나눔바른펜', weight='bold', size=13)
        font14 = tkinter.font.Font(family='나눔바른펜', weight='bold', size=14)
        font15 = tkinter.font.Font(family='나눔바른펜', weight='bold', size=15)

        logo = tk.Label(self, width=375, height=125)
        logo.img = PhotoImage(file="로고3.gif")
        logo.config(image=logo.img)

        btn_reg = tk.Button(self, relief="flat", height=2, width=11, bg="light blue3", font=font14, fg="white",
                            text="새 옷 등록", command=lambda: controller.show_frame(PageReg))
        btn_delete = tk.Button(self, relief="flat", height=2, width=11, bg="light blue3", font=font14, fg="white",
                               text="기존 옷 삭제", command=lambda: controller.show_frame(PageDel))
        btn_codi = tk.Button(self, relief="flat", height=2, width=12, bg="LightPink2", font=font15, fg="white",
                             text="코디하기", command=lambda: controller.show_frame(PageCode))

        entry_weather = tk.Entry(self, width=55, bg="gainsboro")

        logo.place(x=60, y=35)
        btn_reg.place(x=60, y=180)
        btn_delete.place(x=185, y=180)
        btn_codi.place(x=310, y=178)
        entry_weather.place(x=54, y=269)


##        entry_weather.insert(0, todaysky)
##        entry_weather.insert(END, todaypop)
##        entry_weather.insert(END, todayt3h)


class PageReg(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        font13 = tkinter.font.Font(family='나눔바른펜', weight='bold', size=13)
        font14 = tkinter.font.Font(family='나눔바른펜', weight='bold', size=14)
        font15 = tkinter.font.Font(family='나눔바른펜', weight='bold', size=15)

        self.lists = Lists()

        #세부종류 리스트 변수 생성
        self.values_narrow = list()

        # 라벨 설정 값들 (성별, 옷 종류, 세부 종류, 색, 두께 순)
        label_gender = tk.Label(self, text="성별", font=font15, fg="white", bg="light blue3", width="7", height="1")
        label_gender.place(x=70, y=30)
        label_wide = tk.Label(self, text="대분류", font=font15, fg="white", bg="light blue3", width="7", height="1")
        label_wide.place(x=70, y=70)
        label_narrow = tk.Label(self, text="소분류", font=font15, fg="white", bg="light blue3", width="7", height="1")
        label_narrow.place(x=70, y=110)
        label_color = tk.Label(self, text="색상", font=font15, fg="white", bg="light blue3", width="7", height="1")
        label_color.place(x=70, y=150)
        label_thickness = tk.Label(self, text="두께", font=font15, fg="white", bg="light blue3", width="7", height="1")
        label_thickness.place(x=70, y=190)

        self.vars = SetVars()

        # 성별 라디오버튼과 위치
        gender_m = tk.Radiobutton(self, text="남성", font=font14, bg="white", variable=self.vars.var_g, value=1,
                                  command=self.gender_select)
        gender_f = tk.Radiobutton(self, text="여성", font=font14, bg="white", variable=self.vars.var_g, value=2,
                                  command=self.gender_select)
        gender_m.place(x=240, y=30)
        gender_f.place(x=330, y=30)

        # 옷 종류 라디오버튼과 위치
        rdbtn_upper = tk.Radiobutton(self, text="상의", font=font14, bg="white", variable=self.vars.var_t1, value=1,
                                     command=self.type1_select)
        rdbtn_lower = tk.Radiobutton(self, text="하의", font=font14, bg="white", variable=self.vars.var_t1, value=2,
                                     command=self.type1_select)
        rdbtn_over = tk.Radiobutton(self, text="외투", font=font14, bg="white", variable=self.vars.var_t1, value=3,
                                    command=self.type1_select)
        rdbtn_upper.place(x=210, y=70)
        rdbtn_lower.place(x=290, y=70)
        rdbtn_over.place(x=370, y=70)

        # 옷 두께 라디오버튼과 위치
        thickness_1 = tk.Radiobutton(self, text="1", font=font14, bg="white", variable=self.vars.var_thick, value=1)
        thickness_2 = tk.Radiobutton(self, text="2", font=font14, bg="white", variable=self.vars.var_thick, value=2)
        thickness_3 = tk.Radiobutton(self, text="3", font=font14, bg="white", variable=self.vars.var_thick, value=3)
        thickness_1.place(x=210, y=190)
        thickness_2.place(x=290, y=190)
        thickness_3.place(x=370, y=190)

        # 스크롤 선택 - 소분류, 색상, 재질
        self.combobox_narrow = tkinter.ttk.Combobox(self, height=15, values=self.values_narrow)
        self.combobox_narrow.place(x=230, y=115)
        self.combobox_narrow.set("소분류 선택")
        self.combobox_color = tkinter.ttk.Combobox(self, height=15, values=self.lists.values_color)
        self.combobox_color.place(x=230, y=155)
        self.combobox_color.set("색상 선택")

        # 등록
        self.registration = tk.Button(self, relief="flat", text=" 등록 ", font=font15, fg="white", bg="Light Pink2", width=7,
                                      command=self.register)
        self.registration.place(x=210, y=237)

        

    def gender_select(self):
        self.combobox_narrow.set("소분류 선택")
        self.combobox_color.set("색상 선택")
        if self.vars.var_g.get() == 1:
            self.values_narrow = self.lists.values_m_u + self.lists.values_m_l + self.lists.values_m_o
        elif self.vars.var_g.get() == 2:
            self.values_narrow = self.lists.values_f_u + self.lists.values_f_l + self.lists.values_f_o
        self.combobox_narrow.config(values=self.values_narrow)

    def type1_select(self):
        self.combobox_narrow.set("소분류 선택")
        self.combobox_color.set("색상 선택")
        #성별 선택을 불러와서 성별에 맞는 옷 세부종류를 구별해준다
        if self.vars.var_g.get() == 1:
            if self.vars.var_t1.get() == 1:
                self.values_narrow = self.lists.values_m_u
            elif self.vars.var_t1.get() == 2:
                self.values_narrow = self.lists.values_m_l
            else:
                self.values_narrow = self.lists.values_m_o
        elif self.vars.var_g.get() == 2:
            if self.vars.var_t1.get() == 1:
                self.values_narrow = self.lists.values_f_u
            elif self.vars.var_t1.get() == 2:
                self.values_narrow = self.lists.values_f_l
            else:
                self.values_narrow = self.lists.values_f_o
        self.combobox_narrow.config(values=self.values_narrow)

    #등록 함수
    def register(self):
        with open(filename) as f:
            data = json.load(f)
            messagebox.showinfo("오늘 이 옷 어때?", "등록되었습니다")
            print("등록되었습니다")

            # data["items"].append("hello")
            temp_id = str(datetime.datetime.now().time())

            temp_id_elements ={
                "gender": self.vars.var_g.get(),
                "type1": self.vars.var_t1.get(),
                "type2": self.combobox_narrow.get(),
                "color": self.combobox_color.get(),
                "thickness": self.vars.var_thick.get()
                }

            data.update({temp_id:temp_id_elements})

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

class PageDel(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        font13 = tkinter.font.Font(family='나눔바른펜', weight='bold', size=13)
        font14 = tkinter.font.Font(family='나눔바른펜', weight='bold', size=14)
        font15 = tkinter.font.Font(family='나눔바른펜', weight='bold', size=15)

        self.vars = SetVars()
        self.temp_list = []
        self.data = list()

        label_style = tk.Label(self, text="옷 종류", bg="light blue3", fg="white", font=font15, width=7, height=1)

        # 실험하고 있는 변수 1
        self.selected_data = int()

        # type1(상의, 하의, 외투)의 분류를 위한 라디오 버튼들
        self.radbtn_upper = tk.Radiobutton(self, text="상의  ", font=font14, fg="black", bg="white",
                                           variable=self.vars.var_t1, value=1, command=self.type_selected)
        self.radbtn_lower = tk.Radiobutton(self, text="하의  ", font=font14, fg="black", bg="white",
                                           variable=self.vars.var_t1, value=2, command=self.type_selected)
        self.radbtn_over = tk.Radiobutton(self, text="외투  ", font=font14, fg="black", bg="white",
                                          variable=self.vars.var_t1, value=3, command=self.type_selected)

        # 삭제하기 버튼 생성
        self.btn_delete = tk.Button(self, relief="flat", text="삭제하기", font=font15, fg="white", bg="Light Pink2",
                                    height=1, width=10, command=self.delete_inventory)

        frame1 = tk.Frame(self)

        # self.lb_inventory = tk.Listbox(self, selectmode=EXTENDED)
        self.lb_inventory = tk.Listbox(frame1, selectmode=EXTENDED)
        self.lb_inventory.config(width=57, height=12, relief='flat')
        # self.scroll = tk.Scrollbar(self, command=self.lb_inventory.yview)
        self.scroll = tk.Scrollbar(frame1, command=self.lb_inventory.yview)

        # 각 버튼 및 레이블 등 인터페이스 레이아웃
        label_style.place(x=45, y=35)
        self.radbtn_upper.place(x=130, y=35)
        self.radbtn_lower.place(x=200, y=35)
        self.radbtn_over.place(x=270, y=35)
        self.btn_delete.place(x=350, y=30)
      
        # self.lb_inventory.place(x=40, y=80)
        self.lb_inventory.pack(side="left")
        self.scroll.pack(side="right", fill="y")
        frame1.place(x=42, y=85)


    def type_selected(self):
        self.lb_inventory.delete(0, END)

        #라디오 버튼을 눌렀을 때 리스트 새로 생성; 즉, 기존 리스트에 동일한 항목이나 타 항목들 추가 방지
        self.temp_list = []

        #데이터 파일을 불러와서 종류에 맞는 등록 인벤 검색
        with open(filename) as f:
            data = json.load(f)

            for item in data:

                if data[item]["type1"] == self.vars.var_t1.get():
                    self.temp_list.append(item)

                    temp_type2 = data[item]["type2"]
                    temp_color = data[item]["color"]
                    temp_thickness = str(data[item]["thickness"])
                    temp_line = str("세부종류 : %s \t 색 : %s \t 두께 : %s" %(temp_type2, temp_color, temp_thickness))
                    self.lb_inventory.insert(END, temp_line)

    #삭제 함수
    def delete_inventory(self):
        selected = self.lb_inventory.index(ACTIVE)

        with open(filename) as f:
            print("loading data")
            data = json.load(f)

            for item in data:
                if item == self.temp_list[selected]:
                    del data[item]
                    break

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

        messagebox.showinfo("오늘 이 옷 어때?", "삭제되었습니다")
        self.lb_inventory.delete(0, END)

        self.type_selected()

class PageCode(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        self.vars = SetVars()
        self.lists = Lists()

        font13=tkinter.font.Font(family='나눔바른펜', weight='bold', size=13)
        font14=tkinter.font.Font(family='나눔바른펜', weight='bold', size=14)
        font15=tkinter.font.Font(family='나눔바른펜', weight='bold', size=15)

        #상황별 라디오버튼 및 위치

        an_label=tk.Label(self, text="상황을 선택해주세요!", font=font15, fg="white", bg="light blue3", width=18, height=1)
        
        radbtn_daily = tk.Radiobutton(self, text="일상  ", relief="flat", font=font14, fg="black", bg="white", variable=self.vars.var_situation, value=1)
        radbtn_tstnwork = tk.Radiobutton(self, text="시험기간/운동  ", font=font14, fg="black", bg="white",variable=self.vars.var_situation, value=2)
        radbtn_pt = tk.Radiobutton(self, text="발표  ", font=font14, fg="black", bg="white",variable=self.vars.var_situation, value=3)
        radbtn_fancy = tk.Radiobutton(self, text="꾸미고 싶어요  ", font=font14, fg="black", bg="white",variable=self.vars.var_situation, value=4)
        radbtn_wedding = tk.Radiobutton(self, text="결혼식  ", font=font14, fg="black", bg="white",variable=self.vars.var_situation, value=5)
        radbtn_funeral = tk.Radiobutton(self, text="장례식  ", font=font14, fg="black", bg="white",variable=self.vars.var_situation, value=6)

        an_label.place(x=159, y=52)
        radbtn_daily.place(x=77, y=92)
        radbtn_tstnwork.place(x=175, y=92)
        radbtn_pt.place(x=347, y=92)
        radbtn_fancy.place(x=77, y=132)
        radbtn_wedding.place(x=227, y=132)
        radbtn_funeral.place(x=333, y=132)

        
        #코디하기 버튼 및 위치
        btn_codi = tk.Button(self, relief="flat", text="코디하기!", font=font15, bg="Light Pink2", fg="white", height=1, width=10, command=self.codi)
        btn_codi.place(x=195, y=222)

    def codi(self):

        with open(filename) as f:
            data = json.load(f)

            for item in data:
                if data[item]["gender"] == 1:
                    if data[item]["thickness"] == 3:
                        if data[item]["type1"] == 1:
                            self.lists.lst_5l.append(data[item])
                            self.lists.lst_6to9.append(data[item])
                        elif data[item]["type1"] == 2:
                            self.lists.lst_5l.append(data[item])
                        else:
                            if data[item]["type2"] in self.lists.values_without_padding_m:
                                self.lists.lst_6to9.append(data[item])

                            self.lists.lst_5l.append(data[item])
                    elif data[item]["thickness"] == 2:
                        if data[item]["type1"] == 1:
                            self.lists.lst_6to9.append(data[item])
                            self.lists.lst_20to22.append(data[item])
                            self.lists.lst_17to19.append(data[item])
                        elif data[item]["type1"] == 2:
                            self.lists.lst_17to19.append(data[item])
                            self.lists.lst_20to22.append(data[item])
                            self.lists.lst_6to9.append(data[item])
                        else:
                            self.lists.lst_17to19.append(data[item])
                            self.lists.lst_10to17.append(data[item])
                    else:
                        if data[item]["type1"] == 1:
                            if data[item]["type2"] in self.lists.values_banpal_m:
                                self.lists.lst_27h.append(data[item])

                            self.lists.lst_23to27.append(data[item])
                            self.lists.lst_10to17.append(data[item])
                            self.lists.lst_20to22.append(data[item])
                        elif data[item]["type1"] == 2:
                            if data[item]["type2"] in self.lists.values_ginbaji_m:
                                self.lists.lst_23to27.append(data[item])

                            self.lists.lst_10to17.append(data[item])
                            self.lists.lst_27h.append(data[item])
                        else:
                            self.lists.lst_20to22.append(data[item])
                else:
                    if data[item]["thickness"] == 3:
                        if data[item]["type1"] == 1:
                            self.lists.lst_5l.append(data[item])
                            self.lists.lst_6to9.append(data[item])
                        elif data[item]["type1"] == 2:
                            self.lists.lst_5l.append(data[item])
                        else:
                            if data[item]["type2"] in self.lists.values_without_padding_f:
                                self.lists.lst_6to9.append(data[item])

                            self.lists.lst_5l.append(data[item])
                    elif data[item]["thickness"] == 2:
                        if data[item]["type1"] == 1:
                            self.lists.lst_6to9.append(item)
                            self.lists.lst_20to22.append(data[item])
                            self.lists.lst_17to19.append(data[item])
                        elif data[item]["type1"] == 2:
                            self.lists.lst_17to19.append(data[item])
                            self.lists.lst_20to22.append(data[item])
                            self.lists.lst_6to9.append(data[item])
                        else:
                            self.lists.lst_17to19.append(data[item])
                            self.lists.lst_10to17.append(data[item])
                    else:
                        if data[item]["type1"] == 1:
                            if data[item]["type2"] in self.lists.values_banpal_f:
                                self.lists.lst_27h.append(data[item])

                            self.lists.lst_23to27.append(data[item])
                            self.lists.lst_10to17.append(data[item])
                            self.lists.lst_20to22.append(data[item])
                        elif data[item]["type1"] == 2:
                            if data[item]["type2"] in self.lists.values_ginbaji_f:
                                self.lists.lst_23to27.append(data[item])

                            self.lists.lst_10to17.append(data[item])
                            self.lists.lst_27h.append(data[item])
                        else:
                            self.lists.lst_20to22.append(data[item])
        # 현재 온도에 적정한 리스트를 이용하기
        if t3h > 27:
            self.lists.temp_lst1 = self.lists.lst_27h
            self.lists.thickness = [1]
        elif t3h > 22:
            self.lists.temp_lst1 = self.lists.lst_23to27
            self.lists.thickness = [1]
        elif t3h > 19:
            self.lists.temp_lst1 = self.lists.lst_20to22
            self.lists.thickness = [1, 2]
        elif t3h > 16:
            self.lists.temp_lst1 = self.lists.lst_17to19
            self.lists.thickness = [2]
        elif t3h > 9:
            self.lists.temp_lst1 = self.lists.lst_10to17
            self.lists.thickness = [1, 2]
        elif t3h > 5:
            self.lists.temp_lst1 = self.lists.lst_6to9
            self.lists.thickness = [2, 3]
        else:
            self.lists.temp_lst1 = self.lists.lst_5l
            self.lists.thickness = [3]

        if self.vars.var_situation.get() == 1:
            self.dress_daily()
        elif self.vars.var_situation.get() == 2:
            self.dress_exam()
        elif self.vars.var_situation.get() == 3:
            self.dress_pt()
        elif self.vars.var_situation.get() == 4:
            self.dress_fancy()
        elif self.vars.var_situation.get() == 5:
            self.dress_wedding()
        elif self.vars.var_situation.get() == 6:
            self.dress_funeral()

    # 데일리 : 트레이닝 바지랑 니트/셔츠/블라우스/원피스는 조합 안 되게
    # num == 1 이면 트레이닝 바지랑 니트/셔츠/블라우스/원피스는 조합 안 되게 입는 것 ///// num == 2 이면 num == 1 일때 제외
    def dress_daily(self):
        num = random.randint(1, 2)

        self.lists.temp_upper = []
        self.lists.temp_lower = []
        self.lists.temp_over = []

        if num == 1:
            temp_exceptions = []
            temp_upper_acceptions = ['Sleeved T-Half', 'Sleeved T-Long', 'Man-to-Man', 'Hood', 'Sleeveless']
            temp_lower_acceptions = ['Training-Pants']
            temp_over_acceptions = ['Jacket-Denim', 'Jacket-Cotton', 'Jumper', 'Padding-Short', 'Padding-Long',
                                    'Hoodie', 'Kardigan']

            length_templist = len(self.lists.temp_lst1)

            temporary = []

            for i in range(length_templist):
                if self.lists.temp_lst1[i]["type2"] not in temp_exceptions:
                    temporary.append(self.lists.temp_lst1[i])

            for i in range(len(temporary)):
                if temporary[i]["type2"] in temp_upper_acceptions:
                    self.lists.temp_upper.append(temporary[i])
                elif temporary[i]["type2"] in temp_lower_acceptions:
                    self.lists.temp_lower.append(temporary[i])
                elif temporary[i]["type2"] in temp_over_acceptions:
                    self.lists.temp_over.append(temporary[i])

        if num == 2:
            temp_exceptions = []
            temp_upper_acceptions = ['Shirts', 'Knit', 'Man-to-Man', 'Sleeved T-Half', 'Sleeved T-Long', 'Hood',
                                     'Sleeveless', 'Shirts & Blouse', 'One-Piece']
            temp_lower_acceptions = ['Denim-Skinny', 'Denim-Straight', 'Denim-Wide', 'Cotton-Skinny', 'Cotton-Straight',
                                     'Cotton-Wide', 'Slacks', 'Shorts'
                                                              'Denim-Boots-Cut', 'Cotton-Boots-Cut', 'Skirt-Mini',
                                     'Skirt-Midi', 'Skirt-Long']
            temp_over_acceptions = ['Jacket-Denim', 'Jacket-Cotton', 'Jacket-Leather', 'Mustang', 'Jacket-Suit',
                                    'Coat-Short',
                                    'Coat-Long', 'Jumper', 'Padding-Short', 'Padding-Long', 'Hoodie', 'Kardigan']

            length_templist = len(self.lists.temp_lst1)

            temporary = []

            for i in range(length_templist):
                if self.lists.temp_lst1[i]["type2"] not in temp_exceptions:
                    temporary.append(self.lists.temp_lst1[i])
            for i in range(len(temporary)):
                if temporary[i]["type2"] in temp_upper_acceptions:
                    self.lists.temp_upper.append(temporary[i])
                elif temporary[i]["type2"] in temp_lower_acceptions:
                    self.lists.temp_lower.append(temporary[i])
                elif temporary[i]["type2"] in temp_over_acceptions:
                    self.lists.temp_over.append(temporary[i])

        self.final_codi()

    def dress_exam(self):
        temp_exceptions = ['Shirts', 'Shirts & Blouse', 'One-Piece', 'Knit', 'Slacks', 'Skirt-Mini', 'Skirt-Midi', 'Skirt-Long', 'Coat-Long', 'Coat-Short', 'Mustang', 'Jacket-Leather', 'Jacket-Denim', 'Jacket-Cotton', 'Jacket-Suit']
        temp_over_acceptions = ['Padding-Short', 'Padding-Long', 'Hoodie', 'Kardigan']
        length_templist = len(self.lists.temp_lst1)

        temporary = []
        self.lists.temp_upper = []
        self.lists.temp_lower = []
        self.lists.temp_over = []
        for i in range(length_templist):
            if self.lists.temp_lst1[i]["type2"] not in temp_exceptions:
                temporary.append(self.lists.temp_lst1[i])
        for i in range(len(temporary)):
            if temporary[i]["type1"] == 1:
                self.lists.temp_upper.append(temporary[i])
            elif temporary[i]["type2"] == 'Training-Pants':
                self.lists.temp_lower.append(temporary[i])
            elif temporary[i]["type2"] in temp_over_acceptions:
                self.lists.temp_over.append(temporary[i])

        self.final_codi()

    def dress_pt(self):
        temp_exceptions = ['Training-Pants']
        temp_upper_acceptions = ['Shirts', 'Knit', 'Shirts & Blouse']
        temp_over_acceptions = ['Jacket-Denim', 'Jacket-Cotton', 'Jacket-Suit', 'Coat-Short', 'Coat-Long']

        self.lists.temp_upper = []
        self.lists.temp_lower = []
        self.lists.temp_over = []

        length_templist = len(self.lists.temp_lst1)

        temporary = []

        for i in range(length_templist):
            if self.lists.temp_lst1[i]["type2"] not in temp_exceptions:
                temporary.append(self.lists.temp_lst1[i])

        for i in range(len(temporary)):
            if temporary[i]["type2"] in temp_upper_acceptions:
                self.lists.temp_upper.append(temporary[i])
            elif temporary[i]["type1"] == 2:
                self.lists.temp_lower.append(temporary[i])
            elif temporary[i]["type2"] in temp_over_acceptions:
                self.lists.temp_over.append(temporary[i])

        self.final_codi()
    def dress_fancy(self):

        temp_exceptions = ["Training-Pants", "Man-to-Man", "Hood", "Hoodie", "Padding-Short", "Padding-Long", "소분류 선택"]
        length_templist = len(self.lists.temp_lst1)

        temporary_list = []
        temporary_c_list = []
        self.lists.temp_upper = []
        self.lists.temp_lower = []
        self.lists.temp_over = []

        for i in range(length_templist):
            if self.lists.temp_lst1[i]["type2"] not in temp_exceptions:
                temporary_list.append(self.lists.temp_lst1[i])

        for i in range(len(temporary_list)):
            if temporary_list[i]["type1"] == 1:
                self.lists.temp_upper.append(temporary_list[i])
                # self.lists.c_temp_upper.append(temporary_list[i]["color"])
            elif temporary_list[i]["type1"] == 2:
                self.lists.temp_lower.append(temporary_list[i])
                # self.lists.c_temp_lower.append(temporary_list[i]["color"])
            else:
                self.lists.temp_over.append(temporary_list[i])
                # self.lists.c_temp_over.append(temporary_list[i]["color"])

        self.final_codi()

    def dress_wedding(self):

        temp_exceptions = ["Training-Pants", "Man-to-Man", "Hood", "Hoodie", "소분류 선택", "Mustang", "Jacket-Leather"]

        temporary = []
        self.lists.temp_upper = []
        self.lists.temp_lower = []
        self.lists.temp_over = []

        for i in range(len(self.lists.temp_lst1)):
            if self.lists.temp_lst1[i]["type2"] not in temp_exceptions:
                if self.lists.temp_lst1[i]["color"] != "White":
                    temporary.append(self.lists.temp_lst1[i])
        for i in range(len(temporary)):
            if temporary[i]["type1"] == 1:
                self.lists.temp_upper.append(temporary[i])
            elif temporary[i]["type1"] == 2:
                self.lists.temp_lower.append(temporary[i])
            else:
                self.lists.temp_over.append(temporary[i])

        self.final_codi()

    def dress_funeral(self):

        temp_exceptions = ["Training-Pants", "소분류 선택"]
        length_templist = len(self.lists.temp_lst1)
        temporary = []

        self.lists.temp_upper = []
        self.lists.temp_lower = []
        self.lists.temp_over = []

        for i in range(length_templist):
            if self.lists.temp_lst1[i]["type2"] not in temp_exceptions:
                if self.lists.temp_lst1[i]['color'] == "Black":
                    temporary.append(self.lists.temp_lst1[i])
        for i in range(len(temporary)):
            if temporary[i]["type1"] == 1:
                self.lists.temp_upper.append(temporary[i])
            elif temporary[i]["type1"] == 2:
                self.lists.temp_lower.append(temporary[i])
            else:
                self.lists.temp_over.append(temporary[i])

        self.final_codi()

    def final_codi(self):
        #일단 인벤토리에 옷이 있는지 확인부터하고 없으면 else로 돌아가 없다고 알림
        if len(self.lists.temp_upper) > 0:
            self.lists.first_item = random.choice(self.lists.temp_upper)
            starting_color = self.lists.first_item["color"]
            starting_color_u = list()

            # 어느 색인지 리스트에서 파악하고 그 색에 해당하는 조합들을 불러온다
            for i in range(len(self.lists.values_color)):

                if starting_color == self.lists.values_color[i]:
                    starting_color_u = self.lists.c_total[i]

            #하의 목록들 하나씩 보면서 색이 맞는지 살핀다
            for i in range(len(self.lists.temp_lower)):
                if self.lists.temp_lower[i]["color"] in starting_color_u:
                    self.lists.c_temp_lower.append(self.lists.temp_lower[i])

            #만약에 새로 뽑힌 하의 목록에 하나라도 있다면 코디를 진행한
            if self.lists.c_temp_lower:
                self.lists.second_item = random.choice(self.lists.c_temp_lower)
                second_item_c = self.lists.second_item["color"]

            second_color = list()

            #이제 두번째 색의 조합 색 리스트를 불러온다
            for i in range(len(self.lists.values_color)):
                if starting_color == self.lists.values_color[i]:
                    second_color = self.lists.c_total[i]

            #외투 인벤토리 목록을 하나씩 비교
            for i in range(len(self.lists.temp_over)):
                if self.lists.temp_over[i]["color"] in starting_color_u and self.lists.temp_over[i][
                    "color"] in second_color:
                    self.lists.c_temp_over.append(self.lists.temp_over[i])

            #외투 목록이 0이 아니면 조합 실시
            if len(self.lists.c_temp_over) > 0:
                self.lists.third_item = random.choice(self.lists.c_temp_over)
                third_item_c = self.lists.third_item["color"]

            # 옷 조합이 없을 경우
            if not self.lists.c_temp_lower:
                messagebox.showinfo("오늘 이 옷 어때", "옷이 없네용 ㅠㅠ")
            elif not self.lists.c_temp_over:
                messagebox.showinfo("오늘 이 옷 어때", "옷이 없네용 ㅠㅠ")
            else:
                self.lists.recommendation = ("오늘, 두께 %s의 \n[ %s컬러의 %s ]와(과) \n[ %s컬러의 %s ]와(과) \n[ %s컬러의 %s ] 어때요?" % (
                self.lists.thickness, starting_color, self.lists.first_item["type2"], second_item_c,
                self.lists.second_item["type2"], third_item_c, self.lists.third_item["type2"]))
                messagebox.showinfo("오늘 이 옷 어때", self.lists.recommendation)
                print("done")
        else:
            messagebox.showinfo("오늘 이 옷 어때", "옷이 없네용 ㅠㅠ")

app = SeaofBTCapp()
app.geometry("500x320")
app.mainloop()
