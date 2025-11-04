#Visualize the route of the optimal path
#input: Path of points (array)
#Output: visualization of route (png)
#Jason
import os # used for saving the image to the computer
from PIL import Image, ImageDraw # pillow is used to make image


def saveRouteImg(listOfPoints, finalPath, sumOfDistance, input_filename):
    
    # convert data to pairs of coordinates (x, y)
    coords = [(float(p.x), float(p.y)) for p in listOfPoints]
    routePoints = [(float(p.x), float(p.y)) for p in finalPath]
    
    xs, ys = zip(*coords) # use zip function to separate the x's and y's from coords so now have collection of x's and collection of y's
    
    # find max and min of x and of y to define bounding box of points
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    
    # compute total horizontal (dx) and vertical (dy) spans
    dx = max_x - min_x
    dy = max_y - min_y
    
    aspect = dx/dy if dy !=0 else 1 # checks to make sure the set of points is not vertically flat
    min_dim = 1920 # smaller image dimension must be 1920 pixels as specified
    
    # scale the image and make sure to preserve the aspect ratio / smaller side of the two is set to min_dim
    if aspect >= 1:
        height = min_dim
        width = int(height * aspect)
    else:
        width = min_dim
        height = int(width / aspect)
    
    # creates a blank white image to be drawn on
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img) # use this to draw on image
    
    
    # scale/convert coords to pixels adds 10 px margin
    def scale(pt):
        x = 10 + (pt[0] - min_x) / dx * (width - 20)
        y = 10 + (pt[1] - min_y) / dy * (height - 20)
        return (x, height - y) # pixel position and height - y is to keep image upright
    
    # ensure no stray points by making sure all points are plotted are in the final route
    routePointsSet = {(float (x), float (y)) for x, y in routePoints}
    plotPoints = [p for p in listOfPoints if (float(p.x), float(p.y)) in routePointsSet] # goes through each p in listOfPoints  and checks if that x,y coord is in the route set so no extra possible points
    
    # takes all points in plotPoints and uses the scale function to convert them
    scaledCoords = [scale((float(p.x), float(p.y))) for p in plotPoints]

    # apply the scale function to convert all points in routePoints
    scaledRoute = [scale(p) for p in routePoints]
    
    # green dots for all points
    for x, y in scaledCoords: # every coordinate is drawn and appears green (start point color will be changed)
        draw.ellipse((x-5, y-5, x+5, y+5), fill = "green") # dimensions and colors
        
    # black connecting line
    if scaledRoute[0] != scaledRoute[-1]: # checks to see if first element in scaledRoute is the same as the final element
        scaledRoute.append(scaledRoute[0]) # so if the start and ending elements are not the same then append the first point to the end to make sure the drone lands where it took off
    draw.line(scaledRoute, fill = "black", width = 2) # in the order of the best route a line is drawn to follow along the bebst route
    
    # red dot starting/landing coord
    sx, sy = scaledRoute[0] # grab the takeoff/landing coordinate from the route coordinates that was scaled (it is the first point)
    draw.ellipse((sx-5, sy-5, sx+5, sy+5), fill = "red") # draws the dot for this takeoff/landing coordinate and makes it red
    
    # setting up file name
    baseName = os.path.splitext(os.path.basename(input_filename))[0] # takes the original filename that was input and just takes the part with the name not what comes after
    D = int(round(sumOfDistance)) # want a whole rounded number for the distance (distance is part of the file name output1)
    fileSaveName = f"{baseName}_SOLUTION_{D}.png" # full filename that will be saved for the image

    # find path on device desktop
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    oneDrive = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
    if os.path.isdir(oneDrive):
        desktop = oneDrive

    os.makedirs(desktop, exist_ok=True)
    full_path = os.path.join(desktop, fileSaveName)

    # saves the image (as a png) to correct path on device
    img.save(full_path)
    print(f"Image saved to: {full_path}")
    return full_path