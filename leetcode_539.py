class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_time(t1, t2):
            temp1_val1 = t1[0:2]
            temp1_val2 = t1[3:]
            temp2_val1 = t2[0:2]
            temp2_val2 = t2[3:]

            if t1 == "00:00":
                if int(temp2_val1) > 12:
                    return "2360", temp2_val1 + temp2_val2
            elif t2 == "00:00":
                if int(temp1_val1) > 12:
                    return "2360", temp1_val1 + temp1_val2

            if temp1_val2 == "00" and int(temp1_val1) > int(temp2_val1):
                val1 = str(int(temp1_val1) - 1)
                return val1 + "60", temp2_val1 + temp2_val2

            elif temp2_val2 == "00" and int(temp2_val1) > int(temp1_val1):
                val2 = str(int(temp2_val1) - 1)
                return val2 + "60", temp1_val1 + temp1_val2

            else:
                if int(temp1_val1) > int(temp2_val1):
                    return temp1_val1 + temp1_val2, temp2_val1 + temp2_val2
                else:
                    return temp2_val1 + temp2_val2, temp1_val1 + temp1_val2

        min_time = float('inf')
        for i in range(len(timePoints)):
            for j in range(i + 1, len(timePoints)):
                date1, date2 = convert_time(timePoints[i], timePoints[j])
                temp1_val1 = date1[0:2]
                temp1_val2 = date1[2:]
                temp2_val1 = date2[0:2]
                temp2_val2 = date2[2:]

                print(temp1_val1, temp1_val2, temp2_val1, temp2_val2)
                total_mins = 0
                if int(temp1_val2) < int(temp2_val2):
                    mins = 60 - int(temp2_val2) + int(temp1_val2)
                    hour_mins = (int(temp1_val1) - int(temp2_val1) - 1) * 60
                    total_mins = mins + hour_mins
                else:
                    mins = int(temp1_val2) - int(temp2_val2)
                    hour_mins = (int(temp1_val1) - int(temp2_val1)) * 60
                    total_mins = mins + hour_mins

                min_time = min(min_time, total_mins)

        return 0
        return min_time

