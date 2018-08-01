from selenium import webdriver
import time

dr1=webdriver.Chrome()
dr1.get("http://email.163.com/")
dr1.switch_to_frame(dr1.find_element_by_tag_name('iframe'))

# dr1.find_element_by_css_selector("input[name=email]")
time.sleep(5)
dr1.find_element_by_xpath("//*[@id='login-form']/div/div[1]/div[2]/input").send_keys("resume523")
dr1.find_element_by_xpath("//*[@id='content_left']/div[2]/h3/a")

#
# dr1.find_element_by_css_selector("input[name=password]")
# dr1.find_element_by_xpath("//*[name='password']").send_keys("BCM7601")
dr1.find_element_by_name("password").send_keys("BCM7601")
dr1.find_element_by_id("dologin").click()
dr1.implicitly_wait(10)
dr1.find_element_by_css_selector("#_mail_component_76_76 > span.nui-tree-item-text").click()
dr1.implicitly_wait(10)
# js = "window.scrollTo(0, document.body.scrollHeight);"
# dr1.execute_script(js)
# JavascriptExecutor js=(JavascriptExecutor)dr1
# dr1.execute_script()
dr1.execute_script('var q=document.documentElement.scrollTop=10000')
time.sleep(5)