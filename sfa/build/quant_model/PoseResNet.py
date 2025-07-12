# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class PoseResNet(torch.nn.Module):
    def __init__(self):
        super(PoseResNet, self).__init__()
        self.module_0 = py_nndct.nn.Input() #PoseResNet::input_0
        self.module_1 = py_nndct.nn.Module('const') #PoseResNet::PoseResNet/193
        self.module_2 = py_nndct.nn.Module('const') #PoseResNet::PoseResNet/210
        self.module_3 = py_nndct.nn.Module('const') #PoseResNet::594
        self.module_4 = py_nndct.nn.Module('const') #PoseResNet::611
        self.module_5 = py_nndct.nn.Module('const') #PoseResNet::644
        self.module_6 = py_nndct.nn.Module('const') #PoseResNet::661
        self.module_7 = py_nndct.nn.Module('const') #PoseResNet::694
        self.module_8 = py_nndct.nn.Module('const') #PoseResNet::711
        self.module_9 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/188
        self.module_10 = py_nndct.nn.Module('tensor') #PoseResNet::PoseResNet/189
        self.module_11 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/191
        self.module_12 = py_nndct.nn.Module('tensor') #PoseResNet::PoseResNet/192
        self.module_14 = py_nndct.nn.Int() #PoseResNet::PoseResNet/195
        self.module_15 = py_nndct.nn.Int() #PoseResNet::PoseResNet/196
        self.module_16 = py_nndct.nn.Int() #PoseResNet::PoseResNet/197
        self.module_17 = py_nndct.nn.Int() #PoseResNet::PoseResNet/198
        self.module_18 = py_nndct.nn.Int() #PoseResNet::PoseResNet/199
        self.module_19 = py_nndct.nn.Int() #PoseResNet::PoseResNet/200
        self.module_20 = py_nndct.nn.Int() #PoseResNet::PoseResNet/201
        self.module_21 = py_nndct.nn.Int() #PoseResNet::PoseResNet/202
        self.module_22 = py_nndct.nn.Int() #PoseResNet::PoseResNet/203
        self.module_23 = py_nndct.nn.Int() #PoseResNet::PoseResNet/204
        self.module_24 = py_nndct.nn.Int() #PoseResNet::PoseResNet/205
        self.module_25 = py_nndct.nn.Int() #PoseResNet::PoseResNet/206
        self.module_26 = py_nndct.nn.Int() #PoseResNet::PoseResNet/207
        self.module_27 = py_nndct.nn.Int() #PoseResNet::PoseResNet/208
        self.module_28 = py_nndct.nn.Int() #PoseResNet::PoseResNet/209
        self.module_30 = py_nndct.nn.Int() #PoseResNet::PoseResNet/212
        self.module_31 = py_nndct.nn.Int() #PoseResNet::PoseResNet/213
        self.module_32 = py_nndct.nn.Int() #PoseResNet::PoseResNet/214
        self.module_33 = py_nndct.nn.Int() #PoseResNet::PoseResNet/215
        self.module_34 = py_nndct.nn.Int() #PoseResNet::PoseResNet/216
        self.module_35 = py_nndct.nn.Int() #PoseResNet::PoseResNet/217
        self.module_36 = py_nndct.nn.Int() #PoseResNet::PoseResNet/218
        self.module_37 = py_nndct.nn.Int() #PoseResNet::PoseResNet/219
        self.module_38 = py_nndct.nn.Int() #PoseResNet::PoseResNet/220
        self.module_39 = py_nndct.nn.Int() #PoseResNet::PoseResNet/221
        self.module_40 = py_nndct.nn.Int() #PoseResNet::PoseResNet/222
        self.module_41 = py_nndct.nn.Int() #PoseResNet::PoseResNet/223
        self.module_42 = py_nndct.nn.Int() #PoseResNet::PoseResNet/224
        self.module_43 = py_nndct.nn.Int() #PoseResNet::PoseResNet/225
        self.module_44 = py_nndct.nn.Int() #PoseResNet::PoseResNet/226
        self.module_45 = py_nndct.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=[7, 7], stride=[2, 2], padding=[3, 3], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Conv2d[conv1]/input.2
        self.module_47 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/ReLU[relu]/243
        self.module_48 = py_nndct.nn.MaxPool2d(kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], ceil_mode=False) #PoseResNet::PoseResNet/MaxPool2d[maxpool]/input.4
        self.module_49 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[0]/Conv2d[conv1]/input.5
        self.module_51 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[0]/ReLU[relu]/input.7
        self.module_52 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[0]/Conv2d[conv2]/input.8
        self.module_54 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[0]/input.9
        self.module_55 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[0]/ReLU[relu]/input.10
        self.module_56 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[1]/Conv2d[conv1]/input.11
        self.module_58 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[1]/ReLU[relu]/input.13
        self.module_59 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[1]/Conv2d[conv2]/input.14
        self.module_61 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[1]/input.15
        self.module_62 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[1]/ReLU[relu]/input.16
        self.module_63 = py_nndct.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[0]/Conv2d[conv1]/input.17
        self.module_65 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[0]/ReLU[relu]/input.19
        self.module_66 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[0]/Conv2d[conv2]/input.20
        self.module_68 = py_nndct.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=[1, 1], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[0]/Sequential[downsample]/Conv2d[0]/input.21
        self.module_70 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[0]/input.22
        self.module_71 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[0]/ReLU[relu]/input.23
        self.module_72 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[1]/Conv2d[conv1]/input.24
        self.module_74 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[1]/ReLU[relu]/input.26
        self.module_75 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[1]/Conv2d[conv2]/input.27
        self.module_77 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[1]/input.28
        self.module_78 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[1]/ReLU[relu]/input.29
        self.module_79 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[0]/Conv2d[conv1]/input.30
        self.module_81 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[0]/ReLU[relu]/input.32
        self.module_82 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[0]/Conv2d[conv2]/input.33
        self.module_84 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[1, 1], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[0]/Sequential[downsample]/Conv2d[0]/input.34
        self.module_86 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[0]/input.35
        self.module_87 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[0]/ReLU[relu]/input.36
        self.module_88 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[1]/Conv2d[conv1]/input.37
        self.module_90 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[1]/ReLU[relu]/input.39
        self.module_91 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[1]/Conv2d[conv2]/input.40
        self.module_93 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[1]/input.41
        self.module_94 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[1]/ReLU[relu]/input.42
        self.module_95 = py_nndct.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[0]/Conv2d[conv1]/input.43
        self.module_97 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[0]/ReLU[relu]/input.45
        self.module_98 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[0]/Conv2d[conv2]/input.46
        self.module_100 = py_nndct.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=[1, 1], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[0]/Sequential[downsample]/Conv2d[0]/input.47
        self.module_102 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[0]/input.48
        self.module_103 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[0]/ReLU[relu]/input.49
        self.module_104 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[1]/Conv2d[conv1]/input.50
        self.module_106 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[1]/ReLU[relu]/input.52
        self.module_107 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[1]/Conv2d[conv2]/input.53
        self.module_109 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[1]/input.54
        self.module_110 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[1]/ReLU[relu]/input.55
        self.module_111 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/587
        self.module_112 = py_nndct.nn.Module('tensor') #PoseResNet::PoseResNet/588
        self.module_113 = py_nndct.nn.Module('cast') #PoseResNet::PoseResNet/593
        self.module_114 = py_nndct.nn.Module('mul') #PoseResNet::PoseResNet/595
        self.module_115 = py_nndct.nn.Module('cast') #PoseResNet::PoseResNet/600
        self.module_116 = py_nndct.nn.Module('floor') #PoseResNet::PoseResNet/601
        self.module_117 = py_nndct.nn.Int() #PoseResNet::PoseResNet/602
        self.module_118 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/604
        self.module_119 = py_nndct.nn.Module('tensor') #PoseResNet::PoseResNet/605
        self.module_120 = py_nndct.nn.Module('cast') #PoseResNet::PoseResNet/610
        self.module_121 = py_nndct.nn.Module('mul') #PoseResNet::PoseResNet/612
        self.module_122 = py_nndct.nn.Module('cast') #PoseResNet::PoseResNet/617
        self.module_123 = py_nndct.nn.Module('floor') #PoseResNet::PoseResNet/618
        self.module_124 = py_nndct.nn.Int() #PoseResNet::PoseResNet/619
        self.module_125 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/622
        self.module_126 = py_nndct.nn.Cat() #PoseResNet::PoseResNet/input.56
        self.module_127 = py_nndct.nn.Conv2d(in_channels=768, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Conv2d[conv_up_level1]/input.57
        self.module_128 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/637
        self.module_129 = py_nndct.nn.Module('tensor') #PoseResNet::PoseResNet/638
        self.module_130 = py_nndct.nn.Module('cast') #PoseResNet::PoseResNet/643
        self.module_131 = py_nndct.nn.Module('mul') #PoseResNet::PoseResNet/645
        self.module_132 = py_nndct.nn.Module('cast') #PoseResNet::PoseResNet/650
        self.module_133 = py_nndct.nn.Module('floor') #PoseResNet::PoseResNet/651
        self.module_134 = py_nndct.nn.Int() #PoseResNet::PoseResNet/652
        self.module_135 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/654
        self.module_136 = py_nndct.nn.Module('tensor') #PoseResNet::PoseResNet/655
        self.module_137 = py_nndct.nn.Module('cast') #PoseResNet::PoseResNet/660
        self.module_138 = py_nndct.nn.Module('mul') #PoseResNet::PoseResNet/662
        self.module_139 = py_nndct.nn.Module('cast') #PoseResNet::PoseResNet/667
        self.module_140 = py_nndct.nn.Module('floor') #PoseResNet::PoseResNet/668
        self.module_141 = py_nndct.nn.Int() #PoseResNet::PoseResNet/669
        self.module_142 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/input.61
        self.module_143 = py_nndct.nn.Cat() #PoseResNet::PoseResNet/input.58
        self.module_144 = py_nndct.nn.Conv2d(in_channels=384, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Conv2d[conv_up_level2]/input.59
        self.module_145 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/687
        self.module_146 = py_nndct.nn.Module('tensor') #PoseResNet::PoseResNet/688
        self.module_147 = py_nndct.nn.Module('cast') #PoseResNet::PoseResNet/693
        self.module_148 = py_nndct.nn.Module('mul') #PoseResNet::PoseResNet/695
        self.module_149 = py_nndct.nn.Module('cast') #PoseResNet::PoseResNet/700
        self.module_150 = py_nndct.nn.Module('floor') #PoseResNet::PoseResNet/701
        self.module_151 = py_nndct.nn.Int() #PoseResNet::PoseResNet/702
        self.module_152 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/704
        self.module_153 = py_nndct.nn.Module('tensor') #PoseResNet::PoseResNet/705
        self.module_154 = py_nndct.nn.Module('cast') #PoseResNet::PoseResNet/710
        self.module_155 = py_nndct.nn.Module('mul') #PoseResNet::PoseResNet/712
        self.module_156 = py_nndct.nn.Module('cast') #PoseResNet::PoseResNet/717
        self.module_157 = py_nndct.nn.Module('floor') #PoseResNet::PoseResNet/718
        self.module_158 = py_nndct.nn.Int() #PoseResNet::PoseResNet/719
        self.module_159 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/input.64
        self.module_160 = py_nndct.nn.Cat() #PoseResNet::PoseResNet/input.60
        self.module_161 = py_nndct.nn.Conv2d(in_channels=192, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Conv2d[conv_up_level3]/input.67
        self.module_162 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn0_hm_cen]/Conv2d[0]/input.62
        self.module_163 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn0_hm_cen]/ReLU[1]/input.63
        self.module_164 = py_nndct.nn.Conv2d(in_channels=64, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn0_hm_cen]/Conv2d[2]/fpn_out.1
        self.module_165 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/759
        self.module_166 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn1_hm_cen]/Conv2d[0]/input.65
        self.module_167 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn1_hm_cen]/ReLU[1]/input.66
        self.module_168 = py_nndct.nn.Conv2d(in_channels=64, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn1_hm_cen]/Conv2d[2]/fpn_out.2
        self.module_169 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/783
        self.module_170 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn2_hm_cen]/Conv2d[0]/input.68
        self.module_171 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn2_hm_cen]/ReLU[1]/input.69
        self.module_172 = py_nndct.nn.Conv2d(in_channels=64, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn2_hm_cen]/Conv2d[2]/fpn_out.3
        self.module_173 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/fpn_out.4
        self.module_174 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/809
        self.module_175 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/811
        self.module_176 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/813
        self.module_177 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/815
        self.module_178 = py_nndct.nn.Cat() #PoseResNet::PoseResNet/818
        self.module_179 = py_nndct.nn.Module('reshape') #PoseResNet::PoseResNet/821
        self.module_180 = py_nndct.nn.Module('permute') #PoseResNet::PoseResNet/transposed_outs.1
        self.module_181 = py_nndct.nn.Module('softmax',dim=-1) #PoseResNet::PoseResNet/826
        self.module_182 = py_nndct.nn.Module('elemwise_mul') #PoseResNet::PoseResNet/827
        self.module_183 = py_nndct.nn.Module('sum') #PoseResNet::PoseResNet/831
        self.module_184 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn0_cen_offset]/Conv2d[0]/input.70
        self.module_185 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn0_cen_offset]/ReLU[1]/input.71
        self.module_186 = py_nndct.nn.Conv2d(in_channels=64, out_channels=2, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn0_cen_offset]/Conv2d[2]/fpn_out.5
        self.module_187 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/855
        self.module_188 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn1_cen_offset]/Conv2d[0]/input.72
        self.module_189 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn1_cen_offset]/ReLU[1]/input.73
        self.module_190 = py_nndct.nn.Conv2d(in_channels=64, out_channels=2, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn1_cen_offset]/Conv2d[2]/fpn_out.6
        self.module_191 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/879
        self.module_192 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn2_cen_offset]/Conv2d[0]/input.74
        self.module_193 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn2_cen_offset]/ReLU[1]/input.75
        self.module_194 = py_nndct.nn.Conv2d(in_channels=64, out_channels=2, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn2_cen_offset]/Conv2d[2]/fpn_out.7
        self.module_195 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/fpn_out.8
        self.module_196 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/905
        self.module_197 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/907
        self.module_198 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/909
        self.module_199 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/911
        self.module_200 = py_nndct.nn.Cat() #PoseResNet::PoseResNet/914
        self.module_201 = py_nndct.nn.Module('reshape') #PoseResNet::PoseResNet/917
        self.module_202 = py_nndct.nn.Module('permute') #PoseResNet::PoseResNet/transposed_outs.2
        self.module_203 = py_nndct.nn.Module('softmax',dim=-1) #PoseResNet::PoseResNet/922
        self.module_204 = py_nndct.nn.Module('elemwise_mul') #PoseResNet::PoseResNet/923
        self.module_205 = py_nndct.nn.Module('sum') #PoseResNet::PoseResNet/927
        self.module_206 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn0_direction]/Conv2d[0]/input.76
        self.module_207 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn0_direction]/ReLU[1]/input.77
        self.module_208 = py_nndct.nn.Conv2d(in_channels=64, out_channels=2, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn0_direction]/Conv2d[2]/fpn_out.9
        self.module_209 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/951
        self.module_210 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn1_direction]/Conv2d[0]/input.78
        self.module_211 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn1_direction]/ReLU[1]/input.79
        self.module_212 = py_nndct.nn.Conv2d(in_channels=64, out_channels=2, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn1_direction]/Conv2d[2]/fpn_out.10
        self.module_213 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/975
        self.module_214 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn2_direction]/Conv2d[0]/input.80
        self.module_215 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn2_direction]/ReLU[1]/input.81
        self.module_216 = py_nndct.nn.Conv2d(in_channels=64, out_channels=2, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn2_direction]/Conv2d[2]/fpn_out.11
        self.module_217 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/fpn_out.12
        self.module_218 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/1001
        self.module_219 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/1003
        self.module_220 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/1005
        self.module_221 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/1007
        self.module_222 = py_nndct.nn.Cat() #PoseResNet::PoseResNet/1010
        self.module_223 = py_nndct.nn.Module('reshape') #PoseResNet::PoseResNet/1013
        self.module_224 = py_nndct.nn.Module('permute') #PoseResNet::PoseResNet/transposed_outs.3
        self.module_225 = py_nndct.nn.Module('softmax',dim=-1) #PoseResNet::PoseResNet/1018
        self.module_226 = py_nndct.nn.Module('elemwise_mul') #PoseResNet::PoseResNet/1019
        self.module_227 = py_nndct.nn.Module('sum') #PoseResNet::PoseResNet/1023
        self.module_228 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn0_z_coor]/Conv2d[0]/input.82
        self.module_229 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn0_z_coor]/ReLU[1]/input.83
        self.module_230 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn0_z_coor]/Conv2d[2]/fpn_out.13
        self.module_231 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/1047
        self.module_232 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn1_z_coor]/Conv2d[0]/input.84
        self.module_233 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn1_z_coor]/ReLU[1]/input.85
        self.module_234 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn1_z_coor]/Conv2d[2]/fpn_out.14
        self.module_235 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/1071
        self.module_236 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn2_z_coor]/Conv2d[0]/input.86
        self.module_237 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn2_z_coor]/ReLU[1]/input.87
        self.module_238 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn2_z_coor]/Conv2d[2]/fpn_out.15
        self.module_239 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/fpn_out.16
        self.module_240 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/1097
        self.module_241 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/1099
        self.module_242 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/1101
        self.module_243 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/1103
        self.module_244 = py_nndct.nn.Cat() #PoseResNet::PoseResNet/1106
        self.module_245 = py_nndct.nn.Module('reshape') #PoseResNet::PoseResNet/1109
        self.module_246 = py_nndct.nn.Module('permute') #PoseResNet::PoseResNet/transposed_outs.4
        self.module_247 = py_nndct.nn.Module('softmax',dim=-1) #PoseResNet::PoseResNet/1114
        self.module_248 = py_nndct.nn.Module('elemwise_mul') #PoseResNet::PoseResNet/1115
        self.module_249 = py_nndct.nn.Module('sum') #PoseResNet::PoseResNet/1119
        self.module_250 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn0_dim]/Conv2d[0]/input.88
        self.module_251 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn0_dim]/ReLU[1]/input.89
        self.module_252 = py_nndct.nn.Conv2d(in_channels=64, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn0_dim]/Conv2d[2]/fpn_out.17
        self.module_253 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/1143
        self.module_254 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn1_dim]/Conv2d[0]/input.90
        self.module_255 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn1_dim]/ReLU[1]/input.91
        self.module_256 = py_nndct.nn.Conv2d(in_channels=64, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn1_dim]/Conv2d[2]/fpn_out.18
        self.module_257 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/1167
        self.module_258 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn2_dim]/Conv2d[0]/input.92
        self.module_259 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[fpn2_dim]/ReLU[1]/input
        self.module_260 = py_nndct.nn.Conv2d(in_channels=64, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[fpn2_dim]/Conv2d[2]/fpn_out.19
        self.module_261 = py_nndct.nn.Interpolate() #PoseResNet::PoseResNet/fpn_out
        self.module_262 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/1193
        self.module_263 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/1195
        self.module_264 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/1197
        self.module_265 = py_nndct.nn.Module('shape') #PoseResNet::PoseResNet/1199
        self.module_266 = py_nndct.nn.Cat() #PoseResNet::PoseResNet/1202
        self.module_267 = py_nndct.nn.Module('reshape') #PoseResNet::PoseResNet/1205
        self.module_268 = py_nndct.nn.Module('permute') #PoseResNet::PoseResNet/transposed_outs
        self.module_269 = py_nndct.nn.Module('softmax',dim=-1) #PoseResNet::PoseResNet/1210
        self.module_270 = py_nndct.nn.Module('elemwise_mul') #PoseResNet::PoseResNet/1211
        self.module_271 = py_nndct.nn.Module('sum') #PoseResNet::PoseResNet/1215

    def forward(self, *args):
        self.output_module_0 = self.module_0(input=args[0])
        self.output_module_1 = self.module_1(dtype=torch.long, data=4, device='cpu')
        self.output_module_2 = self.module_2(dtype=torch.long, data=4, device='cpu')
        self.output_module_3 = self.module_3(dtype=torch.float, data=2.0, device='cpu')
        self.output_module_4 = self.module_4(dtype=torch.float, data=2.0, device='cpu')
        self.output_module_5 = self.module_5(dtype=torch.float, data=2.0, device='cpu')
        self.output_module_6 = self.module_6(dtype=torch.float, data=2.0, device='cpu')
        self.output_module_7 = self.module_7(dtype=torch.float, data=2.0, device='cpu')
        self.output_module_8 = self.module_8(dtype=torch.float, data=2.0, device='cpu')
        self.output_module_9 = self.module_9(input=self.output_module_0, dim=2)
        self.output_module_10 = self.module_10(dtype=torch.int, data=self.output_module_9, device='cpu')
        self.output_module_11 = self.module_11(input=self.output_module_0, dim=3)
        self.output_module_12 = self.module_12(dtype=torch.int, data=self.output_module_11, device='cpu')
        self.output_module_13 = self.output_module_10 // self.output_module_1
        self.output_module_14 = self.module_14(input=self.output_module_13)
        self.output_module_15 = self.module_15(input=self.output_module_13)
        self.output_module_16 = self.module_16(input=self.output_module_13)
        self.output_module_17 = self.module_17(input=self.output_module_13)
        self.output_module_18 = self.module_18(input=self.output_module_13)
        self.output_module_19 = self.module_19(input=self.output_module_13)
        self.output_module_20 = self.module_20(input=self.output_module_13)
        self.output_module_21 = self.module_21(input=self.output_module_13)
        self.output_module_22 = self.module_22(input=self.output_module_13)
        self.output_module_23 = self.module_23(input=self.output_module_13)
        self.output_module_24 = self.module_24(input=self.output_module_13)
        self.output_module_25 = self.module_25(input=self.output_module_13)
        self.output_module_26 = self.module_26(input=self.output_module_13)
        self.output_module_27 = self.module_27(input=self.output_module_13)
        self.output_module_28 = self.module_28(input=self.output_module_13)
        self.output_module_29 = self.output_module_12 // self.output_module_2
        self.output_module_30 = self.module_30(input=self.output_module_29)
        self.output_module_31 = self.module_31(input=self.output_module_29)
        self.output_module_32 = self.module_32(input=self.output_module_29)
        self.output_module_33 = self.module_33(input=self.output_module_29)
        self.output_module_34 = self.module_34(input=self.output_module_29)
        self.output_module_35 = self.module_35(input=self.output_module_29)
        self.output_module_36 = self.module_36(input=self.output_module_29)
        self.output_module_37 = self.module_37(input=self.output_module_29)
        self.output_module_38 = self.module_38(input=self.output_module_29)
        self.output_module_39 = self.module_39(input=self.output_module_29)
        self.output_module_40 = self.module_40(input=self.output_module_29)
        self.output_module_41 = self.module_41(input=self.output_module_29)
        self.output_module_42 = self.module_42(input=self.output_module_29)
        self.output_module_43 = self.module_43(input=self.output_module_29)
        self.output_module_44 = self.module_44(input=self.output_module_29)
        self.output_module_45 = self.module_45(self.output_module_0)
        self.output_module_47 = self.module_47(self.output_module_45)
        self.output_module_48 = self.module_48(self.output_module_47)
        self.output_module_49 = self.module_49(self.output_module_48)
        self.output_module_51 = self.module_51(self.output_module_49)
        self.output_module_52 = self.module_52(self.output_module_51)
        self.output_module_54 = self.module_54(input=self.output_module_52, alpha=1, other=self.output_module_48)
        self.output_module_55 = self.module_55(self.output_module_54)
        self.output_module_56 = self.module_56(self.output_module_55)
        self.output_module_58 = self.module_58(self.output_module_56)
        self.output_module_59 = self.module_59(self.output_module_58)
        self.output_module_61 = self.module_61(input=self.output_module_59, alpha=1, other=self.output_module_55)
        self.output_module_62 = self.module_62(self.output_module_61)
        self.output_module_63 = self.module_63(self.output_module_62)
        self.output_module_65 = self.module_65(self.output_module_63)
        self.output_module_66 = self.module_66(self.output_module_65)
        self.output_module_68 = self.module_68(self.output_module_62)
        self.output_module_70 = self.module_70(input=self.output_module_66, alpha=1, other=self.output_module_68)
        self.output_module_71 = self.module_71(self.output_module_70)
        self.output_module_72 = self.module_72(self.output_module_71)
        self.output_module_74 = self.module_74(self.output_module_72)
        self.output_module_75 = self.module_75(self.output_module_74)
        self.output_module_77 = self.module_77(input=self.output_module_75, alpha=1, other=self.output_module_71)
        self.output_module_78 = self.module_78(self.output_module_77)
        self.output_module_79 = self.module_79(self.output_module_78)
        self.output_module_81 = self.module_81(self.output_module_79)
        self.output_module_82 = self.module_82(self.output_module_81)
        self.output_module_84 = self.module_84(self.output_module_78)
        self.output_module_86 = self.module_86(input=self.output_module_82, alpha=1, other=self.output_module_84)
        self.output_module_87 = self.module_87(self.output_module_86)
        self.output_module_88 = self.module_88(self.output_module_87)
        self.output_module_90 = self.module_90(self.output_module_88)
        self.output_module_91 = self.module_91(self.output_module_90)
        self.output_module_93 = self.module_93(input=self.output_module_91, alpha=1, other=self.output_module_87)
        self.output_module_94 = self.module_94(self.output_module_93)
        self.output_module_95 = self.module_95(self.output_module_94)
        self.output_module_97 = self.module_97(self.output_module_95)
        self.output_module_98 = self.module_98(self.output_module_97)
        self.output_module_100 = self.module_100(self.output_module_94)
        self.output_module_102 = self.module_102(input=self.output_module_98, alpha=1, other=self.output_module_100)
        self.output_module_103 = self.module_103(self.output_module_102)
        self.output_module_104 = self.module_104(self.output_module_103)
        self.output_module_106 = self.module_106(self.output_module_104)
        self.output_module_107 = self.module_107(self.output_module_106)
        self.output_module_109 = self.module_109(input=self.output_module_107, alpha=1, other=self.output_module_103)
        self.output_module_110 = self.module_110(self.output_module_109)
        self.output_module_111 = self.module_111(input=self.output_module_110, dim=2)
        self.output_module_112 = self.module_112(dtype=torch.int, data=self.output_module_111, device='cpu')
        self.output_module_113 = self.module_113(input=self.output_module_112, dtype=torch.float)
        self.output_module_114 = self.module_114(input=self.output_module_113, other=self.output_module_3)
        self.output_module_115 = self.module_115(input=self.output_module_114, dtype=torch.float)
        self.output_module_116 = self.module_116(input=self.output_module_115)
        self.output_module_117 = self.module_117(input=self.output_module_116)
        self.output_module_118 = self.module_118(input=self.output_module_110, dim=3)
        self.output_module_119 = self.module_119(dtype=torch.int, data=self.output_module_118, device='cpu')
        self.output_module_120 = self.module_120(input=self.output_module_119, dtype=torch.float)
        self.output_module_121 = self.module_121(input=self.output_module_120, other=self.output_module_4)
        self.output_module_122 = self.module_122(input=self.output_module_121, dtype=torch.float)
        self.output_module_123 = self.module_123(input=self.output_module_122)
        self.output_module_124 = self.module_124(input=self.output_module_123)
        self.output_module_125 = self.module_125(input=self.output_module_110, size=[self.output_module_117,self.output_module_124], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_126 = self.module_126(tensors=[self.output_module_125,self.output_module_94], dim=1)
        self.output_module_127 = self.module_127(self.output_module_126)
        self.output_module_128 = self.module_128(input=self.output_module_127, dim=2)
        self.output_module_129 = self.module_129(dtype=torch.int, data=self.output_module_128, device='cpu')
        self.output_module_130 = self.module_130(input=self.output_module_129, dtype=torch.float)
        self.output_module_131 = self.module_131(input=self.output_module_130, other=self.output_module_5)
        self.output_module_132 = self.module_132(input=self.output_module_131, dtype=torch.float)
        self.output_module_133 = self.module_133(input=self.output_module_132)
        self.output_module_134 = self.module_134(input=self.output_module_133)
        self.output_module_135 = self.module_135(input=self.output_module_127, dim=3)
        self.output_module_136 = self.module_136(dtype=torch.int, data=self.output_module_135, device='cpu')
        self.output_module_137 = self.module_137(input=self.output_module_136, dtype=torch.float)
        self.output_module_138 = self.module_138(input=self.output_module_137, other=self.output_module_6)
        self.output_module_139 = self.module_139(input=self.output_module_138, dtype=torch.float)
        self.output_module_140 = self.module_140(input=self.output_module_139)
        self.output_module_141 = self.module_141(input=self.output_module_140)
        self.output_module_142 = self.module_142(input=self.output_module_127, size=[self.output_module_134,self.output_module_141], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_143 = self.module_143(tensors=[self.output_module_142,self.output_module_78], dim=1)
        self.output_module_144 = self.module_144(self.output_module_143)
        self.output_module_145 = self.module_145(input=self.output_module_144, dim=2)
        self.output_module_146 = self.module_146(dtype=torch.int, data=self.output_module_145, device='cpu')
        self.output_module_147 = self.module_147(input=self.output_module_146, dtype=torch.float)
        self.output_module_148 = self.module_148(input=self.output_module_147, other=self.output_module_7)
        self.output_module_149 = self.module_149(input=self.output_module_148, dtype=torch.float)
        self.output_module_150 = self.module_150(input=self.output_module_149)
        self.output_module_151 = self.module_151(input=self.output_module_150)
        self.output_module_152 = self.module_152(input=self.output_module_144, dim=3)
        self.output_module_153 = self.module_153(dtype=torch.int, data=self.output_module_152, device='cpu')
        self.output_module_154 = self.module_154(input=self.output_module_153, dtype=torch.float)
        self.output_module_155 = self.module_155(input=self.output_module_154, other=self.output_module_8)
        self.output_module_156 = self.module_156(input=self.output_module_155, dtype=torch.float)
        self.output_module_157 = self.module_157(input=self.output_module_156)
        self.output_module_158 = self.module_158(input=self.output_module_157)
        self.output_module_159 = self.module_159(input=self.output_module_144, size=[self.output_module_151,self.output_module_158], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_160 = self.module_160(tensors=[self.output_module_159,self.output_module_62], dim=1)
        self.output_module_161 = self.module_161(self.output_module_160)
        self.output_module_162 = self.module_162(self.output_module_142)
        self.output_module_163 = self.module_163(self.output_module_162)
        self.output_module_164 = self.module_164(self.output_module_163)
        self.output_module_165 = self.module_165(input=self.output_module_164, size=[self.output_module_28,self.output_module_44], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_166 = self.module_166(self.output_module_159)
        self.output_module_167 = self.module_167(self.output_module_166)
        self.output_module_168 = self.module_168(self.output_module_167)
        self.output_module_169 = self.module_169(input=self.output_module_168, size=[self.output_module_27,self.output_module_43], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_170 = self.module_170(self.output_module_161)
        self.output_module_171 = self.module_171(self.output_module_170)
        self.output_module_172 = self.module_172(self.output_module_171)
        self.output_module_173 = self.module_173(input=self.output_module_172, size=[self.output_module_26,self.output_module_42], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_174 = self.module_174(input=self.output_module_165, dim=0)
        self.output_module_175 = self.module_175(input=self.output_module_165, dim=1)
        self.output_module_176 = self.module_176(input=self.output_module_165, dim=2)
        self.output_module_177 = self.module_177(input=self.output_module_165, dim=3)
        self.output_module_178 = self.module_178(tensors=[self.output_module_165,self.output_module_169,self.output_module_173], dim=1)
        self.output_module_179 = self.module_179(input=self.output_module_178, size=[self.output_module_174,self.output_module_175,3,self.output_module_176,self.output_module_177])
        self.output_module_180 = self.module_180(input=self.output_module_179, dims=[0,1,3,4,2])
        self.output_module_181 = self.module_181(self.output_module_180)
        self.output_module_182 = self.module_182(input=self.output_module_180, other=self.output_module_181)
        self.output_module_183 = self.module_183(input=self.output_module_182, keepdim=False, dim=(-1))
        self.output_module_184 = self.module_184(self.output_module_142)
        self.output_module_185 = self.module_185(self.output_module_184)
        self.output_module_186 = self.module_186(self.output_module_185)
        self.output_module_187 = self.module_187(input=self.output_module_186, size=[self.output_module_25,self.output_module_41], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_188 = self.module_188(self.output_module_159)
        self.output_module_189 = self.module_189(self.output_module_188)
        self.output_module_190 = self.module_190(self.output_module_189)
        self.output_module_191 = self.module_191(input=self.output_module_190, size=[self.output_module_24,self.output_module_40], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_192 = self.module_192(self.output_module_161)
        self.output_module_193 = self.module_193(self.output_module_192)
        self.output_module_194 = self.module_194(self.output_module_193)
        self.output_module_195 = self.module_195(input=self.output_module_194, size=[self.output_module_23,self.output_module_39], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_196 = self.module_196(input=self.output_module_187, dim=0)
        self.output_module_197 = self.module_197(input=self.output_module_187, dim=1)
        self.output_module_198 = self.module_198(input=self.output_module_187, dim=2)
        self.output_module_199 = self.module_199(input=self.output_module_187, dim=3)
        self.output_module_200 = self.module_200(tensors=[self.output_module_187,self.output_module_191,self.output_module_195], dim=1)
        self.output_module_201 = self.module_201(input=self.output_module_200, size=[self.output_module_196,self.output_module_197,3,self.output_module_198,self.output_module_199])
        self.output_module_202 = self.module_202(input=self.output_module_201, dims=[0,1,3,4,2])
        self.output_module_203 = self.module_203(self.output_module_202)
        self.output_module_204 = self.module_204(input=self.output_module_202, other=self.output_module_203)
        self.output_module_205 = self.module_205(input=self.output_module_204, keepdim=False, dim=(-1))
        self.output_module_206 = self.module_206(self.output_module_142)
        self.output_module_207 = self.module_207(self.output_module_206)
        self.output_module_208 = self.module_208(self.output_module_207)
        self.output_module_209 = self.module_209(input=self.output_module_208, size=[self.output_module_22,self.output_module_38], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_210 = self.module_210(self.output_module_159)
        self.output_module_211 = self.module_211(self.output_module_210)
        self.output_module_212 = self.module_212(self.output_module_211)
        self.output_module_213 = self.module_213(input=self.output_module_212, size=[self.output_module_21,self.output_module_37], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_214 = self.module_214(self.output_module_161)
        self.output_module_215 = self.module_215(self.output_module_214)
        self.output_module_216 = self.module_216(self.output_module_215)
        self.output_module_217 = self.module_217(input=self.output_module_216, size=[self.output_module_20,self.output_module_36], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_218 = self.module_218(input=self.output_module_209, dim=0)
        self.output_module_219 = self.module_219(input=self.output_module_209, dim=1)
        self.output_module_220 = self.module_220(input=self.output_module_209, dim=2)
        self.output_module_221 = self.module_221(input=self.output_module_209, dim=3)
        self.output_module_222 = self.module_222(tensors=[self.output_module_209,self.output_module_213,self.output_module_217], dim=1)
        self.output_module_223 = self.module_223(input=self.output_module_222, size=[self.output_module_218,self.output_module_219,3,self.output_module_220,self.output_module_221])
        self.output_module_224 = self.module_224(input=self.output_module_223, dims=[0,1,3,4,2])
        self.output_module_225 = self.module_225(self.output_module_224)
        self.output_module_226 = self.module_226(input=self.output_module_224, other=self.output_module_225)
        self.output_module_227 = self.module_227(input=self.output_module_226, keepdim=False, dim=(-1))
        self.output_module_228 = self.module_228(self.output_module_142)
        self.output_module_229 = self.module_229(self.output_module_228)
        self.output_module_230 = self.module_230(self.output_module_229)
        self.output_module_231 = self.module_231(input=self.output_module_230, size=[self.output_module_19,self.output_module_35], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_232 = self.module_232(self.output_module_159)
        self.output_module_233 = self.module_233(self.output_module_232)
        self.output_module_234 = self.module_234(self.output_module_233)
        self.output_module_235 = self.module_235(input=self.output_module_234, size=[self.output_module_18,self.output_module_34], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_236 = self.module_236(self.output_module_161)
        self.output_module_237 = self.module_237(self.output_module_236)
        self.output_module_238 = self.module_238(self.output_module_237)
        self.output_module_239 = self.module_239(input=self.output_module_238, size=[self.output_module_17,self.output_module_33], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_240 = self.module_240(input=self.output_module_231, dim=0)
        self.output_module_241 = self.module_241(input=self.output_module_231, dim=1)
        self.output_module_242 = self.module_242(input=self.output_module_231, dim=2)
        self.output_module_243 = self.module_243(input=self.output_module_231, dim=3)
        self.output_module_244 = self.module_244(tensors=[self.output_module_231,self.output_module_235,self.output_module_239], dim=1)
        self.output_module_245 = self.module_245(input=self.output_module_244, size=[self.output_module_240,self.output_module_241,3,self.output_module_242,self.output_module_243])
        self.output_module_246 = self.module_246(input=self.output_module_245, dims=[0,1,3,4,2])
        self.output_module_247 = self.module_247(self.output_module_246)
        self.output_module_248 = self.module_248(input=self.output_module_246, other=self.output_module_247)
        self.output_module_249 = self.module_249(input=self.output_module_248, keepdim=False, dim=(-1))
        self.output_module_250 = self.module_250(self.output_module_142)
        self.output_module_251 = self.module_251(self.output_module_250)
        self.output_module_252 = self.module_252(self.output_module_251)
        self.output_module_253 = self.module_253(input=self.output_module_252, size=[self.output_module_16,self.output_module_32], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_254 = self.module_254(self.output_module_159)
        self.output_module_255 = self.module_255(self.output_module_254)
        self.output_module_256 = self.module_256(self.output_module_255)
        self.output_module_257 = self.module_257(input=self.output_module_256, size=[self.output_module_15,self.output_module_31], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_258 = self.module_258(self.output_module_161)
        self.output_module_259 = self.module_259(self.output_module_258)
        self.output_module_260 = self.module_260(self.output_module_259)
        self.output_module_261 = self.module_261(input=self.output_module_260, size=[self.output_module_14,self.output_module_30], scale_factor=None, mode='bilinear', align_corners=False)
        self.output_module_262 = self.module_262(input=self.output_module_253, dim=0)
        self.output_module_263 = self.module_263(input=self.output_module_253, dim=1)
        self.output_module_264 = self.module_264(input=self.output_module_253, dim=2)
        self.output_module_265 = self.module_265(input=self.output_module_253, dim=3)
        self.output_module_266 = self.module_266(tensors=[self.output_module_253,self.output_module_257,self.output_module_261], dim=1)
        self.output_module_267 = self.module_267(input=self.output_module_266, size=[self.output_module_262,self.output_module_263,3,self.output_module_264,self.output_module_265])
        self.output_module_268 = self.module_268(input=self.output_module_267, dims=[0,1,3,4,2])
        self.output_module_269 = self.module_269(self.output_module_268)
        self.output_module_270 = self.module_270(input=self.output_module_268, other=self.output_module_269)
        self.output_module_271 = self.module_271(input=self.output_module_270, keepdim=False, dim=(-1))
        return self.output_module_183,self.output_module_205,self.output_module_227,self.output_module_249,self.output_module_271
