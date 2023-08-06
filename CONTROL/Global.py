#output control
from dataprocess.hash import HashMap

PROCESS_DETAIL=1
SUBTIME_DATAIL=0
FIRSTSUBMIT_DETAIL=0
FILEREAD_LINES=0
COLTYPE=0
FINAL_NUMS_OF_STD=1
SCOREON=0
LONGTAILLOGDETAIL=0
SHORTTAILEXPDETAIL=0
CHECKFORCOL=0
LESSTHANLEASTSUBMITSHOW=0
MAPZEROSHOW=0

RAWFIGSHOW=0
#para control
LEASTSUBMIT=8
KMEANSCLUSTER=4
LONGTAIL_ZERO_ADD=0.0001
LONGTAIL_INF_ALT= 1000000000
COLLIST=[
"学号",#0
 "题目ID",#1
 "难度",#2
 "首次提交时间",#3
 "最后提交时间",#4
 "投入时间",#5
 "提交次数",#6
 "平均提交间隔",#7
 "通过次数",#8
 "通过率",#9
 "首次AC时间",#10
"首次提交时间和最早提交者的时间差"#11
]
XLIST=[
 "投入时间",#0
 "提交次数",#1
 "平均提交间隔",#2
 "通过次数",#3
 "通过率",#4
 "首次AC时间",#5
 "首次提交时间和最早提交者的时间差",#6
 "学号"#7
]

#PROCESS CONTROL
DELETELESSSUBMIT=1

#PATH CONTROL
RAW_FIGSAVE_PATH="C:\\Users\\11858\\Desktop\\暑期\\data\\rawfigs\\"
FIGSAVE_PATH="C:\\Users\\11858\\Desktop\\暑期\\data\\myfigs\\"
#DATA PROCESS CONTROL log
hashlog=HashMap()
hashlog.put( "投入时间",1)#5
hashlog.put("提交次数",1)#6
hashlog.put("平均提交间隔",1)#7
hashlog.put("通过次数",1)#8
hashlog.put("通过率",0)#9
hashlog.put("首次AC时间",1)#10
hashlog.put("首次提交时间和最早提交者的时间差",0)#11


hashexp=HashMap()
hashexp.put( "投入时间",0)#5
hashexp.put("提交次数",0)#6
hashexp.put("平均提交间隔",0)#7
hashexp.put("通过次数",0)#8
hashexp.put("通过率",0)#9
hashexp.put("首次AC时间",0)#10
hashexp.put("首次提交时间和最早提交者的时间差",1)#11

#DRAWCONTROL
COLORLIST_NAME=['red','orange','green','blue']
COLORLIST_RGB=["#D62728","#FF7F0E","#2CA02C","#1F77B4"]

#RESULTCONTROL
STDID_SHOW=0
STDNUM_SHOW=1