import base64



def base64_decode(base64_data):
    temp = base64.b64decode(base64_data).hex()
    return temp


data = "IrNk"
tem = base64_decode(data)
print("tem %s" % tem)

data1 = "HkX81P5wBTvQYiY="
tem1 = base64_decode(data1)
print("tem1 %s" % tem1)

data2 = "6jCfuLv4SNay9VbRTc1iSg=="
tem2 = base64_decode(data2)
print("tmp2 %s" % tem2)

data3 = "AQAABXCz1f/+iLfI"
tmp3 = base64_decode(data3)
print("tmp3 %s" % tmp3)