
import tkinter as tk
from tkinter import messagebox

# Encapsulation: Use of private variable to hide title and subscription status.
class Video:
    def __init__(self, title):
        self._title = title  # Encapsulation: Private attribute (single underscore)
        self._is_subscribed = False  # Encapsulated variable for subscription status

    def subscribe(self):
        self._is_subscribed = True

    def unsubscribe(self):
        self._is_subscribed = False

    def get_subscription_status(self):
        return self._is_subscribed

    def get_title(self):
        return self._title


# Multiple inheritance: GUI class inherits from tk.Tk (Tkinter main window) and Video class.
class VideoApp(tk.Tk, Video):
    def __init__(self, title):
        tk.Tk.__init__(self)  # Calling the constructor of tk.Tk
        Video.__init__(self, title)  # Calling the constructor of Video
        
        self.title("YouTube Subscription Interface")

        self.geometry("300x200")
        
        # Encapsulation: The video title is encapsulated and only accessible via get_title().
        self.label_title = tk.Label(self, text=self.get_title())


        self.label_title.pack(pady=10)
        
        # Button for subscribing and unsubscribing.
        self.button_subscribe = tk.Button(self, text="Subscribe", command=self.toggle_subscription)


        self.button_subscribe.pack(pady=5)

    # Method to toggle between subscribing and unsubscribing.
    def toggle_subscription(self):
        if not self.get_subscription_status():
            self.subscribe_video()
        else:
            self.unsubscribe_video()

    # Method overriding: Customizing what happens when the subscribe button is clicked.
    def subscribe_video(self):
        self.subscribe()  # Call the subscribe method from Video class
        self.update_subscription_status()

    # Method overriding: Customizing what happens when the unsubscribe button is clicked.
    def unsubscribe_video(self):
        self.unsubscribe()  # Call the unsubscribe method from Video class
        self.update_subscription_status()

    def update_subscription_status(self):
        # Update the button text based on the current subscription status.
        if self.get_subscription_status():
            self.button_subscribe.config(text="Unsubscribe")
            messagebox.showinfo("Subscription", "You have subscribed to this channel!")
        else:
            self.button_subscribe.config(text="Subscribe")
            messagebox.showinfo("Subscription", "You have unsubscribed from this channel.")


# Decorator example: A function decorator to check login status.
def login_required(func):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            return func(*args, **kwargs)
        else:
            messagebox.showwarning("Login required", "You need to login first!")
    return wrapper


# Multiple inheritance and decorators used together.
class User(VideoApp):
    def __init__(self, title, username):
        super().__init__(title)  # Calls the constructor of VideoApp
        self.username = username
        self.is_logged_in = False  # Encapsulation: Keeping track of login status.

        # Login button
        self.button_login = tk.Button(self, text="Login", command=self.login)
        self.button_login.pack(pady=5)

    # Decorator example applied to subscription actions.
    @login_required
    def subscribe_video(self):
        super().subscribe_video()

    @login_required
    def unsubscribe_video(self):
        super().unsubscribe_video()

    def login(self):
        self.is_logged_in = True
        messagebox.showinfo("Login", f"hello {self.username}!")


# Run the application
if __name__ == "__main__":
    app = User("Sample Video", "users")
    app.mainloop()
