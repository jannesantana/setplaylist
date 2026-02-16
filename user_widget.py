# playlist_widget.py
import tkinter as tk
from typing import List, Tuple, Optional


def get_playlist_input(
    title: str = "Playlist Entry",
    geometry: str = "400x600+50+50",
    default_name: str = "Playlist name"):
    """
    Opens a Tkinter window to collect a playlist name and a list of URLs.

    Returns
    -------
    (name, urls)
        name: str or None if user cancelled/closed the window
        urls: list of non-empty, stripped lines
    """
    root = tk.Tk()
    root.title(title)
    root.geometry(geometry)

    plname_var = tk.StringVar(value=default_name)
    result = {"name": None, "urls": []}

    def _submit():
        name = plname_var.get().strip()
        raw = urls_text.get("1.0", "end")
        urls = [line.strip() for line in raw.splitlines() if line.strip()]

        result["name"] = name
        result["urls"] = urls

        root.quit()  # exit mainloop

    def _cancel():
        # leave defaults: name=None, urls=[]
        root.quit()

    # If user closes the window using the window manager "X"
    root.protocol("WM_DELETE_WINDOW", _cancel)

    # --- Widgets ---
    name_entry = tk.Entry(root, textvariable=plname_var)
    name_entry.pack(padx=5, pady=5, fill="x")

    urls_label = tk.Label(root, text="URLs")
    urls_label.pack(padx=5, pady=5, fill="x")

    urls_text = tk.Text(root, width=10, height=30)
    urls_text.pack(padx=5, pady=5, fill="both", expand=True)

    btn_row = tk.Frame(root)
    btn_row.pack(padx=5, pady=5, fill="x")

    submit_btn = tk.Button(btn_row, text="Submit", command=_submit)
    submit_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))

    cancel_btn = tk.Button(btn_row, text="Cancel", command=_cancel)
    cancel_btn.pack(side="left", expand=True, fill="x", padx=(5, 0))

    # Focus and select default name for quick overwrite
    name_entry.focus_set()
    name_entry.selection_range(0, "end")

    root.mainloop()
    root.destroy()

    return result["name"], result["urls"]
