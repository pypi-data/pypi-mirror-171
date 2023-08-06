from chemplus import sdf
from chemplus import draw
import pandas as pd
from rdkit import Chem
from rdkit.Chem import PandasTools
PandasTools.RenderImagesInAllDataFrames()

Chem.Mol.__str__ = draw.draw_mol

def df_from_sdf(filename, name_field="_Name", mol_column="Mol", mol_names=None,
                properties=None, sanitize=True, removeHs=False, strictParsing=True):
    mols_list = []
    
    for mol in sdf.sdf_iter(filename, sanitize=sanitize, removeHs=removeHs, strictParsing=strictParsing):
        if mol is None:
            raise Exception("Mol is None")
        if mol_names is None or mol.GetProp(name_field) in mol_names:
            if not properties:
                mol_row = mol.GetPropsAsDict()
            else:
                mol_row = dict((prop_name, mol.GetProp(prop_name)) for prop_name in mol.GetPropNames() if prop_name in properties)
            mol_row[name_field] = mol.GetProp(name_field)
            for prop_name in mol.GetPropNames():
                mol.ClearProp(prop_name)
            mol_row[mol_column] = mol
            mols_list.append(mol_row)
    
    if not mol_names is None:
        loaded_names = [mol_row[name_field] for mol_row in mols_list]
        for mol_name in mol_names:
            if mol_name not in loaded_names:
                mols_list.append({name_field : mol_name, mol_column : "Not Found"})
                
    df = pd.DataFrame(mols_list)
    df.rename(columns={name_field : "Name"}, inplace=True)
    new_columns_order = ["Name", mol_column] + list(set(df.columns.tolist()) - set(["Name", mol_column]))
    df = df[new_columns_order]
    return df

def df_to_sdf(df, filename, name_column="Name", mol_column="Mol", properties=None):
    writer = sdf.SDFWriter(filename)
    
    if properties is None:
        properties = []
    else:
        properties = list(properties)
        writer.set_props(properties)
    
    for index, row in df.iterrows():
        mol = Chem.Mol(row[mol_column])
        
        for prop in properties:
            value = row[prop]
            mol.SetProp(prop, str(value))
        mol.SetProp("_Name", str(row[name_column]))
        
        writer.write(mol)
    
    writer.close()
