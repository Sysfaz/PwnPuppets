from bs4 import BeautifulSoup
import requests
import sys
import os
import argparse
import random
import string
from fancy import colors

os.system("clear")


def generate_random_id():
    chars = string.ascii_letters + string.digits
    random_id = "".join(random.choice(chars) for _ in range(6))
    return random_id


id = generate_random_id()
folder = "puppets"
filename = f"{id}.txt"
filepath = os.path.join(folder, filename)
while os.path.exists(filepath):
    id = generate_random_id()
    filename = f"{id}.txt"


class Generate:
    def __init__(self, soup):

        name = soup.find("div", class_="address").h3.text.strip()
        address = soup.find("div", class_="address").div.text.strip()

        def generate(value):
            dl_tags = soup.find_all("dl", class_="dl-horizontal")
            for dl_tag in dl_tags:
                if dl_tag.find("dt").text == str(value):
                    text = dl_tag.find("dd").text.strip()
                    return text

        geo_cords = generate("Geo coordinates").split(",")
        lat = geo_cords[0]
        lon = geo_cords[1].strip()
        birth_date = generate("Birthday")
        age = generate("Age")
        zodiac = generate("Tropical zodiac")
        email = generate("Email Address").split(" ", 1)[0]
        if (
            country == "us"
            or country == "uk"
            or country == "br"
            or country == "ca"
            or country == "dk"
            or country == "fr"
            or country == "za"
        ):
            email_link = (
                soup.find_all("div", class_="adtl")[1].find("a").get("href").strip()
            )

        else:
            email_link = (
                soup.find_all("div", class_="adtl")[0].find("a").get("href").strip()
            )
        username = generate("Username")
        password = generate("Password")
        user_agent = generate("Browser user agent")
        company = generate("Company")
        occupation = generate("Occupation")
        height = generate("Height")
        weight = generate("Weight")
        blood_type = generate("Blood type")
        fav_color = generate("Favorite color")
        car_model = generate("Vehicle")

        print(colors.log_success(colors.print_bold("Basic", color=colors.purple)))

        print(
            f"{colors.print_bold('Name:', color=colors.yellow)} {colors.print_bold(name)}"
        )
        print(
            f"{colors.print_bold('Address:', color=colors.yellow)} {colors.print_bold(address)}"
        )
        print(
            f"{colors.print_bold('Latitude:', color=colors.yellow)} {colors.print_bold(lat)}"
        )
        print(
            f"{colors.print_bold('Longitude:', color=colors.yellow)} {colors.print_bold(lon)}"
        )

        print(colors.log_success(colors.print_bold("Birthday", color=colors.purple)))

        print(
            f"{colors.print_bold('Birth Date:', color=colors.yellow)} {colors.print_bold(birth_date)}"
        )
        print(
            f"{colors.print_bold('Age:', color=colors.yellow)} {colors.print_bold(age)}"
        )
        print(
            f"{colors.print_bold('Zodiac Sign:', color=colors.yellow)} {colors.print_bold(zodiac)}"
        )

        print(colors.log_success(colors.print_bold("Online", color=colors.purple)))

        print(
            f"{colors.print_bold('Email:', color=colors.yellow)} {colors.print_bold(email)}"
        )
        print(
            f"{colors.print_bold('Email Link:', color=colors.yellow)} {colors.print_bold(email_link)}"
        )
        print(
            f"{colors.print_bold('Username:', color=colors.yellow)} {colors.print_bold(username)}"
        )
        print(
            f"{colors.print_bold('Password:', color=colors.yellow)} {colors.print_bold(password)}"
        )
        print(
            f"{colors.print_bold('User Agent:', color=colors.yellow)} {colors.print_bold(user_agent)}"
        )

        print(colors.log_success(colors.print_bold("Employpemt", color=colors.purple)))

        print(
            f"{colors.print_bold('Company:', color=colors.yellow)} {colors.print_bold(company)}"
        )
        print(
            f"{colors.print_bold('Occupation:', color=colors.yellow)} {colors.print_bold(occupation)}"
        )

        print(colors.log_success(colors.print_bold("Physical", color=colors.purple)))

        print(
            f"{colors.print_bold('Height:', color=colors.yellow)} {colors.print_bold(height)}"
        )
        print(
            f"{colors.print_bold('Weight:', color=colors.yellow)} {colors.print_bold(weight)}"
        )
        print(
            f"{colors.print_bold('Blood Type:', color=colors.yellow)} {colors.print_bold(blood_type)}"
        )

        print(colors.log_success(colors.print_bold("Others", color=colors.purple)))

        print(
            f"{colors.print_bold('Favorite Color:', color=colors.yellow)} {colors.print_bold(fav_color)}"
        )
        print(
            f"{colors.print_bold('Car Model:', color=colors.yellow)} {colors.print_bold(car_model)}"
        )

        with open(f"puppets/{id}.txt", "w") as f:
            f.write("---BASIC---\n")
            f.write(f"Name: {name}\n")
            f.write(f"Address: {address}\n")
            f.write(f"Latitude: {lat}\n")
            f.write(f"Longitude: {lon}\n")
            f.write("---BIRTHDAY---\n")
            f.write(f"Birth Date: {birth_date}\n")
            f.write(f"Age: {age}\n")
            f.write(f"Zodiac Sign: {zodiac}\n")
            f.write("---ONLINE---\n")
            f.write(f"Email: {email}\n")
            f.write(f"Email Link: {email_link}\n")
            f.write(f"Username: {username}\n")
            f.write(f"Password: {password}\n")
            f.write(f"User Agent: {user_agent}\n")
            f.write("---EMPLOYMENT---\n")
            f.write(f"Company: {company}\n")
            f.write(f"Occupation: {occupation}\n")
            f.write("---PHYSICAL---\n")
            f.write(f"Height: {height}\n")
            f.write(f"Weight: {weight}\n")
            f.write(f"Blood Type: {blood_type}\n")
            f.write("---OTHERS---\n")
            f.write(f"Favorite Color: {fav_color}\n")
            f.write(f"Car Model: {car_model}\n")

        print(colors.log_debug("Generated ID: " + colors.print_bold(id)))


