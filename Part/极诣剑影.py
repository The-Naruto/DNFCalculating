from PublicReference.base import *

#6.15 精确技能伤害数据到小数点后四位，修正回天与聚渊护石伤害加成，增加95技能形态选择

class 极诣剑影主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '太刀':
            return round(self.CD / self.恢复 * 0.95, 1)

class 极诣剑影技能0(主动技能):
    名称 = '鬼步'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 572.0
    成长 = 64.60
    攻击次数 = 3
    CD = 5.0
    TP成长 = 0.1
    TP上限 = 7

class 极诣剑影技能1(主动技能):
    名称 = '鬼连斩'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1856.1111
    成长 = 209.5778
    基础2 = 2129.7333
    成长2 = 240.2667
    攻击次数2 = 1
    CD = 5.0
    TP成长 = 0.1
    TP上限 = 7

class 极诣剑影技能2(被动技能):
    名称 = '剑影太刀精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.0 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)

class 极诣剑影技能3(主动技能):
    名称 = '幻鬼：一闪'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 1914.7143
    成长 = 216.2857
    CD = 6
    TP成长 = 0.10
    TP上限 = 7

class 极诣剑影技能4(被动技能):
    名称 = '幻鬼之力'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.02 * self.等级, 5)

class 极诣剑影技能5(主动技能):
    名称 = '鬼连牙'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3470.1250
    成长 = 391.8750
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7

class 极诣剑影技能6(主动技能):
    名称 = '幻鬼：连斩'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3157.3500
    成长 = 356.6500
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7

class 极诣剑影技能7(主动技能):
    名称 = '共鸣：离魂一闪'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4870.0541
    成长 = 549.9459
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 7


class 极诣剑影技能8(主动技能):
    名称 = '魂破斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 5582.6857
    成长 = 630.3143
    CD = 12
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.15
        self.成长 *= 1.15
        self.CD *= 0.89

class 极诣剑影技能9(主动技能):
    名称 = '共鸣：鬼灵斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 6251.1143
    成长 = 705.8857
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 7

class 极诣剑影技能10(主动技能):
    名称 = '幻鬼：回天'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 2882.50
    成长 = 325.50
    基础2 = 4323.7188
    成长2 = 488.2813
    攻击次数2 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1
        self.成长 *= 1
        self.基础2 *= 1.40
        self.成长2 *= 1.40


class 极诣剑影技能11(主动技能):
    名称 = '冥灵断魂斩'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 17019.3667
    成长 = 1921.6333
    CD = 45
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.15
        self.成长 *= 1.15

class 极诣剑影技能12(主动技能):
    名称 = '冥夜鬼天杀'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 38956.0 * 1.1
    成长 = 11762 * 1.1
    CD = 145.0

class 极诣剑影技能13(被动技能):
    名称 = '鬼夜'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.035 + 0.02 * self.等级, 5)

class 极诣剑影技能14(主动技能):
    名称 = '幻鬼：奈落'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 1
    基础 = 9500.3636
    成长 = 1072.6364
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.13
        self.成长 *= 1.13
        self.CD *= 0.85

class 极诣剑影技能15(主动技能):
    名称 = '共鸣：聚渊'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 1
    基础 = 2361.2941
    成长 = 266.7059
    基础2 = 9448.1765
    成长2 = 1066.8235
    攻击次数2 = 1
    基础3 = 11810.4706
    成长3 = 1333.5294
    攻击次数3 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.基础3 *= 1.23 * 1.20
        self.成长3 *= 1.23 * 1.20

class 极诣剑影技能16(主动技能):
    名称 = '幻鬼：大回天'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 34019.0
    成长 = 3841.0
    CD = 40.0

class 极诣剑影技能17(被动技能):
    名称 = '鬼咲'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

class 极诣剑影技能18(主动技能):
    名称 = '裂魂乱舞'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 47766.6667
    成长 = 5393.3333
    CD = 45.0

class 极诣剑影技能19(主动技能):
    名称 = '鬼隐·夜奈落'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 94278.25
    成长 = 28461.75
    CD = 180.0

class 极诣剑影技能20(被动技能):
    名称 = '睥睨万物'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 极诣剑影技能21(主动技能):
    名称 = '无式·极影剑'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 87214.0
    成长 = 9848
    攻击次数 = 1
    基础2 = 73375.60
    成长2 = 8284.40
    攻击次数2 = 0
    CD = 60.0

class 极诣剑影技能22(主动技能):
    名称 = '灭魂极影剑·止煞'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 254722.0
    成长 = 76902.50
    CD = 290.0

    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

极诣剑影技能列表 = []
i = 0
while i >= 0:
    try:
        exec('极诣剑影技能列表.append(极诣剑影技能'+str(i)+'())')
        i += 1
    except:
        i = -1

极诣剑影技能序号 = dict()
for i in range(len(极诣剑影技能列表)):
    极诣剑影技能序号[极诣剑影技能列表[i].名称] = i

