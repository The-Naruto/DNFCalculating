from PublicReference.base import *

class 毒神绝主动技能(主动技能):
    中毒基础 = 0
    中毒成长 = 0
    中毒倍率 = 1
    出血基础 = 0
    出血成长 = 0
    出血倍率 = 1
    灼伤基础 = 0
    灼伤成长 = 0
    灼伤倍率 = 1
    涂毒基础 = 0
    涂毒成长 = 0
    涂毒倍率 = 1

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级)
                 + self.中毒倍率 * (self.中毒基础 + self.中毒成长 * self.等级)
                 + self.出血倍率 * (self.出血基础 + self.出血成长 * self.等级) 
                 + self.灼伤倍率 * (self.灼伤基础 + self.灼伤成长 * self.等级) 
                 + self.涂毒倍率 * (self.涂毒基础 + self.涂毒成长 * self.等级))
                 * (1 + self.TP成长 * self.TP等级) * self.倍率)

class 毒神绝技能0(被动技能):
    名称 = '基础精通'
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['天罗地网']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.463 + 0.0889 * self.等级, 5)

class 毒神绝技能1(毒神绝主动技能):
    名称 = '抛沙'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 48
    基础 = 398.234042553192
    成长 = 54.7659574468085
    涂毒基础 = 39.531914893617
    涂毒成长 = 5.46808510638298
    CD = 3.0
    TP成长 = 0.08
    TP上限 = 7

class 毒神绝技能2(毒神绝主动技能):
    名称 = '擒月炎'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1382.2
    成长 = 142.8
    攻击次数 = 1.6 #异常倍率
    涂毒基础 = 137.755555555556
    涂毒成长 = 14.2444444444444
    CD = 5.5
    TP成长 = 0.10
    TP上限 = 7

class 毒神绝技能3(毒神绝主动技能):
    名称 = '毒影针'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 732.309523809524
    成长 = 82.6904761904762
    中毒基础 = 710.761904761905
    中毒成长 = 80.2380952380952
    出血基础 = 710.761904761905
    出血成长 = 80.2380952380952
    涂毒基础 = 214.666666666667
    涂毒成长 = 24.3333333333333
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7

class 毒神绝技能4(毒神绝主动技能):
    名称 = '双重投掷'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    是否有伤害 = 0
    关联技能 = ['无']


class 毒神绝技能5(被动技能):
    名称 = '爪精通'
    所在等级 = 25
    等级上限 = 30
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.01* self.等级, 5)
    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)
    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

class 毒神绝技能6(毒神绝主动技能):
    名称 = '砖袭'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 2094.3
    成长 = 236.7
    涂毒基础 = 207.3
    涂毒成长 = 23.7
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7

class 毒神绝技能7(毒神绝主动技能):
    名称 = '天罗地网'
    备注 = '(TP为基础精通)'
    所在等级 = 35
    等级上限 = 11
    基础等级 = 1
    基础 = 1257
    涂毒基础 = 127
    CD = 11
    TP成长 = 0.10
    TP上限 = 5

class 毒神绝技能8(毒神绝主动技能):
    名称 = '挑衅'
    所在等级 = 35
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.15 + 0.01* self.等级, 5)

class 毒神绝技能9(毒神绝主动技能):
    名称 = '伏虎霸王拳'
    备注 = '(不可抓取)'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 455.486486486486
    成长 = 51.5135135135135
    攻击次数 = 1.6 #异常倍率
    涂毒基础 = 44.8648648648649
    涂毒成长 = 5.13513513513514
    涂毒倍率 = 1.6 #异常倍率
    CD = 15.0
    TP上限 = 7
    TP成长 = 0.845
    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级)
                 + self.涂毒倍率 * (self.涂毒基础 + self.涂毒成长 * self.等级))
                 * (8.445 + self.TP成长 * self.TP等级) * self.倍率)

