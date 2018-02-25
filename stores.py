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


class MemberPosts:
    posts=[]

    def add(self,post):
        MemberPosts.posts.append(post)

    def get_all(self):
        return MemberPosts.posts
