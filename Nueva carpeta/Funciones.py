import random
from datetime import datetime, timedelta

# inicio = datetime.now() - timedelta(days=6574)
# final =  datetime.now()

# i = 1
# while i < 6:
#     random_date = inicio + (final - inicio) * random.random()
#     print(random_date.strftime("%x"))
#     i += 1

nombresMasculinos = ("Adel", "Adonis", "Ajaz", "Akos", "Aldo", "Amets", "Amaro", "Aquiles", "Algimantas", "Alpidio", "Amrane", "Anish", "Arián", "Ayun", "Azariel", "Bagrat", "Bencomo", "Bertino", "Candi", "Cesc", "Cirino", "Crisólogo", "Cruz", "Danilo", "Dareck", "Dariel", "Darin", "Delmiro", "Damen", "Dilan", "Dipa", "Doménico", "Drago", "Edivaldo", "Elvis", "Elyan", "Emeric", "Engracio", "Ensa", "Eñaut", "Eleazar", "Eros", "Eufemio", "Feiyang", "Fiorenzo", "Foudil", "Galo", "Gastón", "Giulio", "Gautam", "Gentil", "Gianni", "Gianluca", "Giorgio", "Gourav", "Grober", "Guido", "Guifre", "Guim", "Hermes", "Inge", "Irai", "Iraitz", "Iyad", "Iyán", "Jeremías", "Joao", "Jun", "Khaled", "Leónidas", "Lier", "Lionel", "Lisandro", "Lucián", "Mael", "Misael", "Moad", "Munir", "Nael", "Najim", "Neo", "Neil", "Nikita", "Nilo", "Otto", "Pep", "Policarpo", "Radu", "Ramsés", "Rómulo", "Roy", "Severo", "Sidi", "Simeón", "Taha", "Tao", "Vadim", "Vincenzo", "Zaid", "Zigor", "Zouhair", "Hugo", "Mateo", "Martín", "Lucas", "Leo", "Daniel", "Alejandro", "Manuel", "Pablo", "Álvaro", "Adrián", "Enzo", "Mario", "Diego", "David", "Oliver", "Marcos", "Thiago", "Marco", "Álex", "Javier", "Izan", "Bruno", "Miguel", "Antonio", "Gonzalo", "Liam", "Gael", "Marc", "Carlos", "Juan", "Ángel", "Dylan", "Nicolás", "José", "Sergio", "Gabriel", "Luca", "Jorge", "Darío", "Íker", "Samuel", "Eric", "Adam", "Héctor", "Francisco", "Rodrigo", "Jesús", "Erik", "Amir", "Jaime", "Ian", "Rubén", "Aarón", "Iván", "Pau", "Víctor", "Guillermo", "Luis", "Mohamed", "Pedro", "Julen", "Unai", "Rafael", "Santiago", "Saúl", "Alberto", "Noah", "Aitor", "Joel", "Nil", "Jan", "Pol", "Raúl", "Matías", "Martí", "Fernando", "Andrés", "Rayan", "Alonso", "Ismael", "Asier", "Biel", "Ander", "Aleix", "Axel", "Alan", "Ignacio", "Fabio", "Neizan", "Jon", "Teo", "Isaac", "Arnau", "Luka", "Max", "Imran", "Youssef", "Anas", "Elías", "Abaigar", "Adei", "Adur", "Adiran", "Aimar", "Aitor", "Andoni", "Ander", "Antxon", "Amets", "Aratz", "Argi", "Aritz", "Asier", "Balkoe", "Baltz", "Bazkoare", "Beltso", "Bernat", "Beñat", "Bikendi", "Biktor", "Bizen", "Dabi", "Dari", "Damen", "Diagur", "Dunixi", "Eako", "Eder", "Edorta", "Edur", "Eki", "Ekaitz", "Eladi", "Elixi", "Eloi", "Emiri", "Eneko", "Endrike", "Eritz", "Etor", "Euken", "Ferran", "Frantzisko", "Ganiz", "Gari", "Gentzen", "Gergori", "Gilem", "Gizon", "Goiznabar", "Gontzal", "Gorka", "Grazian", "Guren", "Haize", "Haran", "Haritz", "Heiko", "Hodei", "Ibai", "Ibar", "Igon", "Igor", "Iker", "Imanol", "Iñaki", "Ipar", "Irai", "Iren", "Izan", "Izei", "Jon", "Jeino", "Joritz", "Josu", "Julen", "Jurgi", "Kai", "Kasi", "Kauldi", "Kutun", "Lain", "Luken", "Maide", "Mairu", "Maren", "Markel", "Martitz", "Mikel", "Negu", "Neketi", "Nikanor", "Odei", "Oier", "Oihan", "Orentzi", "Orixe", "Ortzadar", "Ostertz", "Paken", "Patxi", "Roke", "Sanduru", "Semenko", "Sendoa", "Silban", "Sukil", "Todor", "Txarles", "Ugutz", "Uhaitz", "Unai", "Untzalu", "Urtzi", "Uztai", "Xabier", "Zuhaitz", "Zuri", "Zuzen", "Adolf", "Adrià", "Agustí", "Alberic", "Aleix", "Àlvar", "Amadeu", "Andreu", "Aran", "Ariel", "Arnald", "Arnau", "Artur", "Bernabe", "Bernat", "Biel", "Blai", "Carles", "Cesc", "Climen", "Constantí", "Cosme", "Cristòfol", "Domènech", "Doroteu", "Eduard", "Elies", "Eloi", "Elpidi", "Enric", "Ernest", "Estanislau", "Esteve", "Eugeni", "Eusevi", "Feliu", "Ferran", "Ferrer",
                     "Fredreric", "Genari", "Gener", "Genis", "Gonçal", "Guifré", "Guillem", "Guiu", "Honorat", "Hospici", "Ignasi", "Isidre", "Jacint", "Jan", "Jaume", "Joaquín", "Jonatan", "Jordi", "Leopold", "Lluc", "Marc", "Marcel", "Martí", "Mateu", "Maurici", "Màxim", "Medir", "Moisès", "Nadal", "Nicolau", "Nil", "Oriol", "Osvald", "Ovidi", "Pacomi", "Pelai", "Pere", "Pol", "Prosper", "Rafel", "Raimon", "Raül", "Ricard", "Robert", "Roc", "Roderic", "Roger", "Sanc", "Sàndal", "Serni", "Simó", "Thiago", "Valentí", "Vicenç", "Víctor", "Virgili", "Xavi", "Xavier", "Zoel", "Agostiño", "Airas", "Alberte", "Aleixo", "Aldán", "Alexandre", "Amaro", "Amil", "André", "Anselmo", "Antón", "Antoín", "Antoíño", "Ánxelo", "Anxo", "Anxos", "Artai", "Artur", "Arximiro", "Aurelio", "Basilio", "Benedito", "Bento", "Benvito", "Benxamín", "Bernal", "Bernaldo", "Bernardiño", "Bieito", "Boaventura", "Brais", "Breixo", "Breogán", "Brigo", "Bruno", "Caetano", "Calisto", "Calros", "Camilo", "Cibrán", "Cilistro", "Ciriaco", "Clemenzo", "Clodio", "Cosme", "Cristovo", "Davide", "Diogo", "Domingos", "Duarte", "Eloy", "Estevo", "Euloxio", "Eutelo", "Euxenio", "Exidio", "Fernán", "Fidel", "Filipe", "Firmino", "Fiz", "Frederico", "Froitoso", "Gasparo", "Goio", "Hixinio", "Iago", "Lois", "Luar", "Luís", "Manoel", "Martiño", "Odón", "Pascoal", "Payo", "Peio", "Pello", "Peru", "Quentin", "Roi", "Roxelio", "Rui", "Tadeu", "Uxío", "Vicenzo", "Virxilio", "Xabier", "Xacinto", "Xacobe", "Xacobo", "Xaime", "Xan", "Xandro", "Xaneiro", "Xandre", "Xaquin", "Xenaro", "Xeraldo", "Xerardo", "Xermán", "Xesus", "Xián", "Xoán", "Xoel", "Xorxe", "Xosé", "Xurxo", "Aberbequeye", "Abhau", "Abian", "Ablal", "Acaymo", "Achuteyga", "Achxuraxan", "Acoidan", "Acoran", "Adargoma", "Aday", "Adjoña", "Adxoña", "Afur", "Agoney", "Agualeche", "Aguamuge", "Airam", "Alsagai", "Altaha", "Amalhuyge", "Amuhaici", "Anaterbe", "Anaterve", "Ancor", "Añaterve", "Aray", "Aremoga", "Artemis", "Atacaicate", "Atazaicate", "Ayoze", "Aythami", "Azuquahe", "Azuquahí", "Badenol", "Belicar", "Benchara", "Bencomo", "Beneharo", "Bentagoihe", "Bentor", "Caconaymo", "Caluca", "Chedey", "Choim", "Dailos", "Doramas", "Echedey", "Eraoranhan", "Ergual", "Garoe", "Gaumet", "Geronte", "Idubaren", "Imobach", "Iriome", "Iruen", "Jonay", "Maday", "Mardonio", "Nauzet", "Nuhazet", "Nuhazzet", "Ossinissa", "Rayco", "Tegueste", "Tinguaro", "Ubay", "Ventohey", "Xama", "Yarei", "Yeray", "Zebenzuí", "Aarón", "Abdiel", "Abel", "Abimael", "Abraham", "Acab", "Adán", "Agustín", "Ahzià", "Alejandro", "Andrés", "Aram", "Ashur", "Baltasar", "Bartolomé", "Beltrán", "Benjamín", "Caín", "Caín", "Caleb", "Ciro", "Dámaso", "Daniel", "Darío", "David", "Demócrito", "Édgar", "Efraín", "Elí", "Elías", "Eliel", "Eliseo", "Eneas", "Esteban", "Esteban", "Ezequiel", "Fabián", "Felipe", "Félix", "Francisco", "Gabriel", "Gadiel", "Gaspar", "Germán", "Guido", "Herodes", "Homero", "Hugo", "Isaac", "Isaías", "Isaías", "Ismael", "Israel", "Jacob", "Jaír de Galaad", "Jairo", "Jared", "Jehoram", "Jeremías", "Jesús", "Jiram", "Joanix", "Joaquín", "Jonás", "José", "Josué", "Juan", "Julio", "Labán", "Lemuel", "Leví", "Lucas", "Lucas", "Marcos", "Marduk", "Mateo", "Mateo", "Matías", "Miguel", "Moisés", "Naín", "Neftalí", "Neftalí", "Nicolás", "Noé", "Omar", "Pablo", "Rafael", "Renato", "Rubén", "Salomón", "Samuel", "Saúl", "Sergio", "Set", "Simón", "Tobías", "Uzías", "Zacarías")
