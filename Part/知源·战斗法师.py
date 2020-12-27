from PublicReference.base import *

# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '矛':
#             return round(self.CD / self.恢复 * 1.05, 1)
#         if 武器类型 == '棍棒':
#             return round(self.CD / self.恢复 * 0.95, 1)

class 知源·战斗法师技能0(被动技能):
    名称 = '尼巫的战斗术'
    所在等级=15
    等级上限=11
    基础等级=1
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.18+0.02*self.等级,3)

class 知源·战斗法师技能1(被动技能):
    名称 = '炫纹'
    所在等级=15
    等级上限=60
    基础等级=46  
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.20+0.00*self.等级,3)
    
class 知源·战斗法师技能2(被动技能):
    名称='矛精通'
    所在等级=20
    等级上限=30
    基础等级=20  
    def 加成倍率(self, 武器类型):
        if self.等级==0 or 武器类型 != '矛':
            return 1.0  
        if self.等级<=20:
            return round(1.00+0.01*self.等级,3) 
        if self.等级>20:
            return round(0.80+0.02*self.等级,3)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

class 知源·战斗法师技能3(被动技能):
    名称='棍棒精通'
    所在等级=20
    等级上限=30
    基础等级=20  
    def 加成倍率(self, 武器类型):
        if self.等级==0 or 武器类型 != '棍棒':
            return 1.0  
        if self.等级<=20:
            return round(1.00+0.01*self.等级,3) 
        if self.等级>20:
            return round(0.80+0.02*self.等级,3)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)
    
class 知源·战斗法师技能4(主动技能):
    名称 = '炫纹发射'
    备注 = '(个数,TP为强化炫纹)'
    是否主动 = 0
    所在等级=15
    等级上限=60
    基础等级=46
    # 95被动,默认超大炫纹,倍率*1.5
    数据 = [ i * 1.5 for i in [0, 242, 266, 293, 316, 342, 365, 390, 413, 439, 464, 490, 513, 538, 563, 587, 612, 638, 662, 686, 712, 735,
         760, 784, 809, 835, 860, 883, 909, 932, 957, 980, 1007, 1032, 1057, 1081, 1105, 1131, 1154, 1181, 1205, 1229,
         1252, 1278, 1302, 1326, 1351, 1377, 1402, 1426, 1451, 1476, 1500, 1523, 1551, 1574, 1599, 1623, 1648, 1671,
         1697, 1721, 1748, 1771, 1796, 1819, 1845, 1870, 1893, 1920, 1944]]
    
    CD=0.25
    TP成长=0.10
    TP上限 = 1
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

