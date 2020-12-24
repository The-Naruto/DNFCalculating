from math import *
from PublicReference.base import *


class 重霄·弹药专家·男主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1
    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return round((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率,2)
    
    def 等效CD(self, 武器类型,输出类型):
        return round(self.CD  / self.恢复, 1)

class 重霄·弹药专家·男技能0(被动技能):
    名称 = '弹夹改装'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['交叉射击','聚合弹','凝固汽油弹','轻火力速射']
    关联技能2 = ['爆裂弹']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + (10 + self.等级) / 100, 3)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + (2 * self.等级) / 100, 3)

class 重霄·弹药专家·男技能1(被动技能):
    名称 = '兵器研究'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    冷却关联技能 = ['交叉射击','M18阔剑地雷','C4飞弹','G18冰冻手雷','G35感电手雷','G61重力地雷','G38ARG智能手雷','爆裂弹','聚合弹','重火力支援','镭射狙击','凝固汽油弹','轻火力速射']

    def 加成倍率(self,武器类型):
        return (1.1 + (self.等级 - 10) * 0.02) if self.等级 >= 10 else (1 + self.等级 * 0.01)

    def 物理攻击力倍率(self,武器类型):
        return (1.1 + (self.等级 - 10) * 0.02) if self.等级 >= 10 else (1 + self.等级 * 0.01)

    def 魔法攻击力倍率(self,武器类型):
        return (1.1 + (self.等级 - 10) * 0.02) if self.等级 >= 10 else (1 + self.等级 * 0.01)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 - 0.01 * self.等级, 3)

class 重霄·弹药专家·男技能2(被动技能):
    名称 = '手雷精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['G35感电手雷','G18冰冻手雷']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.1 * self.等级, 3)


class 重霄·弹药专家·男技能3(重霄·弹药专家·男主动技能):
    名称 = 'M18阔剑地雷'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 641.63
    成长 = 72.4
    攻击次数 = 3
    CD = 6.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 重霄·弹药专家·男技能4(重霄·弹药专家·男主动技能):
    名称 = 'G35感电手雷'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 485.91
    成长 = 54.8415
    CD = 3.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    脱手 = 0
    技能施放时间 = 0
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if (self.等级 < 18):
            return 1.0
        else:
            return round(1 + 0.01 * (self.等级-18), 3)

class 重霄·弹药专家·男技能5(重霄·弹药专家·男主动技能):
    名称 = '交叉射击'
    脱手 = 0
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 1171.97 * 1.26
    成长 = 132.3226 * 1.26
    攻击次数 = 3
    技能施放时间 = 0.3
    CD = 10.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 重霄·弹药专家·男技能6(重霄·弹药专家·男主动技能):
    名称 = '爆裂弹'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    基础 = 622.125
    成长 = 105.525
    CD = 5.0

class 重霄·弹药专家·男技能7(重霄·弹药专家·男主动技能):
    名称 = 'G18冰冻手雷'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 588.8 * 1.084
    成长 = 63.2 * 1.084
    CD = 4.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 重霄·弹药专家·男技能8(重霄·弹药专家·男主动技能):
    名称 = '聚合弹'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 8206.58
    成长 = 926.53341
    CD = 18.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

class 重霄·弹药专家·男技能9(重霄·弹药专家·男主动技能):
    名称 = 'C4飞弹'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 7122.49875
    成长 = 804.25125
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 1.23
            self.成长 *= 1.23
            # self.倍率 *= 1.18
        elif x == 1:
            self.基础 *= 1.32
            self.成长 *= 1.32

class 重霄·弹药专家·男技能10(重霄·弹药专家·男主动技能):
    名称 = '凝固汽油弹'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 8871.9827
    成长 = 1001.6475
    基础2 = 45.97 * 1.131
    成长2 = 5.03 * 1.131
    攻击次数2 = 15
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 1.31
            self.成长 *= 1.31
            # self.倍率 *= 1.18
            self.攻击次数2 = 0
            self.CD *=0.94
        elif x == 1:
            self.基础 *= 1.40
            self.成长 *= 1.40
            self.攻击次数2 = 0
            self.CD *=0.94


class 重霄·弹药专家·男技能11(重霄·弹药专家·男主动技能):
    名称 = '镭射狙击'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 3018.806
    成长 = 341.178
    攻击次数 = 5
    CD = 45.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 1.28
            self.成长 *= 1.28
            # self.倍率 *= 1.18
        elif x == 1:
            self.基础 *= 1.36
            self.成长 *= 1.36


