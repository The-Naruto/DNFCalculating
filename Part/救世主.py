﻿from PublicReference.base import *

# 主动技能，单段攻击
class 救世主技能0(主动技能):
    名称 = '罪业加身'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 46
    数据 = [0, 2014, 2220, 2424, 2628, 2832, 3037, 3242, 3446, 3651, 3854, 4059, 4263, 4468, 4672, 4877, 5080, 5285, 5492, 5695, 5900, 6104, 6308, 6514, 6718, 6922, 7126, 7331, 7535, 7740, 7944, 8148, 8352, 8557, 8762, 8966, 9171, 9374, 9579, 9784, 9989, 10194, 10398, 10602, 10807, 11012, 11215, 11420, 11623, 11829, 12034, 12237, 12442, 12646, 12851, 13055, 13260, 13463, 13668, 13872, 14077]
    攻击次数 = 1
    CD = 6.0
    TP成长 = 0.08
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] * self.攻击次数 ) * (1 + self.TP成长 * self.TP等级) * self.倍率

# 主动技能，二段攻击
class 救世主技能1(主动技能):
    名称 = '双重切割'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据1 = [0, 1065, 1172, 1280, 1387, 1497, 1605, 1712, 1821, 1928, 2038, 2145, 2253, 2360, 2468, 2576, 2685, 2792, 2901, 3009, 3117, 3224, 3333, 3440, 3549, 3657, 3764, 3873, 3982, 4090, 4197, 4305, 4412, 4522, 4629, 4737, 4844, 4953, 5061, 5170, 5277, 5385, 5493, 5601, 5709, 5816, 5926, 6034, 6142, 6249, 6357, 6466, 6574, 6681, 6789, 6896, 7007, 7114, 7222, 7329, 7437]
    攻击次数1 = 1
    数据2 = [0, 1597, 1758, 1920, 2084, 2245, 2406, 2570, 2731, 2893, 3055, 3216, 3379, 3542, 3703, 3864, 4028, 4189, 4351, 4515, 4675, 4837, 5000, 5162, 5324, 5486, 5647, 5810, 5973, 6133, 6295, 6457, 6620, 6782, 6942, 7106, 7268, 7429, 7593, 7754, 7915, 8078, 8241, 8402, 8564, 8726, 8888, 9051, 9212, 9373, 9537, 9699, 9860, 10022, 10185, 10346, 10509, 10672, 10832, 10995, 11157]
    攻击次数2 = 1
    CD = 6.0
    TP成长 = 0.1
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

# 武器精通，被动技能，满级前成长为1%，满级后2%
class 救世主技能2(被动技能):
    名称 = '负罪者镰刀精通'
    所在等级 = 15
    等级上限 = 30
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 <= 20:
            return round(1.05 + 0.01 * self.等级, 5)
        else:
            return round(0.85 + 0.02 * self.等级, 5)
    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 <= 20:
            return round(1.05 + 0.01 * self.等级, 5)
        else:
            return round(0.85 + 0.02 * self.等级, 5)

# 被动技能，满级前成长为1%，满级后2%
class 救世主技能3(被动技能):
    名称 = '罪业诱惑'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 * self.等级, 5)

# 主动技能，二段攻击
class 救世主技能4(主动技能):
    名称 = '断头台'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据1 = [0, 1648, 1815, 1982, 2150, 2316, 2483, 2651, 2818, 2985, 3153, 3320, 3487, 3654, 3821, 3988, 4156, 4323, 4490, 4658, 4825, 4991, 5159, 5326, 5493, 5661, 5828, 5995, 6162, 6329, 6496, 6664, 6831, 6998, 7166, 7333, 7499, 7667, 7834, 8001, 8169, 8336, 8503, 8671, 8837, 9004, 9172, 9339, 9506, 9674, 9841, 10007, 10175, 10342, 10509, 10677, 10844, 11011, 11179, 11345, 11512]
    攻击次数1 = 1
    数据2 = [0, 2534, 2791, 3049, 3305, 3563, 3820, 4077, 4334, 4592, 4848, 5106, 5363, 5620, 5877, 6134, 6391, 6649, 6905, 7163, 7420, 7677, 7934, 8192, 8448, 8706, 8963, 9220, 9477, 9735, 9991, 10249, 10506, 10762, 11020, 11276, 11534, 11791, 12048, 12305, 12563, 12819, 13077, 13334, 13591, 13848, 14106, 14362, 14620, 14877, 15134, 15391, 15649, 15905, 16163, 16419, 16677, 16934, 17191, 17448, 17706]
    攻击次数2 = 1
    CD =8.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

