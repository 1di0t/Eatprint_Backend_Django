from django.db import models

class Users(models.Model):
    user_num = models.AutoField(primary_key=True)  # Primary key
    user_id = models.CharField(max_length=100, unique=True)
    user_pw = models.CharField(max_length=255)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id

class Profile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=100)
    profile_image = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nick_name

class Friends(models.Model):
    user = models.ForeignKey(Users, related_name='friends', on_delete=models.CASCADE)
    friend_user = models.ForeignKey(Users, related_name='friend_of', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'friend_user')

    def __str__(self):
        return f"{self.user.user_id} is friends with {self.friend_user.user_id}"
    
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)  # Primary key
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post {self.post_id} by {self.user.user_id}"

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    url = models.CharField(max_length=255)

    def __str__(self):
        return f"Image for Post {self.post.post_id}"

class Hashtag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag_name

class PostHashtag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'hashtag')

    def __str__(self):
        return f"{self.hashtag.tag_name} in Post {self.post.post_id}"

class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment {self.comment_id} by {self.user.user_id}"