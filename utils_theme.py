import tkinter as tk
from tkinter import font
from tkinter import ttk


class Theme:
    ListFont = '宋体 13'
    TableFontSize = 12

    MainBg, MainFg = '#222222', 'gold'
    MenuBg, MenuFg = '#303030', 'gold'
    SelectedBg = '#0078D7'

    BtnBg = '#303030'

    LabelFg = '#E0E0E0'
    TextFg = '#cfcfcf'

    UpColor = 'deeppink'
    DownColor = 'lime'
    EvenColor = 'deepskyblue'
    IndexColor = 'darkorange'

    InsertColor = MainFg

    _DateTheme = dict(
        background=MenuBg,
        foreground=MenuFg,
        bordercolor=MenuBg,
        headersbackground=MenuBg,
        headersforeground=MenuFg,
        selectbackground=MainFg,
        selectforeground=MainBg,
        normalbackground=MainBg,
        normalforeground=MainFg,
        weekendbackground=MainBg,
        weekendforeground=UpColor,
        othermonthbackground=MenuBg,
        othermonthforeground=TextFg,
        othermonthwebackground=MenuBg,
        othermonthweforeground=UpColor,
    )

    @staticmethod
    def InitTheme(root: tk.Tk):

        Theme.InitOptions(root)

        style = ttk.Style(root)
        style.theme_create("mine", parent="alt", settings={
            ".": {"configure": {"background": Theme.MainBg, "foreground": Theme.MainFg, 'insertcolor': Theme.MainFg, 'font': '宋体 12',
                                'insertwidth': 2, 'anchor': tk.CENTER, 'fieldbackground': Theme.MainBg, "selectbackground": Theme.MainFg,
                                "selectforeground": Theme.MainBg, 'bordercolor': 'black', 'borderwidth': 0}},

            'TLabelframe.Label': {"configure": {'font': '宋体 15', 'foreground': Theme.LabelFg, 'padding': 0}},

            'TLabel': {"configure": {'font': '宋体 15', 'foreground': Theme.LabelFg, 'padding': 0}},

            "TNotebook.Tab": {"configure": {"padding": [8, 0], 'font': '黑体 16 bold'},
                              "map": {"background": [("selected", Theme.MainFg)], "foreground": [("selected", Theme.MainBg)]}},

            "TCheckbutton": {"configure": {'font': ("Calibri", 13, 'normal'), 'indicatorcolor': Theme.BtnBg, },
                             "map": {"background": [("active", Theme.MainFg)], "foreground": [("active", Theme.MainBg)], "indicatorcolor": [("active", Theme.MainFg)]}},

            "TCombobox": {'configure': {'arrowcolor': Theme.MainFg}, "map": {"background": [("active", Theme.MainFg)], 'arrowcolor': [("active", Theme.MainBg)]}},

            "TButton": {"configure": {"font": ("Calibri", 15, 'bold'), 'background': Theme.BtnBg, 'relief': tk.FLAT, 'padding': 0},
                        "map": {"background": [("active", Theme.MainFg)], "foreground": [("active", Theme.MainBg)]}},

            'TRadiobutton': {"configure": {"font": ("Calibri", 15, 'bold'), 'background': Theme.BtnBg, 'relief': tk.FLAT, 'indicatoron': False, 'offrelief': tk.RAISED, 'selectcolor': 'red'},
                             "map": {"background": [("active", Theme.MainFg)], "foreground": [("active", Theme.MainBg)]}},

        })
        style.theme_use("mine")

        style.configure('big.TCheckbutton', font=("Calibri", 18, 'bold'))
        style.configure('mid.TCheckbutton', font=("Calibri", 15, 'bold'))
        style.configure('big.TButton', font=("Calibri", 18, 'bold'))
        style.configure('mid.TButton', font=("Calibri", 15, 'bold'))
        style.configure('segoe.TButton', font=("Calibri", 18, 'bold'))
        style.configure('btn.TCombobox', fieldbackground=Theme.MainFg,
                        foreground=Theme.MainBg, bordercolor=Theme.MainFg)

    @staticmethod
    def InitOptions(root: tk.Tk):
        '''
        options for *TCombobox*Listbox
                *TCombobox*Listbox.background color
                *TCombobox*Listbox.font font
                *TCombobox*Listbox.foreground color
                *TCombobox*Listbox.selectBackground color
                *TCombobox*Listbox.selectForeground color

        https://www.yisu.com/zixun/570356.html
        如果需要对每个控件进行单独控制，首先要为控件指定名称。下面的代码通过name属性分别为两个标签控件指定了各自的名称。

        # create a label to change state.
        upper_display = Label(root,name='upperDisplay',foreground="#000000",width=24, anchor=E)
        upper_display.grid(row=1, column=0, columnspan=4, sticky=E + W)
        # create a label to change state.
        lower_display = Label(root,name='lowerDisplay',foreground="#000000",width=12, anchor=E)
        lower_display.grid(row=2, column=0, columnspan=4, sticky=E + W)


        名称指定完成之后就可以使用名称为特定的控件指定属性了。为了和分类指定区别，控件的名称必须小写。
        ftTimes1 = Font(family='Times', size=12, weight=BOLD)
        ftTimes2 = Font(family='Times', size=24, weight=BOLD)
        root.option_add('*upperDisplay.font', ftTimes1)
        root.option_add('*lowerDisplay.font', ftTimes2)
        root.option_add('*Button*font', ftTimes1)


        Tkinter还提供了通过配置文件修改控件属性的功能。下面的代码就是指定计算器中每个控件的字体和颜色的实例。
        *Label.background:#a0ffa0
        *upperDisplay.font:times 12 bold
        *lowerDisplay.font:times 24 bold
        *Button*font: Meiryo 12 bold
        *Button*foreground:#007700
        *ckey*foreground:#ff0000
        *cekey*foreground:#ff0000
        *back*foreground:#ff0000
        *devkey*foreground:#0000ff
        *mulkey*foreground:#0000ff
        *minukey*foreground:#0000f
        f*pluskey*foreground:#0000ff
        *equalkey*foreground:#000000

        配置文件完成之后，取一个适当的名字保存即可。本例中使用26 OpDb.txt。
        最后一步就是在代码中增加下面一行以读入配置文件：
        root.option_readfile('26 OpDb.txt')

        '''
        # change Tk option database

        # 改变全局font
        mFont = font.Font(family="microsoft yahei", size=12)
        root.option_add("*Font", mFont)

        # 改变全局 fg
        # root.option_add('*Background', Theme.MainBg)
        # root.option_add('*Foreground', Theme.MainFg)

        # 修改 Combobox的下拉框颜色
        root.option_add("*TCombobox*Listbox.background", Theme.MenuBg)
        root.option_add("*TCombobox*Listbox.foreground", Theme.MenuFg)
        root.option_add("*TCombobox*Listbox.font", '宋体 15')

        root.option_add('*tearOff', False)

        # 修改菜单颜色
        root.option_add('*Menu*foreground', Theme.MainFg)
        root.option_add('*Menu*background', Theme.MainBg)
