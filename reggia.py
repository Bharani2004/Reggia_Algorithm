import itertools

required_functionalities = {'functionality1', 'functionality2', 'functionality3', 'functionality4', 'functionality5'}

software_components = {
    'component1': {'functionality1', 'functionality2', 'functionality3'},
    'component2': {'functionality2', 'functionality3', 'functionality4'},
    'component3': {'functionality3', 'functionality4', 'functionality5'},
    'component4': {'functionality1', 'functionality4', 'functionality5'},
    'component5': {'functionality1', 'functionality2'},
    'component6': {'functionality3', 'functionality5'}
}

def generate_subsets(components):
    subsets = []
    for i in range(1, len(components) + 1):
        subsets.extend(itertools.combinations(components, i))
    return subsets

def reggia_set_cover(required_functionalities, software_components):
    subsets = generate_subsets(software_components.keys())
    optimal_subset = None
    optimal_coverage = set()
    for subset in subsets:
        coverage = set().union(*[software_components[component] for component in subset])
        if coverage == required_functionalities:
            if optimal_subset is None or len(subset) < len(optimal_subset):
                optimal_subset = subset
                optimal_coverage = coverage
    return optimal_subset, optimal_coverage

optimal_subset, optimal_coverage = reggia_set_cover(required_functionalities, software_components)
print("Optimal Subset of Components:", optimal_subset)
print("Coverage of Optimal Subset:", optimal_coverage)
