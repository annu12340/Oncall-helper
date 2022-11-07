

def group_by_alert_type(result):
    alert_dic = {}
    count = 0
    if result:
        count = len(result)
        for alert in result:
            # Format of alert summary is [#id] alert name.
            alert_name = alert["summary"].split("]", 1)[1]
            if alert_name in alert_dic:
                alert_dic[alert_name] += 1
            else:
                alert_dic[alert_name] = 1
        print("------------------------\nalert_dic\n\n", alert_dic)
        return alert_dic, count


def group_by_alert_count(result):
    alert_dic = {}
    count = 0
    if result:
        count = len(result)
        for alert in result:
            # Format of alert summary is [#id] alert name.
            alert_date = alert["created_at"].split("T", 1)[0]
            if alert_date in alert_dic:
                alert_dic[alert_date] += 1
            else:
                alert_dic[alert_date] = 1
        print("------------------------\nalert_dic\n\n", alert_dic)
        return alert_dic, count
