import copy

import numpy as np
from matplotlib import pyplot as plt, cm
from numpy import where

from CONTROL.Global import cnl, XLIST, RESULT_FIGSAVE_PATH, rgb_word, color_word, COLORLIST_RGB, COLORLIST_NAME, \
    std_names

fig_save_path=RESULT_FIGSAVE_PATH
std_labels=std_names
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
    #纯无用
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
    # X 已经被压缩，本函数生成各个颜色的雷达图
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
#合并版
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

def draw_demo4(num_all,ifshowmax=1):
    #各颜色各不同分段占比
    xl=['blue','red','orange','green']
    blue=num_all[0]
    bc=["#1976D2","#2196F3","#00BCD4","#BBDEFB"]
    red=num_all[1]
    rc=["#C2185B","#E91E63","#FF5252","#F8BBD0"]
    orange=num_all[2]
    oc=["#F57C00","#FF9800","#FFC107","#FFE0B2"]
    green=num_all[3]
    print(green)
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
    print("from draw4",fig_save_path + "各颜色各不同分段占比" + "饼状图")
    fig.savefig(fig_save_path + "各颜色各不同分段占比" + "饼状图")  # 保存图片
    fig.show()


def draw_demo5(num_all,ifshowmax=0):
    #各个颜色本身各分段占比
    xl = ['blue', 'red', 'orange', 'green']
    blue = num_all[0]
    bc = ["#1976D2", "#2196F3", "#00BCD4", "#BBDEFB"]
    red = num_all[1]
    rc = ["#C2185B", "#E91E63", "#FF5252", "#F8BBD0"]
    orange = num_all[2]
    oc = ["#F57C00", "#FF9800", "#FFC107", "#FFE0B2"]
    green = num_all[3]
    print(green)
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

        ax.pie(values, explode=explode, labels=label, autopct='%1.1f%%',colors=colorss[i],textprops=textprops,)  # 绘制饼图
        ax.set_title(color_word.get(xl[i])[0:5]+"各分段占比",fontsize=40)  # 绘制标题
        ax.legend(fontsize=15)
        print("from draw5",fig_save_path+xl[i]+"饼状图")
        fig.savefig(fig_save_path+xl[i]+"饼状图")  # 保存图片
        fig.show()




