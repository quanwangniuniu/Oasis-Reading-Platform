# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy, pymysql
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class EPUBPipline(FilesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['book_path'], meta={'id': str(item['id']),'download_timeout': 60,
                                                          'DOWNLOAD_MAXSIZE' : 10485760})

    def file_path(self, request, response=None, info=None, *, item=None):
        filename = f"{request.meta['id']}.epub"  # 获取视频文件名
        return filename  # 返回下载的视频文件名

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            # 如果没有文件下载成功，则中止管道执行并返回DropItem异常
            raise DropItem("文件下载失败")
        item['book_success'] = True
        print(results)
        return item


class ImgPipline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['img_path'], meta={'id': str(item['id'])})

    # 返回图片名称即可
    def file_path(self, request, response=None, info=None, *, item=None):
        filePath = f"{request.meta['id']}.jpeg"
        return filePath

    def item_completed(self, results, item, info):
        item['img_success'] = True
        return item


class DatabasePipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='Wk200211',
            database='test',
            charset='utf8mb4'
        )

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        if item['book_success'] and item['img_success']:
            # sql语句
            result = '\n'.join([s + '\n' for s in item.get('description')])
            item['description'] = result

            keys = ['id', 'title', 'author', 'publisher', 'language', 'rate', 'description', 'book_url', 'img_url']
            values = [item.get(key) for key in keys]
            sql = f"INSERT INTO `book` VALUES ({','.join(['%s'] * len(values))})"
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            cursor.close()
            self.conn.commit()
            return item