class 知源·战斗法师技能5(主动技能):
    名称='双重锤击'
    所在等级=20
    等级上限=60
    基础等级=43  
    #第一击物理攻击力：<data0>%10.6
    数据0 = [0, 456, 503, 552, 600, 645, 692, 740, 787, 834, 881, 927, 972, 1023, 1071, 1116, 1169, 1216, 1262, 1309, 1356, 1403, 1450, 1497, 1543, 1590, 1639, 1686, 1733, 1779, 1828, 1874, 1920, 1966, 2014, 2064, 2110, 2158, 2203, 2250, 2299, 2345, 2392, 2440, 2483, 2538, 2583, 2630, 2679, 2727, 2774, 2820, 2869, 2914, 2961, 3008, 3058, 3102, 3151, 3198, 3244, 3291, 3339, 3386, 3432, 3477, 3528, 3574, 3622, 3668, 3715]
    攻击次数0 = 1.0
    #最后一击物理攻击力：<data1>%
    数据1 = [0, 1675, 1851, 2021, 2194, 2369, 2542, 2716, 2890, 3060, 3234, 3409, 3583, 3753, 3928, 4100, 4276, 4450, 4618, 4794, 4968, 5141, 5317, 5487, 5658, 5834, 6008, 6181, 6353, 6527, 6699, 6875, 7046, 7220, 7393, 7565, 7743, 7916, 8084, 8259, 8434, 8608, 8782, 8951, 9124, 9302, 9474, 9644, 9818, 9991, 10167, 10341, 10511, 10683, 10859, 11035, 11207, 11375, 11551, 11725, 11899, 12075, 12241, 12417, 12594, 12765, 12940, 13110, 13285, 13458, 13634]
    攻击次数1 = 1.0
    #冲击波独立物理攻击力：<data2>%
    数据2 = [0, 1280, 1409, 1543, 1675, 1808, 1941, 2070, 2203, 2336, 2473, 2603, 2736, 2869, 2998, 3131, 3263, 3396, 3528, 3659, 3791, 3923, 4060, 4190, 4326, 4455, 4586, 4719, 4850, 4987, 5116, 5245, 5381, 5511, 5649, 5780, 5908, 6042, 6174, 6305, 6437, 6573, 6702, 6835, 6968, 7095, 7236, 7366, 7494, 7631, 7761, 7895, 8026, 8160, 8286, 8421, 8555, 8686, 8823, 8954, 9081, 9219, 9349, 9480, 9613, 9742, 9878, 10008, 10143, 10274, 10411]
    攻击次数2 = 1.0
    CD=8
    TP成长=0.10
    TP上限 = 5
    演出时间 = 1.1
    def 等效百分比(self, 武器类型):
        return (self.数据0[self.等级]* self.攻击次数 + self.数据1[self.等级]* self.攻击次数2 + self.数据2[self.等级]* self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率    

class 知源·战斗法师技能6(主动技能):
    名称='炫纹爆弹'
    所在等级=25
    等级上限=60
    基础等级=41  
    #直刺5.97
    数据0 = [0, 1170, 1294, 1410, 1536, 1665, 1776, 1908, 2026, 2147, 2266, 2387, 2507, 2631, 2747, 2872, 2992, 3112, 3231, 3350, 3472, 3600, 3712, 3843, 3971, 4082, 4214, 4332, 4453, 4572, 4693, 4814, 4938, 5053, 5177, 5298, 5419, 5537, 5659, 5778, 5909, 6020, 6149, 6275, 6388, 6513, 6628, 6754, 6875, 6994, 7112, 7233, 7354, 7483, 7603, 7725, 7845, 7965, 8084, 8215, 8335, 8455, 8575, 8697, 8815, 8934, 9059, 9181, 9300, 9420, 9539]
    攻击次数0 = 1.0
    #多段
    数据1 = [0, 146, 159, 174, 190, 210, 225, 240, 250, 270, 281, 295, 320, 331, 344, 350, 375, 391, 401, 426, 429, 451, 466, 480, 495, 511, 531, 535, 561, 570, 586, 609, 616, 631, 640, 663, 680, 691, 711, 719, 734, 749, 770, 785, 800, 816, 826, 850, 855, 871, 896, 906, 920, 936, 951, 971, 987, 991, 1011, 1027, 1040, 1056, 1072, 1091, 1105, 1120, 1136, 1146, 1160, 1175, 1191]
    攻击次数1 = 13.0
    #爆炸
    数据2 = [0, 3522, 3883, 4243, 4612, 4977, 5339, 5700, 6068, 6433, 6789, 7156, 7524, 7884, 8255, 8614, 8980, 9350, 9701, 10071, 10429, 10795, 11157, 11527, 11898, 12256, 12617, 12982, 13351, 13703, 14073, 14438, 14797, 15168, 15529, 15900, 16263, 16618, 16984, 17345, 17716, 18075, 18440, 18810, 19171, 19531, 19891, 20266, 20620, 20986, 21356, 21718, 22084, 22442, 22802, 23173, 23534, 23902, 24264, 24629, 24988, 25357, 25720, 26085, 26445, 26814, 27174, 27546, 27906, 28265, 28630]
    攻击次数2 = 1.0
    演出时间 = 12.0
    CD=8
    TP成长=0.10
    TP上限 = 5
    演出时间 = 0.6
    def 等效百分比(self, 武器类型):
        return (self.数据0[self.等级]* self.攻击次数 + self.数据1[self.等级]* self.攻击次数2 + self.数据2[self.等级]* self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 知源·战斗法师技能7(主动技能):
    名称='碎霸'
    所在等级=30
    等级上限=60
    基础等级=38
    数据 = [0, 4057, 4475, 4897, 5316, 5734, 6151, 6570, 6992, 7412, 7830, 8251, 8671, 9091, 9511, 9931, 10347, 10767, 11187, 11605, 12028, 12447, 12866, 13286, 13707, 14128, 14544, 14961, 15382, 15801, 16223, 16641, 17063, 17483, 17902, 18318, 18737, 19157, 19578, 20000, 20417, 20837, 21260, 21677, 22099, 22514, 22933, 23354, 23772, 24193, 24614, 25034, 25453, 25872, 26294, 26708, 27131, 27548, 27969, 28389, 28809, 29230, 29649, 30070, 30485, 30904, 31324, 31743, 32166, 32584, 33004]
    CD=8
    基础释放次数=0
    TP成长=0.10
    TP上限 = 5
    额外倍率 = 0
    触发概率 = 0
    def 等效百分比(self, 武器类型):
        return (1 + self.额外倍率 * self.触发概率) * self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率
    

class 知源·战斗法师技能8(主动技能):
    名称='炫纹融合(旋转)'
    所在等级=30
    等级上限=60
    基础等级=38  
    数据 = [0, 296, 325, 356, 386, 416, 445, 475, 506, 535, 566, 596, 626, 656, 685, 715, 745, 776, 805, 836, 866, 897, 926, 955, 986, 1015, 1046, 1076, 1106, 1136, 1167, 1196, 1225, 1257, 1286, 1316, 1346, 1377, 1406, 1437, 1467, 1496, 1527, 1556, 1586, 1616, 1647, 1677, 1707, 1737, 1767, 1797, 1826, 1857, 1886, 1917, 1947, 1978, 2007, 2037, 2068, 2096, 2127, 2157, 2187, 2217, 2248, 2277, 2307, 2338, 2366]
    攻击次数 = 15
    CD=8
    TP成长=0.10
    TP上限 = 5
    演出时间 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级]* self.攻击次数 * self.倍率


class 知源·战斗法师技能9(主动技能):
    名称='流星闪影击'
    所在等级=35
    等级上限=60
    基础等级=36  
    数据 = [0, 9155, 10084, 11013, 11942, 12870, 13800, 14727, 15659, 16590, 17513, 18442, 19373, 20303, 21230, 22160, 23085, 24016, 24942, 25874, 26804, 27732, 28660, 29589, 30518, 31450, 32379, 33301, 34231, 35162, 36090, 37021, 37950, 38875, 39807, 40732, 41663, 42594, 43522, 44446, 45378, 46308, 47236, 48169, 49095, 50022, 50951, 51881, 52809, 53736, 54666, 55594, 56522, 57454, 58383, 59314, 60235, 61166, 62098, 63026, 63957, 64883, 65812, 66741, 67671, 68600, 69528, 70458, 71384, 72313, 73241]
    CD=20
    TP成长=0.10
    TP上限 = 5
    演出时间 = 0.6
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级]  * (1 + self.TP成长 * self.TP等级) * self.倍率
   
