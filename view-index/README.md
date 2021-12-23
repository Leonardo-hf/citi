# 舆论指标构建 demo

## 基本思路

1. 选取 10 家不同行业 2020 年份存在财务造假的公司;
2. 对于每家造假公司, 选取 1 家同行业不存在财务造假的公司作为对照;
3. 选取 7 对作为训练集, 3 对作为测试集;
4. 对于每家造假公司, 选取其造假日期前 1 年的 20 篇新闻;
5. 对于每家对照公司, 选取其对应的造假公司的新闻选取时间范围内的 20 篇新闻;
6. 对于每家公司的新闻, 构建其积极和消极新闻情感指标 ( 中性未通过显著性分析 );
7. 构建基于新闻情感的财务造假 Logistic 识别模型.

## 项目结构

并没有列出全部文件.

```txt
.
├── app.py # 入口文件
├── data
│   └── pairs.csv # 选取的 10 对公司
├── dict
│   ├── neg.txt # 消极财经词汇
│   └── pos.txt # 积极财经词汇
├── emotion.py # 文本的情感指标比例
├── __init__.py
├── README.md
└── util
    ├── database.py # 用于将数据导入数据库
    └── read.py # 用于读取文件
```

- data, 放置数据文件, 包括公司新闻
- dict, 财经情感词汇
- util, 工具模块, 包括文件工具, 数据库工具, 爬虫工具?
- emotion.py 文本的积极/消极情感指标, 中性指标未考虑, 积极加消极和为 1
- app.py 入口文件, 目前是用于测试...

## 参考

- [中文金融情感词典发布啦 | 附代码](https://jishuin.proginn.com/p/763bfbd60498)
- [基于新闻情感的上市公司财务造假识别方法研究](https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLAST2021&filename=SDKY202101011&uniplatform=NZKPT&v=cRdTjtc-nuK1GfkWlZCIKQC1f2YOxkhL1QPX7UrOpcwezhfrMO1Tyd3AaSdlSwpN)