class 重霄·弹药专家·男技能12(被动技能):
    名称 = '弹药主宰'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    关联技能 = ['所有']
    关联技能2 = ['爆裂弹']

    def 加成倍率(self, 武器类型):
        return 1.105 + self.等级 * 0.015 if self.等级 > 0 else 1

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.3


class 重霄·弹药专家·男技能13(重霄·弹药专家·男主动技能):
    名称 = '黑玫瑰特种战队'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 1373.97702
    成长 = 415.33411
    攻击次数 = 16
    基础2 = 242.389
    成长2 = 73.91189
    攻击次数2 = 90
    CD = 145.0

class 重霄·弹药专家·男技能14(重霄·弹药专家·男主动技能):
    名称 = 'G61重力地雷'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 5003.05 * 1.126
    成长 = 564.95 * 1.126
    基础2 = 167.19 * 1.126
    成长2 = 18.81 * 1.126
    攻击次数 = 1
    攻击次数2 = 30
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 1.83
            self.成长 *= 1.83
            self.技能施放时间 = 1.5
            self.攻击次数2 = 15
            # self.倍率 *= 1.18
        elif x == 1:
            self.基础 *= 2.01
            self.成长 *= 2.01
            self.技能施放时间 = 1.5
            self.攻击次数2 = 15

class 重霄·弹药专家·男技能15(重霄·弹药专家·男主动技能):
    名称 = '轻火力速射'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 1102.5975
    成长 = 124.5825
    攻击次数 = 17
    CD = 30.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x): 
        if x == 0:
            self.基础2 = self.基础*0.22
            self.成长2 = self.成长*0.22
            self.技能施放时间2 = 2
            self.攻击次数2 = 17
            self.CD *=0.95
            # self.倍率 *= 1.18
        elif x == 1:
            self.基础2 = self.基础*0.36
            self.成长2 = self.成长*0.36
            self.技能施放时间2 = 2
            self.攻击次数2 = 17
            self.CD *=0.95

class 重霄·弹药专家·男技能16(被动技能):
    名称 = '战地功勋'
    所在等级 = 75
    等级上限 = 30
    基础等级 = 11
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 3)

class 重霄·弹药专家·男技能17(重霄·弹药专家·男主动技能):
    名称 = '重火力支援'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 4125.33*1.126
    成长 = 465.67*1.126
    攻击次数 = 10
    CD = 45.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    
    def 装备护石(self):
        self.基础 *= 1.35
        self.成长 *= 1.35



class 重霄·弹药专家·男技能18(重霄·弹药专家·男主动技能):
    名称 = 'G38ARG智能手雷'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 13127.83*1.127
    成长 = 1482.17*1.127
    攻击次数 = 1
    基础2 = 3063.17*1.127
    成长2 = 345.83*1.127
    攻击次数2 = 10
    CD = 40.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    
    def 装备护石(self):
        self.基础 *= 4.22
        self.成长 *= 4.22
        self.攻击次数2 = 0

class 重霄·弹药专家·男技能19(重霄·弹药专家·男主动技能):
    名称 = '超新星核爆'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 48138.5*1.139
    成长 = 14532.5*1.139
    攻击次数 = 1
    基础2 = 1374.75*1.139
    成长2 = 415.25*1.139
    攻击次数2 = 15
    脱手 = 0
    技能施放时间 = 1
    CD = 180.0

class 重霄·弹药专家·男技能20(被动技能):
    名称 = '赤诚之心'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 重霄·弹药专家·男技能21(重霄·弹药专家·男主动技能):
    名称 = '皇鹰特战队'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 113194.2
    成长 = 12179.8
    CD = 60.0
    脱手 = 0
    技能施放时间 = 0.2



