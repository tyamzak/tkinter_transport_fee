from multiprocessing import Value
import tkinter
import tkinter as tk
import tkinter.ttk as ttk
from typing_extensions import IntVar

##################追加コード　関数###########################
def radio_click():
    if var.get() == 0:
        cbo_dep["values"] = list_region_yp
        cbo_dst["values"] = list_region_yp
        cbo_size["values"] = size_yp
    elif var.get() == 1:
        cbo_dep["values"] = list_region_yt
        cbo_dst["values"] = list_region_yt
        cbo_size["values"] = size_yt

def answer_print():
    value_dep = cbo_dep.get()
    value_dst = cbo_dst.get()
    size_index = cbo_size.current()

    if value_dep and value_dst:
        if var.get() == 0:
            gyosya = '日本郵便'
            chitai = df_chitai_yp.loc[value_dep,value_dst]
            price = dic_yp[str(chitai)][size_index]
        elif var.get() == 1:
            gyosya = 'ヤマト'
            chitai = df_chitai_yt.loc[value_dep,value_dst]
            price = dic_yt[str(chitai)][size_index]
        label["text"]= f'{value_dep} ~ {value_dst}  業者は{gyosya}  地帯は {chitai} 価格は {price}'
    

        
###########################################################


# Tk生成
tki = tkinter.Tk()
# 画面サイズ
tki.geometry('720x720')
# 画面タイトル
tki.title('配送料計算ツール')


### キャンバス作成
canvas = tkinter.Canvas(master=None, width=720, height=720)


### テキスト描画
canvas.create_text(230, 40, text="配送料計算ツール", anchor="se", font=("HG丸ｺﾞｼｯｸM-PRO",20))
canvas.create_text(220, 70, text="1.配送業者を選択してください。", anchor="se", font=("游コジック",11))

### キャンバス表示
canvas.pack()


# ラジオボタン
rdo1 = tkinter.Radiobutton(tki, text='日本郵便')
rdo1.place(x=30, y=80)

rdo2 = tkinter.Radiobutton(tki, text='ヤマト運輸')
rdo2.place(x=120, y=80)

# チェック有無変数
var = tkinter.IntVar()
# value=0のラジオボタンにチェックを入れる
var.set(0)

# ラジオボタン作成
rdo1 = tkinter.Radiobutton(tki, value=0, variable=var, text='日本郵便')
rdo1.place(x=30, y=80)

rdo2 = tkinter.Radiobutton(tki, value=1, variable=var, text='ヤマト運輸')
rdo2.place(x=120, y=80)

#発着地リスト("北海道", "東北", "関東", "信越", "北陸", "東海", "近畿", "中国", "四国", "九州", "沖縄")



index = 0




########追加コード#######################################
dic_yp = {
    #ゆうパック送料リスト群
    "0" : ["取扱なし", "810", "1030", "1280", "1530", "1780", "2010", "2340", "取扱なし", "取扱なし"], #同一都道府県内運賃
    "1" : ["取扱なし", "870", "1100", "1330", "1590", "1830", "2060", "2410", "取扱なし", "取扱なし"], #第1地帯
    "2" : ["取扱なし", "970", "1200", "1440", "1690", "1950", "2160", "2530", "取扱なし", "取扱なし"],
    "3" : ["取扱なし", "1100", "1310", "1560", "1800", "2060", "2270", "2640", "取扱なし", "取扱なし"],
    "4" : ["取扱なし", "1300", "1530", "1760", "2020", "2260", "2490", "2850", "取扱なし", "取扱なし"],
    "5" : ["取扱なし", "1430", "1650", "1890", "2140", "2390", "2610", "2980", "取扱なし", "取扱なし"],
    "6" : ["取扱なし", "1540", "1750", "2000", "2240", "2500", "2720", "3100", "取扱なし", "取扱なし"],
    "7" : ["取扱なし", "1030", "1290", "1570", "1830", "2110", "2320", "2700", "取扱なし", "取扱なし"],
    "8" : ["取扱なし", "1230", "1510", "1770", "2050", "2310", "2540", "2910", "取扱なし", "取扱なし"],
    "9" : ["取扱なし", "1350", "1630", "1900", "2170", "2440", "2660", "3060", "取扱なし", "取扱なし"],
    "10" : ["取扱なし", "1470", "1730", "2010", "2270", "2550", "2770", "3160", "取扱なし", "取扱なし"],
    "11" : ["取扱なし", "1550", "1760", "2010", "2270", "2550", "2770", "3160", "取扱なし", "取扱なし"]
}

