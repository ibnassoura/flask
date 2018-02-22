import models

member=models.MemberStore()
member.add("Ibrahim",25)
member.add("Ali",33)


post=models.MemberPosts()
post.add("First Post","This is the first post for testing! ")
post.add("Second Post","This is the second post for testing! ")
post.add("Third Post","This is the third post for testing! ")

member.get_all()
post.get_all()
