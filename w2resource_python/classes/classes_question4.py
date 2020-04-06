# 4. Write a Python class to get all possible unique subsets from a set of
#    distinct integers.

# ______________________________________________________________________
# my solution:
class MyClass():
    def my_solution(self, iter):

        my_list = [[]]

        def innerfunction(inner_iter):
            for i in inner_iter:
                current = inner_iter[:]        
                indexPop = current.index(i)
                current.pop(indexPop)        
                current.sort()
                if current not in my_list:
                    my_list.append(current)                
                    innerfunction(current)  

        innerfunction(iter)

        my_list.append(iter)
        my_list.sort()

        return my_list
# ______________________________________________________________________
# web solution:
class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(py_solution().sub_sets([4,5,6,7,8]))


# ______________________________________________________________________

if __name__ == '__main__':
    
    from pprint import pprint

    a = [1,2,3,4,5]
    pprint(MyClass().my_solution(a))

    pprint(py_solution().sub_sets([4,5,6,7,8]))