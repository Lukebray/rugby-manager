import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

class Pitch:
    def __init__(self, length=100, width=70):
        self.length = length
        self.width = width
        self.fig, self.ax = plt.subplots(figsize=(12, 7))
        self.ball_artist, = self.ax.plot([], [], 'o', color='orange', markersize=10)

    def draw_pitch(self):
        # Clear previous drawings
        self.ax.clear()
        
        # Green background for the pitch
        self.ax.add_patch(patches.Rectangle((0, 0), self.length, self.width, edgecolor='white', facecolor='green'))

        # Pitch Outline
        self.ax.plot([0, 0, self.length, self.length, 0], [0, self.width, self.width, 0, 0], color='white')

        # Goal Lines
        self.ax.plot([0, 0], [0, self.width], color='white')
        self.ax.plot([self.length, self.length], [0, self.width], color='white')

        # Halfway Line
        self.ax.plot([self.length / 2, self.length / 2], [0, self.width], color='white', linestyle='--')

        # Goal Areas
        self.ax.add_patch(patches.Rectangle((0, 0), 5, self.width, edgecolor='white', facecolor='green'))
        self.ax.add_patch(patches.Rectangle((self.length-5, 0), 5, self.width, edgecolor='white', facecolor='green'))

        self.ax.set_xlim(0, self.length)
        self.ax.set_ylim(0, self.width)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        return self.fig, self.ax

    def init_animation(self):
        self.ball_artist.set_data([], [])
        return self.ball_artist,

    def update_animation(self, frame, match):
        ball = match.ball
        positions = match.ball_positions
        # Update ball position from predefined positions
        if frame < len(positions):
            new_x, new_y = positions[frame]
            ball.update_position(new_x, new_y)

        self.ball_artist.set_data(ball.position[0], ball.position[1])
        return self.ball_artist,

    def animate(self, match, interval=1000):
        self.draw_pitch()
        ani = FuncAnimation(self.fig, self.update_animation, fargs=(match,), init_func=self.init_animation, blit=True, interval=interval)
        plt.show()
