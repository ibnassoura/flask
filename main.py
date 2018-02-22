import models

member1=models.Member("Ibrahim",25)
member2=models.Member("Ali",33)

post1=models.Posts("First Post","This is the first post for testing! ")
post2=post1=models.Posts("Second Post","This is the second post for testing! ")
post3=models.Posts("Third Post","This is the third post for testing! ")

print member1.name
print member1.age
print post1.title
print post3.content
