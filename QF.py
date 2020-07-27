class QuickFind:
    #initialize our lis id
    id=[]
    #the uf method return a list from 0 to N-1
    def uf(self,N):
        self.id=list(range(N))
        for i in range(0,N):
            self.id[i]=i
            
    #the connected method check if two points are connected
    def connected(self,p,q):
        return self.id[p]==self.id[q]
    
    #the ununion method merge two objects to be connected
    def union(self,p,q):
        p_id=self.id[p]
        q_id=self.id[q]
        for i in range(len(self.id)):
            if self.id[i]==p_id:
                self.id[i]=q_id