# 主动技能，二段攻击
class 救世主技能5(主动技能):
    名称 = '欲望之手'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据1 = [0, 1632, 1796, 1962, 2128, 2293, 2459, 2625, 2790, 2956, 3122, 3287, 3452, 3618, 3784, 3949, 4115, 4280, 4446, 4612, 4777, 4943, 5108, 5274, 5439, 5605, 5770, 5936, 6103, 6267, 6433, 6599, 6765, 6929, 7094, 7260, 7426, 7593, 7757, 7923, 8088, 8255, 8421, 8584, 8750, 8916, 9082, 9248, 9413, 9578, 9745, 9911, 10074, 10240, 10406, 10572, 10738, 10903, 11068, 11235, 11401]
    攻击次数1 = 1
    数据2 = [0, 2580, 2841, 3104, 3366, 3627, 3889, 4151, 4412, 4675, 4936, 5199, 5459, 5722, 5984, 6246, 6507, 6769, 7031, 7294, 7554, 7817, 8078, 8340, 8602, 8864, 9126, 9387, 9649, 9911, 10172, 10435, 10696, 10959, 11219, 11482, 11744, 12006, 12267, 12529, 12791, 13054, 13314, 13577, 13836, 14099, 14361, 14623, 14884, 15146, 15408, 15670, 15931, 16194, 16455, 16718, 16978, 17241, 17503, 17764, 18026]
    攻击次数2 = 1
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

# 主动技能，单段攻击
class 救世主技能6(主动技能):
    名称 = '傲慢之堕'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 27
    数据 = [0, 4755, 5514, 6272, 7030, 7788, 8547, 9305, 10063, 10821, 11579, 12338, 13096, 13854, 14613, 15370, 16128, 16887, 17646, 18403, 19162, 19920, 20677, 21436, 22195, 22953, 23711, 24470, 25227, 25985, 26744, 27502, 28261, 29019, 29776, 30535, 31292, 32051, 32810, 33569, 34325, 35084, 35843, 36600, 37359, 38118, 38875, 39633, 40391, 41150, 41908, 42666, 43425, 44183, 44940, 45699, 46458, 47215, 47974, 48732, 49490]
    攻击次数 = 1
    CD = 10.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率

# 主动技能，空中4段，落地1段
class 救世主技能7(主动技能):
    名称 = '屠戮回旋斩'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据1 = [0, 828, 911, 995, 1079, 1163, 1247, 1331, 1416, 1500, 1583, 1666, 1752, 1835, 1919, 2002, 2088, 2171, 2255, 2339, 2424, 2507, 2590, 2674, 2758, 2844, 2927, 3011, 3095, 3179, 3262, 3347, 3431, 3515, 3599, 3684, 3767, 3850, 3935, 4019, 4103, 4186, 4270, 4355, 4439, 4523, 4607, 4691, 4774, 4858, 4941, 5027, 5111, 5195, 5278, 5363, 5446, 5529, 5615, 5699, 5782]
    攻击次数1 = 4
    数据2 = [0, 3311, 3648, 3984, 4319, 4655, 4991, 5327, 5663, 5998, 6334, 6670, 7006, 7343, 7678, 8015, 8350, 8685, 9022, 9357, 9694, 10029, 10365, 10701, 11038, 11373, 11710, 12044, 12381, 12718, 13053, 13390, 13726, 14062, 14397, 14733, 15069, 15405, 15741, 16077, 16412, 16748, 17085, 17420, 17757, 18093, 18428, 18764, 19099, 19436, 19772, 20108, 20443, 20780, 21115, 21452, 21788, 22124, 22461, 22795, 23132]
    攻击次数2 = 1
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