class 毒神绝技能10(被动技能):
    名称 = '狂霸王拳'
    所在等级 = 40
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['伏虎霸王拳']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.40 + 0.02* self.等级, 5)


class 毒神绝技能11(毒神绝主动技能):
    名称 = '裂地飞沙'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 6396
    成长 = 722
    攻击次数 = 1.2
    涂毒基础 = 638.4
    涂毒成长 = 73.6
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.27
        self.CD *= 1.00

class 毒神绝技能12(毒神绝主动技能):
    名称 = '毒雷引爆'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 1031.6875
    成长 = 116.3125
    中毒基础 = 254.25
    中毒成长 = 28.75
    涂毒基础 = 117.46875
    涂毒成长 = 13.53125
    CD = 24.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.07
        self.CD *= 0.90

class 毒神绝技能13(毒神绝主动技能):
    名称 = '街头风暴'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 8765.5
    成长 = 989.5
    中毒基础 = 1447.5
    中毒成长 = 163.5
    涂毒基础 = 866.3333333
    涂毒成长 = 98.66666667
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.227

class 毒神绝技能14(被动技能):
    名称 = '猛毒之血'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.035 + 0.015 * self.等级, 5)

class 毒神绝技能15(毒神绝主动技能):
    名称 = '死亡毒雾'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    CD = 145
    基础 = 3608.54545454545
    成长 = 1105.45454545455
    攻击次数 = 1
    中毒基础 = 487.454545454545
    中毒成长 = 147.545454545455
    中毒倍率 = 1
    涂毒基础 = 362.818181818182
    涂毒成长 = 110.181818181818
    涂毒倍率 = 1

    def 力智加成(self):
        return 91 + self.等级 * 6.5

    def 防御减少(self):
        return 946 + 186 * self.等级 + (self.等级 + 1) * self.等级 / 2 * 11

class 毒神绝技能16(毒神绝主动技能):
    名称 = '猛毒擒月炎'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    CD = 30.0
    基础 = 7793.72727272727
    成长 = 880.272727272727
    攻击次数 = 1.6  #异常加成
    中毒基础 = 1232.68181818182
    中毒成长 = 139.318181818182
    涂毒基础 = 901
    涂毒成长 = 102
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.06
        self.攻击次数 = 1.84  #异常加成
        self.CD *= 0.80

class 毒神绝技能17(毒神绝主动技能):
    名称 = '爆碎砖袭'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 15753.70588
    成长 = 1779.294118
    涂毒基础 = 1568.941176
    涂毒成长 = 178.0588235
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.119
        self.CD *= 1.00

class 毒神绝技能18(被动技能):
    名称 = '猛毒之伤'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.02 * self.等级, 5)

class 毒神绝技能19(毒神绝主动技能):
    名称 = '连环毒爆弹'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 39486.6066666667
    成长 = 4458.59333333333
    中毒基础 = 880.32
    中毒成长 = 99.68
    涂毒基础 = 4034.60666666667
    涂毒成长 = 455.893333333333
    CD = 40.0

class 毒神绝技能20(毒神绝主动技能):
    名称 = '毒龙轰天雷'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 37226.25
    成长 = 4205.75
    中毒基础 = 2343.33333333333
    中毒成长 = 266.666666666667
    涂毒基础 = 3948.66666666667
    涂毒成长 = 447.333333333333
    CD = 45.0

class 毒神绝技能21(毒神绝主动技能):
    名称 = '万毒噬心诀'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    CD = 60.0
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)
    #技攻倍率不包含蛇拳x3 x4

class 毒神绝技能22(毒神绝主动技能):
    名称 = '禁技：万毒蛇窟'
    所在等级 = 85
    等级上限 = 1
    基础等级 = 1
    基础 = 47664
    成长 = 14384
    涂毒基础 = 4780
    涂毒成长 = 1436
    CD = 180.0

class 毒神绝技能23(毒神绝主动技能):
    名称 = '万毒噬心诀x4'
    所在等级 = 85
    等级上限 = 1
    基础等级 = 1
    基础 = 7185
    成长 = 1257
    涂毒基础 = 715
    涂毒成长 = 126
    CD = 0.1

