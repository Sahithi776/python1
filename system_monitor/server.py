import psutil
import time
from time import localtime, strftime
import json
import asyncio
import websockets


def get_cpu_reading():
    CPU = {}  # we will store the cpu readings here
    CPU_Readings = psutil.cpu_percent(interval=1, percpu=True)

    # {"cpu0": 52.5, "cpu1": 33.0, "cpu2": 54.5, "cpu3": 35.0}
    for i in range(0, len(CPU_Readings)):
        CPU['cpu' + str(i)] = CPU_Readings[i]
    return CPU

def get_load_averages():
    load_Avgs = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    map_Avgs = {"one_min": load_Avgs[0], "five_min": load_Avgs[1], "fifteen_min": load_Avgs[2]}
    return map_Avgs

def get_disk():
    Disk_u = psutil.disk_usage('/')
    return Disk_u[3]

def get_memory():
    Memory = psutil.virtual_memory()
    return Memory[2]

def get_net_traffic(inf="net"):
    net_Stats = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_In = net_Stats.packets_recv
    net_Out = net_Stats.packets_sent
    net_Traffic = (net_In - net_Out)
    net = {"Traffic": net_Traffic}
    return net

def get_internet_download(inf="Wi-Fi"):
    net_Stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_In_1 = net_Stat.bytes_recv
    return round(net_In_1 / 1024 / 1024, 3)

def get_internet_upload(inf="Wi-Fi"):
    net_Stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_Out_1 = net_Stat.bytes_sent
    return round(net_Out_1 / 1024 / 1024, 3)

async def hello(websocket, path):
    name = await websocket.recv()
    time.sleep(1)  # sleep for 1 second
    reading_time = strftime("%H:%M:%S", localtime())
    send_obj = json.dumps({"time": reading_time,
                           "cpu": get_cpu_reading(),
                           "load_avg": get_load_averages(),
                           "virtual_memory_utilized": get_memory(),
                           "disk_utilized": get_disk(),
                           "net_traffic": get_net_traffic(),
                           "net_download": get_internet_download(),
                           "net_upload": get_internet_upload()

                           })

    await websocket.send(send_obj)
    print(send_obj)


start_server = websockets.serve(hello, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


