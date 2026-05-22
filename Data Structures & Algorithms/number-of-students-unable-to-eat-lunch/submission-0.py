class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [students.count(0), students.count(1)]

        for i in sandwiches:
            if count[i] > 0:
                count[i] -= 1
            else:
                break
        
        return sum(count)