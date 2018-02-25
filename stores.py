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
        all_members=MemberStore.get_all()
        for each in all_members:
            if each.id==id:
                return each
            else:
                return None
    def entity_exists(self,member):
        if member is MemberStore.get_by_id(member):
            return False
        else:
            return True

    def delete(self,id):
        did=MemberStore.get_by_id(id)
        if MemberStore.entity.exists(id):
            MemberStore.members.remove(did)
            return MemberStore.members
        else:
            return MemberStore.members

class MemberPosts:
    posts=[]

    def add(self,post):
        MemberPosts.posts.append(post)

    def get_all(self):
        return MemberPosts.posts
