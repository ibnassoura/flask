import models
import stores



member1=models.Member("Ibrahim",25)
member2=models.Member("Ali",33)

member=stores.MemberStore()

member.add(member1)
member.add(member2)


post1=models.Posts("First Post","This is the first post for testing! ")
post2=models.Posts("Second Post","This is the second post for testing! ")
post3=models.Posts("Third Post","This is the third post for testing! ")

post=stores.MemberPosts()
post.add(post1)
post.add(post2)
post.add(post3)

member.get_all()
post.get_all()