# 主动技能，单段攻击
class 救世主技能8(主动技能):
    名称 = '怠惰之息'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据 = [0, 7117, 7839, 8560, 9282, 10004, 10726, 11448, 12172, 12894, 13615, 14337, 15059, 15781, 16503, 17225, 17948, 18670, 19391, 20113, 20835, 21557, 22279, 23001, 23724, 24446, 25167, 25889, 26611, 27333, 28055, 28777, 29500, 30222, 30943, 31665, 32387, 33109, 33831, 34553, 35276, 35997, 36720, 37442, 38164, 38886, 39608, 40330, 41053, 41774, 42496, 43218, 43940, 44662, 45384, 46106, 46829, 47550, 48272, 48994, 49716]
    攻击次数 = 1
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率

# 主动技能，二段攻击
class 救世主技能9(主动技能):
    名称 = '诱魔之手'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [0, 2655, 2925, 3194, 3463, 3733, 4003, 4272, 4542, 4811, 5081, 5350, 5619, 5889, 6158, 6427, 6697, 6966, 7235, 7506, 7775, 8045, 8314, 8583, 8853, 9122, 9391, 9661, 9930, 10199, 10469, 10739, 11009, 11278, 11547, 11817, 12086, 12355, 12625, 12894, 13163, 13433, 13702, 13971, 14242, 14511, 14781, 15050, 15319, 15589, 15858, 16127, 16397, 16666, 16935, 17205, 17474, 17745, 18014, 18283, 18553]
    攻击次数1 = 1
    数据2 = [0, 6196, 6825, 7454, 8083, 8712, 9341, 9968, 10597, 11226, 11855, 12484, 13113, 13742, 14369, 14998, 15627, 16256, 16885, 17514, 18141, 18770, 19399, 20028, 20657, 21286, 21915, 22542, 23171, 23800, 24429, 25058, 25687, 26315, 26943, 27572, 28201, 28830, 29459, 30088, 30716, 31344, 31973, 32602, 33231, 33860, 34488, 35116, 35745, 36374, 37003, 37632, 38261, 38889, 39517, 40146, 40775, 41404, 42033, 42661, 43290]
    攻击次数2 = 1
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

