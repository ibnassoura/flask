import models
class MemberStore():
    members=[]

    def add(self,member,age):
        models.Member(member,age)

    def get_all(self):
        for each in MemberStore.members:
            print "Member Name: " + str(each[0])
            print "Age: " + str(each[1])

class MemberPosts:
    posts=[]

    def add(self,title,content):
        models.Posts(title,content)

    def get_all(self):
        for each in MemberPosts.posts:
            print "Post Title: " +str(each[0])
            print "Post Content: "+ str(each[1])

