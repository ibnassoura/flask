import models
import stores




memberlist=[["Ibrahim",25],["Ali",33],["Mohammed",41]]
for each in memberlist:
    membertoadd=models.Member(each[0],each[1])
    membertostore=stores.MemberStore()
    membertostore.add(membertoadd)



post1=models.Posts("First Post","This is the first post for testing! ")
post2=models.Posts("Second Post","This is the second post for testing! ")
post3=models.Posts("Third Post","This is the third post for testing! ")

post=stores.MemberPosts()
post.add(post1)
post.add(post2)
post.add(post3)

membertostore.get_all()
post.get_all()
