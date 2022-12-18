from pykiwoom.kiwoom import *
import tkinter as tk

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# 조건식을 PC로 다운로드
kiwoom.GetConditionLoad()

# 전체 조건식 리스트 얻기
conditions = kiwoom.GetConditionNameList()

bol = kiwoom.SendCondition("0101", conditions[3][1], conditions[3][0], 0)
stc = kiwoom.SendCondition("0101", conditions[4][1], conditions[4][0], 0)


def JudgeStockSellIndex():
    sell_index = ""
    global bol
    global stc
    for b in bol:
        b_stock_name = kiwoom.GetMasterCodeName(b)
        if checkStockEntry.get() == b_stock_name:
            sell_index += " 볼린저밴드 상한선 접근 "
    for st in stc:
        st_name = kiwoom.GetMasterCodeName(st)
        if checkStockEntry.get() == st_name:
            sell_index += " 스톡캐스트 매도 타점 "
    if sell_index == "":
        sell_index = " 매도 타점이 아님"
    stockSell.configure(text=("{}은/는{}".format(checkStockEntry.get(), sell_index)))


def PlusOwnStock():
    f = open("보유주식목록.txt", "a")
    if stockListEntry.get() != "":
        f.write(stockListEntry.get() + "\n")
    f.close()


def GetOwnStock():
    ownStocks = ""
    f = open("보유주식목록.txt", "r")
    stocks = f.readlines()
    for st in stocks:
        st = st.strip()
        ownStocks += (st + " ")
    f.close()
    ownStockList.configure(text=ownStocks)


def DelOwnStock():
    ownStocks = []
    f = open("보유주식목록.txt", "r")
    stocks = f.readlines()
    for st in stocks:
        st = st.strip()
        if stockListEntry.get() != st:
            ownStocks.append(st)
    f.close()
    f = open("보유주식목록.txt", "w")
    for st in ownStocks:
        f.write(st + "\n")
    f.close()


window = tk.Tk()

window.title("보유 주식 매도 타점 확인")
window.geometry("400x400+100+100")
window.resizable(True, True)

ownStockTxt = tk.Label(window, text="보유 주식 목록", height=2)
getStockList = tk.Button(window, text="보유 주식 목록 가져오기", command=lambda: GetOwnStock())
ownStockList = tk.Label(window, text="", height=2)
plusStockTxt = tk.Label(window, text="주식명 입력")
stockListEntry = tk.Entry(window, width=20)
plusBtn = tk.Button(window, text="보유 주식 목록에 추가", command=lambda: PlusOwnStock())
delBtn = tk.Button(window, text="보유 주식 목록에서 제거", command=lambda: DelOwnStock())

inputStock = tk.Label(window, text="보유 주식 입력\n*주식명 맞는지 확인(필수)*", width=30, height=3)
stockSell = tk.Label(window)
checkStockEntry = tk.Entry(window, width=20)
judgeBtn = tk.Button(window, text="확인", command=lambda: JudgeStockSellIndex())

ownStockTxt.grid(row=0, column=0)
getStockList.place(x=200, y=7)
ownStockList.grid(row=1, column=0)
plusStockTxt.grid(row=2, column=0)
stockListEntry.grid(row=3, column=0)
plusBtn.grid(row=4, column=0, sticky="w", pady=5)
delBtn.place(x=170, y=147)

inputStock.grid(row=5, column=0, pady=20)
checkStockEntry.grid(row=6, column=0)
judgeBtn.grid(row=7, column=0)
stockSell.grid(row=8, column=0)

window.mainloop()