def draw_demo6(num_all):
    import matplotlib.pyplot as plt
    from matplotlib.patches import ConnectionPatch
    import numpy as np
    #作用:生成某一分数段各个颜色比例
    score_color=["#FBC02D","#FFEB3B","#CDDC39","#FFF9C4"]
    xl = ['blue', 'red', 'orange', 'green']
    blue = num_all[0]
    bc = ["#1976D2", "#2196F3", "#00BCD4", "#BBDEFB"]
    red = num_all[1]
    rc = ["#C2185B", "#E91E63", "#FF5252", "#F8BBD0"]
    orange = num_all[2]
    oc = ["#F57C00", "#FF9800", "#FFC107", "#FFE0B2"]
    green = num_all[3]
    gc = ["#388E3C", "#4CAF50", "#8BC34A", "#C8E6C9"]
    all = [blue, red, orange, green]
    colorss = [bc, rc, oc, gc]
    plt.rcParams['font.family'] = 'Microsoft YaHei'
    # make figure and assign axis objects
    for l in range(0, 4):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))
        fig.subplots_adjust(wspace=0.3)

    # pie chart parameters---->各分段人总数
        overall_ratios=[0,0,0,0]
        for i in range(len(all[0])):
            for j in range(len(all)):
                overall_ratios[i]+=all[j][i]

        labels = ['0-9分', '10-19分', '20-29分','30分及以上']
        explode = [0.001, 0.001, 0.001,0.001]
    # rotate so that first wedge is split by the x-axis
    # angle = -180 * overall_ratios[0]
        textprops = {'color': 'k',  # 文本颜色
                 'fontsize': 18,  # 文本大小
                 'fontfamily': 'Microsoft JhengHei',  # 设置微软雅黑字体
                 }
        wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%',colors=score_color,
                         labels=labels, explode=explode,radius=1.5,textprops=textprops,startangle=-360*sum(overall_ratios[0:l])/sum(overall_ratios),
                             labeldistance=1.05)
        ax1.set_title("总成绩分数段",pad=80,fontsize=40)




    # bar chart parameters------>该分段人的比例
        age_labels = std_labels
        bottom = 1
        width = .2
    # age_ratios = [all[0][0]/overall_ratios[0], all[1][0]/overall_ratios[0],all[2][0]/overall_ratios[0],all[3][0]/overall_ratios[0]]

        age_ratios = [all[0][l] / overall_ratios[l],
                  all[1][l] / overall_ratios[l],
                  all[2][l] / overall_ratios[l],
                  all[3][l] / overall_ratios[l]]




    # Adding from the top matches the legend.
        k=0
        for j, (height, label) in enumerate(([*zip(age_ratios, age_labels)])):
            bottom -= height
            bc1 = ax2.bar(0, height, width, bottom=bottom, color=COLORLIST_RGB[k], label=label,alpha=0.5)
            ax2.bar_label(bc1, labels=[f"{height:.0%}"], label_type='center')
            k+=1
        ax2.set_title('该分段各个颜色比例',fontsize=20)
        ax2.legend(loc=(0.70,0.4),fontsize=15)
        ax2.axis('off')
        ax2.set_xlim(- 2.5 * width, 2.5 * width)

    # use ConnectionPatch to draw lines between the two plots
        theta1, theta2 = wedges[l].theta1, wedges[l].theta2
        center, r = wedges[0].center, wedges[0].r
        bar_height = sum(age_ratios)

    # draw top connecting line
        x = r * np.cos(np.pi / 180 * theta2) + center[0]
        y = r * np.sin(np.pi / 180 * theta2) + center[1]
        con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                          xyB=(x, y), coordsB=ax1.transData,
                          arrowstyle="<|-|>")
        con.set_color([0, 0, 0])
        con.set_linewidth(1)
        ax2.add_artist(con)

    # draw bottom connecting line
        x = r * np.cos(np.pi / 180 * theta1) + center[0]
        y = r * np.sin(np.pi / 180 * theta1) + center[1]
        con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                          xyB=(x, y), coordsB=ax1.transData,
                          arrowstyle="<|-|>")
        con.set_color([0, 0, 0])
        ax2.add_artist(con)
        con.set_linewidth(1)
        print("from draw6", fig_save_path + "pie-bar" + labels[l] + "各颜色")
        plt.savefig(fig_save_path + "pie-bar" + labels[l] + "各颜色")
        fig.show()


