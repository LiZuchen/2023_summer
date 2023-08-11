import numpy as np
from matplotlib import pyplot as plt, cm
from CONTROL.Global import cnl, XLIST, RESULT_FIGSAVE_PATH, rgb_word, color_word

fig_save_path=RESULT_FIGSAVE_PATH
# labels=np.array([u"推进","KDA",u"生存",u"团战",u"发育",u"输出"])
# stats=[83, 61, 95, 67, 76, 88]
# # 画图数据准备，角度、状态值
# angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
#
# stats=np.concatenate((stats,[stats[0]]))
#
# angles=np.concatenate((angles,[angles[0]]))
#
# # 用Matplotlib画蜘蛛图
#
# fig = plt.figure()
#
# ax = fig.add_subplot(111, polar=True)
#
# ax.plot(angles, stats, 'o-', linewidth=2)
#
# ax.fill(angles, stats, alpha=0.25)
#
# # 设置中文字体
#
#
#
# ax.set_thetagrids(angles * 180/np.pi, labels, FontProperties=cnl,Fontsize=16)
#
# plt.show()
def draw_demo2():
    # import pandas as pd
    # import matplotlib.pyplot as plt
    # import numpy as np
    # df = pd.read_excel('成绩表.xlsx')
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码
    # labels = np.array(['语文', '数学', '英语', '物理', '化学', '生物'])  # 标签
    # dataLenth = 6  # 数据长度
    # # 计算女生、男生各科平均成绩
    # df1 = np.array(df[df['性别'] == '女'].mean().round(2))
    # df2 = np.array(df[df['性别'] == '男'].mean().round(2))
    #
    # # print(df1-df2)
    # # 设置雷达图的角度，用于平分切开一个平面
    # angles = np.linspace(0, 2 * np.pi, dataLenth, endpoint=False)
    # df1 = np.concatenate((df1, [df1[0]]))  # 使雷达图闭合
    # df2 = np.concatenate((df2, [df2[0]]))  # 使雷达图闭合
    # angles = np.concatenate((angles, [angles[0]]))  # 使雷达图闭合
    # plt.polar(angles, df1, 'r--', linewidth=2, label='女生')  # 设置极坐标系,r--代表red和虚线
    # plt.fill(angles, df1, facecolor='r', alpha=0.5)  # 填充
    # plt.polar(angles, df2, 'b-', linewidth=2, label='男生')  # 设置极坐标系,bo代表blue和实心圆
    # plt.fill(angles, df2, facecolor='b', alpha=0.5)  # 填充
    # plt.thetagrids(angles * 180 / np.pi, labels)  # 设置网格、标签
    # plt.ylim(0, 140)  # 设置y轴上下限
    # plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))  # 图例及图例位置
    # plt.show()
    results = [{"大学英语": 87, "高等数学": 79, "体育": 95, "计算机基础": 92, "程序设计": 85},
               {"大学英语": 80, "高等数学": 90, "体育": 91, "计算机基础": 85, "程序设计": 88}]
    data_length = len(results[0])
    # 将极坐标根据数据长度进行等分
    angles = np.linspace(0, 2 * np.pi, data_length, endpoint=False)
    labels = [key for key in results[0].keys()]
    score = [[v for v in result.values()] for result in results]
    # 使雷达图数据封闭
    score_a = np.concatenate((score[0], [score[0][0]]))
    score_b = np.concatenate((score[1], [score[1][0]]))
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))
    # 设置图形的大小

    # 新建一个子图
    ax = plt.subplot(111, polar=True)
    # 绘制雷达图
    ax.plot(angles, score_a, color='g')
    ax.plot(angles, score_b, color='b')
    # 设置雷达图中每一项的标签显示
    ax.set_thetagrids(angles * 180 / np.pi, labels)
    # 设置雷达图的0度起始位置
    ax.set_theta_zero_location('N')
    # 设置雷达图的坐标刻度范围
    ax.set_rlim(0, 100)
    # 设置雷达图的坐标值显示角度，相对于起始角度的偏移量
    ax.set_rlabel_position(270)
    # fontproperties = "STSong", fontsize = 16
    ax.set_title("计算机专业大一（上）", fontproperties = "STSong")
    plt.legend(["弓长张", "口天吴"], loc='best')
    plt.show()
def draw_demo1(X,color):
    plt.rcParams['font.family'] = 'Microsoft YaHei'
    labels=np.array(XLIST[:7]+["抄袭次数"])

    stats=X

    # 画图数据准备，⻆度、状态值
    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    labels = np.concatenate((labels, [labels[0]]))
    stats=np.concatenate((stats,[stats[0]]))
    angles=np.concatenate((angles,[angles[0]]))

    # ⽤Matplotlib画蜘蛛图
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, stats, 'o-', linewidth=2,color=color) # 连线
    ax.fill(angles, stats, alpha=0.25,c=color) # 填充

    # 设置⻆度
    ax.set_thetagrids(angles*180/np.pi,#⻆度值
                  labels,
                  fontsize = 18)

    ax.set_rgrids([0.2,0.4,0.6,0.8,1.0],fontsize = 18)
    plt.title(rgb_word.get(color)[:5],fontsize = 40,pad=20)
    plt.savefig(fig_save_path +rgb_word.get(color)[:5]+"雷达图" + ".png")
    plt.show()