class 毒神绝技能24(毒神绝主动技能):
    名称 = '万毒噬心诀x3'
    所在等级 = 85
    等级上限 = 1
    基础等级 = 1
    基础 = 5031.5
    成长 = 897.5
    涂毒基础 = 500
    涂毒成长 = 90
    CD = 0.1

class 毒神绝技能25(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 毒神绝技能26(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 毒神绝技能27(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

毒神绝技能列表 = []
i = 0
while i >= 0:
    try:
        exec('毒神绝技能列表.append(毒神绝技能'+str(i)+'())')
        i += 1
    except:
        i = -1

毒神绝技能序号 = dict()
for i in range(len(毒神绝技能列表)):
    毒神绝技能序号[毒神绝技能列表[i].名称] = i

毒神绝一觉序号 = 0
毒神绝二觉序号 = 22
毒神绝三觉序号 = 0
for i in 毒神绝技能列表:
    if i.所在等级 == 50:
        毒神绝一觉序号 = 毒神绝技能序号[i.名称]
    if i.所在等级 == 100:
        毒神绝三觉序号 = 毒神绝技能序号[i.名称]

毒神绝护石选项 = ['无']
for i in 毒神绝技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        毒神绝护石选项.append(i.名称)

毒神绝符文选项 = ['无']
for i in 毒神绝技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        毒神绝符文选项.append(i.名称)

class 毒神绝角色属性(角色属性):

    职业名称 = '毒神绝'

    武器选项 = ['爪']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法百分比', '物理百分比']
    
    #默认
    伤害类型 = '魔法百分比'
    防具类型 = '重甲'
    防具精通属性 = ['力量','智力']

    主BUFF = 9.50
   
    #基础属性(含唤醒)
    基础力量 = 926.0
    基础智力 = 909.0
    
    #适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    #人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13

    死亡毒雾力智开关 = 0
    毒伤结算丢失开关 = 0
  
    def __init__(self):
        self.技能栏= deepcopy(毒神绝技能列表)
        self.技能序号= deepcopy(毒神绝技能序号)

    def 站街力量(self):
        return int(max(self.力量,self.智力))

    def 站街智力(self):
        return self.站街力量()

    def 面板力量(self):
        return max(super().面板力量(), super().面板智力())
      
    def 面板智力(self):
        return self.面板力量()

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['万毒噬心诀x3']].被动倍率 /= self.技能栏[self.技能序号['万毒噬心诀']].加成倍率(self.武器类型)
        self.技能栏[self.技能序号['万毒噬心诀x4']].被动倍率 /= self.技能栏[self.技能序号['万毒噬心诀']].加成倍率(self.武器类型)
        self.技能栏[self.技能序号['万毒噬心诀x3']].等级 = self.技能栏[self.技能序号['万毒噬心诀']].等级
        self.技能栏[self.技能序号['万毒噬心诀x4']].等级 = self.技能栏[self.技能序号['万毒噬心诀']].等级
        self.技能栏[self.技能序号['禁技：万毒蛇窟']].等级 = self.技能栏[self.技能序号['万毒噬心诀']].等级
        
        x = self.技能栏[self.技能序号['双重投掷']].等级
        self.技能栏[self.技能序号['抛沙']].攻击次数 *= 1 + 0.3 + 0.02 * x
        self.技能栏[self.技能序号['抛沙']].涂毒倍率 *= 2

        self.技能栏[self.技能序号['街头风暴']].攻击次数 *= 1 + 0.31 + 0.01 * x
        self.技能栏[self.技能序号['街头风暴']].涂毒倍率 *= 2
    
    def 伤害指数计算(self):

        防御 = 443243
        if self.死亡毒雾力智开关 == 1:
            self.进图力量 += self.技能栏[self.技能序号['死亡毒雾']].力智加成()
            self.进图智力 += self.技能栏[self.技能序号['死亡毒雾']].力智加成()
            防御 -= self.技能栏[self.技能序号['死亡毒雾']].防御减少()

        for i in self.技能栏:
            if i.是否主动 == 1:
                i.涂毒倍率 *= (self.主BUFF - 1)

        基准倍率 = 1.5 * (1 - 防御 / (防御 + 20000))

        面板 = (self.面板智力()/250+1) * (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻)

        self.火属性强化 += int((self.火属性强化 - 22) * self.百分比属强)
        self.冰属性强化 += int((self.冰属性强化 - 22) * self.百分比属强)
        self.光属性强化 += int((self.光属性强化 - 22) * self.百分比属强)
        self.暗属性强化 += int((self.暗属性强化 - 22) * self.百分比属强)
        if self.攻击属性 == 0:
            属性倍率=1.05+0.0045*max(self.火属性强化,self.冰属性强化,self.光属性强化,self.暗属性强化)
        elif self.攻击属性 == 1:
            属性倍率=1.05+0.0045*self.火属性强化
        elif self.攻击属性 == 2:
            属性倍率=1.05+0.0045*self.冰属性强化
        elif self.攻击属性 == 3:
            属性倍率=1.05+0.0045*self.光属性强化
        elif self.攻击属性 == 4:
            属性倍率=1.05+0.0045*self.暗属性强化
        增伤倍率=1+self.伤害增加
        增伤倍率*=1+self.暴击伤害
        增伤倍率*=1+self.最终伤害
        增伤倍率*=self.技能攻击力
        增伤倍率*=1+self.持续伤害*(1-0.1*self.持续伤害计算比例)
        增伤倍率*=1+self.附加伤害+self.属性附加*属性倍率
        self.伤害指数=面板*属性倍率*增伤倍率*基准倍率/100

    def 伤害计算(self, x = 0):
        
        self.所有属性强化(self.进图属强)
        # Will添加
        self.CD倍率计算()
        self.加算冷却计算()

        self.被动倍率计算()
        self.伤害指数计算()

        技能释放次数=[]
        技能单次伤害=[]
        技能总伤害=[]


        #技能释放次数计算
        for i in self.技能栏:
            if i.是否有伤害==1:
                if self.次数输入[self.技能序号[i.名称]] =='/CD':
                    技能释放次数.append(int((self.时间输入 - i.演出时间)/i.等效CD(self.武器类型) + 1 +i.基础释放次数))
                else:
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]]))
            else:
                技能释放次数.append(0)

        #毒伤结算丢失开关 
        if 技能释放次数[self.技能序号['万毒噬心诀x4']] > 3 and self.毒伤结算丢失开关 == 1:  
            self.技能栏[self.技能序号['万毒噬心诀x4']].涂毒倍率 *=(技能释放次数[self.技能序号['万毒噬心诀x4']] - 3) / 技能释放次数[self.技能序号['万毒噬心诀x4']]
    
        #技能单次伤害计算
        for i in self.技能栏:
            if i.是否有伤害==1:
                技能单次伤害.append(i.等效百分比(self.武器类型)*self.伤害指数*i.被动倍率)
            else:
                技能单次伤害.append(0)
      

        #单技能伤害合计
        for i in self.技能栏:
            if i.是否有伤害==1 and 技能释放次数[self.技能序号[i.名称]] != 0:
                技能总伤害.append(技能单次伤害[self.技能序号[i.名称]]*技能释放次数[self.技能序号[i.名称]]*(1+self.白兔子技能*0.20+self.年宠技能*0.10*self.宠物次数[self.技能序号[i.名称]]/技能释放次数[self.技能序号[i.名称]]+self.斗神之吼秘药*0.12))
            else:
                技能总伤害.append(0)
    
        总伤害=0
        for i in self.技能栏:
            总伤害+=技能总伤害[self.技能序号[i.名称]]
        
        if x==0:
            return 总伤害
    
        if x==1:
            详细数据=[]
            for i in range(0,len(self.技能栏)):
                详细数据.append(技能释放次数[i])
                详细数据.append(技能总伤害[i])
                if 技能释放次数[i]!=0:
                    详细数据.append(技能总伤害[i]/技能释放次数[i])
                else:
                    详细数据.append(0)
                if 总伤害!=0:
                    详细数据.append(技能总伤害[i]/总伤害*100)
                else:
                    详细数据.append(0)
            return 详细数据