class 知源·战斗法师技能10(主动技能):
    名称='炫纹强压'
    所在等级=35
    等级上限=60
    基础等级=36  
    数据 = [0, 9768, 10759, 11750, 12741, 13732, 14723, 15714, 16705, 17696, 18687, 19678, 20669, 21660, 22651, 23642, 24633, 25624, 26615, 27606, 28597, 29588, 30579, 31570, 32561, 33552, 34543, 35534, 36525, 37516, 38507, 39498, 40489, 41480, 42471, 43462, 44453, 45444, 46435, 47426, 48417, 49408, 50399, 51390, 52381, 53372, 54363, 55354, 56345, 57336, 58328, 59319, 60310, 61301, 62292, 63284, 64275, 65266, 66257, 67248, 68239, 69230, 70221, 71212, 72203, 73194, 74185, 75176, 76167, 77158, 78149]
    CD=17.9
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.4

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.242
            self.CD *=0.92

        elif x == 1:
            self.倍率*=1.334
            self.CD *=0.92
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级]  * (1 + self.TP成长 * self.TP等级) * self.倍率    


class 知源·战斗法师技能11(主动技能):
    名称='强袭流星打'
    所在等级=40
    等级上限=60
    基础等级=33  
    数据 = [0, 10502, 11591, 12679, 13758, 14843, 15934, 17022, 18108, 19193, 20286, 21368, 22447, 23540, 24625, 25716, 26797, 27880, 28971, 30057, 31139, 32232, 33313, 34405, 35486, 36571, 37664, 38748, 39829, 40919, 42001, 43095, 44181, 45260, 46353, 47436, 48529, 49608, 50695, 51788, 52869, 53947, 55040, 56125, 57219, 58297, 59383, 60477, 61558, 62644, 63731, 64814, 65906, 66989, 68074, 69164, 70252, 71333, 72421, 73509, 74601, 75685, 76763, 77852, 78942, 80029, 81110, 82198, 83287, 84372, 85456]
    CD=25
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 0.5
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.1865
        elif x == 1:
            self.倍率*=1.281
    
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级]  * (1 + self.TP成长 * self.TP等级) * self.倍率
        
