


class Solution(object):
    def generate(self, numRows):

        output = []
        for i in range(numRows):

            if(i == 0):

                prev = [1]
                output.append(prev)
                print(output)
            else:
                curr = [1]
                # print(output)
                j = 1

                while(j < i):

                    curr.append(prev[j-1] + prev[j])
                    print(curr)
                    j+=1

                # print(curr)
                curr.append(1)

                output.append(curr)

                prev = curr
        return output      


if __name__== '__main__':

    numRows = 5




    s = Solution()
    print(s.generate(numRows))

t = False

a=[1]
b=[]
j = 1
k=1
result=[1]
output=[]
	
# print(output)


if t :



	for i in range(3):

		if j == 2:

			a.append(k)
			print(output)
			k +=1
			j = 1
		
		output.append(a)
		a=[1]
		print(output)
		j = 2
	print(output)