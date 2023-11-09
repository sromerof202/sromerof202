import cv2

# img path.
image_path = r'C:\Users\User\Downloads\0.jpg'  

def process_image(image_path):
    """
    Process the image to create a sketch effect.
    """
    # Read the image from the specified path
    image = cv2.imread(image_path)

    if image is None:
        print("The image could not be loaded. Check the file path.")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to the grayscale image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Use Canny edge detection
    edges = cv2.Canny(blur, threshold1=39, threshold2=140)
    
    # Apply threshold to keep only the strongest edges
    ret, thresholded_edges = cv2.threshold(edges, 245, 255, cv2.THRESH_BINARY)
    
    # Invert the thresholded image to get a pencil sketch effect
    inverted_sketch = cv2.bitwise_not(thresholded_edges)
    
    # Display the sketch
    cv2.imshow('Sketch', inverted_sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save the sketch to a file
    cv2.imwrite('sketch_image.jpg', inverted_sketch)

# Call the function
process_image(image_path)