class 知源·战斗法师技能12(主动技能):
    名称='煌龙偃月'
    所在等级=45
    等级上限=60
    基础等级=31  
    数据0 = [0, 4187, 4617, 5056, 5485, 5918, 6351, 6783, 7214, 7653, 8083, 8516, 8949, 9380, 9814, 10250, 10683, 11117, 11546, 11979, 12414, 12848, 13280, 13715, 14146, 14578, 15014, 15445, 15877, 16312, 16745, 17172, 17612, 18042, 18475, 18909, 19341, 19771, 20212, 20642, 21073, 21507, 21939, 22370, 22806, 23239, 23675, 24104, 24536, 24973, 25403, 25837, 26272, 26704, 27134, 27571, 28004, 28434, 28869, 29299, 29731, 30170, 30601, 31031, 31466, 31899, 32328, 32768, 33199, 33627, 34063]
    攻击次数 = 1.0
    数据1 = [0, 1397, 1539, 1687, 1832, 1975, 2117, 2260, 2404, 2552, 2695, 2838, 2983, 3126, 3271, 3416, 3561, 3707, 3850, 3994, 4141, 4284, 4427, 4573, 4716, 4858, 5006, 5150, 5292, 5437, 5582, 5726, 5872, 6015, 6158, 6304, 6447, 6590, 6738, 6882, 7025, 7169, 7313, 7456, 7603, 7746, 7891, 8035, 8178, 8326, 8471, 8613, 8756, 8901, 9045, 9192, 9335, 9479, 9623, 9766, 9910, 10058, 10201, 10345, 10490, 10634, 10776, 10924, 11068, 11213, 11355]
    攻击次数2 = 7.0
    数据2 = [0, 5987, 6602, 7226, 7845, 8460, 9084, 9704, 10316, 10941, 11560, 12175, 12800, 13418, 14031, 14655, 15275, 15894, 16511, 17131, 17751, 18369, 18987, 19610, 20229, 20844, 21467, 22085, 22701, 23325, 23943, 24559, 25182, 25799, 26415, 27037, 27656, 28273, 28900, 29515, 30132, 30758, 31371, 31988, 32613, 33229, 33853, 34470, 35086, 35711, 36328, 36943, 37572, 38186, 38804, 39426, 40044, 40662, 41285, 41902, 42518, 43138, 43757, 44376, 44995, 45615, 46232, 46853, 47468, 48089, 48712]
    攻击次数3 = 1.0
    CD=45
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.24
        elif x == 1:
            self.倍率*=1.318

    def 等效百分比(self, 武器类型):
        return (self.数据0[self.等级]* self.攻击次数 + self.数据1[self.等级]* self.攻击次数2 + self.数据2[self.等级]* self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率
        
class 知源·战斗法师技能13(主动技能):
    名称='煌龙乱舞'
    所在等级=45
    等级上限=60
    基础等级=31  
    数据0 =[0, 1422, 1567, 1711, 1857, 2001, 2146, 2289, 2434, 2578, 2722, 2868, 3012, 3156, 3300, 3445, 3589, 3734, 3877, 4023, 4167, 4311, 4456, 4600, 4744, 4888, 5034, 5178, 5323, 5467, 5611, 5755, 5900, 6045, 6189, 6334, 6477, 6622, 6766, 6911, 7055, 7200, 7344, 7489, 7633, 7777, 7922, 8065, 8211, 8355, 8500, 8644, 8789, 8932, 9077, 9222, 9367, 9511, 9654, 9799, 9943, 10088, 10232, 10378, 10521, 10666, 10810, 10955, 11099, 11242, 11388]
    攻击次数 = 5.0
    数据1 = [0, 10676, 11759, 12841, 13926, 15009, 16092, 17175, 18259, 19341, 20424, 21508, 22590, 23674, 24757, 25841, 26923, 28006, 29090, 30172, 31256, 32339, 33422, 34505, 35589, 36671, 37754, 38838, 39920, 41004, 42087, 43170, 44253, 45336, 46419, 47502, 48586, 49668, 50752, 51835, 52918, 54001, 55084, 56167, 57250, 58334, 59416, 60500, 61583, 62665, 63749, 64832, 65917, 66998, 68083, 69166, 70249, 71332, 72415, 73498, 74581, 75665, 76747, 77831, 78914, 79996, 81080, 82163, 83246, 84329, 85413]
    攻击次数2 = 1.0
    CD=45
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.2552       
        elif x == 1:
            self.倍率*=1.3272

    def 等效百分比(self, 武器类型):
        return (self.数据0[self.等级]* self.攻击次数 + self.数据1[self.等级]* self.攻击次数2 ) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 知源·战斗法师技能14(被动技能):
    名称='斗神意志'
    所在等级=48
    等级上限=40
    基础等级=20
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.05+0.02*self.等级,3)

class 知源·战斗法师技能15(主动技能):
    名称='星纹陨爆'
    所在等级=50
    等级上限=40
    基础等级=12  
    数据 = [0, 55402, 68248, 81095, 93943, 106789, 119637, 132483, 145330, 158177, 171023, 183871, 196717, 209565, 222412, 235258, 248105, 260951, 273799, 286646, 299493, 312340, 325186, 338033, 350881, 363727, 376574, 389421, 402268, 415115, 427961, 440809, 453655, 466503, 479350, 492195, 505043, 517889, 530737, 543584, 556431, 569278, 582124, 594971, 607818, 620665, 633512, 646359, 659206, 672053, 684899, 697747, 710593, 723441, 736288, 749133, 761981, 774827, 787675, 800522, 813369, 826216, 839061, 851909, 864756, 877603, 890450, 903297, 916144, 928991, 941837]
    CD=145.0
    演出时间 = 2

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级]* self.攻击次数 * self.倍率

