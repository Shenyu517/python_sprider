# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exporters import CsvItemExporter

class CSVPipeline:
    def open_spider(self, spider):
        # 在爬虫开始时创建 CSV 文件并初始化导出器
        self.file = open('zufang.csv', 'wb')
        self.exporter = CsvItemExporter(self.file)
        # 设置 CSV 文件中的字段顺序
        self.exporter.fields_to_export = ['title', 'money', 'area', 'address', 'address_detail']
        self.exporter.start_exporting()

    def close_spider(self, spider):
        # 在爬虫结束时关闭文件
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        # 在处理每个数据项时将其导出到 CSV 文件中
        self.exporter.export_item(item)
        return item
