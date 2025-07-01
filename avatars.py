import tkinter as tk
from PIL import Image, ImageTk


# Function to change avatar based on carbon emissions
def update_avatar(emission_level):
    if emission_level < 50:
        # Show happy avatar
        avatar_image = Image.open(r"C:\Users\Gunjan\Downloads\happy.png")
    elif emission_level < 150:
        # Show neutral avatar
        avatar_image = Image.open(r"C:\Users\Gunjan\Downloads\neutral.png")
    else:
        # Show sad avatar
        avatar_image = Image.open(r"C:\Users\Gunjan\Downloads\sad.png")

    # Resize the image to fit the tkinter canvas using LANCZOS resampling
    avatar_image = avatar_image.resize((200, 200), Image.Resampling.LANCZOS)
    avatar_photo = ImageTk.PhotoImage(avatar_image)

    # Update the image on the canvas
    canvas.itemconfig(avatar_on_canvas, image=avatar_photo)
    canvas.image = (
        avatar_photo  # Keep a reference to the image to avoid garbage collection
    )


# Function to simulate carbon emissions (for demonstration purposes)
def simulate_emissions():
    # Example: Carbon emission levels that change over time (you can customize this)
    emission_level = int(entry_emission.get())
    update_avatar(emission_level)


# Initialize the main window
root = tk.Tk()
root.title("Shinchan Avatar Based on Carbon Emissions")

# Create a canvas to display the avatar
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Load the initial image (happy avatar as default)
avatar_image = Image.open(r"C:\Users\Gunjan\Downloads\happy.png")
avatar_image = avatar_image.resize((200, 200), Image.Resampling.LANCZOS)
avatar_photo = ImageTk.PhotoImage(avatar_image)

# Add the image to the canvas
avatar_on_canvas = canvas.create_image(150, 150, image=avatar_photo)
canvas.image = avatar_photo  # Keep a reference to avoid garbage collection

# Create an entry field to simulate carbon emissions level
entry_emission = tk.Entry(root)
entry_emission.pack(pady=10)
entry_emission.insert(tk.END, "0")  # Default to 0 emission

# Create a button to update the avatar based on emission level
button_update = tk.Button(root, text="Update Avatar", command=simulate_emissions)
button_update.pack()

# Start the GUI
root.mainloop()