class 知源·战斗法师技能16(主动技能):
    名称 = '变身贝亚娜'
    备注 = '(一轮)'
    所在等级=50
    等级上限=1
    基础等级=1  
    数据0 = [0, 408, 504, 599, 695, 790, 885, 981, 1077, 1175, 1269, 1364, 1461, 1555, 1653, 1746, 1842, 1938, 2033, 2128, 2226, 2320, 2417, 2512, 2607, 2704, 2799, 2893, 2990, 3085, 3182, 3277, 3373, 3468, 3564, 3662, 3755, 3850, 3947, 4041, 4138, 4234, 4329, 4425, 4521, 4616, 4713, 4806, 4902, 4998, 5093, 5190, 5286, 5380, 5477, 5573, 5670, 5763, 5859, 5954, 6050, 6146, 6242, 6337, 6434, 6528, 6625, 6721, 6815, 6910, 7007]
    攻击次数 = 4.0
    数据1 = [0, 1020, 1259, 1497, 1738, 1976, 2215, 2453, 2695, 2933, 3171, 3410, 3650, 3889, 4127, 4367, 4607, 4846, 5084, 5322, 5563, 5800, 6041, 6279, 6520, 6758, 6997, 7235, 7477, 7715, 7952, 8193, 8431, 8670, 8908, 9150, 9388, 9628, 9865, 10106, 10344, 10582, 10821, 11062, 11301, 11539, 11778, 12018, 12257, 12495, 12733, 12975, 13213, 13452, 13690, 13931, 14169, 14409, 14647, 14888, 15126, 15363, 15603, 15842, 16083, 16320, 16560, 16799, 17039, 17276, 17515]
    攻击次数2 = 1.0
    CD=1

    def 等效百分比(self, 武器类型):
        return (self.数据0[self.等级]* self.攻击次数 + self.数据1[self.等级]* self.攻击次数2 ) * self.倍率

class 知源·战斗法师技能17(主动技能):
    名称='变身贝亚娜苍天击'
    所在等级=50
    等级上限=1
    基础等级=1  
    数据 =[0, 1534, 1894, 2253, 2611, 2970, 3329, 3686, 4049, 4410, 4766, 5124, 5484, 5843, 6202, 6563, 6923, 7281, 7641, 8000, 8359, 8718, 9079, 9438, 9796, 10156, 10513, 10873, 11235, 11592, 11953, 12312, 12670, 13029, 13390, 13749, 14106, 14469, 14827, 15185, 15544, 15904, 16263, 16622, 16982, 17340, 17702, 18061, 18419, 18779, 19137, 19496, 19856, 20216, 20577, 20935, 21294, 21653, 22012, 22373, 22732, 23091, 23449, 23810, 24166, 24526, 24889, 25244, 25605, 25964, 26323]
    CD=1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级]* self.攻击次数 * self.倍率

class 知源·战斗法师技能18(主动技能):
    名称='变身贝亚娜天地碎霸'
    所在等级=50
    等级上限=1
    基础等级=1 
    数据0 = [0, 735, 908, 1080, 1253, 1426, 1757, 1946, 2137, 2326, 2516, 2708, 2895, 3088, 3276, 3465, 3655, 3846, 4034, 4225, 4413, 4605, 4794, 4982, 5174, 5364, 5553, 5743, 5932, 6123, 6313, 6500, 6691, 6881, 7069, 7259, 7448, 7637, 7830, 8020, 8209, 8400, 8588, 8779, 8968, 9156, 9347, 9537, 9726, 9916, 10105, 10297, 10487, 10675, 10867, 11056, 11246, 11433, 11625, 11813, 12003, 12191, 12383, 12572, 12764, 12953, 13143, 13333, 13521, 13711, 13901]
    攻击次数 = 1.0
    数据1 = [0, 3238, 3998, 4753, 5513, 6271, 7734, 8569, 9402, 10241, 11075, 11905, 12742, 13575, 14409, 15243, 16077, 16916, 17748, 18582, 19418, 20251, 21084, 21920, 22755, 23592, 24425, 25259, 26096, 26929, 27762, 28598, 29432, 30265, 31102, 31937, 32771, 33605, 34437, 35276, 36108, 36942, 37779, 38612, 39447, 40280, 41116, 41951, 42784, 43618, 44454, 45288, 46125, 46959, 47793, 48627, 49461, 50297, 51132, 51966, 52799, 53635, 54467, 55304, 56139, 56971, 57809, 58638, 59475, 60311, 61144]
    攻击次数2 = 1.0
    CD=7

    def 等效百分比(self, 武器类型):
        return (self.数据0[self.等级]* self.攻击次数 + self.数据1[self.等级]* self.攻击次数2 ) * self.倍率