# 主动技能，基础攻击段数为9
# 带魔界大战护石22段，减伤50.6%，护石倍率22/9*0.494=1.207555，护石减少15%冷却
# 带圣痕护石22段，减伤46.7%，护石倍率22/9*0.533=1.302888，护石减少15%冷却
class 救世主技能10(主动技能):
    名称 = '贪婪之刺'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据 = [0, 868, 955, 1045, 1132, 1220, 1308, 1396, 1483, 1573, 1661, 1748, 1837, 1924, 2012, 2102, 2190, 2277, 2366, 2454, 2541, 2630, 2718, 2806, 2893, 2982, 3069, 3157, 3245, 3334, 3422, 3510, 3598, 3685, 3775, 3863, 3951, 4039, 4127, 4214, 4303, 4391, 4479, 4568, 4655, 4743, 4831, 4919, 5006, 5096, 5183, 5271, 5361, 5448, 5536, 5625, 5713, 5800, 5889, 5976, 6064]
    攻击次数 = 9
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 22/9*0.494
            self.CD *= 0.85
        elif x == 1:
            self.攻击次数 *= 22/9*0.533
            self.CD *= 0.85
        
    def 等效百分比(self, 武器类型):
            return (self.数据[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率

# 主动技能，基础攻击段数为9
# 带魔界大战护石15段，减伤26.56%，护石倍率15/9*0.7344=1.224
# 带圣痕护石15段，减伤21.12%，护石倍率15/9*0.7888=1.31466
class 救世主技能11(主动技能):
    名称 = '杀戮战镰'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据 = [0, 1281, 1412, 1542, 1672, 1801, 1931, 2061, 2192, 2322, 2452, 2581, 2712, 2842, 2973, 3102, 3232, 3363, 3493, 3624, 3753, 3883, 4012, 4143, 4273, 4403, 4532, 4663, 4793, 4923, 5053, 5183, 5313, 5444, 5573, 5704, 5833, 5964, 6094, 6224, 6353, 6483, 6613, 6744, 6873, 7004, 7133, 7264, 7395, 7524, 7655, 7784, 7915, 8045, 8175, 8305, 8435, 8564, 8695, 8824, 8955]
    攻击次数 = 9
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 15/9*0.7344
        elif x == 1:
            self.攻击次数 *= 15/9* 0.7888

    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率

# 主动技能，单段攻击
# 带魔界大战护石增伤23%，护石倍率1+0.23=1.23
# 带圣痕护石增伤31%，护石倍率1+0.31=1.31
class 救世主技能12(主动技能):
    名称 = '愤怒之袭'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    数据 = [0, 19881, 21897, 23914, 25931, 27949, 29965, 31981, 33999, 36016, 38032, 40050, 42067, 44083, 46101, 48117, 50134, 52152, 54168, 56185, 58203, 60219, 62236, 64252, 66270, 68287, 70303, 72320, 74338, 76354, 78371, 80388, 82405, 84423, 86439, 88455, 90474, 92490, 94506, 96523, 98541, 100557, 102574, 104591, 106608, 108625, 110642, 112659, 114676, 116692, 118710, 120726, 122743, 124761, 126777, 128793, 130812, 132828, 134844, 136862, 138879]
    攻击次数 = 1
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 1.23
        elif x == 1:
            self.攻击次数 *= 1.31
        
    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率

# 主动技能，一觉主动，多段攻击为15段多段伤害+1段爆炸伤害
class 救世主技能13(主动技能):
    名称 = '净化之花'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据1 = [0, 735, 905, 1075, 1246, 1416, 1588, 1757, 1928, 2098, 2270, 2439, 2611, 2780, 2952, 3122, 3293, 3462, 3633, 3805, 3975, 4145, 4316, 4485, 4657, 4827, 4998, 5168, 5340, 5509, 5680, 5850, 6019, 6192, 6362, 6532, 6702, 6874, 7043, 7215, 7385]
    攻击次数1 = 15
    数据2 = [0, 45069, 55518, 65969, 76421, 86871, 97321, 107773, 118223, 128673, 139125, 149575, 160026, 170477, 180929, 191379, 201830, 212282, 222731, 233182, 243634, 254083, 264533, 274986, 285435, 295885, 306338, 316787, 327237, 337690, 348139, 358591, 369042, 379491, 389943, 400394, 410843, 421295, 431746, 442195, 452647]
    攻击次数2 = 1
    CD = 140
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * self.倍率

# 被动技能，一觉被动，每级2%成长
class 救世主技能14(被动技能):
    名称 = '罪业宣告'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.04+0.02 * self.等级, 5)

# 主动技能，二段攻击，第一段为无伤害判定
# 带魔界大战护石增伤19%，护石倍率1+0.19=1.19
# 带圣痕护石增伤28%，护石倍率1+0.28=1.28
class 救世主技能15(主动技能):
    名称 = '嫉妒之吻'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    数据 = [0, 19205, 21155, 23102, 25051, 26999, 28947, 30895, 32844, 34792, 36741, 38690, 40638, 42587, 44534, 46483, 48431, 50381, 52328, 54277, 56225, 58174, 60121, 62070, 64019, 65968, 67916, 69864, 71813, 73760, 75709, 77657, 79607, 81554, 83503, 85452, 87400, 89348, 91296, 93246, 95194]
    攻击次数 = 1
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 1.19
        elif x == 1:
            self.攻击次数 *= 1.28

    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率

# 主动技能，吸收为最高8段攻击，释放为4段
# 带魔界大战护石吸收段数锁定4段，伤害+200%（换算为伤害不变，段数12段（0.5*3*8=12））；释放伤害+8%（换算为伤害不变，段数4.32段（1.08*4=4.32）
# 带圣痕护石吸收段数锁定4段，伤害+200%（换算为伤害不变，段数12段（0.5*3*8=12））；释放伤害+18%（换算为伤害不变，段数4.72段（1.18*4=4.72）
class 救世主技能16(主动技能):
    名称 = '暴食之噬'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据1 = [0, 810, 893, 974, 1057, 1139, 1222, 1303, 1386, 1468, 1551, 1632, 1715, 1797, 1879, 1961, 2044, 2127, 2209, 2291, 2374, 2455, 2538, 2620, 2703, 2784, 2867, 2949, 3032, 3113, 3196, 3278, 3359, 3442, 3524, 3607, 3688, 3771, 3853, 3935, 4017]
    攻击次数1 = 8
    数据2 = [0, 6485, 7143, 7801, 8460, 9118, 9776, 10433, 11091, 11749, 12407, 13066, 13723, 14381, 15039, 15698, 16355, 17012, 17672, 18330, 18987, 19645, 20304, 20962, 21620, 22277, 22936, 23593, 24251, 24908, 25567, 26225, 26883, 27542, 28200, 28858, 29516, 30173, 30831, 31489, 32147]
    攻击次数2 = 4
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 12
            self.攻击次数2 = 4.32
        elif x == 1:
            self.攻击次数1 = 12
            self.攻击次数2 = 4.72
            
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

# 主动技能，二段攻击
# 带圣痕护石增伤29%，护石倍率1+0.29=1.29
class 救世主技能17(主动技能):
    名称 = '灵魂烙印：原罪冲击'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据1 = [0, 9308, 10254, 11198, 12143, 13088, 14032, 14977, 15920, 16863, 17810, 18754, 19698, 20643, 21587, 22532, 23477, 24420, 25366, 26310, 27254, 28200, 29144, 30089, 31032, 31975, 32920, 33867, 34810, 35755, 36699, 37644, 38587, 39532, 40477, 41422, 42366, 43311, 44255, 45199, 46144]
    攻击次数1 = 1
    数据2 = [0, 37237, 41016, 44794, 48572, 52350, 56128, 59905, 63684, 67462, 71241, 75017, 78796, 82574, 86352, 90130, 93908, 97685, 101463, 105242, 109018, 112797, 116575, 120352, 124131, 127908, 131686, 135464, 139243, 143021, 146798, 150576, 154355, 158132, 161909, 165687, 169465, 173243, 177022, 180798, 184577]
    攻击次数2 = 1
    CD = 40
    是否有护石 = 1
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * self.倍率
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 *= 1.29
            self.攻击次数2 *= 1.29
            self.CD *= 0.9

# 单段技能，由75被动拆分，固定冷却时间2s，此处添加演出时间减少释放次数
class 救世主技能18(主动技能):
    名称 = '（光辉）智慧起源：原罪结晶'
    所在等级 = 75
    等级上限 = 0
    基础等级 = 0
    数据 = [0, 3793, 4398, 5004, 5608, 6213, 6818, 7422, 8028, 8632, 9237, 9842, 10447, 11052, 11657, 12261, 12867, 13471, 14076, 14681, 15286, 15891, 16495, 17100, 17705, 18310, 18915, 19520, 20124, 20730, 21334, 21939, 22544, 23149, 23754, 24358, 24963, 25568, 26173, 26778, 27383]
    攻击次数 = 1
    CD = 2
    演出时间 = 2
    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] * self.攻击次数) * self.倍率
    def 等效CD(self, 武器类型):
        return 2

