import random, os
import tkinter as tk
from PIL import ImageTk, Image

class Application:
    def __init__(self, root):
        self.root = root
        self.scale = 0.4
        self.current = 0
        self.image_dir = "./liikenne_merkit/"
        self.current_image = ""
        self.image_label = tk.Label()
        self.init_window()
        self.change_image()

    def change_image(self):
        self.image_label.pack_forget()
        image_list = os.listdir(self.image_dir)
        self.current_image = os.path.abspath(os.path.join(self.image_dir, random.choice(image_list)))
        original_img = Image.open(self.current_image)
        new_width = int(original_img.width * self.scale)
        new_height = int(original_img.height * self.scale)
        img = original_img.resize((new_width, new_height))
        scaled_img = ImageTk.PhotoImage(img)
        self.image_label = tk.Label(self.root, image=scaled_img)
        self.image_label.image = scaled_img
        self.image_label.pack()

    def reveal_name(self):
        self.image_label.pack_forget()
        sign_name = os.path.basename(self.current_image)
        sign_name = sign_name.split(".")[0].split("_")[0].split("-")
        sign_name.pop(0)
        sign_name = " ".join(sign_name)
        self.image_label = tk.Label(self.root, text=sign_name)
        self.image_label.config(font=("TkDefaultFont", 40))
        self.image_label.pack()

    def init_window(self):
        self.root.title("liikennemerkki opiskelu työkaly")
        self.root.geometry("1200x800")
        next_button = tk.Button(self.root, text="next", command=self.change_image)
        reveal_button = tk.Button(self.root, text="reveal", command=self.reveal_name)
        next_button.pack()
        reveal_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    application = Application(root)
    root.mainloop()