nombresFemeninos = ("Adara", "Agata", "Agripina", "Ainhara", "Aixa", "Alegría", "Alia", "Alla", "América", "Aminata", "Amor", "Anahí", "Ania", "Aquilina", "Ariadne", "Arya", "Asia", "Atenea", "Bella", "Benilde", "Camino", "Carmina", "Casandra", "Celina", "Chaymae", "Clemencia", "Cora", "Cruz", "Custodia", "Dalila", "Danae", "Dania", "Demetria", "Denise", "Doina", "Dominica", "Dorina", "Doris", "Duna", "Elaia", "Elida", "Enma", "Erundina", "Etelvina", "Evelia", "Evelin", "Fatma", "Federica", "Flavia", "Florina", "Gadea", "Griselda", "Guacimara", "Guiomar", "Hasna", "Indara", "Inna", "Iraide", "Irantzu", "Ivette", "Jade", "Johana", "Juncal", "Kira", "Larisa", "Laureana", "Leia", "Lena", "Leocadia", "Libe", "Lilia", "Linda", "Lisa", "Liudmila", "Livia", "Lluna", "Luana", "Lucinda", "Mabel", "Manar", "Mariama", "Marianela", "Nadine", "Naila", "Nawal", "Nazareth", "Nelly", "Noah", "Norah", "Penélope", "Remei", "Rosalba", "Sabah", "Safia", "Saliha", "Saloua", "Sana", "Sanaa", "Severina", "Silvina", "Talia", "Tasnim", "Telma", "Valle", "Ximena", "Xiomara", "Yadira", "Yamila", "Yesenia", "Yuliya", "Yumara", "Zakia", "Lucía", "Sofía", "Martina", "María", "Julia", "Paula", "Valeria", "Emma", "Daniela", "Carla", "Alba", "Noa", "Alma", "Sara", "Carmen", "Vega", "Lara", "Mia", "Valentina", "Olivia", "Claudia", "Jimena", "Lola", "Chloe", "Aitana", "Abril", "Ana", "Laia", "Triana", "Candela", "Alejandra", "Elena", "Vera", "Manuela", "Adriana", "Inés", "Marta", "Carlota", "Irene", "Victoria", "Blanca", "Marina", "Laura", "Rocío", "Alicia", "Clara", "Nora", "Lia", "Ariadna", "Zoe", "Amira", "Gala", "Celia", "Leire", "Eva", "Ángela", "Andrea", "África", "Luna", "Ainhoa", "Ainara", "India", "Nerea", "Ona", "Elsa", "Isabel", "Leyre", "Gabriela", "Aina", "Cayetana", "Iria", "Jana", "Mar", "Cloe", "Lina", "Julieta", "Adara", "Naia", "Iris", "Nour", "Mara", "Helena", "Yasmín", "Natalia", "Arlet", "Diana", "Aroa", "Amaia", "Cristina", "Nahia", "Isabella", "Malak", "Elia", "Carolina", "Berta", "Fátima", "Nuria", "Azahara", "Macarena", "Aurora", "Abantza", "Abarne", "Abesti", "Adartza", "Adirane", "Agara", "Agata", "Agate", "Aimara", "Ainara", "Aines", "Ainhoa", "Aintza", "Aintzane.", "Alaia", "Alaikari", "Alaiñe", "Albane", "Alda", "Aliza", "Alize", "Alode", "Alodi", "Aloise", "Amade", "Amaia", "Amane", "Amele", "Andoitza", "Ane", "Antia", "Anuntxi", "Arantxa", "Arantza", "Arene", "Aretxa", "Argia", "Astere", "Begoña", "Dogartze", "Domeka", "Dunixe", "Ederne", "Edurne", "Egia", "Ekaitza", "Elaia", "Elaia", "Elixe", "Enara", "Estibaliz", "Eulari", "Eztia", "Florentzi", "Gadea", "Garaine", "Gorane", "Gure", "Haizea", "Haizeder", "Hegoa", "Ibarne", "Ikerne", "Ilargi", "Iluntze", "Iraide", "Irune", "Izadi", "Jaione", "Julene", "Kaia", "Kaiene", "Keltse", "Kemena", "Laia", "Leire", "Letizia", "Lide", "Loredi", "Lukene", "Lutxi", "Luzia", "Maia", "Maitane", "Maite", "Malen", "Markele", "Mikela", "Milia", "Mirari", "Nagore", "Nahia", "Nahikari", "Naiara", "Naroa", "Nekane", "Nerea", "Oihana", "Oihane", "Olaia", "Paule", "Polentze", "Sabiñe", "Santsa", "Sarabe", "Sua", "Tala", "Taresa", "Uda", "Udane", "Udara", "Ula", "Urzuri", "Yera", "Zeiane", "Zohardi", "Zorione", "Zumaia", "Zuria", "Zuzene", "Abellera", "Agnès", "Aida", "Aïna", "Aisha", "Aixa", "Albà", "Alix", "Alma", "Aloma", "Anaïs", "Àngels", "Anna", "Ares", "Ariadna", "Arlet", "Aura", "Bet", "Beth", "Blau", "Cel", "Cèlia", "Chloé", "Cira", "Clàudia", "Cloè", "Consol",
                    "Cora", "Dàlia", "Dèlia", "Dolça", "Duna", "Dúnia", "Edna", "Elna", "Elsa", "Emma", "Estel", "Etna", "Finestres", "Francina", "Gemma", "Gina", "Iria", "Ivet", "Jana", "Joana", "Judit", "Júlia", "Laia", "Lara", "Lea", "Lena", "Lia", "Lis", "Llora", "Llúcia", "Margarida", "Meritxell", "Mireia", "Montserrat", "Nàdia", "Nara", "Neus", "Nina", "Nit", "Noa", "Nora", "Nura", "Núria", "Ona", "Queralt", "Ramona", "Remei", "Rita", "Roser", "Sança", "Sira", "Socors", "Sol", "Soledat", "Thaís", "Txell", "Vera", "Vinyet", "Xènia", "Zoa", "Ádega", "Agostiña", "Áine", "Alana", "Alborada", "Albura", "Alda", "Aldana", "Alexandra", "Alexia", "Alla", "Alodia", "Aloia", "Amaina", "Amil", "Antela", "Antía", "Antoniña", "Anxa", "Ánxela", "Ánxeles", "Anxélica", "Anxos", "Apana", "Aranza", "Aránzazu", "Arduína", "Arxentina", "Asunta", "Aunia", "Baia", "Balla", "Beata", "Bélxica", "Benvida", "Benxamina", "Branca", "Brenda", "Briana", "Brianda", "Brisda", "Bríxida", "Camiño", "Candea", "Candeloria", "Catuxa", "Cebreiro", "Cecía", "Cela", "Celina", "Celtia", "Chorima", "Cía", "Cilla", "Doa", "Dubra", "Einés", "Elba", "Elvia", "Erea", "Euxea", "Euxenia", "Evelina", "Exeria", "Franqueira", "Fulxencia", "Glenda", "Hixinia", "Icía", "Ifixenia", "Ilduara", "Iria", "Iría", "Irimia", "Lana", "Loucia", "Malvina", "Maxina", "Mencía", "Minia", "Moira", "Mor", "Muma", "Muriel", "Navia", "Noela", "Noreia", "Roxelia", "Roxeria", "Sabela", "Sarela", "Tareixa", "Ulla", "Uxía", "Virxilia", "Xacinta", "Xandra", "Xaquelina", "Xasmín", "Xela", "Xeloíra", "Xema", "Xenevra", "Xenia", "Xenoveva", "Xenxa", "Xiana", "Xilda", "Xosefa", "Xudite", "Xulia", "Xulieta", "Xunqueira", "Xuventina", "Zeltia", "Abenaura", "Acerina", "Adassa", "Agora", "Aja", "Andamana", "Aniagua", "Arai", "Arecida", "Aregoma", "Aremoga", "Arminda", "Atasara", "Ataytana", "Atenyama", "Attagora", "Atteneri", "Attenya", "Attesora", "Attisa", "Ayaya", "Azerina", "Benayga", "Cagora", "Cainana", "Carigaga", "Carumaje", "Cathaysa", "Cazalt", "Chabuta", "Chamaida", "Chamorta", "Chaoro", "Charora", "Chaxiraxi", "Choya", "Collarapa", "Dácil", "Dafra", "Daida", "Daniasa", "Dasil", "Dautinimaria", "Delioma", "Faina", "Famara", "Fayna", "Fiama", "Gara", "Gazmira", "Grimanesa", "Guacimara", "Guajara", "Guaxara", "Guayafanta", "Guayarmina", "Haridian", "Iballa", "Ico", "Idaira", "Iraya", "Iriome", "Iruene", "Isora", "Itahisa", "Ithaisa", "Maday", "May", "Mifaya", "Moneiba", "Moneyba", "Naira", "Nisa", "Ramagua", "Sibisse", "Tahona", "Tamonante", "Tazirga", "Teguise", "Tenesoya", "Teseida", "Timanfaya", "Xerach", "Yaiza", "Yruene", "Yurena", "Abigail", "Abigail", "Ada", "Adira", "Ana", "Angélica", "Arisbeth", "Arisbeth", "Arlet", "Asunción", "Bela", "Belén", "Berenice", "Bethsaida", "Betsabé", "Bitia", "Camila", "Carmela", "Carmen", "Carolina", "Cira", "Claudia", "Cloé", "Concepción", "Dalila", "Dámaris", "Dana", "Daniela", "Daniela", "Dara", "Diana", "Ditza", "Dolores", "Dorotea", "Edén", "Elda", "Elena", "Elisabeth", "Ester", "Eva", "Génesis", "Hadassa", "Heba", "Hefziba", "Inmaculada", "Isabel", "Joela", "Juana", "Judith", "Julia", "Lea", "Lia", "Luz", "Magdalena", "Mara", "María", "María José", "Marilia", "Marta", "Miriam", "Nazareth", "Noa", "Noelia", "Noemí", "Paloma", "Paula", "Prisca", "Raisa", "Raquel", "Rebeca", "Ruth", "Sahily", "Salomé", "Samara", "Sara", "Sara", "Sarabel", "Saray", "Séfora", "Suri", "Susana", "Tamara", "Tara", "Tirsa", "Uma", "Vica", "Zemira", "Zila")

