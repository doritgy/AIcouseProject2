import random
capital_list: list[str] = [
    'Kabul', 'Tirana', 'Algiers', 'Andorra la Vella', 'Luanda', 'Saint John\'s', 'Buenos Aires', 'Yerevan',
    'Canberra', 'Vienna', 'Baku', 'Nassau', 'Manama', 'Dhaka', 'Bridgetown', 'Minsk', 'Brussels', 'Belmopan',
    'Porto-Novo', 'Thimphu', 'Sucre', 'Sarajevo', 'Gaborone', 'Brasília', 'Bandar Seri Begawan', 'Sofia',
    'Ouagadougou', 'Gitega', 'Praia', 'Phnom Penh', 'Yaoundé', 'Ottawa', 'Bangui', 'N\'Djamena', 'Santiago',
    'Beijing', 'Bogotá', 'Moroni', 'Brazzaville', 'Kinshasa', 'San José', 'Zagreb', 'Havana', 'Nicosia',
    'Prague', 'Copenhagen', 'Djibouti', 'Roseau', 'Santo Domingo', 'Quito', 'Cairo', 'San Salvador', 'Malabo',
    'Asmara', 'Tallinn', 'Mbabane', 'Addis Ababa', 'Palikir', 'Suva', 'Helsinki', 'Paris', 'Libreville',
    'Banjul', 'Tbilisi', 'Berlin', 'Accra', 'Athens', 'Saint George\'s', 'Guatemala City', 'Conakry', 'Bissau',
    'Georgetown', 'Port-au-Prince', 'Tegucigalpa', 'Budapest', 'Reykjavík', 'New Delhi', 'Jakarta',
    'Baghdad', 'Dublin', 'Jerusalem', 'Rome', 'Kingston', 'Tokyo', 'Amman', 'Nur-Sultan', 'Nairobi', 'Tarawa',
    'Pyongyang', 'Seoul', 'Kuwait City', 'Bishkek', 'Vientiane', 'Riga', 'Beirut', 'Maseru', 'Monrovia', 'Tripoli',
    'Vaduz', 'Vilnius', 'Luxembourg', 'Antananarivo', 'Lilongwe', 'Kuala Lumpur', 'Malé', 'Bamako', 'Valletta',
    'Majuro', 'Nouakchott', 'Port Louis', 'Mexico City', 'Palau', 'Chisinau', 'Monaco', 'Ulaanbaatar', 'Podgorica',
    'Rabat', 'Maputo', 'Naypyidaw', 'Windhoek', 'Yaren', 'Kathmandu', 'Amsterdam', 'Wellington', 'Managua',
    'Niamey', 'Abuja', 'Skopje', 'Oslo', 'Muscat', 'Islamabad', 'Ngerulmud', 'Panama City', 'Port Moresby',
    'Asunción', 'Lima', 'Manila', 'Warsaw', 'Lisbon', 'Doha', 'Bucharest', 'Moscow', 'Kigali', 'Basseterre',
    'Castries', 'Kingstown', 'Apia', 'San Marino', 'São Tomé', 'Riyadh', 'Dakar', 'Belgrade', 'Victoria',
    'Freetown', 'Singapore', 'Bratislava', 'Ljubljana', 'Honiara', 'Mogadishu', 'Pretoria', 'Juba', 'Madrid',
    'Colombo', 'Khartoum', 'Paramaribo', 'Stockholm', 'Bern', 'Damascus', 'Taipei', 'Dushanbe', 'Dodoma',
    'Bangkok', 'Lomé', 'Nukuʻalofa', 'Port of Spain', 'Tunis', 'Ankara', 'Ashgabat', 'Funafuti', 'Kampala',
    'Kyiv', 'Abu Dhabi', 'London', 'Washington, D.C.', 'Montevideo', 'Tashkent', 'Port Vila', 'Vatican City',
    'Caracas', 'Hanoi', 'Sanaa', 'Lusaka', 'Harare']
while True:
    capital_no:int =  random.randint(0,len(capital_list) - 1)
    a:str = ""
    b:str = ""
    indexx:int = 0
    letter:str = ""
    end:bool = False
    ans:str = ""
    a = capital_list[capital_no].lower()
    print(a)
    b = ["_" for _ in range(len(a))]
    print(b)
    while True:
        letter = input("please try a letter")
        end = False
        for i in range(len(b)):
            if letter == a[i]:
                b[i] = a[i]
                end = True
        if not end:
            print("this letter is not included")
            end = False
        try:
            indexx = b.index("_")
        except Exception as e:
            print("you did find out the capital", b)
            end = True
            break
        print(b)
    if end:
        ans = input("do you want to play again? y/n")
        if ans == "n":
            break








