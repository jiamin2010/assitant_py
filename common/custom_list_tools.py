"""
    针对列表的自定义工具
"""
class ListHelper:

    @staticmethod
    def find_all(target,func_condition):
        """
            查找列表中满足条件的所有元素
        :param target: 列表
        :param func_condition: 条件
            函数／方法类型
            －－　参数：列表中的元素
            －－　返回值：是否满足条件bool值
        :return:
        """
        for item in target:
            if func_condition(item):
                yield item

    @staticmethod
    def first(target,func_condition):
        """
            查找列表中满足条件的第一个元素
        :param target:
        :param func_condition:
        :return:
        """
        for item in target:
            if func_condition(item):
                return item

    @staticmethod
    def select(target,func_condition):
        """
            筛选列表中指定条件的数据
        :param target:
        :param func_condition:
        :return:
        """
        for item in target:
            # yield xxx(item)
            yield func_condition(item)

    @staticmethod
    def sum(target,func_condition):
        """
            计算列表中指定条件的所有元素和
        :param target:
        :param func_condition:
        :return:
        """
        sum_value = 0
        for item in target:
            # sum_value += xxx(item)
            sum_value += func_condition(item)
        return sum_value

    @staticmethod
    def totall(target,func_conditon):
        '''

        :param target:
        :param func_conditon:
        :return:
        '''
        count = 0
        for item in target:
            if func_conditon(item):
                count += 1
        return count
    @staticmethod
    def is_in(target,func_conditon):
        '''
            判断符合条件的是否在列表中
        :param target:
        :param func_conditon:
        :return:
        '''
        target_ls = []
        for item in target:
            target_ls.append(item.hp)
            if func_conditon in target_ls:
                return True
        return False

    @staticmethod
    def delete_all(target, func_conditon):
        '''
            删除满足条件的元素
        :param target:
        :param func_conditon:
        :return:
        '''
        del_count = 0
        for i in range(len(target) - 1, -1, -1):
            if func_conditon(target[i]):
                del target[i]  # 列表是可变无需返回列表
                del_count += 1
        return del_count
    @staticmethod
    def get_max(target,func_condition):
        '''
            获取指定条件最大值
        :param target:
        :param func_conditon:
        :return:
        '''
        max_value = target[0]
        for i in range(len(target)):
            if func_condition(max_value) <func_condition(target[i]):
                max_value = target[i]
        return max_value

    @staticmethod
    def order_by(target,func_condition):
        for r in range(len(target)-1):
            for c in range(r+1,len(target)):
                if func_condition(target[r]) > func_condition(target[c]):
                    target[r],target[c] = target[c],target[r]
        return target