class 知源·战斗法师技能19(主动技能):
    名称='闪击碎霸'
    所在等级=60
    等级上限=40
    基础等级=23  
    数据 = [0, 16576, 18256, 19937, 21619, 23302, 24987, 26664, 28347, 30027, 31710, 33390, 35072, 36755, 38437, 40116, 41800, 43484, 45163, 46845, 48526, 50208, 51891, 53568, 55252, 56937, 58613, 60294, 61980, 63661, 65339, 67022, 68705, 70385, 72066, 73747, 75432, 77113, 78792, 80475, 82160, 83839, 85520, 87201, 88883, 90568, 92245, 93928, 95611, 97289, 98972, 100656, 102338, 104018, 105696, 107379, 109065, 110740, 112425, 114106, 115790, 117469, 119152, 120832, 122517, 124197, 125877, 127560, 129243, 130922, 132602]
    CD=30
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 0.9
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.15
            self.CD *=0.90

        elif x == 1:
            self.倍率*=1.24
            self.CD *=0.90   

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级]  * (1 + self.TP成长 * self.TP等级) * self.倍率

class 知源·战斗法师技能20(主动技能):
    名称='流星雷连击'
    所在等级=70
    等级上限=40
    基础等级=18  
    数据 = [0, 27344, 30116, 32889, 35659, 38433, 41203, 43976, 46749, 49522, 52294, 55067, 57837, 60611, 63382, 66155, 68928, 71700, 74473, 77246, 80017, 82790, 85559, 88333, 91107, 93876, 96650, 99420, 102194, 104966, 107739, 110511, 113285, 116054, 118828, 121598, 124373, 127145, 129917, 132689, 135464, 138233, 141008, 143776, 146550, 149322, 152095, 154867, 157638, 160411, 163183, 165956, 168729, 171502, 174272, 177045, 179815, 182589, 185362, 188133, 190905, 193680, 196450, 199224, 201994, 204767, 207539, 210311, 213083, 215858, 218629]
    CD=50
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.10
        elif x == 1:
            self.倍率*=1.19

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级]  * (1 + self.TP成长 * self.TP等级) * self.倍率

class 知源·战斗法师技能21(被动技能):
    名称='战灵潜能'
    所在等级=75
    等级上限=40
    基础等级=11
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.22+0.02*self.等级,3)

class 知源·战斗法师技能22(主动技能):
    名称='炫纹簇'
    所在等级=75
    等级上限=40
    基础等级=16
    基础 = 5229.5625
    成长 = 590.4375
    攻击次数 = 7.0
    CD=45
    演出时间 = 1.3
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.倍率*=1.3142857 

class 知源·战斗法师技能23(主动技能):
    名称='使徒之舞'
    所在等级=80
    等级上限=40
    基础等级=13  
    数据0 = [0, 1709, 1883, 2056, 2231, 2404, 2577, 2751, 2924, 3098, 3269, 3445, 3617, 3791, 3964, 4139, 4312, 4485, 4657, 4832, 5006, 5179, 5354, 5525, 5698, 5871, 6046, 6221, 6392, 6566, 6741, 6913, 7087, 7262, 7434, 7608, 7780, 7955, 8129, 8300, 8472, 8647, 8821, 8996, 9169, 9342, 9515, 9689, 9864, 10036, 10209, 10382, 10557, 10731, 10902, 11074, 11249, 11423, 11595, 11771, 11944, 12117, 12290, 12465, 12638, 12812, 12982, 13158, 13330, 13504, 13678]
    攻击次数 = 3.0
    数据1 = [0, 3421, 3766, 4114, 4460, 4807, 5154, 5500, 5847, 6195, 6543, 6888, 7237, 7580, 7929, 8275, 8623, 8970, 9318, 9664, 10011, 10356, 10703, 11052, 11398, 11746, 12093, 12440, 12785, 13132, 13479, 13826, 14173, 14521, 14869, 15213, 15563, 15906, 16255, 16602, 16949, 17296, 17644, 17988, 18336, 18684, 19029, 19379, 19724, 20072, 20419, 20765, 21111, 21459, 21804, 22154, 22497, 22847, 23195, 23539, 23888, 24234, 24582, 24928, 25275, 25620, 25969, 26314, 26662, 27011, 27357]
    攻击次数2 = 1.0
    数据2 = [0, 34212, 37676, 41141, 44607, 48070, 51552, 55017, 58480, 61962, 65443, 68893, 72373, 75822, 79304, 82767, 86249, 89714, 93194, 96659, 100125, 103590, 107053, 110535, 114001, 117481, 120946, 124411, 127877, 131340, 134822, 138287, 141752, 145232, 148714, 152162, 155643, 159092, 162574, 166053, 169519, 172984, 176464, 179913, 183395, 186874, 190324, 193822, 197271, 200750, 204216, 207681, 211145, 214626, 218075, 221573, 225021, 228502, 231983, 235432, 238913, 242378, 245859, 249323, 252789, 256253, 259734, 263184, 266665, 270146, 273610]
    攻击次数3 = 1.0
    CD=40
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.倍率*=1.36801   

    def 等效百分比(self, 武器类型):
        return (self.数据0[self.等级]* self.攻击次数 + self.数据1[self.等级]* self.攻击次数2 + self.数据2[self.等级]* self.攻击次数3)  * self.倍率

