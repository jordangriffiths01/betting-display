import tkinter as tk

root = tk.Tk()

# If you only want to remove max, min and resize button below line is sufficient  
root.overrideredirect(True)
# above line will helpful in designing flash screens

# To display the screen in full screen mode
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
print(root.winfo_screenwidth())
print(root.winfo_screenheight())

root.call("::tk::unsupported::MacWindowStyle", "style", root._w, "plain", "none")
root.wm_attributes('-fullscreen', 1)


root.mainloop()