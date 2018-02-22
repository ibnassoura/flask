class MemberStore():
    members=[]

    def add(self,member):
        self.members.append([member.name,member.age])

    def get_all(self):
        for each in self.members:
            print "Member Name: " + str(each[0])
            print "Age: " + str(each[1])

class MemberPosts:
    posts=[]

    def add(self,post):
        self.posts.append([post.title,post.content])

    def get_all(self):
        for each in MemberPosts.posts:
            print "Post Title: " +str(each[0])
            print "Post Content: "+ str(each[1])