# 被动技能，由75被动拆分，每级成长2%
class 救世主技能19(被动技能):
    名称 = '智慧起源：原罪结晶'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)

# 主动技能，刺击为单段伤害，散开为三段伤害。散开伤害根据罪业层数每层+3%，罪业层数最高为7，即散开为3*1.21段伤害
# 带圣痕护石散开部分伤害增加54%，换算为攻击次数2 *= 1.54
class 救世主技能20(主动技能):
    名称 = '肋骨重塑：原罪战矛'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    数据1 = [0, 28618, 31521, 34422, 37326, 40229, 43133, 46036, 48940, 51843, 54746, 57649, 60552, 63456, 66359, 69262, 72166, 75068, 77972, 80874, 83777, 86681, 89584, 92488, 95391, 98295, 101198, 104100, 107004, 109907, 112811, 115713, 118616, 121520, 124423, 127326, 130229, 133133, 136036, 138939, 141843]
    攻击次数1 = 1
    数据2 = [0, 9539, 10506, 11474, 12441, 13409, 14378, 15345, 16313, 17281, 18248, 19216, 20183, 21152, 22120, 23087, 24055, 25023, 25990, 26958, 27925, 28894, 29862, 30829, 31797, 32765, 33732, 34700, 35668, 36636, 37604, 38570, 39538, 40506, 41473, 42442, 43409, 44377, 45345, 46312, 47280]
    攻击次数2 = 3*1.21
    CD = 45.0
    是否有护石 = 1
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * self.倍率
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 1
            self.攻击次数2 *= 1.54

