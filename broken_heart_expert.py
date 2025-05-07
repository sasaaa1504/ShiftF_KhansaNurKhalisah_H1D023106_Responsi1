import tkinter as tk
from tkinter import messagebox
from pyswip import Prolog


prolog = Prolog()
prolog.consult("broken_heart_expert.pl")


pertanyaan_gejala = [
    ("Apakah kamu kesulitan tidur karena memikirkan seseorang?", "sulit_tidur"),
    ("Apakah kamu sering overthinking tentang hubungan itu?", "terlalu_banyak_mikir"),
    ("Apakah kamu sering mikirin dia tiap malam?", "mikirin_dia_setiap_malam"),
    ("Apakah kamu kesulitan untuk move on?", "susah_move_on"),
    ("Apakah kamu sering memantau media sosial dia diam-diam?", "stalking_media_sosial"),
    ("Apakah kamu sering terkenang masa lalu dengannya?", "flashback_tiba_tiba"),
    ("Apakah kamu takut jatuh cinta karena trauma sebelumnya?", "takut_disakiti_lagi"),
    ("Apakah kamu pernah merasa dikhianati atau dibohongi?", "merasa_dibohongi"),
    ("Apakah kamu sering menunggu balasan chat dengan gelisah?", "menunggu_chat"),
    ("Apakah kamu masih berharap bisa balikan?", "berharap_balikan"),
    ("Apakah kamu terus curhat hal yang sama ke teman-temanmu?", "curhat_terus"),
    ("Apakah kamu merasa sangat bergantung secara emosional?", "emosional"),
    ("Apakah kamu merasa kosong dan hampa?", "kosong"),
    ("Apakah kamu kehilangan minat melakukan aktivitas biasa?", "kehilangan_minat"),
    ("Apakah kamu suka stalking pacarnya yang baru?", "stalking_pacar_baru"),
]


root = tk.Tk()
root.title("💔 Broken Heart Expert System")
root.geometry("400x550")
root.configure(bg="#f0f4f8")


canvas = tk.Canvas(root, bg="#f0f4f8", highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#f0f4f8")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)


tk.Label(
    scrollable_frame,
    text="🩺 Jawab pertanyaan berikut dengan jujur:",
    font=("Segoe UI", 12, "bold"),
    bg="#f0f4f8",
    pady=10
).pack()


jawaban_vars = []

for teks, _ in pertanyaan_gejala:
    var = tk.StringVar(value="tidak")
    jawaban_vars.append(var)

    frame = tk.Frame(scrollable_frame, bg="#f0f4f8")
    frame.pack(anchor="w", padx=15, pady=4)

    tk.Label(frame, text=teks, bg="#f0f4f8", font=("Segoe UI", 10)).pack(anchor="w")
    tk.Radiobutton(frame, text="Ya", variable=var, value="ya", bg="#f0f4f8", font=("Segoe UI", 9)).pack(anchor="w")
    tk.Radiobutton(frame, text="Tidak", variable=var, value="tidak", bg="#f0f4f8", font=("Segoe UI", 9)).pack(anchor="w")


def diagnosa():
    prolog.retractall("gejala(_)")

    for (_, gejala), var in zip(pertanyaan_gejala, jawaban_vars):
        if var.get() == "ya":
            prolog.assertz(f"gejala({gejala})")

    hasil = list(prolog.query("diagnosa(X)"))
    if hasil:
        list_diagnosa = "\n".join([
            f"✔ {h['X'].decode() if isinstance(h['X'], bytes) else h['X']}" 
            for h in hasil
        ])
        messagebox.showinfo("Hasil Diagnosa", f"Kamu terindikasi mengalami:\n\n{list_diagnosa}")
    else:
        messagebox.showinfo("Hasil Diagnosa", "Tidak ada diagnosis yang cocok.\nKamu mungkin dalam kondisi baik ❤️")


tk.Button(
    scrollable_frame,
    text="💡 Diagnosa Sekarang",
    command=diagnosa,
    bg="#4682B4",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=10,
    pady=5
).pack(pady=20)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
