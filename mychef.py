from Chef import  Chef
from ChineseChef import  ChineseChef

my_chef = Chef()
my_chef.make_special_dish()

chinese_chef = ChineseChef()
chinese_chef.make_special_dish()
chinese_chef.make_fried_rice()

print(type(chinese_chef))
if type(chinese_chef) == ChineseChef:
    print("ok")
else:
    print("failed")

if type(chinese_chef) == Chef:
    print("ok")
else:
    print("failed")

if isinstance(chinese_chef, ChineseChef):
    print("ok")
else:
    print("failed")

if isinstance(chinese_chef, Chef):
    print("ok")
else:
    print("failed")
