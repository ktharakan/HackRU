
#This file scareps the SOC and goes to each seceiton/major and collects all the classes and puts it itnoa  text file

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# specify the path to geckodriver
path_to_geckodriver = "/Users/shaheersaud/Downloads/geckodrivers"

# initialize a new Firefox browser instance
driver = webdriver.Firefox(service=Service(path_to_geckodriver))
# go to the specified page

# Link for SOC for CS

courseList = {
    "013": "African Languages and Literatures",
    "014": "Africana Studies",
    "016": "African Area Studies",
    "018": "Aging",
    "050": "American Studies",
    "070": "Anthropology",
    "078": "Armenian",
    "080": "Art, Visual",
    "081": "Art",
    '082': "Art History",
    "090": "Arts and Science (college courses)",
    "098": "Asian Studies",
    "105": "Astrophysics",
    "115": "Biochemistry",
    "119": "Biological Sciences",
    "145": "Catalan",
    "146": "Cell Biology and Neuroscience",
    "160": "Chemistry",
    "165": "Chinese",
    "175": "Cinema Studies",
    "185": "Cognitive Science",
    "190": "Classics",
    "195": "Comparative Literature",
    "198": "Computer Science",
    "202": "Criminal Justice",
    "203": "Dance",
    "206": "Dance",
    "214": "East Asian Languages and Area Studies",
    "220": "Economics",
    "300": "Education",
    "350": "English",
    "351": "English: Topics",
    "353": "English: Literary Theory",
    "354": "English: Film Studies",
    "355": "English: Composition and Writing",
    "360": "European Studies",
    "377": "Exercise Science and Sport Studies",
    "420": "French",
    "447": "Genetics",
    "450": "Geography",
    "460": "Geological Sciences",
    "470": "German",
    "489": "Greek, Modern",
    "490": "Greek, Ancient",
    "505": "Hindi",
    "506": "History: General/Comparative",
    "508": "History: African, Asian, and Latin American",
    "510": "History: European",
    "512": "History: American",
    "513": "History/French",
    "514": "History/Political Science",
    "535": "Hungarian",
    "556": "Interdisciplinary Studies, FAS",
    "560": "Italian",
    "563": "Jewish Studies",
    "565": "Japanese",
    "567": "Journalism and Media Studies",
    "574": "Korean",
    "575": "Labor Studies",
    "578": "Labor Studies and Employment Relations",
    "580": "Latin",
    "590": "Latin American Studies",
    "615": "Linguistics",
    "628": "Marine Sciences",
    "640": "Mathematics",
    "660": "Medical Technology",
    "667": "Medieval Studies",
    "685": "Middle Eastern Studies",
    "690": "Military Education, Air Force",
    "691": "Military Education, Army",
    "694": "Molecular Biology and Biochemistry",
    "700": "Music",
    "701": "Music, Applied",
    "711": "Operations Research",
    "730": "Philosophy",
    "750": "Physics",
    "787": "Polish",
    "790": "Political Science",
    "810": "Portuguese",
    "830": "Psychology",
    "836": "Puerto Rican and Hispanic Caribbean Studies",
    "840": "Religion",
    "860": "Russian",
    "910": "Social Work",
    "920": "Sociology",
    "925": "South Asian Studies",
    "940": "Spanish",
    "959": "Study Abroad",
    "960": "Statistics",
    "965": "Theater Arts",
    "966": "Theater Arts",
    "967": "Ukrainian",
    "988": "Women's and Gender Studies"
}


def CourseRefresher(name):
    try:

        # driver.refresh()# may be needed
        expand_locator = '/html/body/div[5]/div[2]/table/tbody/tr/td[2]/div[5]/div[1]/h4/span/u'
        driver.refresh()
        expand = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, expand_locator)))
        expand.click()

        filename = name + ".txt"
        sourceFile = open(filename, 'w')

        print(driver.find_element(By.XPATH, "/html/body").text, file=sourceFile)
        sourceFile.close()
        time.sleep(5)

    except (NoSuchElementException, TimeoutException):
        print("Error: Element not found or loading timed out.")


for keys in courseList.keys():
    Course = keys
    Firstlink = 'https://sis.rutgers.edu/oldsoc/#courses%3Fsubject%3D'
    SecondLink = "%26semester%3D12024%26campus%3DNB%26level%3DU"
    driver.get(Firstlink+Course+SecondLink)
    CourseRefresher(keys)
