from selenium import webdriver



class Driver:

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")

    driver = webdriver.Chrome(options)
