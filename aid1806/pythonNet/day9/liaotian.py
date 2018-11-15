#liaotian.py
class SiChuanMaJiang(object):
    pattern = ('D', 'W', 'T')

    def __init__(self, pai):
        self.pt   = pai[1]
        self.num  = int(pai[0])
        self.view = pai
        self.id   = SiChuanMaJiang.pattern.index(self.pt)*10 + self.num

class InputParse(object):
    @classmethod
    def split_pai(cls, paimian): # 把字符串分开


        result = []
        for i in range(0, 28, 2):
            result.append(paimian[i:i+2])
        return result

class PaiAnaly(object):
    def __init__(self):
        self.total_num = 0
        self.patterns = []
        self.id_list  = []

    def next_one(self, pai_instance):
        if pai_instance.pt not in self.patterns:
            self.patterns.append(pai_instance.pt)
        self.id_list.append(pai_instance.id)
        self.total_num += 1

    @staticmethod
    def qi_pai(pai_instance_list): # 对整个手牌进行统计
        pai_mian = PaiAnaly()
        map(lambda x: pai_mian.next_one(x), pai_instance_list)
        return pai_mian

    @staticmethod
    def find_ok_three(sort_list):
        if sort_list[0] == sort_list[1] and \
            sort_list[1] == sort_list[2]:

                return sort_list[1], sort_list[2]
        idx1 = 0
        idx2 = 0
        for i in range(1, len(sort_list)): # 寻找sort_list[0]+1
            if sort_list[i] > sort_list[0] + 1:
                return False
            if sort_list[i] == sort_list[0] + 1:
                idx1 = i
                break
            if sort_list[i] == sort_list[0]:
                continue
        if idx1 == 0:
            return False

        for j in range(idx1+1, len(sort_list)): # 在找到sort_list[0]+1的情况下，寻找sort_list[0]+2
            if sort_list[j] > sort_list[idx1] + 1:
                return False
            if sort_list[j] == sort_list[idx1] + 1:
                idx2 = j
                break
            if sort_list[j] == sort_list[idx1]:
                continue
        if idx2 == 0:
            return False

        return sort_list[idx1], sort_list[idx2] # 若找到，就返回。

    @staticmethod
    def recur_check(lt): # 递归过程
        if len(lt) != 0: # 当列表为空，就认为可以胡牌
            re = PaiAnaly.find_ok_three(lt) 
            if not re:
                return False
            else: # 如果依然能够配对，就去除已经配对的牌，继续递归调用
                lt.remove(lt[0])
                lt.remove(re[0])
                lt.remove(re[1])
                # print (lt)
                return PaiAnaly.recur_check(lt) 
        else:
            return True

    def find_duizi(self): # 找出手牌中所有的对子，然后以每个对子作为头，调用以上的递归过程
        res = []
        for i in range(13):
            try:
                
                if self.id_list[i] == self.id_list[i+1] and\
                        self.id_list[i] != self.id_list[res[-1]]:
                    res.append(i)
            except IndexError:
                res.append(i)
        # print (res)
        return res


    def judge_hui(self):
        self.id_list.sort()
        if self.total_num != 14:
            return False
        if len(self.patterns) == 3:
            return False

        duizi_index = self.find_duizi()
        # print ('本来牌面: %s' % self.id_list)

        for idx in duizi_index:
            tl = copy.deepcopy(self.id_list)
            # print ('对子: %s%s' % (tl[idx], tl[idx+1]))
            val = tl[idx]
            tl.remove(val)
            tl.remove(val)
            # print ('去除对子以后的牌面: %s' % tl)
            r =  PaiAnaly.recur_check(tl)
            if not r:
                continue
            else:
                return True
                

if __name__ == '__main__':
    pai_string = input('牌面:')
    pai_list = InputParse.split_pai(pai_string)
    pai_instance_list = []
    for p in pai_list:
        a = SiChuanMaJiang(p)
        pai_instance_list.append(a.id)
    pai_instance_list.sort()
    pai_ready = PaiAnaly.qi_pai(pai_instance_list)
    r = pai_ready.judge_hui()

    if r:
        print ('胡了')
    else:
        print ('不能胡')

















