class Member:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        MemberStore.members.append([name,age])



class Posts():
    def __init__(self,title,content):
        self.title=title
        self.content=content
        MemberPosts.posts.append([title,content])
        
class MemberStore():
    members=[]

    def add(self,member,age):
        Member(member,age)

    def get_all(self):
        for each in MemberStore.members:
            print str(each)

class MemberPosts:
    posts=[]

    def add(self,title,content):
        Posts(title,content)

    def get_all(self):
        for each in MemberPosts.posts:
            print str(each)
