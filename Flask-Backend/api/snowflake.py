import time

#　雪花算法生成ｉｄ
class SnowflakeIDGenerator:
    def __init__(self, datacenter_id, worker_id):
        self.epoch = 1420070400000  # 2015-01-01 00:00:00的时间戳，以毫秒为单位
        self.datacenter_id = datacenter_id  # 数据中心ID
        self.worker_id = worker_id  # 工作机器ID
        self.sequence = 0  # 序列号

    def next_id(self):
        timestamp = int(time.time() * 1000 - self.epoch)  # 当前时间戳减去epoch，以毫秒为单位
        id = (timestamp << 22) | (self.datacenter_id << 17) | (self.worker_id << 12) | self.sequence
        self.sequence = (self.sequence + 1) & 0xfff  # 序列号最大为4095
        if self.sequence == 0:
            timestamp = self.wait_for_next_millisecond(timestamp)
        return id

    def wait_for_next_millisecond(self, timestamp):
        next_timestamp = int(time.time() * 1000 - self.epoch)
        while next_timestamp <= timestamp:
            next_timestamp = int(time.time() * 1000 - self.epoch)
        return next_timestamp

id_generator = SnowflakeIDGenerator(1, 1)
print(id_generator.next_id())