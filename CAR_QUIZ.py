import streamlit as st
import time
import pandas as pd
import random

# --- Page config ---
st.set_page_config(
    page_title="Car Brand Quizzes",
    page_icon=":red_car:",
    layout="wide",
)

# --- Custom CSS ---
st.markdown(
    """
    <style>
    div[data-baseweb="select"] > div:focus-within {
        border: 3px solid #6297e3 !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="select"] input:focus {
        border: 3px solid #6297e3 !important;
        border-radius: 8px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Name Modal (must enter name before accessing app) ---
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("Welcome to the Car Brand Quiz Platform! :red_car:")
    st.write("Made with ❤️ by **THE DGLL COMPANY**")
    st.info("Please enter your name to begin.")
    with st.form("user_info_form", clear_on_submit=False):
        name = st.text_input("Name", value=st.session_state.user_name)
        submitted = st.form_submit_button("Enter")
        if submitted:
            if name.strip() == "":
                st.warning("Please enter your name.")
            else:
                st.session_state.user_name = name
                st.session_state.authenticated = True
                st.success("Welcome, " + name + "!" + " :wave_hand:")
                st.write("You can now access the quizzes.")
                st.rerun()
    st.stop()

# --- Sidebar Navigation with Buttons ---
car_brands = [
    "Toyota", "Ford", "BMW", "Mercedes-Benz", "Honda",
    "Nissan", "Audi", "Volkswagen", "Hyundai", "Chevrolet"
]
st.sidebar.title("Navigation")
if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.sidebar.button("Home"):
    st.session_state.page = "Home"
for brand in car_brands:
    if st.sidebar.button(f"{brand} Quiz"):
        st.session_state.page = f"{brand} Quiz"

page = st.session_state.page

# --- Home Page ---
if page == "Home":
    st.title(f"Welcome, {st.session_state.user_name}!")
    st.header("THE DGLL COMPANY's Car Brand Quizzes")
    st.write("Choose a car brand quiz from the sidebar. Each quiz has 20 questions about the brand!")
    st.write("Made with ❤️ by **THE DGLL COMPANY**")

# --- Car Brand Quizzes ---
brand_questions = {
    "Toyota": [
        ("What year was Toyota founded?", ["", "1937", "1947", "1957", "1967"], "1937"),
        ("What is Toyota's luxury vehicle division?", ["", "Lexus", "Acura", "Infiniti", "Genesis"], "Lexus"),
        ("Which Toyota model is the world's best-selling car?", ["", "Corolla", "Camry", "Prius", "Yaris"], "Corolla"),
        ("What is Toyota's hybrid car called?", ["", "Prius", "Insight", "Leaf", "Volt"], "Prius"),
        ("Which country is Toyota from?", ["", "Japan", "USA", "Germany", "South Korea"], "Japan"),
        ("What is the name of Toyota's pickup truck?", ["", "Tacoma", "F-150", "Silverado", "Ranger"], "Tacoma"),
        ("Which Toyota sports car was revived in 2019?", ["", "Supra", "Celica", "MR2", "86"], "Supra"),
        ("What does 'TRD' stand for?", ["", "Toyota Racing Development", "Turbo Road Drive", "Track Ready Design", "Toyota Road Division"], "Toyota Racing Development"),
        ("Which Toyota model is famous for off-roading?", ["", "Land Cruiser", "Prius", "Corolla", "Camry"], "Land Cruiser"),
        ("What is the fuel cell vehicle by Toyota?", ["", "Mirai", "Leaf", "Volt", "Clarity"], "Mirai"),
        ("Which Toyota is a compact SUV?", ["", "RAV4", "Highlander", "Sequoia", "4Runner"], "RAV4"),
        ("What is the Toyota minivan called?", ["", "Sienna", "Odyssey", "Caravan", "Quest"], "Sienna"),
        ("Which Toyota model is known for drifting?", ["", "AE86", "Camry", "Prius", "Avalon"], "AE86"),
        ("What is the Toyota full-size sedan?", ["", "Avalon", "Camry", "Corolla", "Yaris"], "Avalon"),
        ("Which Toyota is a hybrid SUV?", ["", "RAV4 Hybrid", "4Runner", "Sequoia", "Tacoma"], "RAV4 Hybrid"),
        ("What is the Toyota subcompact car?", ["", "Yaris", "Corolla", "Camry", "Prius"], "Yaris"),
        ("Which Toyota is a midsize sedan?", ["", "Camry", "Corolla", "Avalon", "Prius"], "Camry"),
        ("What is the Toyota sports coupe?", ["", "86", "Supra", "Celica", "MR2"], "86"),
        ("Which Toyota is a plug-in hybrid?", ["", "Prius Prime", "Leaf", "Volt", "Insight"], "Prius Prime"),
        ("What is the Toyota luxury SUV?", ["", "Lexus RX", "Highlander", "RAV4", "4Runner"], "Lexus RX"),
    ],
    "Ford": [
        ("What is Ford's iconic sports car?", ["", "Mustang", "Camaro", "Challenger", "Corvette"], "Mustang"),
        ("Which Ford truck is the best-selling vehicle in the US?", ["", "F-150", "Silverado", "Ram", "Tundra"], "F-150"),
        ("What is Ford's electric SUV?", ["", "Mustang Mach-E", "Model Y", "Bolt", "ID.4"], "Mustang Mach-E"),
        ("Which Ford car was famous in the 1960s for racing at Le Mans?", ["", "GT40", "Mustang", "Thunderbird", "Focus"], "GT40"),
        ("What is Ford's luxury division?", ["", "Lincoln", "Mercury", "Cadillac", "Buick"], "Lincoln"),
        ("Which Ford is a compact SUV?", ["", "Escape", "Explorer", "Edge", "Expedition"], "Escape"),
        ("What is the Ford midsize sedan?", ["", "Fusion", "Taurus", "Focus", "Fiesta"], "Fusion"),
        ("Which Ford is a subcompact car?", ["", "Fiesta", "Focus", "Fusion", "Taurus"], "Fiesta"),
        ("What is the Ford full-size SUV?", ["", "Expedition", "Explorer", "Edge", "Escape"], "Expedition"),
        ("Which Ford is a hybrid sedan?", ["", "Fusion Hybrid", "Focus Electric", "Taurus", "Fiesta"], "Fusion Hybrid"),
        ("What is the Ford performance pickup?", ["", "Raptor", "Tremor", "Lightning", "King Ranch"], "Raptor"),
        ("Which Ford is a plug-in hybrid?", ["", "Escape PHEV", "Fusion", "Edge", "Explorer"], "Escape PHEV"),
        ("What is the Ford electric pickup?", ["", "F-150 Lightning", "Ranger EV", "Maverick", "Super Duty"], "F-150 Lightning"),
        ("Which Ford is a compact car?", ["", "Focus", "Fusion", "Fiesta", "Taurus"], "Focus"),
        ("What is the Ford minivan?", ["", "Transit Connect", "Odyssey", "Sienna", "Grand Caravan"], "Transit Connect"),
        ("Which Ford is a police interceptor?", ["", "Explorer", "Taurus", "Fusion", "Edge"], "Explorer"),
        ("What is the Ford muscle car?", ["", "Mustang", "Camaro", "Charger", "Challenger"], "Mustang"),
        ("Which Ford is a crossover?", ["", "Edge", "Escape", "Expedition", "F-150"], "Edge"),
        ("What is the Ford off-road SUV?", ["", "Bronco", "Explorer", "Edge", "Escape"], "Bronco"),
        ("Which Ford is a luxury SUV?", ["", "Lincoln Navigator", "Expedition", "Explorer", "Edge"], "Lincoln Navigator"),
    ],
    "BMW": [
        ("What does BMW stand for?", ["", "Bayerische Motoren Werke", "British Motor Works", "Berlin Motor Works", "Bavarian Motor Works"], "Bayerische Motoren Werke"),
        ("What is BMW's performance division?", ["", "M", "AMG", "RS", "Type R"], "M"),
        ("Which BMW is the flagship sedan?", ["", "7 Series", "5 Series", "3 Series", "X7"], "7 Series"),
        ("What is BMW's electric sub-brand?", ["", "i", "e", "EQ", "ID"], "i"),
        ("Which BMW is a compact executive car?", ["", "3 Series", "5 Series", "7 Series", "X3"], "3 Series"),
        ("What is the BMW SUV called?", ["", "X Series", "Q Series", "GL Series", "RX Series"], "X Series"),
        ("Which BMW is a roadster?", ["", "Z4", "M3", "X5", "i3"], "Z4"),
        ("What is the BMW sports coupe?", ["", "M4", "M5", "M2", "M8"], "M4"),
        ("Which BMW is a plug-in hybrid?", ["", "330e", "320i", "M3", "X1"], "330e"),
        ("What is the BMW luxury SUV?", ["", "X7", "X5", "X3", "X1"], "X7"),
        ("Which BMW is an electric SUV?", ["", "iX", "X5", "X3", "X1"], "iX"),
        ("What is the BMW compact hatchback?", ["", "1 Series", "2 Series", "3 Series", "4 Series"], "1 Series"),
        ("Which BMW is a grand tourer?", ["", "8 Series", "6 Series", "5 Series", "7 Series"], "8 Series"),
        ("What is the BMW crossover coupe?", ["", "X6", "X4", "X2", "X3"], "X6"),
        ("Which BMW is a diesel sedan?", ["", "320d", "330i", "M3", "X1"], "320d"),
        ("What is the BMW electric sedan?", ["", "i4", "i3", "i8", "M5"], "i4"),
        ("Which BMW is a luxury convertible?", ["", "8 Series Convertible", "Z4", "4 Series Convertible", "2 Series Convertible"], "8 Series Convertible"),
        ("What is the BMW compact SUV?", ["", "X1", "X3", "X5", "X7"], "X1"),
        ("Which BMW is a performance wagon?", ["", "M3 Touring", "M5", "X3", "X5"], "M3 Touring"),
        ("What is the BMW hydrogen car?", ["", "iX5 Hydrogen", "i3", "i8", "X5"], "iX5 Hydrogen"),
    ],
    "Mercedes-Benz": [
        ("What is the Mercedes performance division?", ["", "AMG", "M", "RS", "Type S"], "AMG"),
        ("What does 'S-Class' stand for?", ["", "Sonderklasse", "Sport Class", "Super Class", "Special Class"], "Sonderklasse"),
        ("Which Mercedes is the flagship sedan?", ["", "S-Class", "E-Class", "C-Class", "A-Class"], "S-Class"),
        ("What is the Mercedes compact car?", ["", "A-Class", "C-Class", "E-Class", "S-Class"], "A-Class"),
        ("Which Mercedes is a luxury SUV?", ["", "GLS", "GLE", "GLC", "GLA"], "GLS"),
        ("What is the Mercedes electric sub-brand?", ["", "EQ", "i", "e", "ID"], "EQ"),
        ("Which Mercedes is a coupe SUV?", ["", "GLE Coupe", "GLS", "GLA", "GLC"], "GLE Coupe"),
        ("What is the Mercedes roadster?", ["", "SL", "SLC", "AMG GT", "Cabriolet"], "SL"),
        ("Which Mercedes is a plug-in hybrid?", ["", "C 300e", "A 180", "GLA 200", "E 220d"], "C 300e"),
        ("What is the Mercedes minivan?", ["", "V-Class", "B-Class", "A-Class", "C-Class"], "V-Class"),
        ("Which Mercedes is a performance sedan?", ["", "AMG C63", "E 220d", "A 180", "GLA 200"], "AMG C63"),
        ("What is the Mercedes compact SUV?", ["", "GLA", "GLC", "GLE", "GLS"], "GLA"),
        ("Which Mercedes is a luxury coupe?", ["", "S-Class Coupe", "E-Class Coupe", "C-Class Coupe", "A-Class Coupe"], "S-Class Coupe"),
        ("What is the Mercedes electric SUV?", ["", "EQC", "GLC", "GLA", "GLE"], "EQC"),
        ("Which Mercedes is a diesel sedan?", ["", "E 220d", "C 300e", "A 180", "GLA 200"], "E 220d"),
        ("What is the Mercedes luxury convertible?", ["", "S-Class Cabriolet", "SL", "E-Class Cabriolet", "C-Class Cabriolet"], "S-Class Cabriolet"),
        ("Which Mercedes is a performance wagon?", ["", "AMG E63 Wagon", "GLA", "GLC", "GLE"], "AMG E63 Wagon"),
        ("What is the Mercedes hydrogen car?", ["", "GLC F-CELL", "EQC", "GLA", "GLE"], "GLC F-CELL"),
        ("Which Mercedes is a luxury MPV?", ["", "V-Class", "B-Class", "A-Class", "C-Class"], "V-Class"),
        ("What is the Mercedes off-road SUV?", ["", "G-Class", "GLS", "GLA", "GLC"], "G-Class"),
    ],
    "Honda": [
        ("What is Honda's luxury division?", ["", "Acura", "Lexus", "Infiniti", "Genesis"], "Acura"),
        ("Which Honda is a compact sedan?", ["", "Civic", "Accord", "Fit", "Insight"], "Civic"),
        ("What is Honda's hybrid sedan?", ["", "Insight", "Accord", "Civic", "Fit"], "Insight"),
        ("Which Honda is a midsize sedan?", ["", "Accord", "Civic", "Fit", "Insight"], "Accord"),
        ("What is Honda's compact SUV?", ["", "CR-V", "Pilot", "Passport", "Ridgeline"], "CR-V"),
        ("Which Honda is a minivan?", ["", "Odyssey", "Sienna", "Quest", "Caravan"], "Odyssey"),
        ("What is Honda's pickup truck?", ["", "Ridgeline", "Tacoma", "Frontier", "Colorado"], "Ridgeline"),
        ("Which Honda is a subcompact car?", ["", "Fit", "Civic", "Accord", "Insight"], "Fit"),
        ("What is Honda's sports car?", ["", "NSX", "S2000", "Civic Type R", "Accord"], "NSX"),
        ("Which Honda is a plug-in hybrid?", ["", "Clarity", "Insight", "Accord", "Civic"], "Clarity"),
        ("What is Honda's three-row SUV?", ["", "Pilot", "CR-V", "Passport", "HR-V"], "Pilot"),
        ("Which Honda is a crossover?", ["", "HR-V", "CR-V", "Pilot", "Passport"], "HR-V"),
        ("What is Honda's performance hatchback?", ["", "Civic Type R", "Fit", "Accord", "Insight"], "Civic Type R"),
        ("Which Honda is an electric car?", ["", "Clarity Electric", "Fit EV", "Accord Hybrid", "Insight"], "Clarity Electric"),
        ("What is Honda's luxury SUV?", ["", "Acura MDX", "Pilot", "CR-V", "Passport"], "Acura MDX"),
        ("Which Honda is a hybrid SUV?", ["", "CR-V Hybrid", "Pilot", "Passport", "HR-V"], "CR-V Hybrid"),
        ("What is Honda's compact hatchback?", ["", "Fit", "Civic", "Accord", "Insight"], "Fit"),
        ("Which Honda is a performance coupe?", ["", "Civic Si", "Accord", "Fit", "Insight"], "Civic Si"),
        ("What is Honda's fuel cell vehicle?", ["", "Clarity Fuel Cell", "Insight", "Accord", "Civic"], "Clarity Fuel Cell"),
        ("Which Honda is a luxury sedan?", ["", "Acura TLX", "Accord", "Civic", "Insight"], "Acura TLX"),
    ],
    "Nissan": [
        ("What is Nissan's luxury division?", ["", "Infiniti", "Lexus", "Acura", "Genesis"], "Infiniti"),
        ("Which Nissan is famous for drifting?", ["", "350Z", "Altima", "Sentra", "Maxima"], "350Z"),
        ("What is Nissan's electric car?", ["", "Leaf", "Bolt", "Prius", "Model 3"], "Leaf"),
        ("Which Nissan is a compact SUV?", ["", "Rogue", "Murano", "Pathfinder", "Armada"], "Rogue"),
        ("What is Nissan's sports car?", ["", "GT-R", "370Z", "350Z", "Altima"], "GT-R"),
        ("Which Nissan is a midsize sedan?", ["", "Altima", "Sentra", "Maxima", "Versa"], "Altima"),
        ("What is Nissan's pickup truck?", ["", "Frontier", "Tacoma", "Ridgeline", "Colorado"], "Frontier"),
        ("Which Nissan is a full-size SUV?", ["", "Armada", "Rogue", "Murano", "Pathfinder"], "Armada"),
        ("What is Nissan's compact car?", ["", "Sentra", "Altima", "Maxima", "Versa"], "Sentra"),
        ("Which Nissan is a hybrid?", ["", "Altima Hybrid", "Leaf", "GT-R", "370Z"], "Altima Hybrid"),
        ("What is Nissan's minivan?", ["", "Quest", "Odyssey", "Sienna", "Caravan"], "Quest"),
        ("Which Nissan is a crossover?", ["", "Juke", "Rogue", "Murano", "Pathfinder"], "Juke"),
        ("What is Nissan's performance sedan?", ["", "Maxima", "Altima", "Sentra", "Versa"], "Maxima"),
        ("Which Nissan is a plug-in hybrid?", ["", "Note e-Power", "Leaf", "Altima", "GT-R"], "Note e-Power"),
        ("What is Nissan's luxury SUV?", ["", "Infiniti QX80", "Armada", "Rogue", "Murano"], "Infiniti QX80"),
        ("Which Nissan is a subcompact car?", ["", "Versa", "Sentra", "Altima", "Maxima"], "Versa"),
        ("What is Nissan's three-row SUV?", ["", "Pathfinder", "Rogue", "Murano", "Armada"], "Pathfinder"),
        ("Which Nissan is a hatchback?", ["", "Versa Note", "Sentra", "Altima", "Maxima"], "Versa Note"),
        ("What is Nissan's luxury sedan?", ["", "Infiniti Q50", "Altima", "Maxima", "Sentra"], "Infiniti Q50"),
        ("Which Nissan is a performance coupe?", ["", "370Z", "GT-R", "Altima", "Sentra"], "370Z"),
    ],
    "Audi": [
        ("What is Audi's performance division?", ["", "RS", "M", "AMG", "Type S"], "RS"),
        ("Which Audi is the flagship sedan?", ["", "A8", "A6", "A4", "A3"], "A8"),
        ("What is Audi's electric SUV?", ["", "e-tron", "Q5", "Q7", "Q3"], "e-tron"),
        ("Which Audi is a compact car?", ["", "A3", "A4", "A6", "A8"], "A3"),
        ("What is Audi's sports car?", ["", "R8", "TT", "A5", "A7"], "R8"),
        ("Which Audi is a plug-in hybrid?", ["", "Q5 TFSI e", "Q7", "Q3", "A4"], "Q5 TFSI e"),
        ("What is Audi's luxury SUV?", ["", "Q7", "Q5", "Q3", "Q2"], "Q7"),
        ("Which Audi is a crossover?", ["", "Q3", "Q5", "Q7", "Q2"], "Q3"),
        ("What is Audi's wagon called?", ["", "Avant", "Touring", "Estate", "Sportback"], "Avant"),
        ("Which Audi is a coupe SUV?", ["", "Q8", "Q7", "Q5", "Q3"], "Q8"),
        ("What is Audi's compact SUV?", ["", "Q3", "Q5", "Q7", "Q2"], "Q3"),
        ("Which Audi is a diesel sedan?", ["", "A6 TDI", "A4", "A8", "A3"], "A6 TDI"),
        ("What is Audi's convertible called?", ["", "Cabriolet", "Roadster", "Spider", "Targa"], "Cabriolet"),
        ("Which Audi is a performance wagon?", ["", "RS6 Avant", "A6", "A4", "Q5"], "RS6 Avant"),
        ("What is Audi's luxury coupe?", ["", "A5", "A7", "A3", "A4"], "A5"),
        ("Which Audi is a hatchback?", ["", "A3 Sportback", "A4", "A6", "A8"], "A3 Sportback"),
        ("What is Audi's hydrogen car?", ["", "A7 h-tron", "A6", "A4", "Q5"], "A7 h-tron"),
        ("Which Audi is a performance SUV?", ["", "RS Q8", "Q7", "Q5", "Q3"], "RS Q8"),
        ("What is Audi's luxury convertible?", ["", "A5 Cabriolet", "A3 Cabriolet", "A4 Cabriolet", "A6 Cabriolet"], "A5 Cabriolet"),
        ("Which Audi is a subcompact car?", ["", "A1", "A3", "A4", "A6"], "A1"),
    ],
    "Volkswagen": [
        ("What is Volkswagen's best-selling model?", ["", "Golf", "Passat", "Jetta", "Polo"], "Golf"),
        ("Which VW is an electric car?", ["", "ID.3", "Golf", "Passat", "Tiguan"], "ID.3"),
        ("What is VW's compact SUV?", ["", "Tiguan", "Touareg", "Atlas", "Golf"], "Tiguan"),
        ("Which VW is a midsize sedan?", ["", "Passat", "Jetta", "Golf", "Arteon"], "Passat"),
        ("What is VW's luxury sedan?", ["", "Phaeton", "Passat", "Golf", "Jetta"], "Phaeton"),
        ("Which VW is a hatchback?", ["", "Golf", "Polo", "Passat", "Jetta"], "Golf"),
        ("What is VW's minivan?", ["", "Sharan", "Touran", "Caddy", "Transporter"], "Sharan"),
        ("Which VW is a crossover?", ["", "T-Roc", "Tiguan", "Touareg", "Golf"], "T-Roc"),
        ("What is VW's pickup truck?", ["", "Amarok", "Caddy", "Transporter", "Tiguan"], "Amarok"),
        ("Which VW is a plug-in hybrid?", ["", "Golf GTE", "Passat GTE", "ID.3", "Tiguan"], "Golf GTE"),
        ("What is VW's performance hatchback?", ["", "Golf GTI", "Polo GTI", "Passat", "Jetta"], "Golf GTI"),
        ("Which VW is a subcompact car?", ["", "Polo", "Golf", "Passat", "Jetta"], "Polo"),
        ("What is VW's three-row SUV?", ["", "Atlas", "Tiguan", "Touareg", "Golf"], "Atlas"),
        ("Which VW is a diesel sedan?", ["", "Passat TDI", "Golf", "Jetta", "Arteon"], "Passat TDI"),
        ("What is VW's luxury SUV?", ["", "Touareg", "Tiguan", "Atlas", "Golf"], "Touareg"),
        ("Which VW is a convertible?", ["", "Beetle Convertible", "Golf", "Passat", "Jetta"], "Beetle Convertible"),
        ("What is VW's compact sedan?", ["", "Jetta", "Passat", "Golf", "Arteon"], "Jetta"),
        ("Which VW is a performance wagon?", ["", "Golf R Variant", "Passat", "Jetta", "Polo"], "Golf R Variant"),
        ("What is VW's hydrogen car?", ["", "Golf HyMotion", "ID.3", "Passat", "Tiguan"], "Golf HyMotion"),
        ("Which VW is a microbus?", ["", "ID. Buzz", "Transporter", "Caddy", "Sharan"], "ID. Buzz"),
    ],
    "Hyundai": [
        ("What is Hyundai's luxury division?", ["", "Genesis", "Lexus", "Acura", "Infiniti"], "Genesis"),
        ("Which Hyundai is an electric car?", ["", "Ioniq 5", "Kona", "Elantra", "Sonata"], "Ioniq 5"),
        ("What is Hyundai's compact SUV?", ["", "Tucson", "Santa Fe", "Kona", "Venue"], "Tucson"),
        ("Which Hyundai is a midsize sedan?", ["", "Sonata", "Elantra", "Accent", "Azera"], "Sonata"),
        ("What is Hyundai's subcompact car?", ["", "Accent", "Elantra", "Sonata", "Azera"], "Accent"),
        ("Which Hyundai is a hybrid?", ["", "Ioniq Hybrid", "Kona", "Tucson", "Santa Fe"], "Ioniq Hybrid"),
        ("What is Hyundai's performance hatchback?", ["", "Veloster N", "Elantra N", "Sonata", "Accent"], "Veloster N"),
        ("Which Hyundai is a plug-in hybrid?", ["", "Ioniq Plug-in", "Kona", "Tucson", "Santa Fe"], "Ioniq Plug-in"),
        ("What is Hyundai's three-row SUV?", ["", "Palisade", "Santa Fe", "Tucson", "Venue"], "Palisade"),
        ("Which Hyundai is a crossover?", ["", "Kona", "Tucson", "Santa Fe", "Venue"], "Kona"),
        ("What is Hyundai's minivan?", ["", "Staria", "H-1", "Carnival", "Odyssey"], "Staria"),
        ("Which Hyundai is a luxury sedan?", ["", "Genesis G90", "Sonata", "Elantra", "Accent"], "Genesis G90"),
        ("What is Hyundai's compact sedan?", ["", "Elantra", "Sonata", "Accent", "Azera"], "Elantra"),
        ("Which Hyundai is a diesel SUV?", ["", "Santa Fe Diesel", "Tucson", "Kona", "Venue"], "Santa Fe Diesel"),
        ("What is Hyundai's hydrogen car?", ["", "Nexo", "Ioniq 5", "Kona", "Santa Fe"], "Nexo"),
        ("Which Hyundai is a luxury SUV?", ["", "Genesis GV80", "Santa Fe", "Tucson", "Venue"], "Genesis GV80"),
        ("What is Hyundai's pickup truck?", ["", "Santa Cruz", "Tucson", "Santa Fe", "Venue"], "Santa Cruz"),
        ("Which Hyundai is a hatchback?", ["", "i20", "i30", "Elantra", "Sonata"], "i20"),
        ("What is Hyundai's performance sedan?", ["", "Elantra N", "Sonata", "Accent", "Azera"], "Elantra N"),
        ("Which Hyundai is a micro SUV?", ["", "Venue", "Kona", "Tucson", "Santa Fe"], "Venue"),
    ],
    "Chevrolet": [
        ("What is Chevrolet's iconic sports car?", ["", "Corvette", "Camaro", "Mustang", "Charger"], "Corvette"),
        ("Which Chevy is a compact car?", ["", "Cruze", "Malibu", "Impala", "Spark"], "Cruze"),
        ("What is Chevy's electric car?", ["", "Bolt EV", "Volt", "Spark", "Malibu"], "Bolt EV"),
        ("Which Chevy is a midsize sedan?", ["", "Malibu", "Impala", "Cruze", "Spark"], "Malibu"),
        ("What is Chevy's full-size SUV?", ["", "Tahoe", "Suburban", "Traverse", "Equinox"], "Tahoe"),
        ("Which Chevy is a pickup truck?", ["", "Silverado", "Colorado", "Avalanche", "Sierra"], "Silverado"),
        ("What is Chevy's subcompact car?", ["", "Spark", "Sonic", "Cruze", "Malibu"], "Spark"),
        ("Which Chevy is a hybrid?", ["", "Volt", "Bolt EV", "Cruze", "Malibu"], "Volt"),
        ("What is Chevy's performance sedan?", ["", "SS", "Malibu", "Impala", "Cruze"], "SS"),
        ("Which Chevy is a crossover?", ["", "Equinox", "Traverse", "Tahoe", "Suburban"], "Equinox"),
        ("What is Chevy's minivan?", ["", "Orlando", "Uplander", "Venture", "Astro"], "Orlando"),
        ("Which Chevy is a luxury SUV?", ["", "Suburban Premier", "Tahoe", "Traverse", "Equinox"], "Suburban Premier"),
        ("What is Chevy's compact SUV?", ["", "Trax", "Equinox", "Traverse", "Tahoe"], "Trax"),
        ("Which Chevy is a diesel car?", ["", "Cruze Diesel", "Malibu", "Impala", "Spark"], "Cruze Diesel"),
        ("What is Chevy's three-row SUV?", ["", "Traverse", "Tahoe", "Suburban", "Equinox"], "Traverse"),
        ("Which Chevy is a convertible?", ["", "Camaro Convertible", "Corvette", "Malibu", "Cruze"], "Camaro Convertible"),
        ("What is Chevy's hatchback?", ["", "Sonic", "Cruze", "Spark", "Malibu"], "Sonic"),
        ("Which Chevy is a plug-in hybrid?", ["", "Volt", "Bolt EV", "Cruze", "Malibu"], "Volt"),
        ("What is Chevy's microcar?", ["", "Spark", "Sonic", "Cruze", "Malibu"], "Spark"),
        ("Which Chevy is a performance coupe?", ["", "Camaro", "Corvette", "Cruze", "Malibu"], "Camaro"),
    ],
}

def get_jumbled_options(options, correct):
    # Always keep blank as first, jumble the rest
    opts = options[1:]
    random.shuffle(opts)
    return [""] + opts

for brand in car_brands:
    quiz_page = f"{brand} Quiz"
    if page == quiz_page:
        st.title(f"{brand} Quiz :red_car:")
        st.header(f"Test your knowledge about {brand} with this fun quiz! :smile:")

        questions = brand_questions.get(brand, [])
        quiz_key = f"{brand.lower()}"

        if f"{quiz_key}_submitted" not in st.session_state:
            st.session_state[f"{quiz_key}_submitted"] = False
        if f"{quiz_key}_user_answers" not in st.session_state:
            st.session_state[f"{quiz_key}_user_answers"] = {}

        # Score counter in top right
        left, right = st.columns([6, 1])
        with right:
            if st.session_state[f"{quiz_key}_submitted"]:
                score = 0
                for idx, (_, opts, correct) in enumerate(questions):
                    user_ans = st.session_state[f"{quiz_key}_user_answers"].get(f"q_{idx}", "")
                    if user_ans == correct:
                        score += 1
                total = len(questions)
                st.markdown(
                    f"<div style='text-align:right; font-size:22px; font-weight:bold;'>Score: {score}/{total}</div>",
                    unsafe_allow_html=True
                )

        # Render questions
        for idx, (q, opts, correct) in enumerate(questions):
            st.subheader(f"Question {idx+1}")
            st.write(q)
            key = f"q_{idx}"
            # Jumble options except blank
            jumbled_opts = get_jumbled_options(opts, correct)
            if not st.session_state[f"{quiz_key}_submitted"]:
                st.session_state[f"{quiz_key}_user_answers"][key] = st.selectbox(
                    "Select your answer:", jumbled_opts, key=f"{quiz_key}_{key}"
                )
            else:
                # Show the options in the same order as when answered
                answered = st.session_state[f"{quiz_key}_user_answers"][key]
                # Find the options order used when answered
                st.selectbox(
                    "Select your answer:",
                    jumbled_opts,
                    key=f"{quiz_key}_{key}",
                    index=jumbled_opts.index(answered) if answered in jumbled_opts else 0,
                    disabled=True
                )

        # Submit button
        if not st.session_state[f"{quiz_key}_submitted"]:
            if st.button("Submit Answers", key=f"{quiz_key}_submit"):
                st.session_state[f"{quiz_key}_submitted"] = True
                st.write("Calculating your score...")
                time.sleep(1)
                score = 0
                for idx, (_, opts, correct) in enumerate(questions):
                    user_ans = st.session_state[f"{quiz_key}_user_answers"][f"q_{idx}"]
                    if user_ans == correct:
                        score += 1
                total = len(questions)
                if score > total * 0.5:
                    st.success(f"Quiz finished! Your score is {score}/{total}!")
                    st.balloons()
                else:
                    st.error(f"Quiz finished! Your score is {score}/{total}. Better luck next time!")
                time.sleep(2)
                st.write("Thank you for participating in the quiz! :smile:")
                st.write("You can retake the quiz by refreshing the page.")

        # Show answers table after submission
        if st.session_state[f"{quiz_key}_submitted"]:
            if st.button("Reveal Answers Table", key=f"{quiz_key}_answers"):
                answers_data = []
                for idx, (q, _, correct) in enumerate(questions):
                    user_ans = st.session_state[f"{quiz_key}_user_answers"][f"q_{idx}"]
                    is_correct = "✅" if user_ans == correct else "❌"
                    answers_data.append([q, correct, user_ans, is_correct])
                df_answers = pd.DataFrame(
                    answers_data,
                    columns=["Question", "Correct Answer", "Your Answer", "Result"]
                )
                st.table(df_answers)
        st.write("Made with ❤️ by **THE DGLL COMPANY**")