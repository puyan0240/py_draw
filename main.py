import tkinter


mouse_x = mouse_y = 0
mouse_old_x = mouse_old_y = 0
mouse_in_canvas = mouse_left_pushed = False


############################################################
#マウス移動
############################################################
def mouse_move(e):
    global mouse_x,mouse_y
    global mouse_old_x,mouse_old_y
    global mouse_in_canvas,mouse_left_pushed

    if mouse_in_canvas == False:
        return  #マウスがキャンバス内に居ない
    if mouse_left_pushed == False:
        return  #マウス左ボタンが押されていない

    #座標更新
    mouse_old_x = mouse_x
    mouse_old_y = mouse_y
    mouse_x = e.x
    mouse_y = e.y

    #キャンバスに線を描く
    canvas.create_line(mouse_x, mouse_y, mouse_old_x, mouse_old_y, fill="BLACK", width=100)


############################################################
#マウス左ボタン押す
############################################################
def mouse_push_left(e):
    global mouse_x,mouse_y
    global mouse_old_x,mouse_old_y
    global mouse_in_canvas,mouse_left_pushed

    if mouse_in_canvas == False:
        return  #マウスがキャンバス内に居ない

    mouse_x = e.x
    mouse_y = e.y
    mouse_left_pushed = True


############################################################
#マウス左ボタン離す
############################################################
def mouse_release_left(e):
    global mouse_x,mouse_y
    global mouse_old_x,mouse_old_y
    global mouse_in_canvas,mouse_left_pushed

    mouse_x = mouse_y = mouse_old_x = mouse_old_y = 0
    mouse_left_pushed = False


############################################################
#マウスがキャンバスに入った
############################################################
def mousu_enter_canvas(e):
    global mouse_in_canvas
    mouse_in_canvas = True


############################################################
#マウスがキャンバスから出た
############################################################
def mousu_leave_canvs(e):
    global mouse_in_canvas
    mouse_in_canvas = False

    #マウス監視状態をクリアする
    mouse_release_left(e)


############################################################
#クリアボタンが押された
############################################################
def btn_clr_clicked():
    canvas.delete("all")    #キャンバス内を全クリア


############################################################
#保存ボタンが押された
############################################################
def btn_save_clicked():
    try:
        canvas.postscript(file="test.ps", colormode="color")
    except Exception as e:
        print(e)


color_list = ["black","gray","white","blue","green","yellow","red","black"]

############################################################
#背景色ボタンが押された
############################################################
def btn_bg_clicked():
    global color_list

    now_color = btn_bg["text"]  #現在の背景色
    idx = color_list.index(now_color)
    next_color = color_list[idx+1]  #次の背景色を選択

    #ボタンのテキスト/色を変更
    btn_bg.config(text=next_color, bg=next_color)

    #キャンパスの背景色を変更
    canvas.config(bg=next_color)




root = tkinter.Tk()
root.title("Draw")
#root.geometry("600x400")

root.bind("<Motion>", mouse_move)
root.bind("<Button-1>", mouse_push_left)
root.bind("<ButtonRelease-1>", mouse_release_left)

frame_left = tkinter.Frame(root, padx=5, pady=5, width=200)
frame_left.propagate(False)     #フーレムサイズの自動調整を無効にする
frame_left.pack(side=tkinter.LEFT, fill=tkinter.Y)
#クリアボタン
btn_clr = tkinter.Button(frame_left, text="クリア", width=15, command=btn_clr_clicked)
btn_clr.pack()

#保存ボタン
btn_save = tkinter.Button(frame_left, text="保存", width=15, command=btn_save_clicked)
btn_save.pack(pady=5)

#背景色
label_bg = tkinter.Label(frame_left, text="背景色")
label_bg.pack(pady=(20,0))
btn_bg = tkinter.Button(frame_left, text="white" ,width=15, bg="white", command=btn_bg_clicked)
btn_bg.pack()


canvas = tkinter.Canvas(root, bg="WHITE", width=800, height=600)
canvas.bind("<Enter>", mousu_enter_canvas)
canvas.bind("<Leave>", mousu_leave_canvs)

canvas.pack(side=tkinter.LEFT)

root.mainloop()