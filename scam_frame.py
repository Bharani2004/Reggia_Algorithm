class ICMFramework:
    def __init__(self):
        self.design_patterns = {}
        self.drim = {}
        self.search_algorithms = {}

    def add_design_pattern(self, pattern_name, pattern_description):
        self.design_patterns[pattern_name] = pattern_description

    def add_drim_entry(self, drim_name, drim_details):
        self.drim[drim_name] = drim_details

    def add_search_algorithm(self, algorithm_name, algorithm_code):
        self.search_algorithms[algorithm_name] = algorithm_code

    def retrieve_design_pattern(self, pattern_name):
        if pattern_name in self.design_patterns:
            return self.design_patterns[pattern_name]
        else:
            return "Design pattern not found."

    def search_drim(self, keyword):
        results = []
        for drim_name, drim_details in self.drim.items():
            if keyword.lower() in drim_details.lower():
                results.append((drim_name, drim_details))
        return results

    def search_using_algorithm(self, algorithm_name, query):
        if algorithm_name in self.search_algorithms:
            return self.search_algorithms[algorithm_name](query)
        else:
            return "Algorithm not found."

framework = ICMFramework()
framework.add_design_pattern("Factory Method", "Defines an interface for creating objects but allows subclasses to alter the type of objects that will be created.")
framework.add_design_pattern("Singleton", "Ensures a class has only one instance and provides a global point of access to it.")
framework.add_design_pattern("Facade Pattern","The pattern provides a unified interface to a set of interfaces in a subsystem. Simplifies the existing subsystem.")
framework.add_drim_entry("Database Connection", "DRIM entry for establishing a connection to the database.")
framework.add_drim_entry("User Authentication", "DRIM entry for authenticating users.")

def search_drim(self, keyword):
    results = []
    for drim_name, drim_details in self.drim.items():
        print("Keyword:", keyword.lower())
        print("DRIM Details:", drim_details.lower())
        if keyword.lower() in drim_details.lower():
            results.append((drim_name, drim_details))
    return results

def simple_search(query):
    results = []
    for pattern_name, pattern_description in framework.design_patterns.items():
        if query.lower() in pattern_description.lower():
            results.append((pattern_name, pattern_description))
    return results

framework.add_search_algorithm("Simple Search", simple_search)
print(framework.retrieve_design_pattern("Facade Pattern"))
print(framework.drim["User Authentication"])
print(framework.drim)
print(framework.search_using_algorithm("Simple Search", "interface"))