class 毒神绝(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 毒神绝角色属性()
        self.角色属性A = 毒神绝角色属性()
        self.角色属性B = 毒神绝角色属性()
        self.一觉序号 = 毒神绝一觉序号
        self.二觉序号 = 毒神绝二觉序号
        self.三觉序号 = 毒神绝三觉序号
        self.护石选项 = deepcopy(毒神绝护石选项)
        self.符文选项 = deepcopy(毒神绝符文选项)

    def 界面(self):
        super().界面()
        self.死亡毒雾力智开关=QCheckBox('死亡毒雾效果',self.main_frame2)
        self.死亡毒雾力智开关.resize(100,20)
        self.死亡毒雾力智开关.move(325,450)
        self.死亡毒雾力智开关.setStyleSheet(复选框样式)
        self.死亡毒雾力智开关.setToolTip('包含力智和减防')
        self.死亡毒雾力智开关.setChecked(True)

        self.毒伤结算丢失开关=QCheckBox('毒伤丢失补正',self.main_frame2)
        self.毒伤结算丢失开关.resize(100,20)
        self.毒伤结算丢失开关.move(325,480)
        self.毒伤结算丢失开关.setStyleSheet(复选框样式)
        self.毒伤结算丢失开关.setToolTip('伤害统计将不计入最后3轮4X蛇拳的毒伤')
        self.毒伤结算丢失开关.setChecked(True)


        self.毒雷个数数选择=MyQComboBox(self.main_frame2)
        for i in range(9):
            self.毒雷个数数选择.addItem('毒雷引爆：' + str(i) + '颗')
        self.毒雷个数数选择.setToolTip('包含冲击波次数')
        self.毒雷个数数选择.setCurrentIndex(5)
        self.毒雷个数数选择.resize(120,20)
        self.毒雷个数数选择.move(315,510)

        self.毒雾爆炸段数选择=MyQComboBox(self.main_frame2)
        for i in range(11):
            self.毒雾爆炸段数选择.addItem('毒雾爆炸：' + str(i) + '段')
        self.毒雾爆炸段数选择.setCurrentIndex(5)
        self.毒雾爆炸段数选择.resize(120,20)
        self.毒雾爆炸段数选择.move(315,540)
    
        self.毒雾中毒次数选择=MyQComboBox(self.main_frame2)
        for i in range(21):
            self.毒雾中毒次数选择.addItem('毒雾中毒：' + str(i) + '段')
        self.毒雾中毒次数选择.setCurrentIndex(8)
        self.毒雾中毒次数选择.resize(120,20)
        self.毒雾中毒次数选择.move(315,570)   

    def 输入属性(self, 属性):
        super().输入属性(属性)
        if self.死亡毒雾力智开关.isChecked():
            属性.死亡毒雾力智开关 = 1
        if self.毒伤结算丢失开关.isChecked():
            属性.毒伤结算丢失开关 = 1
        属性.技能栏[属性.技能序号['毒雷引爆']].倍率 *= self.毒雷个数数选择.currentIndex()
        属性.技能栏[属性.技能序号['死亡毒雾']].攻击次数 *= self.毒雾爆炸段数选择.currentIndex()
        属性.技能栏[属性.技能序号['死亡毒雾']].涂毒倍率 *= self.毒雾爆炸段数选择.currentIndex()
        属性.技能栏[属性.技能序号['死亡毒雾']].中毒倍率 *= self.毒雾中毒次数选择.currentIndex()