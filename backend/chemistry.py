from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski

class ChemistryAnalyzer:
    def __init__(self, smiles):
        self.molecule = Chem.MolFromSmiles(smiles)
        if self.molecule is None:
            raise ValueError('Invalid SMILES string')

    def detect_stereochemistry(self):
        stereochem = Chem.FindMolChiralCenters(self.molecule, includeUnassigned=True)
        return stereochem

    def identify_functional_groups(self):
        functional_groups = []
        # Define some simple patterns for functional groups
        patterns = {
            'Alcohol': '[O][H]',
            'Aldehyde': 'C(=O)[H]',
            'Ketone': 'C(=O)',
            'Carboxylic Acid': 'C(=O)[OH]',
            'Amine': 'N',
            'Aromatic': 'c',
        }
        for name, pattern in patterns.items():
            if Chem.MolHasSubstructMatch(self.molecule, Chem.MolFromSmarts(pattern)):
                functional_groups.append(name)
        return functional_groups

    def evaluate_lipinski_rules(self):
        logp = Descriptors.MolLogP(self.molecule)
        num_h_donors = Lipinski.NumHDonors(self.molecule)
        num_h_acceptors = Lipinski.NumHAcceptors(self.molecule)
        return {
            'LogP': logp,
            'HDonors': num_h_donors,
            'HAcceptors': num_h_acceptors
        }

    def calculate_identifiers(self):
        identifiers = {
            'Molecular Weight': Descriptors.MolWt(self.molecule),
            'Number of Rings': Descriptors.RingCount(self.molecule),
            'Number of Aromatic Rings': Descriptors.NumAromaticRings(self.molecule)
        }
        return identifiers

# Example usage:
# analyzer = ChemistryAnalyzer('CCO')
# print(analyzer.detect_stereochemistry())
# print(analyzer.identify_functional_groups())
# print(analyzer.evaluate_lipinski_rules())
# print(analyzer.calculate_identifiers())
