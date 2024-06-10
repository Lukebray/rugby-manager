import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
from ball import Ball

class Pitch:
    def __init__(self, length=100, width=70, ball_positions=[]):
        self.length = length
        self.width = width
        self.ball_positions = ball_positions
        self.ball = Ball(50, 35)
        self.current_position_index = 0

    def draw_pitch(self):
        fig, ax = plt.subplots(figsize=(12, 7))

        # Green background for the pitch
        ax.add_patch(patches.Rectangle((0, 0), self.length, self.width, edgecolor='white', facecolor='green'))

        # Pitch Outline
        plt.plot([0, 0, self.length, self.length, 0], [0, self.width, self.width, 0, 0], color='black')

        # Halfway Line
        plt.plot([self.length / 2, self.length / 2], [0, self.width], color='white')

        ax.set_facecolor('green')
        ax.set_xlim(0, self.length)
        ax.set_ylim(0, self.width)
        ax.set_aspect('equal')
        ax.axis('off')
        return fig, ax

    def animate_ball(self, ball):
        fig, ax = self.draw_pitch()
        ball_plot, = ax.plot([ball.position[0]], [ball.position[1]], 'o', color='orange', markersize=10)
        ball_text = ax.text(5, self.width + 5, '', color='black')

        def init():
            ball_plot.set_data([ball.position[0]], [ball.position[1]])
            return ball_plot, ball_text
    
        def update(frame):
            if self.current_position_index < len(self.ball_positions):
                position = self.ball_positions[self.current_position_index]
                ball.position = position  # Update the ball's position
                ball_plot.set_data([ball.position[0]], [ball.position[1]])
                ball_text.set_text(f'Position index: ({self.current_position_index}) \n Position: ({ball.position[0]}, {ball.position[1]})')

                self.current_position_index += 1  # Move to the next position for the next frame
            return ball_plot, ball_text

        ani = animation.FuncAnimation(fig, update, frames=len(self.ball_positions), init_func=init, blit=False, interval=1000)
        plt.show()
