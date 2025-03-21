# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class PoseResNet(torch.nn.Module):
    def __init__(self):
        super(PoseResNet, self).__init__()
        self.module_0 = py_nndct.nn.Input() #PoseResNet::input_0
        self.module_1 = py_nndct.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=[7, 7], stride=[2, 2], padding=[3, 3], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Conv2d[conv1]/input.2
        self.module_3 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/ReLU[relu]/175
        self.module_4 = py_nndct.nn.MaxPool2d(kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], ceil_mode=False) #PoseResNet::PoseResNet/MaxPool2d[maxpool]/input.4
        self.module_5 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[0]/Conv2d[conv1]/input.5
        self.module_7 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[0]/ReLU[relu]/input.7
        self.module_8 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[0]/Conv2d[conv2]/input.8
        self.module_10 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[0]/input.9
        self.module_11 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[0]/ReLU[relu]/input.10
        self.module_12 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[1]/Conv2d[conv1]/input.11
        self.module_14 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[1]/ReLU[relu]/input.13
        self.module_15 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[1]/Conv2d[conv2]/input.14
        self.module_17 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[1]/input.15
        self.module_18 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer1]/BasicBlock[1]/ReLU[relu]/input.16
        self.module_19 = py_nndct.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[0]/Conv2d[conv1]/input.17
        self.module_21 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[0]/ReLU[relu]/input.19
        self.module_22 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[0]/Conv2d[conv2]/input.20
        self.module_24 = py_nndct.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=[1, 1], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[0]/Sequential[downsample]/Conv2d[0]/input.21
        self.module_26 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[0]/input.22
        self.module_27 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[0]/ReLU[relu]/input.23
        self.module_28 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[1]/Conv2d[conv1]/input.24
        self.module_30 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[1]/ReLU[relu]/input.26
        self.module_31 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[1]/Conv2d[conv2]/input.27
        self.module_33 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[1]/input.28
        self.module_34 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer2]/BasicBlock[1]/ReLU[relu]/input.29
        self.module_35 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[0]/Conv2d[conv1]/input.30
        self.module_37 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[0]/ReLU[relu]/input.32
        self.module_38 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[0]/Conv2d[conv2]/input.33
        self.module_40 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[1, 1], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[0]/Sequential[downsample]/Conv2d[0]/input.34
        self.module_42 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[0]/input.35
        self.module_43 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[0]/ReLU[relu]/input.36
        self.module_44 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[1]/Conv2d[conv1]/input.37
        self.module_46 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[1]/ReLU[relu]/input.39
        self.module_47 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[1]/Conv2d[conv2]/input.40
        self.module_49 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[1]/input.41
        self.module_50 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer3]/BasicBlock[1]/ReLU[relu]/input.42
        self.module_51 = py_nndct.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[0]/Conv2d[conv1]/input.43
        self.module_53 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[0]/ReLU[relu]/input.45
        self.module_54 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[0]/Conv2d[conv2]/input.46
        self.module_56 = py_nndct.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=[1, 1], stride=[2, 2], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[0]/Sequential[downsample]/Conv2d[0]/input.47
        self.module_58 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[0]/input.48
        self.module_59 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[0]/ReLU[relu]/input.49
        self.module_60 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[1]/Conv2d[conv1]/input.50
        self.module_62 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[1]/ReLU[relu]/input.52
        self.module_63 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[1]/Conv2d[conv2]/input.53
        self.module_65 = py_nndct.nn.Add() #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[1]/input.54
        self.module_66 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[layer4]/BasicBlock[1]/ReLU[relu]/517
        self.module_67 = py_nndct.nn.ConvTranspose2d(in_channels=512, out_channels=256, kernel_size=[4, 4], stride=[2, 2], padding=[1, 1], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #PoseResNet::PoseResNet/Sequential[deconv_layers]/ConvTranspose2d[0]/input.55
        self.module_69 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[deconv_layers]/ReLU[2]/534
        self.module_70 = py_nndct.nn.ConvTranspose2d(in_channels=256, out_channels=256, kernel_size=[4, 4], stride=[2, 2], padding=[1, 1], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #PoseResNet::PoseResNet/Sequential[deconv_layers]/ConvTranspose2d[3]/input.57
        self.module_72 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[deconv_layers]/ReLU[5]/551
        self.module_73 = py_nndct.nn.ConvTranspose2d(in_channels=256, out_channels=256, kernel_size=[4, 4], stride=[2, 2], padding=[1, 1], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #PoseResNet::PoseResNet/Sequential[deconv_layers]/ConvTranspose2d[6]/input.59
        self.module_75 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[deconv_layers]/ReLU[8]/input.61
        self.module_76 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[hm_cen]/Conv2d[0]/input.62
        self.module_77 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[hm_cen]/ReLU[1]/input.63
        self.module_78 = py_nndct.nn.Conv2d(in_channels=64, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[hm_cen]/Conv2d[2]/589
        self.module_79 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[cen_offset]/Conv2d[0]/input.64
        self.module_80 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[cen_offset]/ReLU[1]/input.65
        self.module_81 = py_nndct.nn.Conv2d(in_channels=64, out_channels=2, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[cen_offset]/Conv2d[2]/610
        self.module_82 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[direction]/Conv2d[0]/input.66
        self.module_83 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[direction]/ReLU[1]/input.67
        self.module_84 = py_nndct.nn.Conv2d(in_channels=64, out_channels=2, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[direction]/Conv2d[2]/631
        self.module_85 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[z_coor]/Conv2d[0]/input.68
        self.module_86 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[z_coor]/ReLU[1]/input.69
        self.module_87 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[z_coor]/Conv2d[2]/652
        self.module_88 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[dim]/Conv2d[0]/input.70
        self.module_89 = py_nndct.nn.ReLU(inplace=True) #PoseResNet::PoseResNet/Sequential[dim]/ReLU[1]/input
        self.module_90 = py_nndct.nn.Conv2d(in_channels=64, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #PoseResNet::PoseResNet/Sequential[dim]/Conv2d[2]/673

    def forward(self, *args):
        self.output_module_0 = self.module_0(input=args[0])
        self.output_module_1 = self.module_1(self.output_module_0)
        self.output_module_3 = self.module_3(self.output_module_1)
        self.output_module_4 = self.module_4(self.output_module_3)
        self.output_module_5 = self.module_5(self.output_module_4)
        self.output_module_7 = self.module_7(self.output_module_5)
        self.output_module_8 = self.module_8(self.output_module_7)
        self.output_module_10 = self.module_10(alpha=1, input=self.output_module_8, other=self.output_module_4)
        self.output_module_11 = self.module_11(self.output_module_10)
        self.output_module_12 = self.module_12(self.output_module_11)
        self.output_module_14 = self.module_14(self.output_module_12)
        self.output_module_15 = self.module_15(self.output_module_14)
        self.output_module_17 = self.module_17(alpha=1, input=self.output_module_15, other=self.output_module_11)
        self.output_module_18 = self.module_18(self.output_module_17)
        self.output_module_19 = self.module_19(self.output_module_18)
        self.output_module_21 = self.module_21(self.output_module_19)
        self.output_module_22 = self.module_22(self.output_module_21)
        self.output_module_24 = self.module_24(self.output_module_18)
        self.output_module_26 = self.module_26(alpha=1, input=self.output_module_22, other=self.output_module_24)
        self.output_module_27 = self.module_27(self.output_module_26)
        self.output_module_28 = self.module_28(self.output_module_27)
        self.output_module_30 = self.module_30(self.output_module_28)
        self.output_module_31 = self.module_31(self.output_module_30)
        self.output_module_33 = self.module_33(alpha=1, input=self.output_module_31, other=self.output_module_27)
        self.output_module_34 = self.module_34(self.output_module_33)
        self.output_module_35 = self.module_35(self.output_module_34)
        self.output_module_37 = self.module_37(self.output_module_35)
        self.output_module_38 = self.module_38(self.output_module_37)
        self.output_module_40 = self.module_40(self.output_module_34)
        self.output_module_42 = self.module_42(alpha=1, input=self.output_module_38, other=self.output_module_40)
        self.output_module_43 = self.module_43(self.output_module_42)
        self.output_module_44 = self.module_44(self.output_module_43)
        self.output_module_46 = self.module_46(self.output_module_44)
        self.output_module_47 = self.module_47(self.output_module_46)
        self.output_module_49 = self.module_49(alpha=1, input=self.output_module_47, other=self.output_module_43)
        self.output_module_50 = self.module_50(self.output_module_49)
        self.output_module_51 = self.module_51(self.output_module_50)
        self.output_module_53 = self.module_53(self.output_module_51)
        self.output_module_54 = self.module_54(self.output_module_53)
        self.output_module_56 = self.module_56(self.output_module_50)
        self.output_module_58 = self.module_58(alpha=1, input=self.output_module_54, other=self.output_module_56)
        self.output_module_59 = self.module_59(self.output_module_58)
        self.output_module_60 = self.module_60(self.output_module_59)
        self.output_module_62 = self.module_62(self.output_module_60)
        self.output_module_63 = self.module_63(self.output_module_62)
        self.output_module_65 = self.module_65(alpha=1, input=self.output_module_63, other=self.output_module_59)
        self.output_module_66 = self.module_66(self.output_module_65)
        self.output_module_67 = self.module_67(self.output_module_66)
        self.output_module_69 = self.module_69(self.output_module_67)
        self.output_module_70 = self.module_70(self.output_module_69)
        self.output_module_72 = self.module_72(self.output_module_70)
        self.output_module_73 = self.module_73(self.output_module_72)
        self.output_module_75 = self.module_75(self.output_module_73)
        self.output_module_76 = self.module_76(self.output_module_75)
        self.output_module_77 = self.module_77(self.output_module_76)
        self.output_module_78 = self.module_78(self.output_module_77)
        self.output_module_79 = self.module_79(self.output_module_75)
        self.output_module_80 = self.module_80(self.output_module_79)
        self.output_module_81 = self.module_81(self.output_module_80)
        self.output_module_82 = self.module_82(self.output_module_75)
        self.output_module_83 = self.module_83(self.output_module_82)
        self.output_module_84 = self.module_84(self.output_module_83)
        self.output_module_85 = self.module_85(self.output_module_75)
        self.output_module_86 = self.module_86(self.output_module_85)
        self.output_module_87 = self.module_87(self.output_module_86)
        self.output_module_88 = self.module_88(self.output_module_75)
        self.output_module_89 = self.module_89(self.output_module_88)
        self.output_module_90 = self.module_90(self.output_module_89)
        return self.output_module_78,self.output_module_81,self.output_module_84,self.output_module_87,self.output_module_90