apellidos = ('González', 'Muñoz', 'Rojas', 'Díaz', 'Pérez', 'Soto', 'Contreras', 'Silva', 'Martínez', 'Sepúlveda', 'Morales', 'Rodríguez', 'López', 'Fuentes', 'Hernández', 'Torres', 'Araya', 'Flores', 'Espinoza', 'Valenzuela', 'Castillo', 'Tapia', 'Reyes', 'Gutiérrez', 'Castro', 'Pizarro', 'Álvarez', 'Vásquez', 'Sánchez', 'Fernández', 'Ramírez', 'Carrasco', 'Gómez', 'Cortés', 'Herrera', 'Núñez', 'Jara', 'Vergara', 'Rivera', 'Figueroa', 'Riquelme', 'García', 'Miranda', 'Bravo', 'Vera', 'Molina', 'Vega', 'Campos', 'Sandoval', 'Orellana',
             'Cárdenas', 'Olivares', 'Alarcón', 'Gallardo', 'Ortiz', 'Garrido', 'Salazar', 'Guzmán', 'Henríquez', 'Saavedra', 'Navarro', 'Aguilera', 'Parra', 'Romero', 'Aravena', 'Vargas', 'Vázquez', 'Cáceres', 'Yáñez', 'Leiva', 'Escobar', 'Ruiz', 'Valdés', 'Vidal', 'Salinas', 'Zúñiga', 'Peña', 'Godoy', 'Lagos', 'Maldonado', 'Bustos', 'Medina', 'Pino', 'Palma', 'Moreno', 'Sanhueza', 'Carvajal', 'Navarrete', 'Sáez', 'Alvarado', 'Donoso', 'Poblete', 'Bustamante', 'Toro', 'Ortega', 'Venegas', 'Lopez', 'Mendoza', 'Farías', 'San Martín')