def draw_demo7(num_all):
    #这个是饼-->颜色，bar：分段
    import matplotlib.pyplot as plt
    from matplotlib.patches import ConnectionPatch
    import numpy as np
    xl = ['blue', 'red', 'orange', 'green']
    blue = num_all[0]
    bc = ["#1976D2", "#2196F3", "#00BCD4", "#BBDEFB"]
    red = num_all[1]
    rc = ["#C2185B", "#E91E63", "#FF5252", "#F8BBD0"]
    orange = num_all[2]
    oc = ["#F57C00", "#FF9800", "#FFC107", "#FFE0B2"]
    green = num_all[3]
    gc = ["#388E3C", "#4CAF50", "#8BC34A", "#C8E6C9"]
    all = [blue, red, orange, green]
    colorss = [bc, rc, oc, gc]
    plt.rcParams['font.family'] = 'Microsoft YaHei'
    # make figure and assign axis objects
    for l in range(0,4):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))
        fig.subplots_adjust(wspace=0.3)
        overall_ratios = [0, 0, 0, 0]
        for j in range(len(all)):
            overall_ratios[j] = sum(all[j])
    # pie chart parameters---->各颜色人数


        labels = std_labels
        explode = [0.001, 0.001, 0.001, 0.001]
    # rotate so that first wedge is split by the x-axis
    # angle = -180 * overall_ratios[0]
        textprops = {'color': 'k',  # 文本颜色
                    'fontsize': 18,  # 文本大小
                    'fontfamily': 'Microsoft JhengHei',  # 设置微软雅黑字体
                    }
        wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%',
                         labels=labels, explode=explode,colors=COLORLIST_RGB,
                             textprops=textprops,radius=1.5,
                             startangle=-360*sum(overall_ratios[0:l])/sum(overall_ratios),
                             labeldistance=1.05)
        ax1.set_title("总人数颜色分布", pad=80, fontsize=40)





    # bar chart parameters------>该分段人的比例
        age_ratios = [all[l][0] / overall_ratios[l],
                      all[l][1] / overall_ratios[l],
                      all[l][2] / overall_ratios[l],
                        all[l][3] / overall_ratios[l]]

        age_labels = ['0-9分', '10-19分', '20-29分','30分及以上']
        bottom = 1
        width = .2

    # Adding from the top matches the legend.
        k = 0
        for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
            bottom -= height
            bc1 = ax2.bar(0, height, width, bottom=bottom, color=colorss[l][3-k], label=label,
                     alpha=0.8)
            ax2.bar_label(bc1, labels=[f"{height:.0%}"], label_type='center')
            k += 1
        ax2.set_title('该颜色各个分段比例',fontsize=20)
        ax2.legend(loc=(0.70, 0.4), fontsize=15)
        ax2.axis('off')
        ax2.set_xlim(- 2.5 * width, 2.5 * width)

    # use ConnectionPatch to draw lines between the two plots
        theta1, theta2 = wedges[l].theta1, wedges[l].theta2
        center, r = wedges[0].center, wedges[0].r
        bar_height = sum(age_ratios)

    # draw top connecting line
        x = r * np.cos(np.pi / 180 * theta2) + center[0]
        y = r * np.sin(np.pi / 180 * theta2) + center[1]
        con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                          xyB=(x, y), coordsB=ax1.transData,arrowstyle="<|-|>")
        con.set_color([0, 0, 0])
        con.set_linewidth(1)
        ax2.add_artist(con)

    # draw bottom connecting line
        x = r * np.cos(np.pi / 180 * theta1) + center[0]
        y = r * np.sin(np.pi / 180 * theta1) + center[1]
        con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                          xyB=(x, y), coordsB=ax1.transData,arrowstyle="<|-|>")
        con.set_color([0, 0, 0])
        ax2.add_artist(con)
        con.set_linewidth(1)
        print("from draw7",fig_save_path+"pie-bar"+labels[l]+"各分段")
        plt.savefig(fig_save_path+"pie-bar"+labels[l]+"各分段")
        fig.show()
# draw_demo4()
# draw_demo5()
# draw_demo6()
# draw_demo7()
def draw_demo0(X=None,yhat=None,listnum=None):
    rgb = COLORLIST_RGB
    print("in draw0")
    for i in range(0,4):
        row_ix=where(yhat==i)
        color_i=rgb[listnum.index(row_ix[0].size)]
        fig=plt.figure(figsize=(40, 10), dpi=100)

        myxlabel =copy.deepcopy(XLIST[0:8])

        myxlabel[6]='和最早提交者时间差'
        myxlabel[7] = '抄袭次数'
        for j in row_ix[0]:
            scores = X[j]
            #线条
            plt.plot(myxlabel, scores[:8], c=color_i)
            #点
            plt.scatter(myxlabel, scores[:8], c=color_i,marker='*')

        # plt.yticks(y_ticks[::0.1])
        plt.tick_params(labelsize=30)
        plt.grid(True, linestyle='--', alpha=0.5)
        # plt.xlabel("各个维度", fontdict={'size': 40})
        # plt.ylabel("值", fontdict={'size': 16})
        plt.title(color_word.get(COLORLIST_NAME[listnum.index(row_ix[0].size)])[0:5]+"学生", fontdict={'size': 40})
        plt.savefig(fig_save_path+color_word.get(COLORLIST_NAME[listnum.index(row_ix[0].size)])[0:5]+"学生")

        plt.show()