极诣剑影一觉序号 = 0
极诣剑影二觉序号 = 0
极诣剑影三觉序号 = 0
for i in 极诣剑影技能列表:
    if i.所在等级 == 50:
        极诣剑影一觉序号 = 极诣剑影技能序号[i.名称]
    if i.所在等级 == 85:
        极诣剑影二觉序号 = 极诣剑影技能序号[i.名称]
    if i.所在等级 == 100:
        极诣剑影三觉序号 = 极诣剑影技能序号[i.名称]

极诣剑影护石选项 = ['无']
for i in 极诣剑影技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        极诣剑影护石选项.append(i.名称)

极诣剑影符文选项 = ['无']
for i in 极诣剑影技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        极诣剑影符文选项.append(i.名称)

class 极诣剑影角色属性(角色属性):

    职业名称 = '极诣剑影'

    武器选项 = ['太刀']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['物理百分比']
    
    #默认
    伤害类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    主BUFF = 2.00
   
    #基础属性(含唤醒)
    基础力量 = 923.0
    基础智力 = 827.0
    
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

    无式极影剑形态 = 0
  
    def __init__(self):
        self.技能栏= deepcopy(极诣剑影技能列表)
        self.技能序号= deepcopy(极诣剑影技能序号)

    def 装备基础(self):
        for i in [0,1,2,3,4]:
            temp = 装备列表[装备序号[self.装备栏[i]]]
            x = temp
            if temp.所属套装 != '智慧产物':
                x = 精通计算(temp.装备等级,temp.品质,self.强化等级[i],部位列表[i])
            else:
                x = 精通计算(temp.装备等级,temp.品质,0,部位列表[i])
            if '力量' in self.防具精通属性:
                self.力量 += x + temp.力量[self.防具类型]
            if '智力' in self.防具精通属性:
                self.智力 += x + temp.智力[self.防具类型]
  
        for i in [9,10]:
            temp = 装备列表[装备序号[self.装备栏[i]]]
            if temp.所属套装 != '智慧产物':
                x = 左右计算(temp.装备等级,temp.品质,self.强化等级[i])
                self.力量 += x
                self.智力 += x

        for i in range(0,12):
            temp = 装备列表[装备序号[self.装备栏[i]]]
            if self.是否增幅[i] and temp.所属套装 != '智慧产物':
                x = 增幅计算(temp.装备等级,temp.品质,self.强化等级[i])
                if '物理' in self.伤害类型 or '力量' in self.伤害类型:
                    self.力量 += x
                else:
                    self.智力 += x
        
        temp = 装备列表[装备序号[self.装备栏[11]]]
        if temp.所属套装 != '智慧产物':
            self.物理攻击力 += 武器计算(temp.装备等级,temp.品质,self.强化等级[11],self.武器类型,'魔法')
            self.魔法攻击力 += 武器计算(temp.装备等级,temp.品质,self.强化等级[11],self.武器类型,'魔法')
            self.独立攻击力 += 锻造计算(temp.装备等级,temp.品质,self.武器锻造等级)
        
        temp = 装备列表[装备序号[self.装备栏[8]]]
        if temp.所属套装 != '智慧产物':
            x = 耳环计算(temp.装备等级,temp.品质,self.强化等级[8])
            self.物理攻击力 += x
            self.魔法攻击力 += x
            self.独立攻击力 += x

        for i in [5,6,7,8,9,10,11]:
            temp = 装备列表[装备序号[self.装备栏[i]]]
            self.力量 += temp.力量
            self.智力 += temp.智力
            self.物理攻击力 += temp.魔法攻击力
            self.魔法攻击力 += temp.魔法攻击力
            self.独立攻击力 += temp.独立攻击力


    def 被动倍率计算(self):
        super().被动倍率计算()

        if self.无式极影剑形态 == 0:
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数 = 1
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数2 = 0
        if self.无式极影剑形态 == 1:
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数 = 0
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数2 = 1


class 极诣剑影(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 极诣剑影角色属性()
        self.角色属性A = 极诣剑影角色属性()
        self.角色属性B = 极诣剑影角色属性()
        self.一觉序号 = 极诣剑影一觉序号
        self.二觉序号 = 极诣剑影二觉序号
        self.三觉序号 = 极诣剑影三觉序号
        self.护石选项 = deepcopy(极诣剑影护石选项)
        self.符文选项 = deepcopy(极诣剑影符文选项)

    def 界面(self):
        super().界面()
        self.无式极影剑形态选择=MyQComboBox(self.main_frame2)
        self.无式极影剑形态选择.addItem('无式极影剑(共鸣)')
        self.无式极影剑形态选择.addItem('无式极影剑(幻鬼)')
        self.无式极影剑形态选择.setCurrentIndex(0)
        self.无式极影剑形态选择.resize(130,20)
        self.无式极影剑形态选择.move(315,300)

    def 输入属性(self, 属性):
        super().输入属性(属性)

        属性.无式极影剑形态 = self.无式极影剑形态选择.currentIndex()