class 知源·战斗法师技能24(主动技能):
    名称='一骑当千碎霸'
    所在等级=85
    等级上限=40
    基础等级=5  
    数据0 = [0, 55000, 67752, 80506, 93260, 106011, 118764, 131520, 144272, 157026, 169779, 182534, 195287, 208041, 220790, 233544, 246298, 259052, 271805, 284561, 297314, 310066, 
322819, 335572, 348327, 361080, 373833, 386585, 399339, 412092, 424847, 437599, 450354, 463106, 475859, 488613, 501367, 514121, 526874, 539625, 552377, 565132, 577887, 
590640, 603394, 616147, 628900, 641655, 654406, 667159, 679913, 692665, 705418, 718175, 730928, 743682, 756436, 769186, 781939, 794693, 807445, 820200, 832953, 845708, 
858459, 871216, 883968, 896721, 909475, 922229, 934981]
    攻击次数 = 1.0
    数据1 = [0, 36666, 45169, 53670, 62174, 70677, 79178, 87677, 96180, 104682, 113185, 121689, 130189, 138693, 147195, 155696, 164199, 172703, 181207, 189707, 198208, 206710, 215212, 223716, 232219, 240718, 249222, 257725, 266226, 274730, 283230, 291734, 300235, 308739, 317238, 325742, 334246, 342746, 351249, 359752, 368253, 376757, 385257, 393760, 402263, 410765, 419267, 427768, 436270, 444773, 453275, 461779, 470280, 478782, 487287, 495787, 504291, 512792, 521295, 529799, 538298, 546799, 555302, 563805, 572306, 580809, 589309, 597814, 606316, 614819, 623322]
    攻击次数2 = 1.0
    CD=180

    def 等效百分比(self, 武器类型):
        return (self.数据0[self.等级]* self.攻击次数 + self.数据1[self.等级]* self.攻击次数2)  * self.倍率
    
class 知源·战斗法师技能25(主动技能):
    名称='炫纹之源：太古神光'
    所在等级=95
    等级上限=60
    基础等级=6  
    基础 = 90673.8
    成长 = 10237.2
    # 额外计算10次炫纹
    炫纹倍率 = 0
    炫纹次数 = 10
    CD=58

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率 + self.炫纹倍率 * self.炫纹次数)    

class 知源·战斗法师技能26(被动技能):
    名称='太古之力'
    所在等级=95
    等级上限=40
    基础等级=4
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.18+0.02*self.等级,3)

class 知源·战斗法师技能27(主动技能):
    名称='太古星河·殒灭'
    所在等级=100
    等级上限=40
    基础等级=2  
    基础 = 9665*4 + 7733*5 + 38660 + 25772 + 7733*15
    成长 = 2917*4 + 2333*5 + 11669 + 7780 + 2333*15
    CD=290
    演出时间 = 5
    def 加成倍率(self, 武器类型):
        return 0.0

class 知源·战斗法师技能28(主动技能):
    名称='基本攻击'
    备注 = '(一轮,TP为基础精通)'
    所在等级=1
    等级上限=1
    基础等级=1  
    基础 = 225.2*2.662/1.115*1.1
    基础2 = 1.16 * 225.2*2.662/1.115*1.1
    基础3 = 1.8 * 225.2*2.662/1.115*1.1
    CD=1
    TP成长=0.10
    TP上限 = 3

class 知源·战斗法师技能29(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['基本攻击']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)

知源·战斗法师技能列表 = []
i = 0
while i >= 0:
    try:
        exec('知源·战斗法师技能列表.append(知源·战斗法师技能'+str(i)+'())')
        i += 1
    except:
        i = -1

