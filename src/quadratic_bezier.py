import time

def create_bezier(ctrl1, ctrl2, ctrl3, iterations, canvas, canvas_width, canvas_height):
    start_time_quadratic = time.time()
    bezier_points = []
    control_points = [ctrl1, ctrl2, ctrl3]  
    
    def populate_bezier_points(ctrl1, ctrl2, ctrl3, current_iteration, iterations):
        nonlocal bezier_points
        if current_iteration < iterations:
            mid_point1 = mid_point(ctrl1, ctrl2)
            mid_point2 = mid_point(ctrl2, ctrl3)
            mid_point3 = mid_point(mid_point1, mid_point2)
            current_iteration += 1
            populate_bezier_points(ctrl1, mid_point1, mid_point3, current_iteration, iterations)
            bezier_points.append(mid_point3)
            populate_bezier_points(mid_point3, mid_point2, ctrl3, current_iteration, iterations)
        else:
            bezier_points.extend([ctrl1, ctrl3])
        
    def mid_point(control_point1, control_point2):
        return ((control_point1[0] + control_point2[0]) / 2, (control_point1[1] + control_point2[1]) / 2)
    
    populate_bezier_points(ctrl1, ctrl2, ctrl3, 0, iterations)
    
    scaled_bezier_points = [((point[0] * canvas_width/14.07 + 30), (canvas_height - point[1] * canvas_height/20.25) - 105) for point in bezier_points if point[0] >= 0 and point[1] >= 0]
    scaled_control_points = [((point[0] * canvas_width/14.07 + 30), (canvas_height - point[1] * canvas_height/20.25) - 105) for point in control_points if point[0] >= 0 and point[1] >= 0]
    
    canvas.create_line(scaled_bezier_points, smooth=True, fill="blue")
    
    for point in scaled_control_points:
        canvas.create_oval(point[0]-2, point[1]-2, point[0]+2, point[1]+2, fill="red")
    
    for i in range(len(scaled_control_points)-1):
        canvas.create_line(scaled_control_points[i], scaled_control_points[i+1], fill="black")
    
    end_time_quadratic = time.time() 
    execution_time_quadratic = (end_time_quadratic - start_time_quadratic) * 1000
    
    return execution_time_quadratic