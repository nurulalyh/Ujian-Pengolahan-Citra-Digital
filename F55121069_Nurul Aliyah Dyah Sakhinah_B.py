# Nama : Nurul Aliyah Dyah Sakhinah
# NIM : F55121069
# Kelas : B

#Import semua library yang dibutuhkan
import cv2
import tkinter as tk
import numpy as np
from tkinter import filedialog
from PIL import ImageTk, Image

# Fungsi untuk membuka citra
def open_image():
    global image_path, image, original_image, filtered_image, enhanced_image, sharpened_image
    # Membuka jendela dialog untuk memilih file gambar
    image_path = filedialog.askopenfilename()
    # Membaca gambar menggunakan OpenCV
    image = cv2.imread(image_path, 0)
    # Mengkonversi gambar ke format yang dapat ditampilkan pada Tkinter
    original_image = Image.fromarray(image)
    original_image = ImageTk.PhotoImage(original_image)
    # Menampilkan gambar pada jendela utama
    canvas.itemconfig(image_display, image=original_image)
    # Memperbarui label informasi pada jendela utama
    info_label.config(text=f'Image path: {image_path}, Size: {image.shape}')

# Fungsi untuk menerapkan filter median
def apply_median_filter():
    global filtered_image, enhanced_image, sharpened_image
    # Menerapkan filter median menggunakan OpenCV
    filtered_image = cv2.medianBlur(image, 3)
    # Mengkonversi gambar ke format yang dapat ditampilkan pada Tkinter
    filtered_image = Image.fromarray(filtered_image)
    filtered_image = ImageTk.PhotoImage(filtered_image)
    # Menampilkan gambar hasil filter median pada jendela utama
    canvas.itemconfig(image_display, image=filtered_image)
    # Memperbarui label informasi pada jendela utama
    info_label.config(text='Filter applied: Median')

# Fungsi untuk menerapkan teknik perbaikan kontras
def apply_contrast_enhancement():
    global enhanced_image, sharpened_image
    # Menerapkan teknik perbaikan kontras menggunakan OpenCV
    enhanced_image = cv2.equalizeHist(filtered_image)
    # Mengkonversi gambar ke format yang dapat ditampilkan pada Tkinter
    enhanced_image = Image.fromarray(enhanced_image)
    enhanced_image = ImageTk.PhotoImage(enhanced_image)
    # Menampilkan gambar hasil perbaikan kontras pada jendela utama
    canvas.itemconfig(image_display, image=enhanced_image)
    # Memperbarui label informasi pada jendela utama
    info_label.config(text='Filter applied: Contrast Enhancement')

# Fungsi untuk menerapkan filter gaussian
def apply_gaussian_filter():
    global filtered_image, enhanced_image, sharpened_image
    # Menerapkan filter gaussian menggunakan OpenCV
    filtered_image = cv2.GaussianBlur(image, (5,5), 0)
    # Mengkonversi gambar ke format yang dapat ditampilkan pada Tkinter
    filtered_image = Image.fromarray(filtered_image)
    filtered_image = ImageTk.PhotoImage(filtered_image)
    # Menampilkan gambar hasil filter gaussian pada jendela utama
    canvas.itemconfig(image_display, image=filtered_image)
    # Memperbarui label informasi pada jendela utama
    info_label.config(text='Filter applied: Gaussian')

# Fungsi untuk menerapkan filter laplacian
def apply_laplacian_sharpening():
    global filtered_image, enhanced_image, sharpened_image
    # Menerapkan filter laplacian menggunakan OpenCV
    laplacian_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(image, -1, laplacian_kernel)
    # Mengkonversi gambar ke format yang dapat ditampilkan pada Tkinter
    sharpened_image = Image.fromarray(sharpened_image)
    sharpened_image = ImageTk.PhotoImage(sharpened_image)
    # Menampilkan gambar hasil sharpening pada jendela utama
    canvas.itemconfig(image_display, image=sharpened_image)
    # Memperbarui label informasi pada jendela utama
    info_label.config(text='Filter applied: Laplacian Sharpening')

# Membuat jendela utama
root = tk.Tk()
root.title('Image Enhancement')

# Membuat objek canvas untuk menampilkan gambar
canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

# Membuat label nama dan nim di GUI
label_nama = tk.Label(root, text="Nama: Nurul Aliyah Dyah Sakhinah")
label_nama.pack(side=tk.TOP, padx=10, pady=5)

label_nim = tk.Label(root, text="NIM: F55121069")
label_nim.pack(side=tk.TOP, padx=10, pady=5)

# Membuat label informasi
info_label = tk.Label(root, text='No image selected')
info_label.pack()

# Membuat tombol untuk membuka citra
open_button = tk.Button(root, text='Open Image', command=open_image)
open_button.pack()

# Membuat tombol untuk menerapkan filter median
median_filter_button = tk.Button(root, text='Apply Median Filter', command=apply_median_filter)
median_filter_button.pack()

# Membuat tombol untuk menerapkan teknik perbaikan kontras
contrast_enhancement_button = tk.Button(root, text='Apply Contrast Enhancement', command=apply_contrast_enhancement)
contrast_enhancement_button.pack()

# Membuat tombol untuk menerapkan filter gaussian
gaussian_filter_button = tk.Button(root, text='Apply Gaussian Filter', command=apply_gaussian_filter)
gaussian_filter_button.pack()

# Membuat tombol untuk menerapkan filter laplacian
laplacian_sharpening_button = tk.Button(root, text='Apply Laplacian Sharpening', command=apply_laplacian_sharpening)
laplacian_sharpening_button.pack()

# Membuat objek placeholder untuk menampilkan gambar
image_display = canvas.create_image(0, 0, anchor='nw')

# Menjalankan aplikasi
root.mainloop()