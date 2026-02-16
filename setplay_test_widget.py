import tkinter as tk
root = tk.Tk()
root.title("Tkinter Entry")
root.geometry("400x600+50+50")
plname_var = tk.StringVar()



def submit():
    name = plname_var.get()
    urlss = URLs_text.get("1.0", "end")
    list_urls = urlss.splitlines()
    print(f"playlist name = {name}")
    print(list_urls)
    plname_var.set("")
    root.destroy()
    


plname_entry = tk.Entry(root,textvariable=plname_var)
plname_entry.insert(0, "Playlist name")

plname_entry.pack(padx=5, pady=5, fill="x")



URLs_label = tk.Label(root, text="URLs")
URLs_label.pack(padx=5,pady=5,fill='x')

URLs_text = tk.Text(root,width=10,height=30)
URLs_text.pack(padx=5,pady=5,fill='x')


sub_btn=tk.Button(root,text = 'Submit', command =submit)
sub_btn.pack(padx=5,pady=5,fill='x')

root.mainloop()

