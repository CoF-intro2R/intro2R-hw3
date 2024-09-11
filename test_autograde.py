
import pytest
import pandas as pd
import os

# check dir structure first
def test_dir_struc():
  assert os.path.isdir("R")
  assert os.path.isfile("R/hw3.R")
  assert os.path.isfile("Data/hja_verts_cleaned.csv")

# check that the column names are formatted correctly
def test_names():
  if os.path.isfile("Data/hja_verts_cleaned.csv"):
    
    dat = pd.read_csv("Data/hja_verts_cleaned.csv")
    names = sorted(dat.columns.tolist())
    
    expected_names = ['clip', 'length_1_mm', 'length_2_mm', 
      'notes', 'pass', 'pitnumber', 'reach', 'sample_date', 
      'section', 'site', 'species', 'unitnum', 'unittype', 
      'vert_index', 'weight_g', 'x', 'y', 'year']
      
    assert expected_names == names
    
# check that the salamander and trout data were merged
def test_rbind():
  if os.path.isfile("Data/hja_verts_cleaned.csv"):
    
    dat = pd.read_csv("Data/hja_verts_cleaned.csv")
    sp = sorted(dat['species'].unique().tolist())
    
    expected_sp = ['coastal_giant_salamander', 'cutthroat_trout']
    
    assert expected_sp == sp
    
    
# check that dates were reformated
def test_dates():
  if os.path.isfile("Data/hja_verts_cleaned.csv"):
    
    dat = pd.read_csv("Data/hja_verts_cleaned.csv")
    dates = sorted(dat['sample_date'].tolist())
    
    assert dates[1] == '1987-10-06'
