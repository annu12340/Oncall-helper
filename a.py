

dic = {' |Onprem Replicator| efg_cluster@india: JVM uptime < 60': 8, ' | Log pipeline Demux Replicator | abc_cluster@usa Category Latency > 100': 5, ' Log pipeline Demux Replicator | abc_cluster@usa Category Latenc': 2, ' og pipeline Demux Replicator | abc_cluster@usa Category Latenc': 2,
       ' |critical-pageout| hadoop-proc-atla: hadoop sharedcachemante in seconds (should be ~60)': 1, ' sfsfds': 1, ' vvvvvvvvvvvvvvvvvvvvvvvvvvvv': 1, ' xxxxxxxxxxxxxxxxxxxx': 1, ' bbbbbbbbbbb': 1, ' qqqqqqqqqqqq': 1, ' |Hadoop| tst@india: Namenode Uptime Rate< 30': 1, '  |Onprem Replicator| efg_cluster@india: JVM uptime < 60': 1}


def a():
    response = ""
    for key, value in dic.items():
        response += (f"\n*{key} -> {value}")
    return response


print(a())
