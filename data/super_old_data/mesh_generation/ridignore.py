ignore = ["15131.off", "21289.off", "1166.off", "10316.off", "1655.off", "1901.off", "6923.off", "2129.off", "5690.off", "6619.off", "11840.off", "11561.off", "10267.off", "11230.off", "18247.off", "19298.off", "1051.off", "13585.off", "24661.off", "19663.off", "5036.off", "23876.off", "3093.off", "7557.off", "1858.off", "20719.off", "3085.off", "790.off", "14849.off", "1043.off", "2723.off", "18545.off", "7452.off", "5655.off", "16729.off", "24507.off", "1097.off", "1645.off", "6213.off", "10265.off", "2191.off", "20720.off", "3912.off", "3914.off", "5687.off", "23572.off", "19297.off", "7231.off", "12992.off", "23827.off", "5658.off", "19068.off", "5675.off", "22955.off", "1942.off", "749.off", "16928.off", "18415.off", "2588.off", "15192.off", "11644.off", "24911.off", "3391.off", "6282.off", "5035.off", "11387.off", "3855.off", "20233.off", "1739.off", "6268.off", "3395.off", "18543.off", "23266.off", "12078.off", "784.off", "3921.off", "13509.off", "18549.off", "5225.off", "2423.off", "3092.off", "290.off", "15017.off", "8703.off", "1713.off", "3925.off", "116.off", "6108.off", "1200.off", "7564.off", "13794.off", "2815.off", "24166.off", "17428.off", "14.off", "18548.off", "2033.off", "22693.off", "5.off", "12658.off", "1036.off", "4986.off", "1098.off", "9019.off", "12632.off", "10583.off", "7521.off", "13842.off", "10266.off", "1049.off", "15924.off", "6264.off", "7555.off", "14799.off", "19392.off", "3923.off", "2822.off", "5651.off", "16728.off", "6226.off", "10268.off", "395.off", "25174.off", "10541.off", "5685.off", "14632.off", "14552.off", "14627.off", "19550.off", "16500.off", "2720.off", "5681.off", "14756.off", "11956.off", "5516.off", "3910.off", "5039.off", "10367.off", "5467.off", "2592.off", "2138.off", "6518.off", "23282.off", "5670.off", "9012.off", "3716.off", "6475.off", "6250.off", "15289.off", "3394.off", "8660.off", "796.off", "4985.off", "9564.off", "14850.off", "12228.off", "20717.off", "11751.off", "3911.off", "11231.off", "10368.off", "3084.off", "20229.off", "6221.off", "2719.off", "5457.off", "7304.off", "3920.off", "5686.off", "4385.off", "6155.off", "10673.off", "13691.off", "6443.off", "12637.off", "6263.off", "23407.off", "11800.off", "2813.off", "14550.off", "4984.off", "22633.off", "23198.off", "11643.off", "6278.off", "5455.off", "3096.off", "6258.off", "1129.off", "19874.off", "23563.off", "11802.off", "6214.off", "18547.off", "14626.off", "12635.off", "6265.off", "5456.off", "3918.off", "20718.off", "2589.off", "5407.off", "2721.off", "3906.off", "3083.off", "1048.off", "3907.off", "5674.off", "867.off", "3389.off", "6900.off", "10310.off", "3687.off", "6428.off", "3908.off", "6147.off", "14467.off", "5689.off", "20399.off", "12503.off", "20296.off", "9661.off", "5709.off", "3689.off", "1055.off", "6262.off", "20642.off", "6444.off", "6257.off", "10208.off", "5083.off", "20415.off", "5383.off", "13116.off", "13699.off", "20114.off", "17134.off", "9530.off", "1523.off", "18550.off", "24195.off", "14730.off", "22843.off", "23835.off", "1119.off", "3502.off", "3878.off", "24196.off", "13150.off", "16961.off", "3867.off", "5684.off", "14321.off", "3917.off", "5041.off", "2422.off", "7325.off", "1705.off", "14824.off", "10097.off", "10620.off", "10369.off", "17364.off", "15198.off", "10384.off", "1198.off", "14667.off", "1199.off"]

import os
import shutil
for i, _file in enumerate(os.listdir("off/dex/train")):
    if _file in ignore:
        shutil.move("off/dex/train/" + _file, _file)
        print(_file)

for i, _file in enumerate(os.listdir("off/dex/test")):
    if _file in ignore:
        shutil.move("off/dex/test/" + _file, _file)
        print(_file)

for i, _file in enumerate(os.listdir("off/lev/train")):
    if _file in ignore:
        shutil.move("off/lev/train/" + _file, _file)
        print(_file)

for i, _file in enumerate(os.listdir("off/lev/test")):
    if _file in ignore:
        shutil.move("off/lev/test/" + _file, _file)
        print(_file)
