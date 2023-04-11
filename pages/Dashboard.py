from pages.base_page import BasePage


class Dashboard(BasePage):

    player_count_xpath = " /html/body/div[1]/div[1]/main/div[2]/div[1]/div/div[2]/b "
    matches_count_xpath = " /html/body/div[1]/div[1]/main/div[2]/div[2]/div/div[2]/b "
    reports_count_xpath = " /html/body/div[1]/div[1]/main/div[2]/div[3]/div/div[2]/b "
    events_count_xpath = " /html/body/div[1]/div[1]/main/div[2]/div[4]/div/div[2]/b "
    logo_xpath = " /html/body/div[1]/div[1]/main/div[3]/div[1]/div/div[1] "
    dev_team_contact_xpath = " /html/body/div[1]/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1] "
    add_player_xpath = " /html/body/div[1]/div[1]/main/div[3]/div[2]/div/div/a/button/span[1] "
    last_created_player_xpath = " /html/body/div[1]/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1] "
    last_updated_player_xpath = " /html/body/div[1]/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1] "
    last_created_match_xpath = " /html/body/div[1]/div[1]/main/div[3]/div[3]/div/div/a[3]/button/span[1] "
    last_updated_match_xpath = " /html/body/div[1]/div[1]/main/div[3]/div[3]/div/div/a[4]/button/span[1] "
    last_updated_report_xpath = "/html/body/div[1]/div[1]/main/div[3]/div[3]/div/div/a[5]/button/span[1] "


pass
