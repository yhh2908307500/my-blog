class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = []
        plist = path.split('/')
        for pos in plist:
            if pos:
                if pos == '..':
                    try:
                        # 返回上一级
                        result.pop()
                    except:
                        # 已到顶层
                        result = []
                elif pos != '.':
                    result.append(pos)
        return '/'+'/'.join(result)