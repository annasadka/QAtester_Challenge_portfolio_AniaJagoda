from pages.base_page import BasePage


class Dashboard(BasePage):
    email_xpath = "/html/body/div[1]/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    name_xpath = "/html/body/div[1]/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    surname_xpath = "/html/body/div[1]/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    phone_xpath = "/html/body/div[1]/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
    weight_xpath = "/html/body/div[1]/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    height_xpath = "/html/body/div[1]/div[1]/main/div[2]/form/div[2]/div/div[6]/div/div/input"
    age_xpath = "/html/body/div[1]/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
    leg_xpath = "/html/body/div[1]/div[1]/main/div[2]/form/div[2]/div/div[8]/div/div/div "
    club_xpath = "/html/body/div[1]/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input"
    level_xpath = "/html/body/div[1]/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"


pass