class 重霄·弹药专家·男技能22(重霄·弹药专家·男主动技能):
    名称 = '赤魂风暴狙击'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 2695.0
    成长 = 814.0
    攻击次数 = 12
    基础2 = 113232.0
    成长2 = 34183.0
    攻击次数2 = 1
    基础3 = 40440.0
    成长3 = 12208.0
    攻击次数3 = 4
    基础4 = 2155.0
    成长4 =652.0
    攻击次数4 = 3
    基础5 = 9705.0
    成长5 = 2930.0
    攻击次数5 = 1
    CD = 290.0
    脱手 = 0
    技能施放时间 = 6.3
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0
    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return round((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)+ self.攻击次数4 * (
                        self.基础4 + self.成长4 * self.等级)+ self.攻击次数5 * (
                        self.基础5 + self.成长5 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率,2)

重霄·弹药专家·男技能列表 = []
i = 0
while i >= 0:
    try:
        exec('重霄·弹药专家·男技能列表.append(重霄·弹药专家·男技能'+str(i)+'())')
        i += 1
    except:
        i = -1

重霄·弹药专家·男技能序号 = dict()
for i in range(len(重霄·弹药专家·男技能列表)):
    重霄·弹药专家·男技能序号[重霄·弹药专家·男技能列表[i].名称] = i

重霄·弹药专家·男一觉序号 = 0
重霄·弹药专家·男二觉序号 = 0
重霄·弹药专家·男三觉序号 = 0
for i in 重霄·弹药专家·男技能列表:
    if i.所在等级 == 50:
        重霄·弹药专家·男一觉序号 = 重霄·弹药专家·男技能序号[i.名称]
    if i.所在等级 == 85:
        重霄·弹药专家·男二觉序号 = 重霄·弹药专家·男技能序号[i.名称]
    if i.所在等级 == 100:
        重霄·弹药专家·男三觉序号 = 重霄·弹药专家·男技能序号[i.名称]

重霄·弹药专家·男护石选项 = ['无']
for i in 重霄·弹药专家·男技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        重霄·弹药专家·男护石选项.append(i.名称)

重霄·弹药专家·男符文选项 = ['无']
for i in 重霄·弹药专家·男技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1 and i.名称!='爆裂弹':
        重霄·弹药专家·男符文选项.append(i.名称)

class 重霄·弹药专家·男角色属性(角色属性):

    实际名称 = '重霄·弹药专家·男'
    角色 = '神枪手(男)'
    职业 = '弹药专家'

    武器选项 = ['手弩','步枪']
    
    类型选择 = ['魔法百分比','物理百分比']
    
    类型 = '魔法百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['智力','力量']

    主BUFF = 1.84

    远古记忆 = 0
  
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(重霄·弹药专家·男技能列表)
        self.技能序号= deepcopy(重霄·弹药专家·男技能序号)

    def 技能释放次数计算(self):
        技能释放次数 = []
        技能消耗时间 = 0.0
        爆裂弹间隔 = 0.115
        每轮射击次数 = 0.5 * (16 + floor(0.5 * (min(self.技能栏[self.技能序号['弹夹改装']].等级, 20)-10)))

        if (self.武器类型 != '手弩'):
            爆裂弹间隔 = 0.14
            每轮射击次数 = 0.5 * (9 + floor(0.5 * (min(self.技能栏[self.技能序号['弹夹改装']].等级, 20)-9)))

        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if i.名称 == '爆裂弹':
                    技能释放次数.append(0)
                else:
                    if self.次数输入[self.技能序号[i.名称]] == '/CD':
                        技能释放次数.append(int((self.时间输入) / (i.等效CD(self.武器类型,self.类型)+i.技能施放时间) + 1 + i.基础释放次数))
                        if i.脱手 ==1:
                            技能消耗时间 += int((self.时间输入) / (i.等效CD(self.武器类型,self.类型) + i.技能施放时间) + 1 + i.基础释放次数) * 0.2
                        else:
                            技能消耗时间 += int((self.时间输入) / (i.等效CD(self.武器类型,self.类型) + i.技能施放时间) + 1 + i.基础释放次数) *  i.技能施放时间
                    elif self.次数输入[self.技能序号[i.名称]] != '0':
                        技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]]))
                    else:
                        技能释放次数.append(0)
            else:
                技能释放次数.append(0)

        if self.次数输入[self.技能序号['爆裂弹']] == '/CD':
            技能释放次数[self.技能序号['爆裂弹']] =int(floor((self.时间输入-技能消耗时间)/爆裂弹间隔))
        else:
            if self.次数输入[self.技能序号['爆裂弹']] != '0':
                技能释放次数[self.技能序号['爆裂弹']] = int(self.次数输入[self.技能序号['爆裂弹']])*每轮射击次数
            else:
                技能释放次数[self.技能序号['爆裂弹']] = 0
        return 技能释放次数

    def 伤害指数计算(self):
        super().伤害指数计算()
        self.伤害指数 *= 1.1

class 重霄·弹药专家·男(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 重霄·弹药专家·男角色属性()
        self.角色属性A = 重霄·弹药专家·男角色属性()
        self.角色属性B = 重霄·弹药专家·男角色属性()
        self.一觉序号 = 重霄·弹药专家·男一觉序号
        self.二觉序号 = 重霄·弹药专家·男二觉序号
        self.三觉序号 = 重霄·弹药专家·男三觉序号
        self.护石选项 = deepcopy(重霄·弹药专家·男护石选项)
        self.符文选项 = deepcopy(重霄·弹药专家·男符文选项)