# 主动技能，二觉主动，三段攻击
class 救世主技能21(主动技能):
    名称 = '失乐园'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    数据1 = [0, 20182, 24863, 29543, 34223, 38904, 43584, 48265, 52944, 57624, 62306, 66987, 71666, 76347, 81027, 85706, 90387, 95068, 99748, 104428, 109108, 113789, 118469, 123149, 127830, 132510, 137189, 141870, 146550, 151231, 155911, 160591, 165271, 169951, 174631, 179312, 183993, 188672, 193353, 198033, 202712]
    攻击次数1 = 1
    数据2 = [0, 40367, 49727, 59089, 68449, 77809, 87170, 96531, 105890, 115251, 124612, 133971, 143333, 152693, 162054, 171414, 180774, 190135, 199495, 208856, 218216, 227579, 236938, 246299, 255660, 265019, 274380, 283741, 293102, 302461, 311823, 321183, 330543, 339904, 349265, 358624, 367985, 377346, 386706, 396067, 405427]
    攻击次数2 = 1
    数据3 = [0, 74006, 91167, 108328, 125489, 142649, 159812, 176972, 194132, 211294, 228455, 245616, 262776, 279938, 297099, 314259, 331421, 348582, 365743, 382903, 400065, 417226, 434386, 451549, 468709, 485869, 503030, 520192, 537353, 554513, 571675, 588836, 605996, 623157, 640319, 657479, 674640, 691802, 708963, 726122, 743286]
    攻击次数3 = 1
    CD = 180.0
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * self.倍率

