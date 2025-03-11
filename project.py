import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def display_mobile_resources():
    # Assume you have a list of dictionaries with equipment details
    mobile_resources = [
        {'name': 'Crane', 'image_path': 'crane.png', 'utilization': 85, 'cost': 500, 'criticality': 'High'},
        {'name': 'Forklift', 'image_path': 'forklift.png', 'utilization': 75, 'cost': 300, 'criticality': 'Medium'},
        {'name': 'Boom Lift', 'image_path': 'boom_lift.png', 'utilization': 95, 'cost': 700, 'criticality': 'High'},
        {'name': 'Scissor Lift', 'image_path': 'scissor_lift.png', 'utilization': 80, 'cost': 400, 'criticality': 'Medium'},
        {'name': 'Excavator', 'image_path': 'excavator.png', 'utilization': 70, 'cost': 600, 'criticality': 'Medium'},
        {'name': 'Bulldozer', 'image_path': 'bulldozer.png', 'utilization': 100, 'cost': 800, 'criticality': 'High'},
        {'name': 'Tow Truck', 'image_path': 'tow_truck.png', 'utilization': 90, 'cost': 400, 'criticality': 'Medium'},
        {'name': 'Mobile Generator', 'image_path': 'mobile_generator.png', 'utilization': 85, 'cost': 300, 'criticality': 'Low'},
        {'name': 'Concrete Pump', 'image_path': 'concrete_pump.png', 'utilization': 60, 'cost': 900, 'criticality': 'Medium'},
        {'name': 'Mobile Medical Unit', 'image_path': 'mobile_medical_unit.png', 'utilization': 90, 'cost': 1000, 'criticality': 'High'}
    ]

    # Create a Tkinter window
    window = tk.Tk()
    window.title("Available Mobile Resources")
    window.state("zoomed")
    

    # Create a grid of 3x3
    for i in range(3):
        window.columnconfigure(i, weight=1, minsize=200)
        window.rowconfigure(i, weight=1, minsize=200)

    # Create a counter for equipment
    count = 0

    # Insert equipment data into the grid
    for resource in mobile_resources:
        name = resource['name']
        utilization = resource['utilization']
        cost = resource['cost']
        criticality = resource['criticality']
        image_path = resource['image_path']

        # Open and resize the image
        image = Image.open(image_path)
        image = image.resize((100, 100), Image.Resampling.LANCZOS)

        # Convert the image to Tkinter format
        photo = ImageTk.PhotoImage(image)

        # Create a frame for each equipment
        frame = ttk.Frame(window)
        frame.grid(row=count // 3, column=count % 3, padx=10, pady=10)

        # Create labels and image for each equipment
        label_name = ttk.Label(frame, text=name)
        label_name.pack()

        label_utilization = ttk.Label(frame, text=f"Utilization: {utilization}%")
        label_utilization.pack()

        if utilization < 50:
            label_status = ttk.Label(frame, text="Status: Underutilized")
        elif utilization >= 90:
            label_status = ttk.Label(frame, text="Status: Unavailable (Emergency)")
        else:
            label_status = ttk.Label(frame, text="Status: Utilized")
        label_status.pack()

        label_criticality = ttk.Label(frame, text=f"Criticality: {criticality}")
        label_criticality.pack()

        label_cost = ttk.Label(frame, text=f"Cost: ₹{cost:,}")
        label_cost.pack()

        label_image = ttk.Label(frame, image=photo)
        label_image.pack()

        label_image.image = photo

        count += 1

    # Start the Tkinter event loop
    window.mainloop()

display_mobile_resources()
