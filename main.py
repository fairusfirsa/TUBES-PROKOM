import programutama as h1
import tkinter as tk 


main = tk.Tk()
main.state('zoomed')
main.title('Cicilan Aman')
main.resizable(False,False)

page_check=0

if __name__=='__main__':
    h1.halaman1(main)
    main.mainloop()
