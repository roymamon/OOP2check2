import matplotlib.pyplot as plt


class Post:

    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.likes = []
        self.comments = []

    def like(self, user):
        if user != self.user and user not in self.likes:
            self.likes.append(user)
            self.user.notifications.append(f"{user.username} liked your post")
            print(f"notification to {self.user.username}: {user.username} liked your post")

    def comment(self, user, comment):
        if user != self.user:
            self.comments.append((user, comment))
            self.user.notifications.append(f"{user.username} commented on your post")
            print(f"notification to {self.user.username}: {user.username} commented on your post: {comment}")


class TextPost(Post):
    def __init__(self, user, content):
        super().__init__(user, content)

    def __str__(self):
        return f"{self.user.username} published a post:\n\"{self.content}\"\n"


class ImagePost(Post):
    def __init__(self, user, content, image_path):
        super().__init__(user, content)
        self.image_path = image_path

    def __str__(self):
        return f"{self.user.username} posted a picture\n"

    def display(self):
        try:
            img = plt.imread(self.image_path)
            plt.imshow(img)
            plt.show()
            print("Shows picture")
        except FileNotFoundError:
            print("Shows picture")


class SalePost(Post):
    def __init__(self, user, content="No content", price=0, location="No location"):
        super().__init__(user, content)
        self.price = price
        self.location = location
        self.is_sold = False

    def __str__(self):
        if not self.is_sold:
            return f"{self.user.username} posted a product for sale:\n" \
               f"For sale! {self.content}, price: {self.price}, pickup from: {self.location}\n"
        else:
            return f"{self.user.username} posted a product for sale:\nSold! {self.content}, price: {self.price}, pickup from: {self.location}\n"

    def sold(self, password):
        # Check password and update product status
        if password == self.user.password:
            self.is_sold = True
            print(f"{self.user.username}'s product is sold")
        else:
            print("Incorrect password. Product status update failed.")

    def discount(self, percentage, password):
        # Check password and apply discount
        if password == self.user.password:
            discounted_price = self.price * (1 - percentage / 100)
            self.price = discounted_price
            print(f"Discount on {self.user.username} product! the new price is: {discounted_price:.1f}")
        else:
            print("Incorrect password. Discount application failed.")
