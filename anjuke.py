from selenium import webdriver
import  time
# timepic=time.strftime("%Y-%m-%d-%H_%M_%S")
# dr1=webdriver.Chrome()
# dr1.get("https://shanghai.anjuke.com/")
# dr1.implicitly_wait(5)
# dr1.execute_script('var q=document.documentElement.scrollTop=10000')
# dr1.save_screenshot("D:/345/"+timepic+".png")
# time.sleep(10)
# dr1.quit()

def sum_2_nums(a,b,*args):

    reult=a+b
    for num in args:
        reult=reult+num
    return reult

print(sum_2_nums(1,2,3))
def test(a,b,c=33,*args,**kwargsa):
    print(a+b+c)
    print(args)
    print(kwargsa)
A=(44,55,66)
B={'name':"laowang",'age':18}
test(11,22,33,*A,**B)  #拆包，把A元组传进去，B字典传进去
