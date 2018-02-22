import stores
class Member:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        stores.MemberStore.members.append([name,age])



class Posts():
    def __init__(self,title,content):
        self.title=title
        self.content=content
        stores.MemberPosts.posts.append([title,content])
        
