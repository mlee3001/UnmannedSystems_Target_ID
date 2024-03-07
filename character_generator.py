import matplotlib.pyplot as plt
import random



'''

Uncomment line 56 to save the images as pngs

'''




 # Define a list of random colors
colors = ["red", "blue", "green", "purple", "black", "brown", "orange"]
characters = ['0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S','T','U','V','W','X','Y','Z']
SZ = 100

def draw_block_letters(i):
    ch = characters[i]
    rot = random.randint(0,359)
    fig, ax = plt.subplots(figsize=(5,5))
    ax.add_artist(ax.patch)
    ax.patch.set_zorder(-1)

    # Choose a random color from the list
    background_color = random.choice(colors)

    letter_color = "white"
    

    # Set the background color of the plot
    ax.set_facecolor(background_color)

    # Draw the letter A with rotation
    text_obj = ax.text(0.5, 0.5, ch, size=SZ, ha='center', va='center', weight='bold', rotation=rot, color= letter_color)
    
    
    # Set aspect ratio
    ax.set_aspect('equal')

    # Set axis limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Hide axes
    ax.axis('off')

    file_name = "figure"
    file_name += str(i)
    file_name += ".png"

    
    
    #fig.savefig(file_name, bbox_inches='tight', pad_inches = 0.0)
    # Show the plot
    plt.show()

    plt.waitforbuttonpress()

    plt.close()

# Call the function to draw the letters
for i in range(0,len(characters)):
    draw_block_letters(i)