知源·战斗法师技能序号 = dict()
for i in range(len(知源·战斗法师技能列表)):
    知源·战斗法师技能序号[知源·战斗法师技能列表[i].名称] = i

知源·战斗法师一觉序号 = 15
知源·战斗法师二觉序号 = 0
知源·战斗法师三觉序号 = 0
for i in 知源·战斗法师技能列表:
    if i.所在等级 == 85:
        知源·战斗法师二觉序号 = 知源·战斗法师技能序号[i.名称]
    if i.所在等级 == 100:
        知源·战斗法师三觉序号 = 知源·战斗法师技能序号[i.名称]

知源·战斗法师护石选项 = ['无']
for i in 知源·战斗法师技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        知源·战斗法师护石选项.append(i.名称)

知源·战斗法师符文选项 = ['无']
for i in 知源·战斗法师技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        知源·战斗法师符文选项.append(i.名称)

class 知源·战斗法师角色属性(角色属性):

    实际名称 = '知源·战斗法师'
    角色 = '魔法师(女)'
    职业 = '战斗法师'

    武器选项 = ['矛', '棍棒']
    
    类型选择 = ['物理百分比', '魔法百分比']
    
    类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量', '智力']

    主BUFF = 1.790

    远古记忆 = 0
  
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(知源·战斗法师技能列表)
        self.技能序号= deepcopy(知源·战斗法师技能序号)

    def 被动倍率计算(self):
        if self.武器类型 == '矛':
            self.技能栏[self.技能序号['棍棒精通']].关联技能 = ['无']
        elif self.武器类型 == '棍棒':
            self.技能栏[self.技能序号['矛精通']].关联技能 = ['无']
        for i in [16, 17, 18]:
            self.技能栏[i].等级 = self.技能栏[15].等级
        super().被动倍率计算()
        self.技能栏[self.技能序号['炫纹之源：太古神光']].炫纹倍率 = self.技能栏[self.技能序号['炫纹发射']].等效百分比(self.武器类型)

    def 站街力量(self):
        return int(max(self.力量,self.智力))

    def 站街智力(self):
        return self.站街力量()

    def 面板力量(self):
        return max(super().面板力量(), super().面板智力())
      
    def 面板智力(self):
        return self.面板力量()

    def 技能释放次数计算(self):
        技能释放次数 = []
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if self.次数输入[self.技能序号[i.名称]] == '/CD':
                    技能释放次数.append(int((self.时间输入 - i.演出时间) / i.等效CD(self.武器类型,self.类型) + 1 + i.基础释放次数))
                elif self.次数输入[self.技能序号[i.名称]] != '0':
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]]))
                else:
                    技能释放次数.append(0)
            else:
                技能释放次数.append(0)

        if '闪击碎霸' in [self.护石第一栏, self.护石第二栏, self.护石第三栏]:
            技能释放次数[self.技能序号['碎霸']] += 技能释放次数[self.技能序号['闪击碎霸']]
            
        return 技能释放次数

    def 武器基础(self):
        temp = 装备列表[装备序号[self.装备栏[11]]]

        self.力量 += temp.力量
        self.智力 += temp.智力
        self.物理攻击力 += temp.物理攻击力
        self.魔法攻击力 += temp.物理攻击力
        self.独立攻击力 += temp.独立攻击力

        if temp.所属套装 != '智慧产物':
            self.物理攻击力 += 武器计算(temp.等级,temp.品质,self.强化等级[11],self.武器类型,'物理')
            self.魔法攻击力 += 武器计算(temp.等级,temp.品质,self.强化等级[11],self.武器类型,'物理')
            self.独立攻击力 += 锻造计算(temp.等级,temp.品质,self.武器锻造等级)

class 知源·战斗法师(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 知源·战斗法师角色属性()
        self.角色属性A = 知源·战斗法师角色属性()
        self.角色属性B = 知源·战斗法师角色属性()
        self.一觉序号 = 知源·战斗法师一觉序号
        self.二觉序号 = 知源·战斗法师二觉序号
        self.三觉序号 = 知源·战斗法师三觉序号
        self.护石选项 = deepcopy(知源·战斗法师护石选项)
        self.符文选项 = deepcopy(知源·战斗法师符文选项)

    def 界面(self):
        super().界面()
        self.碎霸概率=MyQComboBox(self.main_frame2)
        self.碎霸概率.resize(130,20)
        self.碎霸概率.move(320,450)
        for i in range(11):
            self.碎霸概率.addItem('歼灵灭魂矛：' + str(i * 10) + '%')
        self.碎霸概率.setCurrentIndex(1)

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        属性.技能栏[属性.技能序号['碎霸']].触发概率 = round(self.碎霸概率.currentIndex() / 10, 2)

