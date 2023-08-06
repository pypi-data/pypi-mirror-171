THIS MY FIRST PYTHON PACKAGE! DO WHAT YOU WANT ON INSTAGRAM!

HOW TO USE:
```python
from Darling_Instagram.Darling import DarlingInstagram

#START
IG = DarlingInstagram(cookie="YOUR INSTAGRAM COOKIE!")

# FOLLOW USER
follow = IG.FollowUser(user_url="https://www.instagram.com/quang722008/") #USER URL

# LIKE POST
like = IG.LikePost(user_url="https://www.instagram.com/p/CjnZsxqvyH0/") #POST URL

# COMMENT POST
comment = IG.comment_post(url_post="https://www.instagram.com/p/CjnZsxqvyH0/",content="Mquang Đẹp Trai!") #URL POST & COMMENT CONTENT

#UNFOLLOW USER
unfollow = IG.UnfollowUser(user_url="https://www.instagram.com/quang722008/") #USER URL

#CHANGE PROFILE PICTURE
change_profile_picture = IG.UploadProfilePicture(img_path="PATH PICTURE") #PATH PICTURE

#POST
post = IG.UploadPost(img_path="PATH PICTURE") #PATH PICTURE

```