#宅急便送料リスト群
dic_yt = {
    "1" : ["680", "930", "1150", "1390", "1610", "1850", "2070", "取扱なし", "2400", "2840"],
    "2" : ["790", "1150", "1370", "1610", "1830", "2070", "2290", "取扱なし", "2620", "3060"],
    "3" : ["840", "1260", "1480", "1720", "1940", "2180", "2400", "取扱なし", "2730", "3170"],
    "4" : ["900", "1370", "1590", "1830", "2050", "2290", "2510", "取扱なし", "2840", "3280"],
    "5" : ["900", "1370", "1590", "1830", "2050", "2290", "2510", "取扱なし", "2840", "3280"],
    "6" : ["950", "1480", "1700", "1940", "2160", "2400", "2620", "取扱なし", "2950", "3390"],
    "7" : ["950", "1480", "1700", "1940", "2160", "2400", "2620", "取扱なし", "2950", "3390"],
    "8" : ["1060", "1700", "1920", "2160", "2380", "2620", "2840", "取扱なし", "3170", "3610"],
    "9" : ["1120", "1810", "2030", "2270", "2490", "2730", "2950", "取扱なし", "3280", "3720"],
    "10" : ["1120", "1810", "2030", "2270", "2490", "2730", "2950", "取扱なし", "3280", "3720"],
    "11" : ["1230", "2030", "2250", "2490", "2710", "2950", "3170", "取扱なし", "3500", "3940"],
    "12" : ["1230", "2030", "2580", "3150", "3700", "4270", "4820", "取扱なし", "5370", "5920"],
    "13" : ["730", "1040", "1260", "1500", "1720", "1960", "2180", "取扱なし", "2510", "2950"],
    "14" : ["1010", "1590", "1810", "2050", "2270", "2510", "2730", "取扱なし", "3060", "3500"],
    "15" : ["1060", "1700", "2250", "2820", "3370", "3940", "4490", "取扱なし", "5040", "5590"],
    "16" : ["1010", "1590", "2140", "2710", "3260", "3830", "4380", "取扱なし", "4930", "5480"],
    "17" : ["900", "1370", "1920", "2490", "3040", "3610", "4160", "取扱なし", "2710", "5260"],
    "18" : ["950", "1480", "2030", "2600", "3150", "3720", "4270", "取扱なし", "4820", "5370"],
    "19" : ["840", "1260", "1810", "2380", "2930", "3500", "4050", "取扱なし", "4600", "5150"]
}

##############100##地帯選択###########

rdo1["command"] = radio_click
rdo2["command"] = radio_click
        

#発着地リスト("北海道", "東北", "関東", "信越", "北陸", "東海", "近畿", "中国", "四国", "九州", "沖縄")
list_region_yp = ["北海道", "東北", "関東", "信越", "北陸", "東海", "近畿", "中国", "四国", "九州", "沖縄"]
list_region_yt = ["北海道","北東北","南東北","関東","信越","北陸","中部","関西","中国","四国","九州","沖縄"]
cbo_dep_label = ttk.Label(tki,text="発送地")
cbo_dst_label = ttk.Label(tki,text="到着地")

cbo_dep = ttk.Combobox(tki)
cbo_dst = ttk.Combobox(tki)

cbo_dep_label.place(x=30, y=120)
cbo_dst_label.place(x=200, y=120)
cbo_dep.place(x=30, y=140)
cbo_dst.place(x=200, y=140)



##############200#################
cbo_size = ttk.Combobox(tki)
cbo_size.place(x=30, y = 200)
size_yt = ["宅急便コンパクト","60サイズ","80サイズ","100サイズ","120サイズ","140サイズ","160サイズ","170サイズ","180サイズ","200サイズ"]
size_yp = ["60","80","100","120","140","160","170"]
##############250#################

import pandas as pd

df_chitai_yp = pd.read_csv('yp_chitai.csv',index_col=0,header=0)
df_chitai_yt = pd.read_csv('yt_chitai.csv',index_col=0,header=0)


#値の取得
button_answer = tk.Button(tki, text="表示", command=answer_print)
button_answer.place(x=30, y=250)

label = tk.Label(tki, text="")
label.place(x = 80, y = 250)


########追加コード終わり#######################################




#計算開始ボタン


### イベントループ
canvas.mainloop()


