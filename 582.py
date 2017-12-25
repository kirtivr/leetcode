class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        
        numPid = len(pid)
        child = {}
        
        for i in range(numPid):
            curr = pid[i]
            parent = ppid[i]

            if parent in child:
                child[parent].append(curr)
            else:
                child[parent] = [curr]


        queue = [kill]
        count = 0
        kills = [kill]
        
        while len(queue) > 0:
            el = queue.pop()
            count = count + 1

            queue.extend(child[el] if el in child else [])
            kills.extend(child[el] if el in child else [])
                        
        return kills