def draw_demo3(XALL,colorall):
#学生X的雷达图向量

    plt.rcParams['font.family'] = 'Microsoft YaHei'
    labels = np.array(XLIST[:7] + ["抄袭次数"])
    # 画图数据准备，⻆度、状态值
    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    labels = np.concatenate((labels, [labels[0]]))
        # ⽤Matplotlib画蜘蛛图
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, polar=True)
    angles = np.concatenate((angles, [angles[0]]))
    for i in range(len(XALL)):
        stats = XALL[i]
        color = colorall[i]
        stats=np.concatenate((stats,[stats[0]]))

        ax.plot(angles, stats, 'o-', linewidth=2,color=color) # 连线
        ax.fill(angles, stats, alpha=0.25,c=color) # 填充

        # 设置⻆度
    ax.set_thetagrids(angles*180/np.pi,#⻆度值
                  labels,
                  fontsize = 18)

    ax.set_rgrids([0.2,0.4,0.6,0.8,1.0],fontsize = 18)
    plt.title("雷达图合并版", fontsize=40, pad=20)
    plt.savefig(fig_save_path+"雷达图合并版"+".png")
    plt.show()

def draw_demo4(ifshowmax=1):
    xl=['blue','red','orange','green']
    blue=[50, 14, 6, 1]
    bc=["#1976D2","#2196F3","#00BCD4","#BBDEFB"]
    red=[114, 77, 63, 0]
    rc=["#C2185B","#E91E63","#FF5252","#F8BBD0"]
    orange=[30, 52, 409, 29]
    oc=["#F57C00","#FF9800","#FFC107","#FFE0B2"]
    green=[81, 89, 376, 16]
    gc=["#388E3C","#4CAF50","#8BC34A","#C8E6C9"]
    all= [blue,red,orange,green]
    colorss = [bc,rc,oc,gc]
    plt.rcParams['font.family'] = 'Microsoft YaHei'
    fig=plt.figure(figsize=(20, 20))
    # fig, axes = plt.subplots(2, 2)
    # ax1 = axes[0, 0]
    # ax2 = axes[0, 1]
    # ax3 = axes[1, 0]
    # ax4 = axes[1, 1]
    for i in range(0, len(all)):
        # 将画布设定为正方形，则绘制的饼图是正圆
        axi=fig.add_subplot(2, 2, i + 1)
        label = ['0-9分', '10-19分', '20-29分', '30分及以上']  # 定义饼图的标签，标签是列表
        explode = [0.001, 0.001, 0.001,0.001] # 设定各项距离圆心n个半径
        if ifshowmax:
            explode[all[i].index(max(all[i]))] = 0.1

        # plt.pie(values[-1,3:6],explode=explode,labels=label,autopct='%1.1f%%')#绘制饼图
        values = all[i]
        textprops = {'color': 'k',  # 文本颜色
                     'fontsize': 20,  # 文本大小
                     'fontfamily': 'Microsoft JhengHei',  # 设置微软雅黑字体
                     }

        axi.pie(values, explode=explode, labels=label, autopct='%1.1f%%', colors=colorss[i],
                textprops=textprops)  # 绘制饼图
        axi.legend()
        axi.set_title(color_word.get(xl[i])[0:5] + "各分段占比", fontsize=40)  # 绘制标题
        # plt.savefig(fig_save_path + xl[i] + "饼状图")
        # 保存图片
    fig.suptitle("各颜色各不同分段占比", fontsize=80)
    fig.savefig(fig_save_path + "各颜色各不同分段占比" + "饼状图")  # 保存图片
    fig.show()
draw_demo4()

def draw_demo5(ifshowmax=0):
    xl = ['blue', 'red', 'orange', 'green']
    blue = [50, 14, 6, 1]
    bc = ["#1976D2", "#2196F3", "#00BCD4", "#BBDEFB"]
    red = [114, 77, 63, 0]
    rc = ["#C2185B", "#E91E63", "#FF5252", "#F8BBD0"]
    orange = [30, 52, 409, 29]
    oc = ["#F57C00", "#FF9800", "#FFC107", "#FFE0B2"]
    green = [81, 89, 376, 16]
    gc = ["#388E3C", "#4CAF50", "#8BC34A", "#C8E6C9"]
    all = [blue, red, orange, green]
    colorss = [bc, rc, oc, gc]
    plt.rcParams['font.family'] = 'Microsoft YaHei'

    for i in range(0,len(all)):
         # 将画布设定为正方形，则绘制的饼图是正圆
        fig = plt.figure(figsize=(10, 10))
        ax=fig.add_subplot(111)
        label = ['0-9分', '10-19分', '20-29分','30分及以上']  # 定义饼图的标签，标签是列表
        explode = [0.001, 0.001, 0.001,0.001]  # 设定各项距离圆心n个半径
        if ifshowmax:
            explode[all[i].index(max(all[i]))]=0.1
        # plt.pie(values[-1,3:6],explode=explode,labels=label,autopct='%1.1f%%')#绘制饼图
        values = all[i]
        textprops = {'color': 'k',  # 文本颜色
                 'fontsize': 20,  # 文本大小
                 'fontfamily': 'Microsoft JhengHei',  # 设置微软雅黑字体
                 }

        ax.pie(values, explode=explode, labels=label, autopct='%1.1f%%',colors=colorss[i],textprops=textprops)  # 绘制饼图
        ax.set_title(color_word.get(xl[i])[0:5]+"各分段占比",fontsize=40)  # 绘制标题
        ax.legend(loc='best',fontsize=15)
        fig.savefig(fig_save_path+xl[i]+"饼状图")  # 保存图片
        fig.show()


draw_demo5(0)