#Visualize the route of the optimal path
#input: Path of points (array)
#Output: visualization of route
#Jason
import os # used for saving the image to the computer
from PIL import Image, ImageDraw # pillow is used to make image


def saveRouteImg(listOfPoints, finalPath, sumOfDistance, input_filename):
    
    # convert data to pairs of coordinates
    coords = [(float(p.x), float(p.y)) for p in listOfPoints]
    routePoints = [(float(p.x), float(p.y)) for p in finalPath]
    
    # test
    # print(coords[:6])
    # print(routePoints[:6])
    
    # bounds
    xs, ys = zip(*coords) # separates the x's and y's from coords so now have collection of x's and collection of y's
    
    # find max and min of x and of y
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    
    # test
    # print (xs)
    # print (ys)
    
    # print (min_x)
    # print (max_x)
    # print (min_y)
    # print (max_y)
    
    # make image size & smaller side 1920 px (specified)
    
    dx = max_x - min_x # span of min x to max x so total width
    dy = max_y - min_y # span of min y to max y so total height
    
    aspect = dx/dy if dy !=0 else 1 # checks to make sure the set of points is not vertically flat
    min_dim = 1920 # was specified
    
    if aspect >= 1:
        height = min_dim
        width = int(height * aspect)
    else:
        width = min_dim
        height = int(width / aspect)
        
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    
    
    # scale/convert coords to pixels adds 10 px margin
    
    def scale(pt):
        x = 10 + (pt[0] - min_x) / dx * (width - 20)
        y = 10 + (pt[1] - min_y) / dy * (height - 20)
        return (x, height - y) # pixel position and height - y is to keep image upright
    
    # ensure no stray points
    routePointsSet = {(float (x), float (y)) for x, y in routePoints}
    plotPoints = [p for p in listOfPoints if (float(p.x), float(p.y)) in routePointsSet] # goes through each p in listOfPoints  and checks if that x,y coord is in the route set so no extra possible points
    
    # actual scaling
    scaledCoords = [scale((float(p.x), float(p.y))) for p in plotPoints]
    scaledRoute = [scale(p) for p in routePoints]
    
    # draw scaled points (green)
    for x, y in scaledCoords:
        draw.ellipse((x-5, y-5, x+5, y+5), fill = "green")
        
    # black connecting line
    if scaledRoute[0] != scaledRoute[-1]:
        scaledRoute.append(scaledRoute[0])
    draw.line(scaledRoute, fill = "black", width = 2)
    
    # red dot starting/landing coord
    sx, sy = scaledRoute[0]
    draw.ellipse((sx-5, sy-5, sx+5, sy+5), fill = "red")
    
    # setting up file name
    baseName = os.path.splitext(os.path.basename(input_filename))[0]
    D = int(round(sumOfDistance))
    fileSaveName = f"{baseName}_SOLUTION_{D}.png"

    # --- find Desktop path ---
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    oneDrive = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
    if os.path.isdir(oneDrive):
        desktop = oneDrive

    os.makedirs(desktop, exist_ok=True)
    full_path = os.path.join(desktop, fileSaveName)

    # --- save the image ---
    img.save(full_path)
    print(f"Image saved to: {full_path}")
    return full_path