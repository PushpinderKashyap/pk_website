# import matplotlib.pyplot as plt

# def draw_step(ax, arr, step_info, step_num):
#     ax.set_xlim(-1, len(arr))
#     ax.set_ylim(-1.5, 2.5)
#     ax.axis('off')
    
#     left, mid, right, found = step_info['left'], step_info['mid'], step_info['right'], step_info['found']

#     for idx, val in enumerate(arr):
#         # Color logic: Highlight search range vs out-of-bounds
#         if idx < left or idx > right:
#             color, alpha = 'lightgray', 0.3
#         elif idx == mid:
#             color, alpha = ('#90EE90', 1.0) if found else ('#FFD700', 1.0)
#         else:
#             color, alpha = 'white', 1.0
            
#         rect = plt.Rectangle((idx-0.4, 0), 0.8, 1, facecolor=color, edgecolor='black', lw=2, alpha=alpha)
#         ax.add_patch(rect)
#         ax.text(idx, 0.5, str(val), ha='center', va='center', fontsize=14, fontweight='bold')
#         ax.text(idx, 1.2, str(idx), ha='center', alpha=0.5) # Index number

#     # Add the Arrows (Low, Mid, High)
#     ax.annotate('Left', xy=(left, 0), xytext=(left, -1.0), arrowprops=dict(arrowstyle='->', color='red'), ha='center', color='red')
#     ax.annotate('Right', xy=(right, 0), xytext=(right, -1.0), arrowprops=dict(arrowstyle='->', color='blue'), ha='center', color='blue')
#     ax.annotate('Mid', xy=(mid, 0), xytext=(mid, -1.0), arrowprops=dict(arrowstyle='->', color='orange'), ha='center', color='orange')
    
#     ax.set_title(f"Step {step_num}: Left: {left}, Right: {right}, Mid: {mid}", loc='left', fontsize=10)
# # --- Execution ---
# arr = [3,4,7,9,13,14,17,23,27,30,35,41]
# key = 35
# left =0 
# right =  len(arr) - 1

# # Setup the figure (max 5 rows for typical searches)
# fig, axes = plt.subplots(3, 1, figsize=(7,8))
# for a in axes: a.axis('off') # Hide all rows initially

# step_count = 0
# while left <= right:
#     mid = left + ((right-left)//2)
    
#     # Capture state and draw in the current row
#     current_step = {'left': left, 'mid': mid, 'right': right, 'found': (arr[mid] == key)}
#     draw_step(axes[step_count], arr, current_step, step_count + 1)
    
#     plt.pause(1.5) # THIS CREATES THE "ONE-BY-ONE" EFFECT
    
#     if (arr[mid] == key):       
#         break
#     elif arr[mid] < key:
#         left = mid + 1
#     else:
#         right = mid - 1
#     step_count += 1

# plt.show()


import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 2. Logic to capture each step
def get_steps(arr, val):
    left, right = 0, len(arr) - 1
    path = []
    while left <= right:
        mid = left + ((right-left)//2)
        path.append({'left': left, 'right': right, 'mid': mid, 'found': arr[mid] == val})
        if arr[mid] == val: break
        elif arr[mid] < val: left = mid + 1
        else: right = mid - 1
    return path

def generate_binary_search_gif(arr, key):

    steps = get_steps(arr, key)

    # 3. Create the Visuals
    fig, ax = plt.subplots(figsize=(8, 4))

    def update(frame):
        ax.clear()
        ax.set_xlim(-1, len(arr))
        ax.set_ylim(-2, 3)
        ax.axis('off')
        
        curr = steps[frame]
        
        # Draw the boxes (array)
        for i, num in enumerate(arr):
            color = 'white'
            if i == curr['mid']: color = "#D5942D" # Highlight Mid
            if curr['found'] and i == curr['mid']: color = '#90EE90' # Found Green
                
            # Draw box
            rect = plt.Rectangle((i-0.5, 0), 1, 1, facecolor=color, edgecolor='black', lw=2)
            ax.add_patch(rect)
            ax.text(i, 0.5, str(num), ha='center', va='center', fontsize=16, fontweight='bold')
            ax.text(i, 1.2, str(i), ha='center', alpha=0.5) # Index number

        # Draw the Pointers (matching your handwriting)
        # Low Pointer
        ax.annotate('Left', xy=(curr['left'], 0), xytext=(curr['left'], -0.8),
                    arrowprops=dict(arrowstyle='->', color='red', lw=2),
                    ha='center', color='red', fontsize=12, fontweight='bold')
        
        # High Pointer
        ax.annotate('Right', xy=(curr['right'], 0), xytext=(curr['right'], -1.5),
                    arrowprops=dict(arrowstyle='->', color='blue', lw=2),
                    ha='center', color='blue', fontsize=12, fontweight='bold')
        
        # Mid Pointer
        ax.annotate('Mid', xy=(curr['mid'], 1), xytext=(curr['mid'], 2),
                    arrowprops=dict(arrowstyle='->', color='orange', lw=2),
                    ha='center', color='orange', fontsize=12, fontweight='bold')

        ax.set_title(f"Binary Search: Finding {key} (Step {frame + 1})", fontsize=14)

    # 4. Run the animation
    ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=2000, repeat=True)

    # To save it for your blog as a GIF:
    ani.save('static/gifs/binary_search_animation.gif', writer='pillow')


# plt.show()
