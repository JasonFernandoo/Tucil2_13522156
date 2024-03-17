from Point import Point
import time

def generate_bezier_bruteforce(start_point, control_point, end_point, iterations, canvas, canvas_width, canvas_height):
    start_time_brute = time.time()
    num_points = 2 ** iterations
    points = [start_point]
    for i in range(1, num_points):
        t = i / num_points
        x = (1 - t)**2 * start_point.x + 2 * (1 - t) * t * control_point.x + t**2 * end_point.x
        y = (1 - t)**2 * start_point.y + 2 * (1 - t) * t * control_point.y + t**2 * end_point.y
        points.append(Point(x, y))
    points.append(end_point)
    
    scaled_brute_force_points = [(point.x * canvas_width/14, (canvas_height - point.y * canvas_height/20)-105) for point in points if point.x >= 0 and point.y >= 0]
    canvas.create_line(scaled_brute_force_points, smooth=True, fill="red")
    
    end_time_brute = time.time() 
    execution_time_brute_force = (end_time_brute - start_time_brute) * 1000
    
    return execution_time_brute_force