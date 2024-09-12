from textfsm import TextFSM
import os

# Import the correct path for opening Arelion.textfsm
base_dir = os.path.dirname(__file__)  # 获取当前脚本文件所在的目录
file_path = os.path.join(base_dir, 'Plugin', 'Arelion.textfsm')

def arelion(message):
    """
    This is the policy for Arelion.
    We need to specify rules and characteristics of email
    * body: The body of the email message
    * my_time: Scheduled maintenance time
    * Vendor's cid: Circuit ID
    * Duration: Maintenance time frame
    """

    body = message.body
    my_time = []
    reason = ""
    cid = []
    duration = "During the maintenance window"

    with open(file_path, encoding='utf8') as textfsm_file:

        # Format TextFSM template
        template = TextFSM(textfsm_file)
        datas = template.ParseTextToDicts(body)

        # Use queue to deal with service type and working status
        service_type = []
        work_status = []

        # Judge each line
        for line in datas:

            # Reason
            if len(line['REASON']) > 0:
                reason = line['REASON']

            # Arelion work status
            # strip() to avoid spaces in front or end of the string
            if len(line['WORK_STATUS']) > 0:
                work_status.append(line['WORK_STATUS'].strip())

            # Judge whether it is a primary or backup maintenance
            if len(line['SERVICE_TYPE']) > 0:
                # print(line['SERVICE_TYPE'])
                service_type.append(line['SERVICE_TYPE'].strip())

            # If this maintenance is cancelled, skip
            # If this maintenance is in process, skip
            if work_status and (work_status[-1] == 'Cancelled' or work_status[-1] == 'In process'):
                continue

            # Judge whether it is a primary or backup maintenance
            # We only record CID information when in primary
            if service_type and service_type[-1] == 'primary':
                # Service ID:
                if len(line['IMPACT_SERVICE_ID']) > 0:
                    # print(line['IMPACT_SERVICE_ID'])
                    cid.append(line['IMPACT_SERVICE_ID'])

            # Time
            # No matter primary or backup maintenance we both need to record the time
            if len(line['WINDOW_START']) != 0: # and status.pop(0) == "Confirmed": -> Put it in filter
                temp = line['WINDOW_START'] + ' ' + line['WINDOW_END']
                my_time.append(temp)

            # Future modify filter for arelion
            # if any(word in line['UPDATE_CONTENT'] for word in ["rescheduled", "Implemented", "Cancelled"]):
            #     return [], "", []

    return reason, my_time, cid, duration

