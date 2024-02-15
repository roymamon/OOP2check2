from Post import TextPost, SalePost, ImagePost


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = []
        self.following = []
        self.posts = []
        self.notifications = []
        self.isConnected = True

    def __str__(self):
        return f"User name: {self.username}, Number of posts: {len(self.posts)}, Number of followers: {len(self.followers)}"

    def follow(self, other_user):
        if other_user not in self.following and other_user != self:
            self.following.append(other_user)
            other_user.add_follower(self)
            print(f"{self.username} started following {other_user.username}")

    def unfollow(self, other_user):
        if other_user in self.following:
            self.following.remove(other_user)
            other_user.remove_follower(self)
            print(f"{self.username} unfollowed {other_user.username}")

    def add_follower(self, follower): # helper method
        self.followers.append(follower)

    def remove_follower(self, follower): # helper method
        if follower in self.followers:
            self.followers.remove(follower)

    def notify(self, notification):
        self.notifications.append(notification)

    def print_notifications(self):
        print(f"{self.username}'s notifications:")

        for notification in self.notifications:
            print(notification)

    def publish_post(self, post_type, *args):
        post = None
        if post_type == "Text":
            post = TextPost(self, *args)
        elif post_type == "Image":
            if len(args) == 1:
                # If only one argument is provided, assume it's the image path
                post = ImagePost(self, "No content", *args)
            else:
                # Otherwise, assume the first argument is the content and the second is the image path
                post = ImagePost(self, *args)
        elif post_type == "Sale":
            if len(args) >= 3:
                # If at least three arguments are provided, create the SalePost
                post = SalePost(self, *args)
            else:
                # If fewer than three arguments are provided, set default values for missing arguments
                post = SalePost(self, "No content", 0, "No location")
        else:
            print("Invalid post type.")
        if post:
            self.posts.append(post)
            print(post)
            for follower in self.followers:
                follower.notify(f"{self.username} has a new post")

        return post
