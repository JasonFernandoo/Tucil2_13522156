import tkinter as tk
import time
import quadratic_bezier
import brute_force

root = tk.Tk()
root.title("Bezier Curves")

frame1 = tk.Frame(root)
frame1.pack(side=tk.LEFT)

frame2 = tk.Frame(root)
frame2.pack(side=tk.RIGHT)

canvas1 = tk.Canvas(frame1, width=700, height=400)
canvas1.pack()

canvas2 = tk.Canvas(frame2, width=700, height=400)
canvas2.pack()

ctrl1_label = tk.Label(root, text="Control Point 1 (x, y):")
ctrl1_label.pack()
ctrl1_entry = tk.Entry(root)
ctrl1_entry.pack()

ctrl2_label = tk.Label(root, text="Control Point 2 (x, y):")
ctrl2_label.pack()
ctrl2_entry = tk.Entry(root)
ctrl2_entry.pack()

ctrl3_label = tk.Label(root, text="Control Point 3 (x, y):")
ctrl3_label.pack()
ctrl3_entry = tk.Entry(root)
ctrl3_entry.pack()

iterations_label = tk.Label(root, text="Iterations:")
iterations_label.pack()
iterations_entry = tk.Entry(root)
iterations_entry.pack()

def draw_quadratic_bezier(canvas1):
    ctrl1_str = ctrl1_entry.get()
    ctrl2_str = ctrl2_entry.get()
    ctrl3_str = ctrl3_entry.get()
    iterations_str = iterations_entry.get()

    try:
        ctrl1 = tuple(map(float, ctrl1_str.split(',')))
        ctrl2 = tuple(map(float, ctrl2_str.split(',')))
        ctrl3 = tuple(map(float, ctrl3_str.split(',')))
        iterations = int(iterations_str)
    except ValueError:
        tk.messagebox.showerror("Error", "Invalid input. Please enter numbers separated by commas.")
        return

    canvas_width = canvas1.winfo_width()
    canvas_height = canvas1.winfo_height()

    start_time_quadratic = time.time()
    canvas1.create_line(30, 300, 650, 300, fill="black")
    for x in range(1, 13):  
        canvas1.create_line(x * 50, 295, x * 50, 305, fill="black") 
        canvas1.create_text(x * 50, 315, text=str(x), anchor=tk.N) 
    canvas1.create_line(30, 300, 30, 40, fill="black")
    for y in range(20, 240, 20):
        canvas1.create_line(27, y + 60, 35, y + 60, fill="black")
        canvas1.create_text(25, y + 60, text=str(12 - y // 20), anchor=tk.E)  
    execution_time_quadratic = quadratic_bezier.create_bezier(ctrl1, ctrl2, ctrl3, iterations, canvas1, canvas_width, canvas_height)
    end_time_quadratic = time.time() 
    execution_time_quadratic = (end_time_quadratic - start_time_quadratic) * 1000 
    label_exec_time_quadratic = tk.Label(frame1, text=f"Quadratic Bezier execution time: {execution_time_quadratic:.6f} ms", fg="black")
    label_exec_time_quadratic.pack(side=tk.BOTTOM)  


def draw_brute_force(canvas2):
    ctrl1_str = ctrl1_entry.get()
    ctrl2_str = ctrl2_entry.get()
    ctrl3_str = ctrl3_entry.get()
    iterations_str = iterations_entry.get()

    try:
        ctrl1 = tuple(map(float, ctrl1_str.split(',')))
        ctrl2 = tuple(map(float, ctrl2_str.split(',')))
        ctrl3 = tuple(map(float, ctrl3_str.split(',')))
        iterations = int(iterations_str)
    except ValueError:
        tk.messagebox.showerror("Error", "Invalid input. Please enter numbers separated by commas.")
        return

    canvas_width = canvas2.winfo_width()
    canvas_height = canvas2.winfo_height()

    start_time_brute = time.time()
    canvas2.create_line(30, 300, 650, 300, fill="black")
    for x in range(1, 13):  
        canvas2.create_line(x * 50, 295, x * 50, 305, fill="black")  
        canvas2.create_text(x * 50, 315, text=str(x), anchor=tk.N)  
    canvas2.create_line(30, 300, 30, 40, fill="black")
    for y in range(20, 240, 20):
        canvas2.create_line(27, y + 60, 35, y + 60, fill="black")
        canvas2.create_text(25, y + 60, text=str(12 - y // 20), anchor=tk.E)  
    start_point = brute_force.Point(*ctrl1)
    control_point = brute_force.Point(*ctrl2)
    end_point = brute_force.Point(*ctrl3)
    execution_time_brute_force = brute_force.generate_bezier_bruteforce(start_point, control_point, end_point, iterations, canvas2, canvas_width, canvas_height)
    end_time_brute = time.time() 
    execution_time_brute_force = (end_time_brute - start_time_brute) * 1000
    label_exec_time_brute_force = tk.Label(frame2, text=f"Brute Force execution time: {execution_time_brute_force:.6f} ms", fg="black")
    label_exec_time_brute_force.pack(side=tk.BOTTOM)


draw_button = tk.Button(root, text="Draw Curve", command=lambda: (draw_quadratic_bezier(canvas1), draw_brute_force(canvas2)))
draw_button.pack()

root.mainloop()
