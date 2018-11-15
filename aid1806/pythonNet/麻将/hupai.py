#hupai3.py


class SiChuanMaJiang(object):
    pattern = ('D', 'W', 'T')

    def __init__(self, pai):
        self.pt   = pai[1]
        self.num  = int(pai[0])
        self.view = pai
        self.id   = SiChuanMaJiang.pattern\
        .index(self.pt)*10 + self.num



class InputParse(object):
    @classmethod
    def split_pai(cls, paimian): # 把字符串分开


        result = []
        if len(paimian) == 28:
            for i in range(0, 28, 2):
                result.append(paimian[i:i+2])
            return result
        elif len(paimian) == 22:
            for i in range(0, 22, 2):
                result.append(paimian[i:i+2])
            return result

        elif len(paimian) == 16:
            for i in range(0, 16, 2):
                result.append(paimian[i:i+2])
            return result

        elif len(paimian) == 10:
            for i in range(0, 10, 2):
                result.append(paimian[i:i+2])
            return result

        elif len(paimian) == 4:  #大对子
            if paimian[0:2] == paimian[2:4]:
                return True


class Paifenxi:
    def __init__(self,paimian):
        self.patterns = []
        self.total_num = len(paimian)
        self.id_list = paimian


    

    def find_duizi(self):
        if self.id_list[0] == self.id_list[1] and\
        self.id_list[2] == self.id_list[3] and \
        self.id_list[4] == self.id_list[5] and \
        self.id_list[6] == self.id_list[7] and \
        self.id_list[8] == self.id_list[9] and \
        self.id_list[10] == self.id_list[11] and \
        self.id_list[12] == self.id_list[13]: #暗七对
            
            return self.id_list

        if (self.id_list[0] == self.id_list[1] ==\
        self.id_list[2] == self.id_list[3] and \
        self.id_list[4] == self.id_list[5] and \
        self.id_list[6] == self.id_list[7] and \
        self.id_list[8] == self.id_list[9] and \
        self.id_list[10] == self.id_list[11] and \
        self.id_list[12] == self.id_list[13]) or\
        (self.id_list[0] == self.id_list[1] and\
        self.id_list[2] == self.id_list[3] == \
        self.id_list[4] == self.id_list[5] and \
        self.id_list[6] == self.id_list[7] and \
        self.id_list[8] == self.id_list[9] and \
        self.id_list[10] == self.id_list[11] and \
        self.id_list[12] == self.id_list[13]) or \
        (self.id_list[0] == self.id_list[1] and\
        self.id_list[2] == self.id_list[3] and \
        self.id_list[4] == self.id_list[5] == \
        self.id_list[6] == self.id_list[7] and \
        self.id_list[8] == self.id_list[9] and \
        self.id_list[10] == self.id_list[11] and \
        self.id_list[12] == self.id_list[13]) or \
        (self.id_list[0] == self.id_list[1] and\
        self.id_list[2] == self.id_list[3] and \
        self.id_list[4] == self.id_list[5] and \
        self.id_list[6] == self.id_list[7] == \
        self.id_list[8] == self.id_list[9] and \
        self.id_list[10] == self.id_list[11] and \
        self.id_list[12] == self.id_list[13]) or\
        (self.id_list[0] == self.id_list[1] and\
        self.id_list[2] == self.id_list[3] and \
        self.id_list[4] == self.id_list[5] and \
        self.id_list[6] == self.id_list[7] and \
        self.id_list[8] == self.id_list[9] == \
        self.id_list[10] == self.id_list[11] and \
        self.id_list[12] == self.id_list[13]) or\
        (self.id_list[0] == self.id_list[1] and\
        self.id_list[2] == self.id_list[3] and \
        self.id_list[4] == self.id_list[5] and \
        self.id_list[6] == self.id_list[7] and \
        self.id_list[8] == self.id_list[9] and \
        self.id_list[10] == self.id_list[11] == \
        self.id_list[12] == self.id_list[13]): #龙七对
            return self.id_list

        else:
            for i in self.id_list:
                if self.id_list.count(i) == 2:
                    self.id_list.remove(i)
                    self.id_list.remove(i)
            return self.id_list
        

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

        return sort_list[idx1], sort_list[idx2] 
    @staticmethod
    def pai_digui(lt):
        
        if len(lt) != 0: # 当列表为空，胡牌
            re = Paifenxi.find_ok_three(lt) 
            if not re:
                return False
            else: 
                lt.remove(lt[0])
                lt.remove(re[0])
                lt.remove(re[1])
                
                return Paifenxi.pai_digui(lt) 
        else:
            return True
    @staticmethod
    def judge_hui(paimian):
        pai_patterns = []
        total_num = len(paimian)
        
            
        for pai in pai_list:
            if pai[1] not in pai_patterns:
                pai_patterns.append(pai[1])
        
        return pai_patterns,total_num

if __name__ == '__main__':
    pai_string = input('牌面:')
    pai_list = InputParse.split_pai(pai_string)
    if pai_list == True:
        print('胡了大对子') 
    else:
        pai_instance_list = []
        for p in pai_list:
            a = SiChuanMaJiang(p)
            pai_instance_list.append(a.id)
        pai_instance_list.sort()
        b = Paifenxi(pai_instance_list)
        q = b.find_duizi()
        for i in q:
            if q.count(i) == 4:
                print('胡了龙七对')
                break
        
            elif q.count(i) == 2:
                print('胡了暗七对')
                break
        else:
            c,m = Paifenxi.judge_hui(pai_list)


            if (len(c) == 2 or len(c) == 1)and \
            ((m == 14) or (m == 11) or (m == 8) or (m == 5)):
                
                if len(c) == 1 and m == 14:
                    d = b.find_duizi()
                    
                    e = Paifenxi.pai_digui(d)
                    if e == True:
                        print('胡了清一色')

                else:
                    d = b.find_duizi()
                    
                    e = Paifenxi.pai_digui(d)
                    if e == True:
                        print('胡了屁胡')



        
    

