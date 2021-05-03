class Solution:
    def convert(self, s: str, numRows: int) -> str:
        counter = 0
        matrix = list()
        while (len(s) > 1):
            if counter % (numRows) == 0:
                if len(s) < numRows:
                    remains = numRows - len(s)
                    lis = remains * ['0']
                    rem = list(s)
                    rem.extend(lis)
                    matrix.append(rem)
                    s = ''
                else:
                    temp_str = s[0:numRows]
                    s = s[numRows:]
                    matrix.append(list(temp_str))
            elif counter % numRows == (numRows):
                pass
            elif counter % numRows == 1:
                pass
            else:
                sparsh_arr = ['0'] * numRows
                sparsh_arr[(numRows - counter) % (numRows)] = s[0]
                s = s[1:]
                matrix.append(sparsh_arr)
            counter += 1

        remains = numRows - len(s)
        if remains < numRows:
            lis = remains * ['0']
            rem = list(s)
            rem.extend(lis)
            matrix.append(rem)
        print(matrix)
        result = ''
        matrix = list(map(list, zip(*matrix)))
        matrix = sum(matrix, [])
        for i in matrix:
            if i != '0':
                result += str(i)
        return result

obj = Solution()
print(obj.convert("zftkhjgdapavigvtdbvdxrxsmemqbbwaipmpysuyjxvtdqnitimrzllopyeqbasjrgapaxpmukfzdskwdynejzubzztcbmntunkvkahgmmgphsomqdqzcladmwfpisieivbuxibjxjbgbrstuiszvvch",36))