parser = argparse.ArgumentParser(
    description="Python script to Generate a Sock Puppet Profile",
    usage="python3 %(prog)s -g female -c US -ns AU",
    epilog="Check country_codes.txt for country codes and name_sets.txt for name sets",
)

parser.add_argument(
    "-g",
    "--gender",
    help="Gender of the Sock Puppet",
    dest="gender",
    nargs=1,
    choices=["male", "female", "random"],
    default="random",
)

parser.add_argument(
    "-c",
    "--country",
    help="Country of the Sock Puppet",
    dest="country",
    nargs=1,
    choices=[
        "US",  # United States
        "UK",  # United Kingdom
        "AU",  # Australia
        "BR",  # Brazil
        "CA",  # Canada
        "DK",  # Denmark
        "FR",  # France
        "GR",  # Germany
        "NL",  # Netherlands
        "NZ",  # New Zealand
        "PT",  # Portugal
        "ZA",  # South Africa
        "SP",  # Spain
    ],
    default="US",
)

parser.add_argument(
    "-ns",
    "--name-set",
    help="Name Set of the Sock Puppet",
    dest="name_set",
    nargs=1,
    choices=[
        "US",  # United States
        "AU",  # Australia
        "BR",  # Brazil
        "HR",  # Croatia
        "DK",  # Denmark
        "FR",  # France
        "IT",  # Italy
        "JP",  # Japan
        "FA",  # Persian
        "RU",  # Russia
        "VN",  # Vietnam
        "Ninja",  # Ninja
    ],
    default="US",
)

parser.add_argument(
    "-v",
    "--version",
    help="Show the version of the script",
    action="version",
    version="%(prog)s 1.0",
)

args = parser.parse_args()

if type(args.gender) == list:
    gender = args.gender[0].lower()
else:
    gender = args.gender.lower()

if type(args.country) == list:
    country = args.country[0].lower()
else:
    country = args.country.lower()

if type(args.name_set) == list:
    name_set = args.name_set[0].lower()
else:
    name_set = args.name_set.lower()


header = {"User-Agent": "Mozilla/5.0"}
if len(sys.argv) == 1:
    source = requests.get("https://www.fakenamegenerator.com/", headers=header).text
    soup = BeautifulSoup(source, "lxml")
    Generate(soup)
else:
    source = requests.get(
        f"https://www.fakenamegenerator.com/gen-{gender}-{name_set}-{country}.php",
        headers=header,
    ).text
    soup = BeautifulSoup(source, "lxml")
    Generate(soup)