vehiculos = (["Chevrolet", "Orlando"], ["Chevrolet", "Captiva"], ["Hyundai", "Tucson"], ["Hyundai", "Santa Fe"], ["Chevrolet", "Colorado"], ["Chevrolet", "Spin"],
             ["Suzuki", "S-Presso"], ["Suzuki", "Vitara"], ["Suzuki", "Gran Nomade"], ["Ford",
                                                                                       "F-150"], ["Ford", "Bronco"], ["Volkswagen", "Tiguan"], ["Kia", "Frontier"],
             ["Citroën", "Berlingo"], ["Peugeot", "Partner"], ["Jeep", "Wrangler"], [
                 "Jeep", "Grand Cherokee"], ["Jeep", "Compass"], ["Dodge", "Durango"], ["Suzuki", "Samurai"],
             ["Dodge", "Ram"])

direcciones = ["Av Daigonal", "Av Transversal", "Av Longitudinal", "Bernardo O'Higgins", "Arturo Prat", "Gabriela Mistral", "Pablo Neruda", "Vicente Huidobro",
               "Jose Miguel Carrera", "José Manuel Balmaceda", "Manuel Blanco Encalada", "Manuel Bulnes", "Joaquín Prieto", "Manuel Bulnes", "Luis Barros Borgoño",
               "Pedro Aguirre Cerda", "Algarrobo", "Chañar", "Pacama", "Queñoa", "Tamarugo", "Patahua", "Pelu", "Petra", "Boldo", "Bollen", "Corontillo", "Frangel", "Maiten",
               "Molle", "Petrillo"]


