class MemberStore():
    members=[]
    last_id = 1

    def add(self,member):
            member.id = MemberStore.last_id
            MemberStore.members.append(member)
            MemberStore.last_id += 1


    def get_all(self):
        return MemberStore.members
            

    def get_by_id(self,id):
        all_members=self.get_all()
        result=None
        
        for each in all_members:
            if each.id==id:
                result=each
                break
        return result

    def get_by_name(self,name):
        all_members=self.get_all()
        result=[]
        for each in all_members:
            if each.name==name:
                result.append(each)
        return result
        
    def entity_exists(self,member):
        result = True
        if self.get_by_id(member.id) is None:
            result=False
        return result

    def delete(self,id):
        did=self.get_by_id(id)
        MemberStore.members.remove(did)

    def update(self,member):
        users=self.get_all()
        for index, each in enumerate(users):
            if member.id==each.id:
                users[index]=member
                break
            
    def get_members_with_posts(self,all_posts):
        allmembers=self.get_all()

        for member in allmembers:
            for post in all_posts:
                if member.id==post.member_id:
                    member.posts.append(post)
        return self.get_all()
            

    def get_top_two(self,members):

        newlist=sorted(self.get_members_with_posts(members),key=lambda x: len(x.posts),reverse=True)
        return newlist[:2]
        


class PostStore:
    posts=[]
    last_id=1

    def add(self,post):
        post.id=PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id+=1

    def get_all(self):
        return PostStore.posts


        