#被动技能，二觉被动，成长2%
class 救世主技能22(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

#主动技能
class 救世主技能23(被动技能):
     名称 = '超卓之心'
     所在等级 = 95
     等级上限 = 11
     基础等级 = 1
     def 加成倍率(self, 武器类型):
         if self.等级 == 0:
             return 1.0
         else:
             return round(1.045 + 0.005 * self.等级, 5)

#主动技能
class 救世主技能24(被动技能):
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


救世主技能列表 = []
i = 0
while i >= 0:
    try:
        exec('救世主技能列表.append(救世主技能'+str(i)+'())')
        i += 1
    except:
        i = -1

救世主技能序号 = dict()
for i in range(len(救世主技能列表)):
    救世主技能序号[救世主技能列表[i].名称] = i

救世主一觉序号 = 0
救世主二觉序号 = 0
救世主三觉序号 = 0
for i in 救世主技能列表:
    if i.所在等级 == 50:
        救世主一觉序号 = 救世主技能序号[i.名称]
    if i.所在等级 == 85:
        救世主二觉序号 = 救世主技能序号[i.名称]
    if i.所在等级 == 100:
        救世主三觉序号 = 救世主技能序号[i.名称]

救世主护石选项 = ['无']
for i in 救世主技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        救世主护石选项.append(i.名称)

救世主符文选项 = ['无']
for i in 救世主技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        救世主符文选项.append(i.名称)

class 救世主角色属性(角色属性):

    实际名称 = '救世主'
    角色 = '圣职者(女)'
    职业 = '诱魔者'

    武器选项 = ['镰刀']
    
    伤害类型选择 = ['魔法百分比']
    
    伤害类型 = '魔法百分比'
    防具类型 = '重甲'
    防具精通属性 = ['智力']

    主BUFF = 2.01
    BUFF属强 = 0

    远古记忆 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(救世主技能列表)
        self.技能序号= deepcopy(救世主技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['（光辉）智慧起源：原罪结晶']].等级 = self.技能栏[self.技能序号['智慧起源：原罪结晶']].等级

    def 伤害指数计算(self):
        self.所有属性强化(self.BUFF属强)
        super().伤害指数计算()

class 救世主(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 救世主角色属性()
        self.角色属性A = 救世主角色属性()
        self.角色属性B = 救世主角色属性()
        self.一觉序号 = 救世主一觉序号
        self.二觉序号 = 救世主二觉序号
        self.三觉序号 = 救世主三觉序号
        self.护石选项 = deepcopy(救世主护石选项)
        self.符文选项 = deepcopy(救世主符文选项)

    def 护石判断(self):
        sign = 0
        for x in range(3):
            if self.护石栏[x].currentText() == '暴食之噬':
                sign = 1
        if sign == 1:
            self.暴食段数选择.setEnabled(False)
            self.暴食段数选择.setStyleSheet(不可选择下拉框样式)
        else:
            self.暴食段数选择.setEnabled(True)
            self.暴食段数选择.setStyleSheet(下拉框样式)

    def 界面(self):
        super().界面()

        self.BUFF.move(self.BUFF.x() - 18, self.BUFF.y())
        self.BUFF输入.move(self.BUFF输入.x() - 20, self.BUFF输入.y())
        self.BUFF输入.resize(40, 25)
        self.BUFF输入.setToolTip('纯C最高值为101')

        self.BUFF输入2 = QLineEdit(self.main_frame2)
        self.BUFF输入2.setText(str(self.初始属性.BUFF属强))
        self.BUFF输入2.resize(40, 25)
        self.BUFF输入2.move(self.BUFF输入.x() + 45, self.BUFF输入.y())
        self.BUFF输入2.setStyleSheet("QLineEdit{font-size:12px;color:white;background-color:rgba(70,134,197,0.8);border:1px;border-radius:3px} QLineEdit:hover{background-color:rgba(65,105,225,0.8)}")
        self.BUFF输入2.setAlignment(Qt.AlignCenter)
        self.BUFF输入2.setToolTip('七宗罪Buff属强值')

        for i in range(3):
            self.护石栏[i].currentIndexChanged.connect(lambda state: self.护石判断())

        self.净化之花冷却Buff = QCheckBox('净化之花冷却Buff', self.main_frame2)
        self.净化之花冷却Buff.resize(120, 20)
        self.净化之花冷却Buff.move(320, 370)
        self.净化之花冷却Buff.setStyleSheet(复选框样式)

        self.凈化之花多段段数选择=MyQComboBox(self.main_frame2)
        for i in range(16):
            self.凈化之花多段段数选择.addItem('净化之花:' + str(i) + '+1段')
        self.凈化之花多段段数选择.setCurrentIndex(15)
        self.凈化之花多段段数选择.resize(120,20)
        self.凈化之花多段段数选择.move(320,400)

        self.暴食段数选择=MyQComboBox(self.main_frame2)
        for i in range(9):
            self.暴食段数选择.addItem('暴食之噬:' + str(i) + '+4段')
        self.暴食段数选择.setCurrentIndex(8)
        self.暴食段数选择.resize(120,20)
        self.暴食段数选择.move(320,430)

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        if self.净化之花冷却Buff.isChecked():
            属性.技能冷却缩减(1, 48, 0.10)
            属性.技能冷却缩减(55, 100, 0.10)
        
        属性.技能栏[属性.技能序号['净化之花']].攻击次数1 = self.凈化之花多段段数选择.currentIndex()

        if self.暴食段数选择.isEnabled():
            属性.技能栏[属性.技能序号['暴食之噬']].攻击次数1 = self.暴食段数选择.currentIndex()

        try:
            self.BUFF全属强 = int(self.BUFF输入2.text())
        except:
            self.BUFF全属强 = self.初始属性.BUFF属强
        属性.BUFF属强 = self.BUFF全属强