def generarNombreCompleto():
    op = ["M", "F"]
    x = random.choice(op)
    if x == "M":
        nombre = [random.choice(nombresMasculinos), random.choice(
            nombresMasculinos), random.choice(apellidos), random.choice(apellidos)]
    elif x == "F":
        nombre = [random.choice(nombresFemeninos), random.choice(
            nombresFemeninos), random.choice(apellidos), random.choice(apellidos)]
    return nombre


def generarCorreo(nombre, apellido):
    dominio = ["gmail.com", "hotmail.com", "outlook.com"]
    correo = nombre[:3] + apellido[:3] + str(random.randint(0, 9)) + str(
        random.randint(0, 9)) + "@" + random.choice(dominio)
    return correo.lower()


def generarPatenteAntigua():
    pat = chr(random.randint(65, 90))
    pat = pat + chr(random.randint(65, 90))
    pat = pat + str(random.randint(0, 9))
    pat = pat + str(random.randint(0, 9))
    pat = pat + str(random.randint(0, 9))
    pat = pat + str(random.randint(0, 9))
    return pat


def generarPatenteNueva():
    pat = chr(random.randint(65, 90))
    pat = pat + chr(random.randint(65, 90))
    pat = pat + chr(random.randint(65, 90))
    pat = pat + chr(random.randint(65, 90))
    pat = pat + str(random.randint(0, 9))
    pat = pat + str(random.randint(0, 9))
    return pat


def generarRut():
    rut = str(random.randint(6, 21))
    rut = rut + "."
    rut = rut + str(random.randint(0, 9))
    rut = rut + str(random.randint(0, 9))
    rut = rut + str(random.randint(0, 9))
    rut = rut + "."
    rut = rut + str(random.randint(0, 9))
    rut = rut + str(random.randint(0, 9))
    rut = rut + str(random.randint(0, 9))
    rut = rut + "-"
    dv = random.randint(-2, 9)
    if dv < 0:
        rut = rut + "K"
    else:
        rut = rut + str(dv)
    return rut


def generarTelefono():
    tel = "+569"
    tel = tel + str(random.randint(0, 9))
    tel = tel + str(random.randint(0, 9))
    tel = tel + str(random.randint(0, 9))
    tel = tel + str(random.randint(0, 9))
    tel = tel + str(random.randint(0, 9))
    tel = tel + str(random.randint(0, 9))
    tel = tel + str(random.randint(0, 9))
    tel = tel + str(random.randint(0, 9))
    return tel

################################################################################################################################################################


autos = []

i = 1
while i < 6:
  print(i)
  i += 1
